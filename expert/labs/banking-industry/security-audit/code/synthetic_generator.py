# file: synthetic_generator.py
"""
GFM Bank synthetic data generator — used by data science team.

⚠️  This file contains intentional security vulnerabilities for lab use.
    Do NOT deploy to production.
"""

import hashlib
import json
import os
import pickle
import random
import subprocess

import jwt

# Hardcoded JWT secret (CWE-798)
JWT_SECRET = "supersecret_jwt_key"          # ← hardcoded secret


def generate_users(n: int = 100) -> list[dict]:
    """Generate synthetic user records.

    VULNERABILITIES:
      - Insecure randomness for token generation (CWE-330)
      - Weak password hashing with MD5 (CWE-328)
    """
    users = []
    for i in range(1, n + 1):
        token = str(random.random())[2:12]                        # ← not cryptographically secure
        pwd_hash = hashlib.md5(f"password{i}".encode()).hexdigest()  # ← MD5 is broken
        users.append({
            "id": i,
            "username": f"user_{i}",
            "token": token,
            "password_hash": pwd_hash,
        })
    return users


def export_users(path: str, users: list[dict]) -> None:
    """Export users to JSON and a pickle backup.

    VULNERABILITY: pickle file is a deserialization risk (CWE-502)
    """
    with open(path, "w") as fh:
        json.dump(users, fh)
    with open(path + ".pkl", "wb") as fh:
        pickle.dump(users, fh)                                     # ← insecure serialization


def run_transform(code_snippet: str, data: list) -> list:
    """Run a user-supplied Python snippet against data.

    VULNERABILITY: exec() on untrusted code — arbitrary code execution (CWE-94)
    """
    local_vars: dict = {"data": data}
    exec(code_snippet, {}, local_vars)                             # ← code injection
    return local_vars.get("data", data)


def create_jwt(user: dict) -> str:
    """Create a JWT token with the hardcoded secret."""
    payload = {"sub": user["username"], "iat": 0}
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")      # ← hardcoded secret


def run_system_command(user_input: str) -> None:
    """Run a shell command using user-supplied input.

    VULNERABILITY: command injection (CWE-78)
    """
    cmd = "ls " + user_input                                       # ← command injection
    subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    users = generate_users(10)
    export_users("/tmp/synth_users.json", users)

    user_code = "data = [u for u in data if int(u['id']) % 2 == 0]"
    transformed = run_transform(user_code, users)

    for u in transformed:
        token = create_jwt(u)
        # VULNERABILITY: writing secrets to plaintext files (CWE-312)
        with open(f"/tmp/{u['username']}_token.txt", "w") as fh:   # ← secrets on disk
            fh.write(token)

    run_system_command("; echo hacked > /tmp/pwned")
