#!/usr/bin/env python3
"""
teller_client.py – GFM Bank teller CLI

Usage examples:
  # Balance inquiry
  python teller_client.py --src-iban DE89545769475769453536

  # Transfer
  python teller_client.py --src-iban DE89545769475769453536 \\
      --dst-iban DE27200400600570150100 --amount 250

  # Request overdraft from back office
  python teller_client.py --src-iban DE89545769475769453536 --request-overdraft 500

Environment:
  COREBANK_URL   Base URL of the API  (default: http://127.0.0.1:8000)
"""

import argparse
import os
import pprint
import sys

import requests

BASE_URL = os.getenv("COREBANK_URL", "http://127.0.0.1:8000")


def _login() -> str:
    r = requests.post(
        f"{BASE_URL}/token",
        data={
            "username": os.getenv("TELLER_USER", "teller"),
            "password": os.getenv("TELLER_PASS", "teller123"),
        },
        timeout=10,
    )
    r.raise_for_status()
    return r.json()["access_token"]


def _auth(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def _get_accounts(token: str) -> list:
    r = requests.get(f"{BASE_URL}/accounts", headers=_auth(token), timeout=10)
    r.raise_for_status()
    return r.json()


def _get_ledger(token: str, account_id: str) -> list:
    r = requests.get(f"{BASE_URL}/transactions/{account_id}", headers=_auth(token), timeout=10)
    r.raise_for_status()
    return r.json()


def _post_transfer(token: str, src_id: str, dst_id: str, amount: float) -> dict:
    r = requests.post(
        f"{BASE_URL}/transfer",
        headers=_auth(token),
        json={
            "source_account_id": src_id,
            "destination_account_id": dst_id,
            "amount_eur": amount,
        },
        timeout=10,
    )
    r.raise_for_status()
    return r.json()


def main() -> None:
    ap = argparse.ArgumentParser(description="GFM Bank teller CLI")
    ap.add_argument("--src-iban", required=True, help="Source IBAN to inspect or debit")
    ap.add_argument("--dst-iban", help="Destination IBAN (required for transfer)")
    ap.add_argument("--amount", type=float, default=0.0, help="Amount in EUR (0 = balance inquiry only)")
    ap.add_argument("--request-overdraft", type=float, metavar="EUR",
                    help="Print overdraft request message for back office")
    args = ap.parse_args()

    if args.amount > 0 and not args.dst_iban:
        ap.error("--dst-iban is required when --amount > 0")

    token = _login()
    accounts = _get_accounts(token)

    src = next((a for a in accounts if a["iban"] == args.src_iban), None)
    if not src:
        print(f"Source IBAN {args.src_iban!r} not found.")
        sys.exit(1)

    ledger = _get_ledger(token, src["account_id"])
    balance = sum(tx["amount_eur"] for tx in ledger)
    latest = sorted(ledger, key=lambda x: x["booking_ts"], reverse=True)[:5]

    print(f"\n{'='*50}")
    print(f"  Account : {args.src_iban}")
    print(f"  Balance : €{balance:,.2f}")
    print(f"{'='*50}")
    print("\nLatest 5 transactions:")
    pprint.pprint(latest, sort_dicts=False)

    if args.request_overdraft is not None:
        print(f"\n*** OVERDRAFT REQUEST ***")
        print(f"Please grant €{args.request_overdraft:,.2f} overdraft on {args.src_iban}")

    if args.amount > 0:
        dst = next((a for a in accounts if a["iban"] == args.dst_iban), None)
        if not dst:
            print(f"Destination IBAN {args.dst_iban!r} not found.")
            sys.exit(1)
        print(f"\nPosting transfer of €{args.amount:,.2f}…")
        result = _post_transfer(token, src["account_id"], dst["account_id"], args.amount)
        pprint.pprint(result, sort_dicts=False)

        updated = sorted(_get_ledger(token, src["account_id"]),
                         key=lambda x: x["booking_ts"], reverse=True)[:5]
        print("\nLedger after transfer:")
        pprint.pprint(updated, sort_dicts=False)


if __name__ == "__main__":
    main()
