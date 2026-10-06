# OpenSlava Labs — Test Plan

Branch: `test-labs`  
Scope: Every step in every lab across all four tracks (Beginner, Intermediate, Expert, Challenge)  
Purpose: Confirm that every instruction, prompt, file path, command, and expected outcome is correct, reproducible, and unambiguous before the event.

---

## How to use this document

Work through each section in order. For each test item:

1. Execute the exact step described in the lab guide.
2. Compare the actual result against the **Expected result** column.
3. Mark the status:  
   - `✅ PASS` — result matches expected exactly  
   - `⚠️ WARN` — result is mostly correct but deviates in a minor, non-blocking way (document deviation)  
   - `❌ FAIL` — step does not work or produces a wrong result (document error and open a fix)

Capture all failures and warnings in the **Issues log** at the end of this file.

---

## Prerequisites checklist

Run these checks once before starting any lab.

| # | Prerequisite | How to verify | Status |
|---|---|---|---|
| P1 | IBM Bob IDE installed and signed in | Launch Bob; user avatar shown in sidebar | |
| P2 | Node.js 20 LTS installed | `node --version` → `v20.x.x` | |
| P3 | Python 3.11+ installed | `python3 --version` → `3.11.x` or higher | |
| P4 | Git installed and configured | `git config user.name` and `git config user.email` return values | |
| P5 | Galaxium Travels repo cloned | `ls galaxium-travels/start.sh` exits 0 | |
| P6 | GitHub account exists | Can log in at github.com | |
| P7 | GitHub personal access token with `repo` scope created | Token string available | |
| P8 | GitHub MCP installed in Bob | Sidebar → MCP shows GitHub entry with no red error badge | |
| P9 | `galaxium-travels` submodule initialised | `ls galaxium-travels/booking_system_frontend` exits 0 | |

---

## Track B — Beginner

### Lab B1 — Explore Modes & Build the OpenSlava 2026 Welcome App

**Setup:** Open IBM Bob on an **empty folder** (not the openslava repo).

