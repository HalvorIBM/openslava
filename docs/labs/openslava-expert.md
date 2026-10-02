# OpenSlava — Expert Track

Four labs · ~90 minutes total · For experienced Bob users

---

## Track Overview

| # | Lab | Time | Goal |
|---|---|---|---|
| E1 | **GFM Bank: Architecture, React UI & Security Audit** | 25 min | Three-part banking lab — understand, build, and secure |
| E2 | **`/init`, Re-Init & Fintech Rules** | 20 min | Deep dive into `/init` and production-grade rules authoring |
| E3 | **Custom Mode, Mode-Scoped Rules & Re-Init** | 20 min | Build a read-only `fintech-reviewer` mode with PCI-DSS rules |
| E4 | **GitHub MCP Integration** | 25 min | Issue → branch → implement → PR driven entirely by Bob with GitHub MCP |

---

## Prerequisites

- [ ] VS Code installed with IBM Bob extension, signed in
- [ ] Python 3.11+ and Node.js 20 LTS installed
- [ ] Git configured with `user.name` and `user.email`
- [ ] GitHub account with a personal access token (`repo` scope) — needed for E4
- [ ] GitHub MCP installed in Bob — needed for E4

---

## Lab E1 — GFM Bank: Architecture, React UI & Security Audit

**25 minutes**

### What you will learn

The GFM Bank lab is an industry-grade demo with a Python/FastAPI backend, a teller CLI, a back-office CLI, and a deliberately vulnerable data pipeline. This lab runs all three parts in compressed form.

### Setup

```bash
cd labs/banking-industry/gfm-bank
./start.sh
```

API running at `http://127.0.0.1:8000` · Docs at `http://127.0.0.1:8000/docs`

**Test credentials:**

| User | Password | Role |
|---|---|---|
| `teller` | `teller123` | TELLER |
| `backoffice` | `backoffice123` | BACKOFFICE |

**Sample IBAN:** `DE89545769475769453536` (Alice Müller)

### Part 1 — Architecture Understanding (8 min)

Open `labs/banking-industry/gfm-bank/` in VS Code. Switch to **Ask** mode:

```
Analyse the GFM Bank codebase (demo_api.py, teller_client.py, backoffice_client.py).
Explain the architecture, the role-based access model, and the transaction processing logic.
Create a Mermaid diagram showing the system components and a sequence diagram for a money transfer.
```

### Part 2 — Build the React Teller UI (10 min)

Switch to **Agent** mode:

```
Build a React + Vite teller front-end for GFM Bank connected to http://127.0.0.1:8000.
Include: login form (credentials from .env), server health indicator, balance inquiry,
transaction history, money transfer form, and overdraft request message.
Plain CSS — no external component library.
```

### Part 3 — Security Audit (7 min)

Open `labs/banking-industry/security-audit/code/` in VS Code. Switch to **Agent** mode:

```
Analyse data_pipeline.py and synthetic_generator.py for security vulnerabilities.
For each finding provide: file, line, CWE category, severity, attack scenario,
and remediation recommendation.
Then generate SECURITY_AUDIT_REPORT.md.
```

!!! tip "Expected findings"
    Bob should find at minimum: hardcoded credentials, SQL injection, command injection, insecure `pickle` deserialization, disabled SSL, and MD5 password hashing. A total of 12 vulnerabilities across both files.

---

## Lab E2 — `/init`, Re-Init & Fintech Rules

**20 minutes** · Requires E1 complete

### What you will learn

`/init` reverse-engineers your codebase into a living `AGENTS.md` — Bob's persistent context document. Re-running it after adding modules updates that context. Rules let you encode compliance standards that Bob enforces automatically.

### Step 1 — Run /init

From `labs/banking-industry/gfm-bank/`, switch to **Agent** mode, type `/init` and send.

**Read `AGENTS.md`:**

- What did Bob infer about the project structure?
- What frameworks and patterns did it identify?
- What constraints did it record (e.g. Decimal for monetary values)?

**Open `.bob/rules-agent/AGENTS-agent.md`:** compare to the root file. What is mode-specific?

### Step 2 — Author fintech rules

Create `.bob/rules/fintech-standards.md`:

```markdown
All Python functions that handle monetary values must use the Decimal type, never float.

After every Bob interaction, append a one-line audit entry to bob-audit/audit.log
in the format: [ISO timestamp] [mode] [brief description of change]
```

### Step 3 — Test the rules

In **Agent** mode:

```
Add a function called calculate_transfer_fee to demo_api.py
that calculates a 0.1% fee on a transfer amount and returns the fee value.
```

**Observe:**

- Bob uses `Decimal` for the calculation automatically
- `bob-audit/audit.log` has a new entry

### Step 4 — Add a module and re-init

In **Agent** mode:

```
Add a notifications/ module with a send_alert(event: str, account_id: str) function
that logs a structured alert message.
```

Re-run `/init`. Open `AGENTS.md` — observe `notifications/` now appears in the codebase context.

### Step 5 — Commit

```bash
git add . && git commit -m "Add fintech Bob rules and updated AGENTS.md"
```

---

## Lab E3 — Custom Mode, Mode-Scoped Rules & Re-Init

**20 minutes** · Requires E2 complete

### What you will learn

Custom modes let you create role-specific Bob personas with their own tool restrictions and auto-injected instructions. A `fintech-reviewer` mode that can only read and report — never edit — is a powerful compliance tool.

### Step 1 — Create the custom mode

Open Bob Settings → **Modes** → **Edit Project Modes** (`.bob/custom_modes.yaml`).

Add the following complete mode definition:

