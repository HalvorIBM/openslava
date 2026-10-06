# 🏆 OpenSlava — Final Challenge

**Open build · No time limit · First 3 to submit win a prize**

---

## The Challenge

You have spent the last 90 minutes learning every dimension of IBM Bob — modes, `/init`, rules, custom modes, MCP, GitHub automation, and security auditing. Now put it all together in one coherent product, built entirely with Bob.

**The first three participants to submit a passing pull request win a prize.**

---

## Your Mission: PocketLedger

Build **PocketLedger** — a personal finance tracker with a React frontend, a FastAPI backend, and a full Bob-powered development workflow baked in.

### Application description

PocketLedger helps individuals track income and expenses. Users add transactions, see a live balance, and review a spending breakdown by category. The codebase must be clean, tested, and security-aware from the start — because you are going to use Bob to enforce that, not just hope for it.

### Feature list

| # | Feature | Layer |
|---|---|---|
| F1 | Add a transaction (amount, description, category, date) | Backend + Frontend |
| F2 | List all transactions, newest first | Backend + Frontend |
| F3 | Delete a transaction by ID | Backend + Frontend |
| F4 | Live balance display (sum of all amounts, signed) | Frontend |
| F5 | Spending breakdown by category (aggregated totals) | Backend + Frontend |
| F6 | Simple bar chart for category totals (vanilla JS Canvas or SVG — no charting library) | Frontend |
| F7 | Filter transactions by category via a dropdown | Frontend |
| F8 | Data persisted to a SQLite database (no in-memory store) | Backend |
| F9 | All API endpoints protected by a static bearer token (from environment variable) | Backend |
| F10 | At least 5 unit tests covering the data layer | Backend |

### Technology constraints

- **Backend:** Python 3.11+ · FastAPI · SQLite (via `sqlite3` or `SQLAlchemy`) · `uvicorn`
- **Frontend:** React 18+ · Vite · plain CSS (no component library, no Tailwind)
- **No external charting libraries** (Chart.js, D3, Recharts, etc.) for F6
- **Auth:** static bearer token read from `POCKETLEDGER_TOKEN` env var — no OAuth, no sessions

---

## Bob Requirements

This is not just an application challenge — it is a **Bob workflow** challenge. Your submission must demonstrate that you used Bob correctly and completely. The following Bob artefacts are **required** and will be checked by the judges.

### B-REQ-1 — `/init` generated `AGENTS.md`

Run `/init` on the completed codebase. The `AGENTS.md` at the repo root must exist and must describe:

- The two-service architecture (backend + frontend)
- The auth model (bearer token from env)
- The database layer
- At least one project-specific constraint Bob inferred or that you added

### B-REQ-2 — Team rules file

Create `.bob/rules/pocketledger-standards.md` containing at minimum these three rules:

```markdown
All Python functions that handle monetary amounts must use float with exactly
2 decimal places of precision — never store raw user input directly to the DB.

All React components must have a JSDoc comment describing their props.

After every Agent mode interaction, append a one-line entry to bob-audit/audit.log
in the format: [ISO timestamp] [mode] [brief description of change]
```

Run at least one Agent mode interaction after creating the rules and confirm `bob-audit/audit.log` has a new entry.

### B-REQ-3 — Custom `ledger-reviewer` mode

Create `.bob/custom_modes.yaml` with a `ledger-reviewer` mode that:

- Has `read` and `mcp` tool groups only (no `edit`, no `command`)
- Has a `roleDefinition` describing it as a security-focused finance code reviewer
- Has at least 3 `customInstructions` items covering: float precision, hardcoded secrets, and input validation

Use the mode to run at least one review prompt and include the output (copy it into a file `ledger-review/initial-review.md` in the repo).

### B-REQ-4 — GitHub issue → PR loop

1. Push your repo to GitHub (public or private, your choice)
2. Create a GitHub issue titled **"Add CSV export for transactions"** with a description of the feature
3. Use **Agent** mode (with GitHub MCP) to read the issue, implement the endpoint, commit on a feature branch, and open a PR that references the issue number

The PR must exist on GitHub and must reference the issue. The CSV export endpoint does not need to be production-perfect — it just needs to exist and work for the basic case.

---

## Submission

### What to submit

Post a link to your **pull request** in the `#openslava-challenge` Slack channel (or hand it to a facilitator). The PR must be on a public (or IBM-internal) GitHub repo.

### What judges will check

| Check | Pass criteria |
|---|---|
| All 10 features (F1–F10) present | Verified by running `./start.sh` and testing the UI |
| `AGENTS.md` exists and is non-trivial | File present, >20 lines, describes architecture |
| `.bob/rules/pocketledger-standards.md` exists | File present, contains the 3 required rules |
| `bob-audit/audit.log` has entries | File present, at least 1 entry |
| `.bob/custom_modes.yaml` defines `ledger-reviewer` | Mode present, read-only groups only |
| `ledger-review/initial-review.md` present | File present, non-empty |
| GitHub PR references the issue | PR description contains `#<issue-number>` |
| Tests pass | `pytest` exits 0 in the backend directory |

### Scoring tiebreaker

If multiple submissions arrive at the same time, the tiebreaker is quality of `AGENTS.md` — specifically how well Bob was guided to capture the real architectural decisions of the project.

---

## Hints & Guidance

These hints are here if you get stuck. Try without them first.

??? tip "Hint 1 — Recommended start sequence"
    1. Create an empty folder `pocketledger/`
    2. Open it in **IBM Bob**, switch to **Plan** mode, paste the feature list and ask Bob to design the full project structure
    3. Switch to **Agent** mode, scaffold both services
    4. Run `/init` once the skeleton is in place
    5. Create your rules file before writing any business logic
    6. Build features F1–F10 in Agent mode

??? tip "Hint 2 — Bearer token pattern (FastAPI)"
    ```python
    from fastapi import Header, HTTPException
    import os

    def verify_token(authorization: str = Header(...)):
        expected = f"Bearer {os.environ['POCKETLEDGER_TOKEN']}"
        if authorization != expected:
            raise HTTPException(status_code=401, detail="Unauthorized")
    ```
    Add `Depends(verify_token)` to every route that should be protected.

??? tip "Hint 3 — Vanilla JS bar chart approach"
    Ask Bob in **Plan** mode first:
    ```
    Design a vanilla JS bar chart using the Canvas API that takes an array of
    { category: string, total: number } objects and renders horizontal bars.
    No external library.
    ```
    Then switch to **Agent** mode to implement.

??? tip "Hint 4 — start.sh template"
    Your repo should include a `start.sh` at the root that starts both services so judges can run it easily:
    ```bash
    #!/usr/bin/env bash
    set -e
    export POCKETLEDGER_TOKEN="${POCKETLEDGER_TOKEN:-dev-token-123}"
    cd backend && pip install -r requirements.txt -q && uvicorn main:app --reload --port 8000 &
    cd ../frontend && npm install -q && npm run dev &
    wait
    ```

??? tip "Hint 5 — GitHub MCP PR prompt"
    ```
    Read GitHub issue #<number> from this repo.
    Create a branch called feature/csv-export.
    Implement a GET /transactions/export endpoint in main.py that returns
    a CSV with columns: id, date, description, category, amount.
    Use Python's built-in csv module.
    Commit the change and open a pull request referencing the issue.
    ```

---

## Prize

The **first 3 participants** to submit a passing pull request receive an IBM Bob prize. 🏆

Good luck — and enjoy building with Bob.
