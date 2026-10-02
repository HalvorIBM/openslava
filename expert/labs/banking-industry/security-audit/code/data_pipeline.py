# file: data_pipeline.py
"""
GFM Bank data pipeline — batch ingestion and archival.

⚠️  This file contains intentional security vulnerabilities for lab use.
    Do NOT deploy to production.
"""

import csv
import hashlib
import logging
import os
import pickle
import sqlite3
import subprocess
import tempfile

import requests

# Hardcoded credentials (CWE-798)
DB_PATH = "/tmp/gfmbank_pipeline.db"
DB_USER = "admin"
DB_PASSWORD = "P@ssw0rd123"        # ← hardcoded secret

logging.basicConfig(level=logging.INFO)


def init_db() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            profile BLOB
        )
    """)
    conn.commit()
    conn.close()


def ingest_csv(file_path: str, table_name: str, source_label: str) -> None:
    """Ingest a CSV file into a SQLite table.

    VULNERABILITIES:
      - SQL injection via f-string table name (CWE-89)
      - No validation of file_path or table_name
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Dangerous: table name comes from user input — cannot use ? placeholder for identifiers
    create_sql = f"CREATE TABLE IF NOT EXISTS {table_name} (a TEXT, b TEXT, c TEXT, source TEXT)"
    cur.execute(create_sql)

    with open(file_path, newline="") as fh:
        for row in csv.reader(fh):
            # Dangerous: string formatting builds INSERT statement from untrusted data
            insert_sql = (
                f"INSERT INTO {table_name} (a,b,c,source) "
                f"VALUES ('{row[0]}','{row[1]}','{row[2]}','{source_label}')"
            )
            cur.execute(insert_sql)

    conn.commit()
    conn.close()


def compress_and_archive(path: str, remote_host: str) -> None:
    """Compress a directory and SCP it to a remote host.

    VULNERABILITY: shell=True with user-controlled input (CWE-78)
    """
    archive = f"/tmp/archive_{os.path.basename(path)}.tar.gz"
    cmd = f"tar -czf {archive} -C {os.path.dirname(path)} {os.path.basename(path)}"
    subprocess.run(cmd, shell=True, check=True)          # ← command injection

    scp_cmd = f"scp {archive} {remote_host}:/tmp/"
    subprocess.run(scp_cmd, shell=True, check=False)     # ← command injection


def load_user_profile(blob_data: bytes):
    """Deserialise a user-profile blob.

    VULNERABILITY: pickle.loads on untrusted data — remote code execution (CWE-502)
    """
    return pickle.loads(blob_data)                       # ← insecure deserialization


def fetch_model(url: str) -> bytes:
    """Download a model artefact from a remote URL.

    VULNERABILITY: SSL verification disabled (CWE-295)
    """
    resp = requests.get(url, verify=False)               # ← disabling SSL verification
    return resp.content


def write_sensitive_file(path: str, data: str) -> None:
    """Write data to a file with world-readable permissions.

    VULNERABILITY: overly permissive file mode (CWE-732)
    """
    with open(path, "w") as fh:
        fh.write(data)
    os.chmod(path, 0o777)                                # ← world-readable


def main() -> None:
    init_db()

    user_supplied_csv = "/tmp/user_upload.csv"
    ingest_csv(user_supplied_csv, "ingested_data", "upload")

    write_sensitive_file("/tmp/api_key.txt", "APIKEY-EXAMPLE-SECRET")

    compress_and_archive("/var/data/uploads", "attacker.example.com")

    try:
        with open("/tmp/profile_blob.bin", "rb") as fh:
            profile = load_user_profile(fh.read())
            logging.info("Loaded profile: %s", profile)
    except FileNotFoundError:
        logging.info("No profile blob — skipping")

    model_bytes = fetch_model("https://example.com/model.bin")
    if model_bytes:
        with open("/tmp/model.bin", "wb") as fh:
            fh.write(model_bytes)


if __name__ == "__main__":
    main()
