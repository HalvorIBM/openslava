"""
demo_api.py – GFM Bank Core Banking API

A FastAPI backend for the GFM Bank demo application.
Provides account management, transaction processing, and role-based access control.

Roles:
  teller     – balance inquiry, transfers, ledger view
  backoffice – all of the above + customer list, overdraft management, manual postings

Start:
  pip install fastapi uvicorn python-multipart pydantic
  uvicorn demo_api:app --reload
"""

import hashlib
import sqlite3
import uuid
from datetime import datetime as dt, timezone
UTC = timezone.utc

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, condecimal

DB_PATH = "corebank.db"
oauth = OAuth2PasswordBearer(tokenUrl="token")
app = FastAPI(title="GFM Bank Core Banking API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Database helpers
# ---------------------------------------------------------------------------

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


def _verify(tok: str, db) -> sqlite3.Row:
    row = db.execute(
        "SELECT username, role FROM users WHERE username = ?", (tok,)
    ).fetchone()
    if not row:
        raise HTTPException(status_code=401, detail="Invalid token")
    return row


def _require_role(row: sqlite3.Row, allowed: set[str]) -> sqlite3.Row:
    if row["role"] not in allowed:
        raise HTTPException(status_code=403, detail="Forbidden")
    return row


# ---------------------------------------------------------------------------
# Auth
# ---------------------------------------------------------------------------

@app.post("/token")
def login(form: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    row = db.execute(
        "SELECT hashed_password FROM users WHERE username = ?", (form.username,)
    ).fetchone()
    if not row or hashlib.sha256(form.password.encode()).hexdigest() != row["hashed_password"]:
        raise HTTPException(status_code=401, detail="Bad credentials")
    return {"access_token": form.username, "token_type": "bearer"}


# ---------------------------------------------------------------------------
# Accounts & customers
# ---------------------------------------------------------------------------

@app.get("/accounts")
def list_accounts(db=Depends(get_db), token: str = Depends(oauth)):
    user = _verify(token, db)
    rows = db.execute("SELECT * FROM accounts").fetchall()
    if user["role"] == "BACKOFFICE":
        return [dict(r) for r in rows]
    return [{k: r[k] for k in ("account_id", "iban", "customer_id")} for r in rows]


@app.get("/customers")
def list_customers(db=Depends(get_db), token: str = Depends(oauth)):
    _require_role(_verify(token, db), {"BACKOFFICE"})
    return [dict(r) for r in db.execute("SELECT * FROM customers")]


# ---------------------------------------------------------------------------
# Transactions
# ---------------------------------------------------------------------------

@app.get("/transactions/{account_id}")
def get_transactions(account_id: str, db=Depends(get_db), token: str = Depends(oauth)):
    _verify(token, db)
    return [dict(r) for r in db.execute(
        "SELECT * FROM transactions WHERE account_id = ?", (account_id,)
    )]


class Transfer(BaseModel):
    source_account_id: str
    destination_account_id: str
    amount_eur: condecimal(gt=0, max_digits=14, decimal_places=2)  # type: ignore[valid-type]


@app.post("/transfer")
def make_transfer(body: Transfer, db=Depends(get_db), token: str = Depends(oauth)):
    _verify(token, db)
    bal = db.execute(
        "SELECT COALESCE(SUM(amount_eur), 0) AS bal FROM transactions WHERE account_id = ?",
        (body.source_account_id,),
    ).fetchone()["bal"]
    od = db.execute(
        "SELECT overdraft_limit_eur FROM accounts WHERE account_id = ?",
        (body.source_account_id,),
    ).fetchone()["overdraft_limit_eur"]
    if bal - float(body.amount_eur) < -od:
        raise HTTPException(
            status_code=403,
            detail=f"Insufficient funds. Balance {bal:.2f}, overdraft limit {od:.2f}",
        )
    now = dt.now(UTC).isoformat(timespec="seconds")
    debit, credit = str(uuid.uuid4()), str(uuid.uuid4())
    try:
        db.execute("BEGIN")
        db.execute(
            "INSERT INTO transactions VALUES (?,?,?,?,?)",
            (debit, body.source_account_id, now, -float(body.amount_eur), "TRANSFER_OUT"),
        )
        db.execute(
            "INSERT INTO transactions VALUES (?,?,?,?,?)",
            (credit, body.destination_account_id, now, float(body.amount_eur), "TRANSFER_IN"),
        )
        db.commit()
    except Exception:
        db.rollback()
        raise
    return {"status": "POSTED", "debit_tx": debit, "credit_tx": credit, "timestamp": now}


# ---------------------------------------------------------------------------
# Back-office operations
# ---------------------------------------------------------------------------

@app.patch("/accounts/{account_id}/overdraft")
def set_overdraft(
    account_id: str, limit_eur: float, db=Depends(get_db), token: str = Depends(oauth)
):
    _require_role(_verify(token, db), {"BACKOFFICE"})
    if not (0 <= limit_eur <= 10_000):
        raise HTTPException(status_code=400, detail="Limit must be 0–10 000 EUR")
    db.execute(
        "UPDATE accounts SET overdraft_limit_eur = ? WHERE account_id = ?",
        (limit_eur, account_id),
    )
    db.commit()
    return {"account_id": account_id, "overdraft_limit_eur": limit_eur}


class ManualTx(BaseModel):
    amount_eur: float
    type: str
    booking_ts: str


@app.post("/transactions/{account_id}")
def manual_post(
    account_id: str, tx: ManualTx, db=Depends(get_db), token: str = Depends(oauth)
):
    _require_role(_verify(token, db), {"BACKOFFICE"})
    if tx.type not in ("FEE_REVERSAL", "MANUAL_ADJ"):
        raise HTTPException(status_code=400, detail="Only FEE_REVERSAL or MANUAL_ADJ allowed")
    tx_id = str(uuid.uuid4())
    db.execute(
        "INSERT INTO transactions VALUES (?,?,?,?,?)",
        (tx_id, account_id, tx.booking_ts, tx.amount_eur, tx.type),
    )
    db.commit()
    return {"status": "POSTED", "tx_id": tx_id}


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------

@app.get("/health")
def health():
    return {"status": "ok"}