```yaml
customModes:
  - slug: fintech-reviewer
    name: 🏦 Fintech Reviewer
    roleDefinition: >-
      You are a senior fintech code reviewer specialising in PCI-DSS compliance,
      Python Decimal correctness, and secure API design.
      You analyse code for correctness, security, and regulatory compliance.
      You never modify files — you only report findings.
    whenToUse: >-
      Use this mode to review banking application code for compliance
      and quality issues without risk of accidental changes.
    customInstructions: |-
      - Always check for float usage where Decimal is required in monetary calculations
      - Flag any hardcoded secrets, API keys, or credentials
      - Check that all user inputs are validated server-side
      - Verify error messages do not expose stack traces or internal paths
      - Output findings as a numbered list with severity: Critical / High / Medium / Low
    groups:
      - read
      - mcp
      - skill
```

!!! info "Why `read`, `mcp`, `skill` only?"
    Omitting `edit` and `command` makes this a **read-only** mode. Bob can analyse files and call MCP tools (e.g. to look up CVEs), but cannot write files or run commands. This is enforced at the tool-permission level — it cannot be overridden by a prompt.

### Step 2 — Mode-scoped rules

Create `.bob/rules-fintech-reviewer/01-pci-checklist.md`:

```markdown
When reviewing, always check these PCI-DSS items:

1. No card numbers, CVVs, or PINs logged or stored in plaintext
2. All API endpoints require authentication
3. Error messages do not reveal stack traces or internal file paths
4. All dependencies are on vendor-supported versions
5. Secrets and credentials are not hardcoded or committed to version control
```

### Step 3 — Test the mode

1. Switch to **🏦 Fintech Reviewer** mode in the Bob sidebar
2. Send:

```
Review the payments module (demo_api.py and data_pipeline.py)
for compliance issues.
```

**Observe:**

- Bob reports a numbered finding list with severities
- If you ask `"Fix the SQL injection in data_pipeline.py"`, Bob refuses — it has no `edit` tools

### Step 4 — Re-init and commit

Switch back to **Agent** mode. Re-run `/init` — the new custom mode now appears in `AGENTS.md`.

```bash
git add .bob/ && git commit -m "Add fintech-reviewer custom mode and PCI-DSS review checklist"
```

### Reflection

In **Ask** mode:

```
How do custom modes, rules, and MCP servers differ as Bob extension mechanisms?
When would you use each one?
```

---

## Lab E4 — GitHub MCP Integration

**25 minutes** · Requires E3 complete · GitHub account + PAT required

### What you will learn

MCP servers extend Bob with real-world integrations. GitHub MCP lets Bob read issues, create branches, commit code, and open PRs as native Bob actions — no shell scripts, no copy-paste.

### Step 1 — Install GitHub MCP (if not done in Intermediate track)

1. Bob sidebar → **Marketplace** → search **GitHub** → Install
2. Settings → MCP → GitHub → set `GITHUB_TOKEN` (needs `repo` scope)
3. Verify: no error badge; Bob shows GitHub tools in the sidebar

!!! tip "Push your banking lab to GitHub first"
    ```bash
    cd labs/banking-industry/gfm-bank
    git init && git add . && git commit -m "Initial GFM Bank commit"
    gh repo create gfm-bank --public --source=. --push
    ```
    Or use any repo you already have on GitHub.

### Step 2 — Create a GitHub issue with Bob

In **Agent** mode:

```
Use GitHub MCP to create a new issue in this repo titled
"Add transaction export to CSV endpoint"
with label "enhancement" and body:
"Users need to download their transaction history as a CSV file.
The endpoint should accept an account_id parameter and return
a CSV with columns: date, amount, type."
```

**Observe:** Bob calls the GitHub MCP `create_issue` tool. Verify the issue appears on GitHub.

### Step 3 — Issue-to-PR loop

```
Read the issue you just created.
Create a feature branch called "feature/csv-export".
Implement a GET /transactions/{account_id}/export endpoint in demo_api.py
that returns a CSV response (Content-Type: text/csv) with columns:
booking_ts, amount_eur, type.
Commit the change and open a pull request with a description referencing the issue number.
```

**Observe Bob:**

1. Reads the issue via `get_issue` MCP tool
2. Creates the branch via `create_branch`
3. Implements the endpoint in `demo_api.py`
4. Commits and pushes via `create_or_update_file` or `push_files`
5. Opens a PR via `create_pull_request` referencing `#<issue-number>`

### Step 4 — Verify the endpoint

```
Test the new export endpoint with the sample IBAN DE89545769475769453536.
Show me the CSV output.
```

### Discussion questions

- [ ] What other MCP servers would fit this banking domain? (Jira, PagerDuty, Datadog, Vault)
- [ ] How does GitHub MCP differ from Bob rules as an extension mechanism?
- [ ] When should you use a custom mode vs. a rule vs. an MCP server?

---

## Expert Track Reference

### Bob extension mechanisms — comparison

| Mechanism | Scope | Modifies files? | Requires setup? |
|---|---|---|---|
| **Rules** | Per-project or per-mode | No (informs Bob) | Create `.bob/rules/*.md` |
| **Custom modes** | Per-project | No (restricts tools) | Edit `.bob/custom_modes.yaml` |
| **MCP servers** | Per-workspace | Yes (via Bob actions) | Install from Marketplace + token |
| **`/init`** | Per-project | Yes (writes `AGENTS.md`) | Run once, re-run after changes |

### Mode tool groups reference

| Group | What it allows |
|---|---|
| `read` | Read files, search codebase |
| `edit` | Create and modify files |
| `command` | Run shell commands |
| `mcp` | Use installed MCP servers |
| `skill` | Use installed skills |
| `browser` | Web browsing |
| `subtask` | Spawn subtasks |
