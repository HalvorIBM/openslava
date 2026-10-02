"""
seed_db.py – Initialise and seed corebank.db

Run once before starting the API:
  python seed_db.py

Creates tables and inserts sample customers, accounts, and transactions.
"""

import hashlib
import sqlite3
import uuid
from datetime import datetime as dt, timedelta, timezone
UTC = timezone.utc

DB_PATH = "corebank.db"


def _hash(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()


def init(db_path: str = DB_PATH) -> None:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # -----------------------------------------------------------------
    # Schema
    # -----------------------------------------------------------------
    c.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            username        TEXT PRIMARY KEY,
            hashed_password TEXT NOT NULL,
            role            TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS customers (
            customer_id TEXT PRIMARY KEY,
            name        TEXT NOT NULL,
            email       TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS accounts (
            account_id         TEXT PRIMARY KEY,
            iban               TEXT UNIQUE NOT NULL,
            customer_id        TEXT NOT NULL,
            currency           TEXT NOT NULL DEFAULT 'EUR',
            overdraft_limit_eur REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        );

        CREATE TABLE IF NOT EXISTS transactions (
            tx_id      TEXT PRIMARY KEY,
            account_id TEXT NOT NULL,
            booking_ts TEXT NOT NULL,
            amount_eur REAL NOT NULL,
            type       TEXT NOT NULL,
            FOREIGN KEY (account_id) REFERENCES accounts(account_id)
        );
    """)

    # -----------------------------------------------------------------
    # Users
    # -----------------------------------------------------------------
    users = [
        ("teller",     _hash("teller123"),     "TELLER"),
        ("backoffice", _hash("backoffice123"), "BACKOFFICE"),
    ]
    c.executemany(
        "INSERT OR IGNORE INTO users VALUES (?,?,?)", users
    )

    # -----------------------------------------------------------------
    # Customers
    # -----------------------------------------------------------------
    customers = [
        ("CUST-001", "Alice Müller",   "alice@example.com"),
        ("CUST-002", "Bob Schmidt",    "bob@example.com"),
        ("CUST-003", "Carol Becker",   "carol@example.com"),
        ("CUST-004", "David Fischer",  "david@example.com"),
    ]
    c.executemany(
        "INSERT OR IGNORE INTO customers VALUES (?,?,?)", customers
    )

    # -----------------------------------------------------------------
    # Accounts
    # -----------------------------------------------------------------
    accounts = [
        ("ACC-001", "DE89545769475769453536", "CUST-001", "EUR", 500.0),
        ("ACC-002", "DE27200400600570150100", "CUST-001", "EUR", 0.0),
        ("ACC-003", "DE89370400440532013000", "CUST-002", "EUR", 0.0),
        ("ACC-004", "DE75512108001245126199", "CUST-003", "EUR", 1000.0),
        ("ACC-005", "DE46500105174528566855", "CUST-004", "EUR", 0.0),
    ]
    c.executemany(
        "INSERT OR IGNORE INTO accounts VALUES (?,?,?,?,?)", accounts
    )

    # -----------------------------------------------------------------
    # Transactions (seed ledger)
    # -----------------------------------------------------------------
    base = dt.now(UTC) - timedelta(days=30)

    def ts(days_ago: float) -> str:
        return (base + timedelta(days=days_ago)).isoformat(timespec="seconds")

    txs = [
        # Alice – main account
        (str(uuid.uuid4()), "ACC-001", ts(0),  10_000.00, "OPENING_CREDIT"),
        (str(uuid.uuid4()), "ACC-001", ts(1),    -250.00, "TRANSFER_OUT"),
        (str(uuid.uuid4()), "ACC-001", ts(5),   -1_500.00, "TRANSFER_OUT"),
        (str(uuid.uuid4()), "ACC-001", ts(10),   2_000.00, "TRANSFER_IN"),
        (str(uuid.uuid4()), "ACC-001", ts(15),    -45.00,  "TRANSFER_OUT"),
        # Alice – savings account
        (str(uuid.uuid4()), "ACC-002", ts(0),   5_000.00, "OPENING_CREDIT"),
        (str(uuid.uuid4()), "ACC-002", ts(7),   1_000.00, "TRANSFER_IN"),
        # Bob
        (str(uuid.uuid4()), "ACC-003", ts(0),   3_500.00, "OPENING_CREDIT"),
        (str(uuid.uuid4()), "ACC-003", ts(3),    -300.00, "TRANSFER_OUT"),
        (str(uuid.uuid4()), "ACC-003", ts(12),    200.00, "TRANSFER_IN"),
        # Carol
        (str(uuid.uuid4()), "ACC-004", ts(0),  20_000.00, "OPENING_CREDIT"),
        (str(uuid.uuid4()), "ACC-004", ts(2),  -5_000.00, "TRANSFER_OUT"),
        # David
        (str(uuid.uuid4()), "ACC-005", ts(0),     750.00, "OPENING_CREDIT"),
    ]
    c.executemany(
        "INSERT OR IGNORE INTO transactions VALUES (?,?,?,?,?)", txs
    )

    conn.commit()
    conn.close()
    print(f"Database initialised at {db_path}")


if __name__ == "__main__":
    init()