| # | Step | Action | Expected result | Status | Notes |
|---|---|---|---|---|---|
| B1-01 | Open empty folder | Open any empty directory in Bob | Bob opens with no files listed in the file tree | | |
| B1-02 | Switch to Ask mode | Click Ask in the mode selector | Mode indicator shows "Ask" | | |
| B1-03 | Ask about modes | Paste prompt: *"What are the three built-in Bob modes, what tools does each one permit, and when should I use each?"* | Bob returns a response describing Ask (read-only), Plan (read + propose), and Agent (read/write/command). No files are created or modified | | |
| B1-04 | Verify Ask is read-only | Attempt to run a shell command from Ask mode | Bob cannot run commands; no terminal output appears | | |
| B1-05 | Switch to Plan mode | Click Plan in the mode selector | Mode indicator shows "Plan" | | |
| B1-06 | Plan the Welcome App | Paste the Vite/React/confetti planning prompt exactly as written in lab B1 Step 2 | Bob produces a component list, CSS animation approach, and file layout. **No files are written to disk** | | |
| B1-07 | Verify Plan writes nothing | Check the empty folder's contents after Plan response | Folder remains empty | | |
| B1-08 | Switch to Agent mode | Click Agent in the mode selector | Mode indicator shows "Agent" | | |
| B1-09 | Implement the Welcome App | Paste the Agent implementation prompt from lab B1 Step 3 | Bob requests approval to run `npm create vite`; approve. Bob creates `src/WelcomeScreen.tsx` and `src/confetti.ts` | | |
| B1-10 | Verify scaffolded files | After Agent completes, check that these files exist: `src/WelcomeScreen.tsx`, `src/confetti.ts`, `src/index.css`, `package.json` | All four files present | | |
| B1-11 | Run the app | Run `npm run dev` in the scaffolded folder | Server starts; no build errors; `http://localhost:5173` is reachable | | |
| B1-12 | Verify confetti loads | Open `http://localhost:5173` in a browser | Full-screen IBM Bob blue (#0f62fe) background, "Welcome to OpenSlava 2026" heading, confetti animation plays on load | | |
| B1-13 | Reflection task | Click **+ New task**, switch to Ask mode, send the reflection prompt about npm install in Ask/Plan mode | Bob gives a coherent answer about mode permissions. No commands are executed | | |

---

### Lab B2 — Connect & Expand Galaxium Travels: Flights with Layovers

**Setup:** Galaxium Travels repo cloned and reachable.

| # | Step | Action | Expected result | Status | Notes |
|---|---|---|---|---|---|
| B2-01 | Navigate to repo | `cd galaxium-travels` | Shell prompt is inside `galaxium-travels/` | | |
| B2-02 | Start the app | `./start.sh` | Script runs without error; waits ~2 minutes. Backend on `:8001`, frontend on `:5173` | | |
| B2-03 | Verify Galaxium UI | Open `http://localhost:5173` | Galaxium flight booking UI loads; at least one route is displayed | | |
| B2-04 | Open repo in Bob | Open `galaxium-travels/` folder in IBM Bob | Bob shows the file tree of the repo | | |
| B2-05 | Switch to Agent mode | Click Agent | Mode indicator shows "Agent" | | |
| B2-06 | Run `/init` | Type `/init` and send | Bob reads the codebase and writes `AGENTS.md`, `.bob/rules-agent/AGENTS-agent.md`, `.bob/rules-plan/AGENTS-plan.md`, `.bob/rules-ask/AGENTS-ask.md` | | |
| B2-07 | Verify AGENTS.md content | Open `AGENTS.md` in the repo | File is non-empty. Mentions: the three services (frontend/backend/hold), Tailwind tokens, FastMCP, and the constraint about MCP tools matching REST endpoints | | |
| B2-08 | Verify all four context files | Check `.bob/rules-agent/AGENTS-agent.md`, `.bob/rules-plan/AGENTS-plan.md`, `.bob/rules-ask/AGENTS-ask.md` | All three files exist and are non-empty | | |
| B2-09 | Plan layovers (Plan mode) | Switch to Plan mode, paste the layovers planning prompt | Bob produces a plan touching: TypeScript types, Python models, price calculation (+10% per stop), and UI card update. **No files written** | | |
| B2-10 | Implement layovers (new task) | Click **+ New task**, switch to Agent mode, paste the layovers implementation prompt | Bob edits: `models.py` (LayoverStop), `server.py` (route + MCP tool), `types/` (TypeScript type), `Flights.tsx`, and creates `LayoverBadge` component | | |
| B2-11 | Verify backend model | Open `booking_system_backend/models.py` | `LayoverStop` model exists with `planet` (string) and `duration_minutes` (int) fields | | |
| B2-12 | Verify MCP tool | Open `booking_system_backend/server.py` | New MCP tool registration exists alongside the REST endpoint for layovers | | |
| B2-13 | Verify TypeScript type | Open `booking_system_frontend/src/types/` | `LayoverStop` TypeScript type file exists | | |
| B2-14 | Restart and test | Restart the backend, refresh browser | Route cards display layover stops inline; multi-stop routes show badge | | |
| B2-15 | Verify in Ask mode | Switch to Ask mode, send the AGENTS.md constraint verification prompt | Bob confirms (or identifies gaps in) the REST+MCP constraint compliance. No files changed | | |

---

### Lab B3 — Date Picker, Price Ranker & Booking Agent

**Setup:** Galaxium Travels running from B2, Bob has `galaxium-travels/` open in Agent mode.

| # | Step | Action | Expected result | Status | Notes |
|---|---|---|---|---|---|
| B3-01 | Enhancement 1: Date picker | Paste the date picker prompt in Agent mode | Bob adds a native `<input type="date">` to the flight search form. No external date library is imported in `package.json` | | |
| B3-02 | Test date input | Refresh browser, select a date | Results list updates client-side to show only flights on that date | | |
| B3-03 | Enhancement 2: Sort toggle | Paste the sort toggle prompt in Agent mode | Bob adds a button that cycles between "Price: Low to High" and "Price: High to Low". Sort is implemented in component state | | |
| B3-04 | Test sort toggle | Refresh browser, click the sort toggle | Flight results re-order on each click; no page reload | | |
| B3-05 | Enhancement 3: BookingAgent plan | Switch to Plan mode, paste the BookingAgent planning prompt | Bob produces a design: text input + submit, keyword matcher, intent detector (cheapest/fastest), top-3 result display. No files written | | |
| B3-06 | BookingAgent implementation | Click **+ New task**, switch to Agent mode, paste the BookingAgent implementation prompt | Bob creates `BookingAgent` component with: text input, intent parser, flight filter/ranker, top-3 card display | | |
| B3-07 | Test BookingAgent | In browser, type `"cheapest route to Europa"` and submit | Top 3 cheapest Europa flights are displayed as cards | | |
| B3-08 | Ask mode explanation | Switch to Ask mode, ask how BookingAgent decides "cheapest" intent | Bob explains the client-side logic clearly. No files changed | | |

---

## Track I — Intermediate

### Lab I1 — GitHub SDLC with Bob

**Setup:** GitHub account with PAT (`repo` scope). GitHub MCP installed in Bob.

| # | Step | Action | Expected result | Status | Notes |
|---|---|---|---|---|---|
| I1-01 | Open lab folder | `cd intermediate/labs/github-sdlc` and open in Bob | Bob shows the file tree including `WORKSHOP-part1-BUILD.md`, `.github/`, `.bob/` | | |
| I1-02 | Verify GitHub MCP | Bob sidebar → MCP section | GitHub entry visible, no red error badge | | |
| I1-03 | Install GitHub MCP (if needed) | Marketplace → GitHub → Install → set `GITHUB_TOKEN` | No error badge after setup | | |
| I1-04 | Plan the finance dashboard | Agent mode, paste the review + plan prompt | Bob proposes a build plan: directory structure, data-fetching strategy, UI sections, testing strategy | | |
| I1-05 | Scaffold the app | Paste the scaffold prompt | Bob creates `finance-app/` directory with: `src/`, `components/`, `services/`, `package.json`, `README.md` | | |
| I1-06 | Verify scaffold structure | Check `finance-app/` contents | Directories `src/`, `components/`, `services/` exist | | |
| I1-07 | Implement data layer (new task) | **+ New task**, paste the Yahoo Finance data layer prompt | Bob implements a finance service with functions for Euro Stoxx 50, DAX, Nikkei, DJI, and MSCI World; normalised data shape | | |
| I1-08 | Implement dashboard views | In same chat, paste the dashboard views prompt | Bob creates 3 views: current day, last 7 days, last quarter — all five indices — using charts and summary cards | | |
| I1-09 | Run the app | `cd finance-app && npm install && npm start` | App starts; `http://localhost:3000` (or Vite port) loads the dashboard without console errors | | |
| I1-10 | Add validation and tests (new task) | **+ New task**, paste the validation prompt | Bob adds unit tests for data utilities, integration test for a dashboard view with MSW mocks, and a `validate` script in `package.json` | | |
| I1-11 | Run validate | `npm run validate` | Lint, type-check, tests, and build all pass. Exit code 0 | | |
| I1-12 | Create GitHub repo | Go to github.com/new, create `finance-app` (no README, no .gitignore) | Repo created and URL available | | |
| I1-13 | Copy CI config | `cp -r .github finance-app/.github` from the lab root | `.github/workflows/` exists inside `finance-app/` | | |
| I1-14 | Init and push | Run the git init/add/commit/remote/push commands from the lab | `git push` succeeds; repo visible on GitHub with all files | | |
| I1-15 | Enable Issues on GitHub | GitHub → Settings → General → Issues checkbox | Issues tab visible on the repo | | |
| I1-16 | Create feature branch | `git checkout -b feature/user-selected-chart && git push -u origin feature/user-selected-chart` | Branch visible on GitHub | | |
| I1-17 | Create GitHub issue | GitHub Issues → New issue with the specified title and body | Issue created; note the issue number (e.g. `#1`) | | |
| I1-18 | Issue-to-PR: analyse (new task) | **+ New task** in Agent mode, paste the "Fetch and analyze" prompt with actual issue number | Bob calls GitHub MCP `get_issue`; returns the feature description and identifies files to change | | |
| I1-19 | Issue-to-PR: implement | In same chat, paste the implement prompt | Bob adds user input for stock ticker, fetches and displays chart, preserves existing views | | |
| I1-20 | Issue-to-PR: validate | In same chat, paste the validation prompt | Bob runs `npm run validate`; reports pass/fail accurately | | |
| I1-21 | Review and commit (new task) | **+ New task**, paste the review-and-commit prompt | Bob summarises changes, fixes obvious issues, commits with a meaningful message, pushes to `feature/user-selected-chart` | | |
| I1-22 | Create PR via `/create-pr` | In same chat, type `/create-pr` | Workflow dialog appears. Click "Start workflow", leave repo + base branch pre-filled, click "Generate PR Description" | | |
| I1-23 | Verify PR generated | Bob generates PR description | PR title and body visible in dialog; body references issue number (e.g. `closes #1`) | | |
| I1-24 | Verify PR on GitHub | Visit GitHub Pull requests tab | PR exists; description references issue number | | |
| I1-25 | Reflection | Switch to Ask mode, paste the reflection prompt about automation vs. human steps | Bob identifies: human steps (review, approve, PR review); automated steps (finding files, writing messages, referencing issue) | | |

---

### Lab I2 — Author, Modify & Commit Rules

**Setup:** `galaxium-travels/` open in Bob from Lab B2.

| # | Step | Action | Expected result | Status | Notes |
|---|---|---|---|---|---|
| I2-01 | Create rules directory | Agent mode: `mkdir -p .bob/rules` | `.bob/rules/` directory exists | | |
| I2-02 | Create global rules file | Create `.bob/rules/01-standards.md` with the JSDoc + concise responses + `internal-monologue/` rule content from the lab | File exists with correct content | | |
| I2-03 | Test rules: add utility function | Agent mode, paste the `formatPrice` prompt | Bob adds `formatPrice` to `api.ts` **with a JSDoc comment** (not prompted); a new file appears in `internal-monologue/` | | |
| I2-04 | Verify JSDoc was added | Open `booking_system_frontend/src/services/api.ts` | `formatPrice` has a JSDoc comment block above it | | |
| I2-05 | Verify internal-monologue file | Check `internal-monologue/` directory | At least one file with a timestamp prefix exists (e.g. `2026-01-15_update-api.md`) | | |
| I2-06 | Modify rules | Edit `.bob/rules/01-standards.md`: change `internal-monologue/` to `bob-log/` | File saved with updated path | | |
| I2-07 | Test modified rule | Agent mode (new task), paste the `formatDate` prompt | Bob writes to `bob-log/` (not `internal-monologue/`) | | |
| I2-08 | Verify new log directory | Check `bob-log/` directory | New file created with timestamp prefix in `bob-log/`, not in `internal-monologue/` | | |
| I2-09 | Add mode-scoped rule | Create `.bob/rules-agent/02-agent-commits.md` with the auto-commit rule content | File exists at the correct path | | |
| I2-10 | Test auto-commit | Agent mode (new task), make a small code change (rename any variable) | Bob commits automatically after the change; `git log` shows a new commit with a descriptive message | | |
| I2-11 | Verify git commit | `git log --oneline -1` | Most recent commit message is descriptive (not blank or generic "update") | | |
| I2-12 | Commit the rules | `git add .bob/ && git commit -m "Add team Bob rules for Galaxium Travels"` | Commit succeeds; `.bob/rules/`, `.bob/rules-agent/` tracked in git | | |
| I2-13 | Verify rules persist after restart | Close and reopen Bob; make a simple Agent request | `bob-log/` gets a new entry without being prompted | | |

---

## Track E — Expert

### Lab E1 — GFM Bank: Architecture, React UI & Security Audit

**Setup:** `expert/labs/banking-industry/gfm-bank/` available.

| # | Step | Action | Expected result | Status | Notes |
|---|---|---|---|---|---|
| E1-01 | Start GFM Bank API | `cd expert/labs/banking-industry/gfm-bank && ./start.sh` | API starts at `http://127.0.0.1:8000`; Swagger docs available at `http://127.0.0.1:8000/docs` | | |
| E1-02 | Verify API is local-only | Check the bind address in `start.sh` or `demo_api.py` | Server binds to `127.0.0.1`, not `0.0.0.0` | | |
| E1-03 | Verify credentials table | Test login with `teller/teller123` and `backoffice/backoffice123` via Swagger or curl | Both logins succeed and return JWT tokens | | |
| E1-04 | Open gfm-bank in Bob | Open `expert/labs/banking-industry/gfm-bank/` in Bob | File tree shows `demo_api.py`, `teller_client.py`, `backoffice_client.py` | | |
| E1-05 | Part 1: architecture analysis | Ask mode, paste the architecture analysis prompt | Bob returns: architecture explanation, role-based access description, transaction processing logic, a Mermaid component diagram, and a sequence diagram for money transfer | | |
| E1-06 | Verify Mermaid diagrams | Inspect the Ask response | Two Mermaid code blocks present: one component/architecture diagram and one sequence diagram | | |
| E1-07 | Verify no files changed | Check `git status` in gfm-bank | No modified files — Ask mode made no changes | | |
| E1-08 | Part 2: build React UI (new task) | **+ New task**, Agent mode, paste the React teller front-end prompt | Bob scaffolds a React + Vite app with: login form (credentials from .env), server health indicator, balance inquiry, transaction history, money transfer form, overdraft request message | | |
| E1-09 | Verify credentials in .env | Open the generated `.env` file | Credentials are in `.env`, not hardcoded in source files | | |
| E1-10 | Verify plain CSS | Check `package.json` of the generated UI | No Tailwind, MUI, Bootstrap, or other component library listed | | |
| E1-11 | Run the teller UI | `npm install && npm run dev` in the generated UI folder | App starts without build errors; login form renders | | |
| E1-12 | Part 3: security audit (new task) | Open `expert/labs/banking-industry/security-audit/code/` in Bob, **+ New task**, Agent mode, paste the security audit prompt | Bob returns a numbered finding list with: file, line, CWE category, severity, attack scenario, and remediation | | |
| E1-13 | Verify minimum finding count | Count findings in the response | At least 12 findings listed (as noted in the lab tip) | | |
| E1-14 | Verify expected finding types | Check findings include: hardcoded credentials, SQL injection, command injection, pickle deserialization, disabled SSL, MD5 password hashing | All 6 vulnerability classes present in the report | | |
| E1-15 | Verify SECURITY_AUDIT_REPORT.md | Check file was created | `SECURITY_AUDIT_REPORT.md` exists in `security-audit/code/` with all findings documented | | |

---

### Lab E2 — `/init`, Re-Init & Fintech Rules

**Setup:** `expert/labs/banking-industry/gfm-bank/` open in Bob, API running from E1.

| # | Step | Action | Expected result | Status | Notes |
|---|---|---|---|---|---|
| E2-01 | Run `/init` | Agent mode, type `/init` and send | Bob writes `AGENTS.md` plus the three mode-specific files in `.bob/rules-*/` | | |
| E2-02 | Verify AGENTS.md content | Open `AGENTS.md` | Mentions: FastAPI, Python, JWT auth, Decimal usage, module structure; non-trivial (>15 lines) | | |
| E2-03 | Verify mode-specific files | Check `.bob/rules-agent/AGENTS-agent.md`, `.bob/rules-plan/AGENTS-plan.md`, `.bob/rules-ask/AGENTS-ask.md` | All three files exist and contain mode-appropriate content (agent: file patterns; plan: architecture; ask: overview) | | |
| E2-04 | Create fintech rules | Create `.bob/rules/fintech-standards.md` with the Decimal + audit log rules from the lab | File exists with correct content | | |
| E2-05 | Test Decimal rule | Agent mode, paste the `calculate_transfer_fee` prompt | Function uses `Decimal`, not `float`, in the implementation | | |
| E2-06 | Verify Decimal in code | Open `demo_api.py` | `calculate_transfer_fee` imports and uses `Decimal` | | |
| E2-07 | Verify audit log created | Check `bob-audit/audit.log` | File exists with at least one entry in the format `[ISO timestamp] [mode] [description]` | | |
| E2-08 | Add notifications module | Agent mode, paste the notifications module prompt | `notifications/` directory created with `send_alert` function; function logs a structured message | | |
| E2-09 | Re-run `/init` | Agent mode, type `/init` | Bob re-generates `AGENTS.md` | | |
| E2-10 | Verify notifications in AGENTS.md | Open `AGENTS.md` | `notifications/` module appears in the codebase map | | |
| E2-11 | Commit | `git add . && git commit -m "Add fintech Bob rules and updated AGENTS.md"` | Commit succeeds | | |

---

### Lab E3 — Custom Mode, Mode-Scoped Rules & Re-Init

**Setup:** `expert/labs/banking-industry/gfm-bank/` open in Bob, E2 complete.

| # | Step | Action | Expected result | Status | Notes |
|---|---|---|---|---|---|
| E3-01 | Open custom modes file | Bob Settings → Modes → Edit Project Modes | `.bob/custom_modes.yaml` opens in editor | | |
| E3-02 | Add fintech-reviewer mode | Add the complete YAML block from the lab | File saved; YAML is valid (no parse errors) | | |
| E3-03 | Verify mode appears in sidebar | Check mode selector | `🏦 Fintech Reviewer` appears as a selectable mode | | |
| E3-04 | Verify slash command works | Type `/fintech-reviewer` in chat | Bob switches to Fintech Reviewer mode | | |
| E3-05 | Verify tool groups | In Fintech Reviewer mode, attempt to create a file | Bob cannot create/edit files; reports that edit tools are unavailable | | |
| E3-06 | Create mode-scoped rules | Create `.bob/rules-fintech-reviewer/01-pci-checklist.md` with the five PCI-DSS checklist items | File exists at exact path | | |
| E3-07 | Test the mode: review | Switch to Fintech Reviewer, paste the payments module review prompt | Bob returns a numbered finding list with severity levels (Critical/High/Medium/Low) | | |
| E3-08 | Verify read-only enforcement | While in Fintech Reviewer mode, ask "Fix the SQL injection in data_pipeline.py" | Bob refuses; explains it lacks edit tools | | |
| E3-09 | Re-init after mode creation | Agent mode, run `/init` | `AGENTS.md` updated; custom mode (`fintech-reviewer`) now documented in `AGENTS.md` | | |
| E3-10 | Commit | `git add .bob/ && git commit -m "Add fintech-reviewer custom mode and PCI-DSS review checklist"` | Commit succeeds | | |
| E3-11 | Reflection: extension mechanisms | Ask mode, paste the extension mechanisms comparison prompt | Bob compares Rules vs. Custom Modes vs. MCP Servers with concrete examples; no files changed | | |

---

### Lab E4 — GitHub MCP Integration

**Setup:** GFM Bank code committed and pushed to a GitHub repo. GitHub MCP configured with a PAT.

| # | Step | Action | Expected result | Status | Notes |
|---|---|---|---|---|---|
| E4-01 | Push GFM Bank to GitHub | Run the `git init && git add . && git commit` sequence from the lab (or use `gh repo create`) | Repo visible on GitHub with all files including `.bob/` | | |
| E4-02 | Verify `.bob/` committed | Check GitHub repo | `.bob/rules/`, `.bob/custom_modes.yaml`, `AGENTS.md` all visible | | |
| E4-03 | Create issue via Bob | Agent mode, paste the create-issue prompt | Bob calls `create_issue` via GitHub MCP; issue appears on GitHub with correct title, label, and body | | |
| E4-04 | Note issue number | Open GitHub Issues tab | Issue number recorded (e.g. `#1`) | | |
| E4-05 | Issue-to-PR loop (new task) | **+ New task**, Agent mode, paste the full issue-to-PR prompt | Bob: reads issue (`get_issue`), creates branch (`create_branch`), implements `GET /transactions/{account_id}/export` in `demo_api.py`, commits, opens PR referencing issue number | | |
| E4-06 | Verify MCP tool calls | Watch approval panel | Approvals appear for: `get_issue`, `create_branch`, `create_or_update_file` (or `push_files`), `create_pull_request` | | |
| E4-07 | Verify CSV endpoint in code | Open `demo_api.py` | New endpoint `GET /transactions/{account_id}/export` returns `Content-Type: text/csv` with columns `booking_ts`, `amount_eur`, `type` | | |
| E4-08 | Verify PR on GitHub | Visit Pull requests tab | PR exists; description references `#<issue-number>` | | |
| E4-09 | Test the endpoint | Paste the endpoint test prompt with sample IBAN | Bob invokes the endpoint (via Bob shell or direct request); CSV output returned with correct columns | | |
| E4-10 | Verify PR links to issue | Inspect PR description | PR body contains `closes #<issue-number>` or `fixes #<issue-number>` | | |

---

## Challenge — PocketLedger

**Setup:** Empty folder. All prerequisites met. Fresh Bob session.

| # | Step | Action | Expected result | Status | Notes |
|---|---|---|---|---|---|
| CH-01 | Plan the project (Plan mode) | Plan mode, paste the full feature list (F1–F10) as the planning prompt | Bob produces architecture plan: FastAPI backend structure, React/Vite frontend structure, SQLite schema, auth pattern, test strategy | | |
| CH-02 | Scaffold both services (new task, Agent) | **+ New task**, Agent mode, scaffold backend and frontend per the plan | `backend/` and `frontend/` directories created; `backend/main.py`, `frontend/src/App.tsx`, `requirements.txt`, `package.json` present | | |
| CH-03 | Run `/init` on skeleton | Agent mode, `/init` | `AGENTS.md` generated; describes two-service architecture, auth model, database layer | | |
| CH-04 | Verify AGENTS.md content | Open `AGENTS.md` | Mentions: FastAPI, React, SQLite, bearer token from `POCKETLEDGER_TOKEN` env var; >20 lines | | |
| CH-05 | Create rules file | Create `.bob/rules/pocketledger-standards.md` with the three required rules from B-REQ-2 | File exists; all three rules present (float precision, JSDoc props, audit.log append) | | |
| CH-06 | Implement F1 — Add transaction | **+ New task**, Agent mode, implement `POST /transactions` endpoint + frontend form | Endpoint accepts `amount`, `description`, `category`, `date`; frontend form sends to backend; float rounded to 2 decimal places | | |
| CH-07 | Verify audit.log after F1 | Check `bob-audit/audit.log` | At least one entry in format `[ISO timestamp] [mode] [description]` | | |
| CH-08 | Implement F2 — List transactions | **+ New task**, implement `GET /transactions` (newest first) + frontend list view | Endpoint returns transactions sorted by date descending; UI displays them | | |
| CH-09 | Implement F3 — Delete transaction | **+ New task**, implement `DELETE /transactions/{id}` + delete button in UI | Transaction removed from DB and list on delete | | |
| CH-10 | Implement F4 — Live balance | Live balance display in frontend | Sum of all amounts (signed) shown; updates without page reload | | |
| CH-11 | Implement F5 — Category breakdown | **+ New task**, implement category aggregation endpoint + frontend display | Backend returns `{category: total}` aggregation; frontend shows it | | |
| CH-12 | Implement F6 — Bar chart | **+ New task** (Plan first: vanilla JS Canvas/SVG bar chart), then Agent implement | Chart rendered using Canvas API or SVG; no Chart.js/D3/Recharts in `package.json` | | |
| CH-13 | Implement F7 — Category filter | Category dropdown filter in frontend | Dropdown populated from categories; selecting one filters the transaction list client-side | | |
| CH-14 | Implement F8 — SQLite persistence | Data persisted to SQLite | Transactions survive server restart; `sqlite3` or SQLAlchemy used, not an in-memory store | | |
| CH-15 | Implement F9 — Bearer token auth | All API endpoints protected | Every endpoint returns 401 without the correct `POCKETLEDGER_TOKEN` bearer token | | |
| CH-16 | Implement F10 — Unit tests | At least 5 unit tests for data layer | `pytest` runs and passes with ≥5 tests in the backend directory | | |
| CH-17 | Run tests | `cd backend && pytest` | Exit code 0; ≥5 tests pass | | |
| CH-18 | Create ledger-reviewer mode | Create `.bob/custom_modes.yaml` with `ledger-reviewer` (read + mcp only) | Mode appears in Bob sidebar; has correct tool groups (no edit, no command) | | |
| CH-19 | Run ledger review | Switch to ledger-reviewer, ask for a review | Bob returns findings covering float precision, hardcoded secrets, input validation | | |
| CH-20 | Save review output | Copy review output to `ledger-review/initial-review.md` | File exists and is non-empty | | |
| CH-21 | Re-run `/init` | Agent mode, `/init` | `AGENTS.md` updated; `ledger-reviewer` mode documented | | |
| CH-22 | Push to GitHub | Create GitHub repo, push all code | Repo visible on GitHub | | |
| CH-23 | Create CSV export issue | GitHub Issues → create "Add CSV export for transactions" issue | Issue created with descriptive body; issue number noted | | |
| CH-24 | Issue-to-PR: implement CSV export | Agent mode (with GitHub MCP), implement CSV export endpoint on feature branch, push, open PR | PR exists on GitHub referencing the issue number | | |
| CH-25 | Use `/create-pr` | After commits pushed, type `/create-pr` | Workflow dialog appears; PR description auto-generated with issue reference | | |
| CH-26 | Run `start.sh` from root | `./start.sh` (or the script created per Hint 4) | Both backend (`:8000`) and frontend (`:5173` or similar) start without error | | |
| CH-27 | Facilitator checklist: all features | Load the running app and manually test F1–F10 | All 10 features work end-to-end | | |
| CH-28 | Facilitator checklist: Bob artefacts | Check file existence: `AGENTS.md`, `.bob/rules/pocketledger-standards.md`, `bob-audit/audit.log`, `.bob/custom_modes.yaml`, `ledger-review/initial-review.md` | All five files present and non-empty | | |

---

## Cross-cutting tests

These tests apply across all tracks and validate structural correctness of the lab materials.

| # | Check | How to verify | Expected result | Status |
|---|---|---|---|---|
| CC-01 | All mermaid diagrams in lab docs render | Open `http://localhost:8000` (MkDocs) and visually inspect each mermaid block on every lab page | No mermaid parse errors; all flowcharts render correctly | |
| CC-02 | All internal links in docs resolve | Run `mkdocs serve` and click every link in the nav and body | No 404s | |
| CC-03 | `requirements.txt` installs cleanly | `pip install -r requirements.txt` | No dependency conflicts or resolution errors | |
| CC-04 | MkDocs builds without warnings | `mkdocs build --strict` | Exit code 0; no warnings | |
| CC-05 | All code blocks in beginner lab use correct paths | Grep for hardcoded paths like `galaxium-travels/` in the beginner lab | Paths match actual repo structure | |
| CC-06 | GFM Bank `start.sh` is executable | `ls -l expert/labs/banking-industry/gfm-bank/start.sh` | Execute bit set | |
| CC-07 | Security audit files contain known vulnerabilities | Open `data_pipeline.py` and `synthetic_generator.py` | Hardcoded credentials, SQL injection, pickle deserialization, disabled SSL, MD5 hashing present — at least 12 issues across both files | |
| CC-08 | Galaxium `start.sh` exits cleanly | `./start.sh` then Ctrl-C after UI loads | No Python import errors or Node build errors during startup | |
| CC-09 | `.bob/mcp.json` is valid JSON | `cat .bob/mcp.json | python3 -m json.tool` | Valid JSON, no parse errors | |
| CC-10 | `mkdocs.yml` nav references match actual files | Compare `nav:` entries in `mkdocs.yml` with files in `docs/labs/` | Every nav entry has a matching file | |

---

## Issues log

Record all failures and warnings here during testing.

| # | Lab | Step | Severity | Description | Fix applied | Resolved |
|---|---|---|---|---|---|---|
| — | — | — | — | *No issues yet* | — | — |

---

## Sign-off

| Track | Tester | Date | All PASS? | Notes |
|---|---|---|---|---|
| Beginner (B1–B3) | | | | |
| Intermediate (I1–I2) | | | | |
| Expert (E1–E4) | | | | |
| Challenge | | | | |
| Cross-cutting | | | | |
