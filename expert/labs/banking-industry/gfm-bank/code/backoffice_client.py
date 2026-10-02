#!/usr/bin/env python3
"""
backoffice_client.py – GFM Bank back-office CLI

Usage examples:
  # Look up customer by name
  python backoffice_client.py --customer-name Müller

  # Look up by IBAN
  python backoffice_client.py --iban DE89545769475769453536

  # Set overdraft limit
  python backoffice_client.py --iban DE89545769475769453536 --set-overdraft 1000

  # Post a fee reversal
  python backoffice_client.py --iban DE89545769475769453536 \\
      --fee-reversal-iban DE89545769475769453536 --fee-reversal-amount 15

Environment:
  COREBANK_URL   Base URL of the API  (default: http://127.0.0.1:8000)
"""

import argparse
import datetime as dt
from datetime import timezone as _tz
import os
import pprint
import sys

import requests

BASE_URL = os.getenv("COREBANK_URL", "http://127.0.0.1:8000")


def _login() -> str:
    r = requests.post(
        f"{BASE_URL}/token",
        data={
            "username": os.getenv("BACKOFFICE_USER", "backoffice"),
            "password": os.getenv("BACKOFFICE_PASS", "backoffice123"),
        },
        timeout=10,
    )
    r.raise_for_status()
    return r.json()["access_token"]


def _auth(tok: str) -> dict:
    return {"Authorization": f"Bearer {tok}"}


def _get(endpoint: str, tok: str):
    r = requests.get(f"{BASE_URL}{endpoint}", headers=_auth(tok), timeout=10)
    r.raise_for_status()
    return r.json()


def _post(endpoint: str, tok: str, payload: dict):
    r = requests.post(f"{BASE_URL}{endpoint}", headers=_auth(tok), json=payload, timeout=10)
    r.raise_for_status()
    return r.json()


def main() -> None:
    ap = argparse.ArgumentParser(description="GFM Bank back-office CLI")
    ap.add_argument("--customer-name", help="Customer name substring search")
    ap.add_argument("--iban", help="Look up by IBAN directly")
    ap.add_argument("--fee-reversal-iban", help="IBAN to credit with fee reversal")
    ap.add_argument("--fee-reversal-amount", type=float, default=15.0,
                    help="Fee reversal amount in EUR (default 15.00)")
    ap.add_argument("--set-overdraft", type=float, metavar="EUR",
                    help="Set overdraft limit (0–10 000 EUR)")
    args = ap.parse_args()

    if not args.iban and not args.customer_name:
        ap.error("Provide --iban or --customer-name")

    tok = _login()

    if args.iban:
        accounts = _get("/accounts", tok)
        account = next((a for a in accounts if a["iban"] == args.iban), None)
        if not account:
            print(f"IBAN {args.iban!r} not found.")
            sys.exit(1)
        customers = _get("/customers", tok)
        customer = next(
            (c for c in customers if c["customer_id"] == account["customer_id"]), None
        )
        cust_accounts = [account]
    else:
        customers = _get("/customers", tok)
        matches = [c for c in customers if args.customer_name.lower() in c["name"].lower()]
        if not matches:
            print(f"No customer matching {args.customer_name!r}.")
            sys.exit(1)
        customer = matches[0]
        all_accounts = _get("/accounts", tok)
        cust_accounts = [a for a in all_accounts if a["customer_id"] == customer["customer_id"]]

    print("\n== Customer ==")
    pprint.pprint(customer, sort_dicts=False)
    print("\n== Accounts ==")
    pprint.pprint(cust_accounts, sort_dicts=False)

    if args.set_overdraft is not None:
        target = cust_accounts[0]
        r = requests.patch(
            f"{BASE_URL}/accounts/{target['account_id']}/overdraft",
            headers=_auth(tok),
            params={"limit_eur": args.set_overdraft},
            timeout=10,
        )
        r.raise_for_status()
        print("\nOverdraft updated:", r.json())

    if args.fee_reversal_iban:
        acct = next((a for a in cust_accounts if a["iban"] == args.fee_reversal_iban), None)
        if not acct:
            print("Fee reversal IBAN not found in customer accounts.")
            sys.exit(1)
        result = _post(
            f"/transactions/{acct['account_id']}",
            tok,
            {
                "amount_eur": args.fee_reversal_amount,
                "type": "FEE_REVERSAL",
                "booking_ts": dt.datetime.now(_tz.utc).isoformat(timespec="seconds"),
            },
        )
        print(f"\nFee reversal of €{args.fee_reversal_amount:.2f} posted:", result)


if __name__ == "__main__":
    main()
