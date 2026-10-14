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

- [ ] **IBM Bob IDE** installed and signed in — download from [bob.ibm.com/download](https://bob.ibm.com/download) (standalone app, not a VS Code extension), or **Bob Shell** if you prefer a terminal (`curl -fsSL https://bob.ibm.com/download/bobshell.sh | bash`)
- [ ] Python 3.11+ and Node.js 20 LTS installed
- [ ] Git configured with `user.name` and `user.email`
- [ ] GitHub account with a personal access token (`repo` scope) — needed for E4
- [ ] GitHub MCP installed in Bob — needed for E4

---

## Lab E1 — GFM Bank: Architecture, React UI & Security Audit

**25 minutes**

### What you will learn

The GFM Bank lab is an industry-grade demo with a Python/FastAPI backend, a teller CLI, a back-office CLI, and a deliberately vulnerable data pipeline. This lab runs all three parts in compressed form.

The three parts map directly to three Bob modes and three patterns you should carry into every real project:

1. **Ask** for architecture discovery — understand before you build
2. **Agent** for rapid UI scaffolding — Bob as a full-stack pair programmer
3. **Agent** for security audit — systematic vulnerability analysis, not just guesswork

### Setup

**1 — Clone the workshop repo** (skip if you already have it)

```bash
git clone git@github-halvoribm:HalvorIBM/openslava.git
cd openslava
```

**2 — Start the GFM Bank API**

```bash
cd expert/labs/banking-industry/gfm-bank
./start.sh
```

API running at `http://127.0.0.1:8000` · Docs at `http://127.0.0.1:8000/docs`

!!! info "Why localhost, not 0.0.0.0?"
    Notice the API binds to `127.0.0.1` — not all interfaces. This is a **security best practice**: development services should never be exposed on all network interfaces. The same rule applies to any service Bob scaffolds for you. If Bob suggests `0.0.0.0`, change it before running.

**Test credentials:**

| User | Password | Role |
|---|---|---|
| `teller` | `teller123` | TELLER |
| `backoffice` | `backoffice123` | BACKOFFICE |

**Sample IBAN:** `DE89545769475769453536` (Alice Müller)

### Part 1 — Architecture Understanding (8 min)

Open `expert/labs/banking-industry/gfm-bank/` in **IBM Bob**. Switch to **Ask** mode:

```
Analyse the GFM Bank codebase (demo_api.py, teller_client.py, backoffice_client.py).
Explain the architecture, the role-based access model, and the transaction processing logic.
Create a Mermaid diagram showing the system components and a sequence diagram for a money transfer.
```

!!! info "Why Ask mode for architecture discovery?"
    You are using Ask mode because you want to **understand the system, not change it**. Ask mode is read-only — Bob can read every file and reason about the full codebase, but cannot accidentally modify anything while exploring.

    This is the professional pattern before any major work on an unfamiliar codebase: understand first, then plan, then implement. Using Ask mode enforces this discipline at the tool level.

    Notice how Bob can produce a Mermaid diagram from code it reads — this is architecture documentation generated automatically from the source of truth, not a stale diagram someone drew once and never updated.

### Part 2 — Build the React Teller UI (10 min)

Switch to **Agent** mode. Start a **+ New task** first — you are switching from discovery to implementation:

```
Build a React + Vite teller front-end for GFM Bank connected to http://127.0.0.1:8000.
Include: login form (credentials from .env), server health indicator, balance inquiry,
transaction history, money transfer form, and overdraft request message.
Plain CSS — no external component library.
```

!!! tip "Load credentials from .env, not hardcoded"
    The prompt explicitly says "credentials from .env". This is intentional — **never hardcode passwords or tokens in source code**. Bob follows this instruction and generates a `.env` file pattern.

    If Bob proposes hardcoded credentials anywhere, correct it: `"Move these credentials to a .env file and load them with import.meta.env in Vite"`.

!!! tip "Reference the API spec as context"
    The GFM Bank API has Swagger docs at `http://127.0.0.1:8000/docs`. You can reference this as context by adding `@http://127.0.0.1:8000/openapi.json` in your prompt — Bob fetches the OpenAPI spec and uses the exact endpoint shapes. This produces accurate API client code without trial and error.

### Part 3 — Security Audit (7 min)

Open `expert/labs/banking-industry/security-audit/code/` in **IBM Bob**. Start a **+ New task** and switch to **Agent** mode:

```
Analyse data_pipeline.py and synthetic_generator.py for security vulnerabilities.
For each finding provide: file, line, CWE category, severity, attack scenario,
and remediation recommendation.
Then generate SECURITY_AUDIT_REPORT.md.
```

!!! tip "Expected findings"
    Bob should find at minimum: hardcoded credentials, SQL injection, command injection, insecure `pickle` deserialization, disabled SSL, and MD5 password hashing. A total of 12 vulnerabilities across both files.

!!! info "Why generate SECURITY_AUDIT_REPORT.md?"
    Asking Bob to write a structured audit report is a **smart documentation pattern**. The output:

    - Is immediately shareable with a security team
    - Traces each finding to a specific file and line
    - Includes CWE categories — machine-readable vulnerability identifiers used by security tooling
    - Persists across sessions (it is a file, not a chat message)

    In a real project, you would commit this report and reference it in your PR. The finding is now tracked, not buried in a chat transcript.

---

## Lab E2 — `/init`, Re-Init & Fintech Rules

**20 minutes** · Requires E1 complete

### What you will learn

`/init` reverse-engineers your codebase into a living `AGENTS.md` — Bob's persistent context document. Re-running it after adding modules updates that context. Rules let you encode compliance standards that Bob enforces automatically.

### The stateless problem at scale

In a 50-file banking application, asking Bob to discover the codebase fresh in every conversation wastes tokens and produces inconsistent results. Without context, Bob might:

- Use `float` for monetary values (losing precision)
- Miss the auth pattern used by existing endpoints
- Add a REST endpoint without the required MCP tool counterpart

`/init` solves this by writing **Bob's understanding of the project to disk**, where it persists across every conversation and every team member's machine. Rules go further: they encode the invariants Bob must never violate, regardless of who is prompting or what they ask for.

### Step 1 — Run `/init`

From `expert/labs/banking-industry/gfm-bank/`, switch to **Agent** mode, type `/init` and send.

**Read `AGENTS.md`:**

- What did Bob infer about the project structure?
- What frameworks and patterns did it identify?
- What constraints did it record (e.g. Decimal for monetary values)?

**Open `.bob/rules-agent/AGENTS.md`:** compare to the root file. What is mode-specific?

!!! info "Mode-specific AGENTS.md files"
    `/init` generates **four** context files:

    - `AGENTS.md` — root, loaded in all modes
    - `.bob/rules-agent/AGENTS.md` — extra context for Agent (file structure, implementation patterns)
    - `.bob/rules-plan/AGENTS.md` — extra context for Plan (architecture, constraints)
    - `.bob/rules-ask/AGENTS.md` — extra context for Ask (project overview, glossary)

    Each mode gets the context relevant to its purpose. Plan mode gets architecture guidance; Agent mode gets file layout and naming conventions.

### Step 2 — Author fintech rules

Create `.bob/rules/fintech-standards.md`:

```markdown
All Python functions that handle monetary values must use the Decimal type, never float.

After every Bob interaction, append a one-line audit entry to bob-audit/audit.log
in the format: [ISO timestamp] [mode] [brief description of change]
```

!!! info "Why `Decimal` over `float`?"
    This is a **real production rule** used in fintech systems. IEEE 754 floating-point arithmetic accumulates rounding errors that are unacceptable for financial calculations. `0.1 + 0.2` in Python float is `0.30000000000000004` — not `0.3`. For a bank, that is a compliance issue.

    Encoding this as a Bob rule means Bob enforces it automatically on every function it writes or modifies — no code review step required to catch it.

!!! info "The audit log pattern"
    The audit log rule creates a **machine-readable trail** of every Bob action. In regulated environments, you need to be able to answer: "on this date, what did the AI assistant change?" The `bob-audit/audit.log` file answers that question directly.

    Commit this log alongside your code for a complete development history.

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

!!! tip "Re-init after major structure changes"
    `/init` is not a one-time setup — it should be re-run whenever the project structure meaningfully changes:

    - After adding a new service or module
    - After a major refactor
    - When onboarding a new team member
    - Before a significant feature build

    Think of it as "refresh Bob's map of the codebase". Old `AGENTS.md` with stale paths leads to Bob guessing at file locations — always re-init when in doubt.

### Step 5 — Commit

```bash
git add . && git commit -m "Add fintech Bob rules and updated AGENTS.md"
```

!!! tip "Always commit `.bob/` alongside your code"
    Your Bob configuration is part of the project. Committing `.bob/rules/`, `.bob/custom_modes.yaml`, and `AGENTS.md` means:

    - New team members get the full Bob setup on `git clone`
    - Rule changes are code-reviewed like any other change
    - The history of what Bob was configured to do is auditable

---

## Lab E3 — Custom Mode, Mode-Scoped Rules & Re-Init

**20 minutes** · Requires E2 complete

### What you will learn

Custom modes let you create role-specific Bob personas with their own tool restrictions and auto-injected instructions. A `fintech-reviewer` mode that can only read and report — never edit — is a powerful compliance tool.

### Why custom modes exist

The three built-in modes (Ask, Plan, Agent) cover the development workflow. But real teams have additional workflows that don't fit neatly into "implement" or "review":

- A **compliance reviewer** who should never accidentally modify production code
- A **security auditor** who needs to check for specific vulnerability classes systematically
- A **documentation writer** who only updates `.md` files and never touches source code

Custom modes let you encode these roles with **enforced tool permissions**. The restrictions are at the tool level — they cannot be overridden by a clever prompt. If a mode lacks `edit`, Bob physically cannot write files, no matter what anyone asks.

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

    This is the key security property of custom modes: **the restriction is structural, not advisory**. You cannot accidentally break it by typing "just fix it while you're there".

!!! tip "The `slug` becomes a slash command"
    Once you create a mode with `slug: fintech-reviewer`, you can switch to it instantly by typing `/fintech-reviewer` in the chat. No menu navigation needed. Custom mode slugs become first-class slash commands automatically.

!!! info "Where to save the YAML file"
    - **`.bob/custom_modes.yaml`** — project-scoped, committed to the repo, shared with the team ✅
    - **`~/.bob/custom_modes.yaml`** — global, applies to all your workspaces

    For compliance roles that are project-specific, always use the project-scoped file. For personal productivity modes you use across all projects, use the global file.

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

!!! info "Mode-scoped rules for the custom mode"
    The directory name must match the mode slug: `.bob/rules-fintech-reviewer/`. Bob injects these rules only when that mode is active — so the PCI-DSS checklist runs automatically every time a review is started, without anyone having to remember to include it.

    This is **systematic compliance review**, not best-effort. The checklist is always present, always complete.

### Step 3 — Test the mode

1. Switch to **🏦 Fintech Reviewer** mode in the Bob sidebar (or type `/fintech-reviewer`)
2. Send:

```
Review the payments module (demo_api.py and data_pipeline.py)
for compliance issues.
```

**Observe:**

- Bob reports a numbered finding list with severities
- If you ask `"Fix the SQL injection in data_pipeline.py"`, Bob refuses — it has no `edit` tools

!!! tip "Pair the reviewer mode with an Agent task"
    A good workflow: run `fintech-reviewer` to get the finding list, then start a new Agent mode task and reference the findings: `"Fix findings 1, 3, and 5 from the fintech review."` The reviewer can't write, the agent can't see your restrictions — each mode does exactly one job.

### Step 4 — Re-init and commit

Switch back to **Agent** mode. Re-run `/init` — the new custom mode now appears in `AGENTS.md`.

```bash
git add .bob/ && git commit -m "Add fintech-reviewer custom mode and PCI-DSS review checklist"
```

!!! info "Re-init after adding custom modes"
    When you add a custom mode, re-running `/init` updates `AGENTS.md` to document the mode — its purpose, tool groups, and when to use it. This means:

    - New team members can discover the mode from `AGENTS.md`
    - Bob in any mode knows the `fintech-reviewer` mode exists and can suggest switching to it

### Reflection

In **Ask** mode:

```
How do custom modes, rules, and MCP servers differ as Bob extension mechanisms?
When would you use each one?
```

!!! info "Three extension mechanisms — when to use each"
    | Mechanism | What it does | Best for |
    |---|---|---|
    | **Rules** | Injects instructions into every conversation | Coding standards, output formats, audit logging |
    | **Custom modes** | Creates a new persona with restricted tool access | Compliance roles, specialist reviewers, safe read-only workflows |
    | **MCP servers** | Connects Bob to external systems | GitHub, Jira, Datadog, Vault — anything outside your filesystem |

    They compose: a `fintech-reviewer` mode (custom mode) with PCI rules (rules) that calls a CVE database (MCP) is a complete compliance workflow built from three primitives.

---

## Lab E4 — GitHub MCP Integration

**25 minutes** · Requires E3 complete · GitHub account + PAT required

### What you will learn

MCP servers extend Bob with real-world integrations. GitHub MCP lets Bob read issues, create branches, commit code, and open PRs as native Bob actions — no shell scripts, no copy-paste.

### Why this matters in a regulated codebase

In financial software, the audit trail is not optional. Every change must be traceable:

- **Why** was this change made? (Issue reference)
- **What** was changed? (PR diff)
- **Who** authorized it? (PR review)
- **When** did it happen? (commit timestamp)

Bob with GitHub MCP produces all four automatically. The issue description becomes the requirement. The PR description links to the issue. The commit timestamp is git. The review is your team's normal process. Bob handles the mechanical linkage so nothing falls through the cracks.

### Step 1 — Install GitHub MCP (if not done in Intermediate track)

**Option A — from the chat (recommended):** type `/configure-mcp`, search for **GitHub**, click **Install**, set `GITHUB_TOKEN` (`repo` scope).

**Option B — from the sidebar:** Marketplace → search **GitHub** → Install → Settings → MCP → GitHub → set `GITHUB_TOKEN`.

Verify: no error badge; Bob shows GitHub tools in the sidebar.

!!! warning "Authenticate `gh` CLI before pushing"
    The `gh repo create` command below requires the GitHub CLI to be authenticated. If you haven't done this yet:
    ```bash
    gh auth login
    ```
    Follow the prompts (select GitHub.com → HTTPS → browser). This is a one-time step. Without it, `gh repo create` will fail with an authentication error and block the steps that follow.

!!! tip "Push your banking lab to GitHub first"
    ```bash
    cd expert/labs/banking-industry/gfm-bank
    git init && git add . && git commit -m "Initial GFM Bank commit"
    gh repo create gfm-bank --public --source=. --push
    ```
    Or use any repo you already have on GitHub.

!!! info "Commit your `.bob/` configuration before pushing"
    The rules and custom modes you built in E2 and E3 should be committed before you push:
    ```bash
    git add .bob/ AGENTS.md && git commit -m "Add Bob configuration: fintech rules and custom modes"
    ```
    Anyone who clones your repo now gets the full Bob setup — context, standards, and compliance modes — immediately.

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

!!! tip "Write precise issue bodies"
    The quality of Bob's implementation is directly proportional to the quality of the issue body. A precise issue with column names, parameter names, and expected behaviour produces accurate code on the first pass. Vague issues ("add CSV export") produce vague implementations that require multiple correction rounds.

    This is the same discipline as writing a good acceptance criterion — it benefits both human developers and AI agents equally.

### Step 3 — Issue-to-PR loop

Start a **+ New task** in Bob (**Agent** mode):

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

!!! tip "Watch the MCP tool calls in the approval panel"
    Each GitHub MCP tool call appears as an approval prompt — `create_branch`, `create_or_update_file`, `create_pull_request`. Review them before approving. You can see exactly what branch name Bob chose, what the commit message says, and what the PR description looks like — before any of it happens on GitHub.

    This is the **propose, then approve** pattern at work on a remote system.

### Step 4 — Verify the endpoint

```
Test the new export endpoint for account ACC-001 (Alice Müller).
Show me the CSV output.
```

### Discussion questions

- [ ] What other MCP servers would fit this banking domain? (Jira, PagerDuty, Datadog, Vault)
- [ ] How does GitHub MCP differ from Bob rules as an extension mechanism?
- [ ] When should you use a custom mode vs. a rule vs. an MCP server?

!!! info "Suggested answers for discussion"
    - **Jira MCP** — same issue-to-PR pattern for teams not on GitHub
    - **Vault MCP** — Bob could rotate and reference secrets without ever seeing plaintext values
    - **Datadog MCP** — Bob could read production alerts and implement fixes without leaving the editor
    - **Rules** are project-internal standards. **MCP servers** connect to external systems. **Custom modes** restrict what Bob is allowed to do. All three compose cleanly.

---

## Expert Track Reference

### Bob extension mechanisms — comparison

| Mechanism | Scope | Modifies files? | Requires setup? | Version-controlled? |
|---|---|---|---|---|
| **Rules** | Per-project or per-mode | No (informs Bob) | Create `.bob/rules/*.md` | Yes — commit `.bob/` |
| **Custom modes** | Per-project or global | No (restricts tools) | Edit `.bob/custom_modes.yaml` | Yes — commit `.bob/` |
| **MCP servers** | Per-workspace | Yes (via Bob actions) | Install from Marketplace + token | `.bob/mcp.json` for project scope |
| **`/init`** | Per-project | Yes (writes `AGENTS.md`) | Run once, re-run after changes | Yes — commit `AGENTS.md` |

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

### Context hygiene reference

| Signal | Action |
|---|---|
| You are switching from planning to implementation | Start **+ New task** |
| Bob starts contradicting earlier responses | Start **+ New task** |
| The token counter is > 60% full | Start **+ New task** |
| You added a new module or service | Re-run `/init` |
| You are onboarding a new team member | Re-run `/init` + ensure `.bob/` is committed |
| You changed a rule and want it active now | Start **+ New task** (rules load on task start) |
