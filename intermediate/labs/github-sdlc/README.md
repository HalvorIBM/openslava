# IBM Bob GitHub SDLC Lab — Instructor Guide

This two-part lab shows how **IBM Bob** builds, validates, and evolves a React application end-to-end — from initial scaffolding to GitHub-driven feature delivery.

**Part 1** covers local development: Bob plans, builds, and validates a finance dashboard from scratch.
**Part 2** covers GitHub collaboration: Bob connects the app to a real repository, processes a feature request from a GitHub issue, implements it, and creates a pull request.

---

## Lab Goals

By the end of this lab, participants will have experienced how Bob can:

1. **Build from requirements** — scaffold a React app, integrate an external API, build dashboards, add tests
2. **Validate locally** — run lint, type-check, tests, and build with a single command
3. **Work with GitHub** — connect to a repository, create branches, push commits, open pull requests
4. **Implement from a GitHub issue** — read a feature request, plan and implement the change, validate, and submit a PR

---

## Lab Contents

| File | Purpose |
|---|---|
| [`docs/github-introduction.md`](docs/github-introduction.md) | GitHub primer for participants new to Git/GitHub (signup, CLI install, key concepts, cheat sheet) |
| [`WORKSHOP-part1-BUILD.md`](WORKSHOP-part1-BUILD.md) | Part 1: Build and validate the finance dashboard with Bob |
| [`WORKSHOP-part2-GITHUB-AUTOMATION.md`](WORKSHOP-part2-GITHUB-AUTOMATION.md) | Part 2: Push to GitHub, process an issue, create a PR |
| [`.github/workflows/finance-app-ci.yml`](.github/workflows/finance-app-ci.yml) | CI pipeline (Node 24, runs on push and PR) |
| [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) | PR template used by Bob when creating pull requests |
| [`docs/issue-feature-request-example.md`](docs/issue-feature-request-example.md) | Feature request body participants paste into their GitHub issue |
| [`docs/yahoo-finance-api-notes.md`](docs/yahoo-finance-api-notes.md) | Yahoo Finance v8 API reference: endpoints, response structure, known constraints |
| [`docs/yahoo-finance-proxy-example.md`](docs/yahoo-finance-proxy-example.md) | Minimal Node/Express proxy example for server-side API calls |

---

## Application Scenario

A React finance dashboard for five stock indices:

| Index | ISIN |
|---|---|
| Euro Stoxx 50 | EU0009658145 |
| DAX | DE0008469008 |
| Nikkei 225 | XC0009692440 |
| Dow Jones 30 Industrial | US2605661048 |
| MSCI World | GB00BJDQQQ59 |

Dashboard views: current day · last 7 days · last quarter

Data source: Yahoo Finance public v8 API via a lightweight Node/Express proxy (no npm wrapper — see [`docs/yahoo-finance-api-notes.md`](docs/yahoo-finance-api-notes.md))

---

## Suggested Audience

- Developer advocates
- Solution architects
- Engineering leads
- AI-assisted development champions
- DevOps / platform teams exploring agentic workflows with GitHub

---

## Suggested Lab Duration

- Part 1: 30–45 minutes
- Part 2: 30–45 minutes

---

## Expected Takeaways

Participants leave with a practical understanding of:
- how Bob accelerates application delivery from a plain requirement
- how Bob fits into a Git-based engineering workflow
- how Bob implements a feature starting from a GitHub issue
- what a realistic "AI engineer in the loop" workflow looks like end-to-end

---

## Distributing the Lab to Participants

Participants receive a ZIP export — **not** a clone of this repository. The ZIP contains only the files they need and excludes instructor-only content, build artifacts, and the `finance-app/` solution directory.

### Create the export

```bash
# From the LAB root directory
./export-lab.sh
```

This produces `github-sdlc-lab-<date>.zip` in the same directory.

PDF generation requires [md2pdf](https://github.ibm.com/technology-garage-dach/md-to-pdf). Install it before running the export. If `md2pdf` is not installed, PDF conversion is skipped — the export still works and produces the ZIP without PDFs.

### What the ZIP contains

| Path | Purpose |
|---|---|
| `WORKSHOP-part1-BUILD.md` | Part 1 instructions |
| `WORKSHOP-part2-GITHUB-AUTOMATION.md` | Part 2 instructions |
| `.github/workflows/finance-app-ci.yml` | CI workflow participants copy into their app |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR template participants copy into their app |
| `docs/` | API notes and feature request example |
| `.bob/workshop-hints.md` | Bob context file (loaded automatically by Bob) |
| `.bob/rules/github-pr.md` | Bob rule: always use `gh pr create`, never browser URL |

### What is excluded

- `finance-app/` — the completed solution (participants build this themselves in Part 1)
- `export-lab.sh` — instructor tooling
- `README.md` — this file
- `.DS_Store`, `package-lock.json`, and other build artifacts

### Distribute

Share the ZIP via the workshop platform, Slack, or email. Participants unzip it and open the directory in Bob to start Part 1.

---

## Related Reference

See the existing reference materials in [Git Platform Operations Guide](https://github.ibm.com/ClientEngineering/bob/blob/main/GitOps/README.md).
