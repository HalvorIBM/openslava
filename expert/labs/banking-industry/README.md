# GFM Bank Lab — Banking Industry

A self-contained, three-part IBM Bob workshop built around the **GFM Bank Core Banking System** — a realistic FastAPI backend with a teller CLI, back-office CLI, and intentionally vulnerable data pipeline code for security training.

---

## What's in this lab

| Part | File | Focus | Duration |
|---|---|---|---|
| 1 | [`WORKSHOP-part1-architecture.md`](WORKSHOP-part1-architecture.md) | Understand the codebase, generate architecture docs | 25 min |
| 2 | [`WORKSHOP-part2-react-ui.md`](WORKSHOP-part2-react-ui.md) | Build a React teller UI connected to the API | 25 min |
| 3 | [`WORKSHOP-part3-security.md`](WORKSHOP-part3-security.md) | Security audit and remediation of the data pipeline | 20 min |

---

## Quick Start

```bash
# Start the GFM Bank API
cd gfm-bank
./start.sh
# → API running at http://127.0.0.1:8000
# → Docs at http://127.0.0.1:8000/docs
```

**Test credentials:**

| User | Password | Role |
|---|---|---|
| `teller` | `teller123` | TELLER |
| `backoffice` | `backoffice123` | BACKOFFICE |

**Sample IBAN:** `DE89545769475769453536` (Alice Müller)

---

## Prerequisites

- Python 3.11+
- Node.js 20 LTS (Part 2 only)
- IBM Bob extension installed and signed in

---

## Licence

Original work created for this workspace. Freely usable for IBM Bobathon events.
