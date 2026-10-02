# Bob GitHub SDLC Lab
## IBM Bob LAB — GitHub-Driven Application Evolution | Part 2

### Audience
Developers, DevOps teams, architects, and AI engineering champions who want to experience how **IBM Bob** works with **GitHub** for issue-driven development, code review, pull request creation, and autonomous feature implementation.

### Goal of Part 2
Experience how Bob can:
- set up and manage a GitHub repository
- understand a GitHub issue and turn it into an implementation plan
- implement the requested feature in an existing codebase
- validate the result
- create a pull request with a meaningful description

Part 2 uses the finance dashboard from [Part 1](WORKSHOP-part1-BUILD.md) as the starting point and treats **GitHub as the collaboration surface** for ongoing product evolution.

---

## Before You Start

> **💡 Agent Mode Required**
> Unless stated otherwise, run all steps in **Agent Mode**.

> **💡 Open a terminal in Bob**
> All shell commands in this workshop run from the LAB root directory. In Bob, open an integrated terminal: press **⌘J** (macOS) or **Ctrl+J** (Windows/Linux) to toggle the panel, then select the **Terminal** tab.

### Prerequisite

[Part 1](WORKSHOP-part1-BUILD.md) must be completed. Your `finance-app` directory must exist and `npm run validate` must pass before continuing.

---

## Step 0 — Set Up Your GitHub Repository

### Why this step?
Bob's GitHub integration requires a real GitHub repository. This step connects your local `finance-app` to GitHub so that all following steps can demonstrate pull requests, issues, CI validation, and branch management in a real environment.

### Part A — Create the repository on GitHub

1. Go to [https://github.com/new](https://github.com/new)
2. Repository name: `finance-app`
3. Description: `IBM Bob Workshop — Finance Dashboard`
4. Visibility: Public or Private (your choice)
5. **Do NOT** initialize with README, .gitignore, or license
6. Click **"Create repository"**

### Part B — Copy the GitHub configuration into your finance-app

The LAB directory already contains a GitHub Actions workflow and a PR template. Copy them into your project before initializing Git. After this step, `finance-app/.github/workflows/finance-app-ci.yml` should exist:

```bash
# Run from the LAB root directory
cp -r .github finance-app/.github
```

This copies:
- [`.github/workflows/finance-app-ci.yml`](.github/workflows/finance-app-ci.yml) — CI pipeline that runs on every push and PR
- [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) — PR template Bob will use when creating pull requests

### Part C — Initialize Git and push to GitHub

> **Troubleshooting: Git identity or authentication**
> If `git commit` fails because your identity is not configured, set `user.name` and `user.email` locally or ask your facilitator. If `git push` fails because of authentication, sign in to GitHub in your terminal environment or ask your facilitator for the preferred authentication method.

```bash
# Change into the directory that contains the application
cd finance-app

# Initialize Git
git init
git add .
git commit -m "Initial commit: finance dashboard from Part 1"

# Connect to GitHub (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/finance-app.git
git branch -M main
git push -u origin main
```

### Part D — Verify the setup

- Visit your repository on GitHub.com
- Confirm all files from Part 1 are visible under the **Code** tab
- Open the **Actions** tab — the CI workflow should be visible (not just "suggested workflows")
- Confirm that the GitHub Action run finishes successfully and is marked with a green checkmark
- Open [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) and confirm it exists

> **Troubleshooting: Actions tab shows only "Get started with GitHub Actions"**
> The `.github/workflows/` directory was not pushed. Check locally:
> ```bash
> ls finance-app/.github/workflows/
> # Should show: finance-app-ci.yml
> ```
> If the file is missing, repeat Part B and push again.

> **Troubleshooting: the GitHub Action run does not succeed**
> If the workflow does not finish with a green checkmark, something is wrong with the repository setup. The most common cause is that the Git commands from Part C were run outside the `finance-app` directory. In that case, delete the GitHub repository in **Settings** at the bottom of the page, create it again, then repeat Step 0 carefully and make sure you do not skip any commands.

### Part E — Create a feature branch

```bash
# From inside the finance-app directory
git checkout -b feature/user-selected-chart
git push -u origin feature/user-selected-chart
```

### Part F — Enable GitHub Issues

- Go to repository **Settings → General**
- Confirm that **Issues** is enabled

### Verification Checklist

- [ ] GitHub repository created and accessible
- [ ] All files from Part 1 visible on GitHub
- [ ] GitHub Actions CI workflow visible in Actions tab
- [ ] PR template visible at [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md)
- [ ] Feature branch `feature/user-selected-chart` pushed to GitHub
- [ ] Issues enabled in repository settings

---

## Step A — Review the Current Repository State

### Why this step?
Before Bob works on a GitHub issue, it should first check the repository state: current branch, working tree, and overall project readiness. This step is different from Step C: here Bob verifies that the repository is clean and ready for issue-driven work; in Step C, it analyzes the feature request itself and plans the implementation.

### What to do
Open a **new chat** in Bob and submit the prompt below.

### Prompt
```text
Inspect the current repository state: check the active branch, summarize what the finance dashboard application does, review whether there are any uncommitted changes, and confirm whether the project is ready for GitHub collaboration.
```

### What Bob does
Bob will analyze the repository, list the key files, describe the application, and give you a clear status summary.

### Check before continuing
Confirm that Bob reports the current branch correctly, sees no unexpected uncommitted changes, and considers the repository ready for GitHub collaboration.

---

## Step B — Create a GitHub Issue for the New Feature

### Why this step?
In a real team workflow, new features start as GitHub issues. The issue defines the requirement. Bob reads the issue to understand what to build — this is the trigger for the development work that follows.

### What to do
Create the issue manually on GitHub. Do not shorten the issue body — Bob will use the full issue text as the implementation requirement.

1. Go to your repository's **Issues** tab
2. Click **"New issue"**
3. Title: `Add a graph for a user-selected index`
4. Body: Copy the complete content from [`docs/issue-feature-request-example.md`](docs/issue-feature-request-example.md)
5. Click **"Create"**
6. Note the issue number (e.g., `#1`) — you will need it in the next step

---

## Step C — Analyze the Issue and Plan the Implementation

### Why this step?
This is where GitHub-driven development begins. Bob reads the issue, understands the requirements, identifies what needs to change in the codebase, and creates a concrete plan — before writing a single line of code.

### What to do
Start a **new chat** in Bob and submit the prompt below. Replace `#1` with your actual issue number.

### Prompt
```text
Fetch and analyze GitHub issue #1 from this repository. Explain the requested feature, define the acceptance criteria, identify which files and components need to change in the finance dashboard to support a user-selected stock index graph, and propose an implementation plan.
```

### What Bob does
Bob will read the issue from GitHub, map it to the existing codebase, and give you a clear breakdown of what needs to change and why.

### Check before continuing
Confirm that the response includes acceptance criteria, the affected files or components, and an implementation plan.

---

## Step D — Implement the Feature

### Why this step?
This is the core of the lab. Bob turns the GitHub issue into working code — implementing the feature in the existing codebase without breaking what is already there.

### What to do
In the **same chat** as Step C, submit:

### Prompt
```text
Implement the feature described in the GitHub issue. In addition to the existing fixed index dashboards, the finance dashboard should allow a user to enter a stock ticker symbol at runtime and see a new graph for that symbol. Reuse the existing data service layer where possible, keep the UX simple, and preserve all existing dashboard views.
```

### What Bob does
Bob will implement the feature. The recommended implementation includes:
- an input field or dropdown for the ticker symbol
- validation for empty or unsupported symbols
- a new chart panel for the user-selected symbol
- loading and error states
- the existing dashboards remain fully intact

---

## Step E — Validate the Enhancement

### Why this step?
The new feature is only complete when it passes the same quality bar as the rest of the application.

### What to do
In the **same chat** as Step D, submit:

### Prompt
```text
Run the full validation suite for the finance dashboard. Summarize what passed, what failed, and whether the branch is ready to push to GitHub.
```

### What Bob does
Bob will run `npm run validate` and report the results.

### If validation fails
```text
Fix the failing tests and run validation again.
```

---

## Step F — Review, Commit, and Push

### Why this step?
A convincing GitHub workflow shows the full loop: implement → validate → commit → push. This step closes the development cycle and makes the changes visible on GitHub.

### What to do
Start a **new chat** in Bob and submit:

### Prompt
```text
Review the changes made to implement the user-selected index chart feature in the finance-app/ directory. Summarize what was added, check for any issues, fix any obvious problems, commit the changes with a meaningful message, and push them to the feature/user-selected-chart branch on GitHub. Do not yet create a pull request.
```

### What Bob does
Bob will review the diff, commit the changes with a meaningful message, and push them.

### Check before continuing
Confirm on GitHub that the new commit is visible on the `feature/user-selected-chart` branch.

---

## Step G — Create the Pull Request

### Why this step?
This is where the GitHub loop closes. Bob has implemented the feature, validated it, and pushed the branch. Now it creates a pull request that tells the whole story: what changed, which issue it addresses, and what was validated. This is where `/create-pr` really shines — Bob generates the description directly from the diff and the issue context.

### What to do
In the **same chat** as Step F, type the following command directly into Bob's chat:

### Command
```
/create-pr
```

Bob will display a workflow dialog. Click **"Start workflow"**. In the form that appears, leave the pre-filled values for **Repository** (`finance-app`) and **Base Branch** (`main`) as they are, then click **"Generate PR Description"** to create the pull request.

> **⚠️ Type `/create-pr` exactly**
> Autocomplete may suggest `/create-pull-request` — do not use it. That variant cannot run in an existing chat and will show an error. Use `/create-pr`.

### What Bob does
Bob reads the git diff, detects the linked issue, fills in the PR template, and creates the pull request — no prompt needed.

### Check before continuing
Review the draft PR description, then confirm it. Visit the **Pull requests** tab on GitHub to confirm that the PR exists and references the issue.

> **💡 Could you do this with a prompt instead?**
> Yes — you could ask Bob to "create a pull request, reference the issue, list acceptance criteria, and include validation results". Bob would do it. But `/create-pr` is faster, requires no prompt writing, and has direct git integration that picks up the diff, branch, and linked issue automatically. Use the command.

---

## Workshop Complete

You have now experienced the full GitHub-driven development loop with Bob:

```
GitHub Issue Created (Step B)
       ↓
Bob Analyzes Issue & Plans Implementation (Step C)
       ↓
Bob Implements the Feature (Step D)
       ↓
Bob Runs Validation (Step E)
       ↓
Bob Reviews & Pushes Changes (Step F)
       ↓
Bob Creates Pull Request from Real Diff (Step G)
       ↓
GitHub Actions CI Validates
       ↓
Human Maintainer Reviews & Merges
```

### What you demonstrated
- Bob understanding an existing codebase from a standing start
- Bob reading a GitHub issue and deriving a concrete implementation plan
- Bob implementing a targeted feature without breaking existing functionality
- Bob validating the result with the full test suite
- Bob creating a meaningful pull request from a real diff — not a template

---

## Reference: GitHub Workflow Patterns

For the strongest results with Bob and GitHub, use:
- feature branches with a clear naming convention (e.g., `feature/user-selected-chart`)
- pull request templates (already included in this lab)
- CI validation on every push (already configured in this lab)
- GitHub issues as the single source of requirements

### Further Bob commands to explore
| Command | What it does |
|---|---|
| `/create-pr` | Reads the git diff and creates or updates a pull request |
| `/review` | Reviews the current branch diff and reports findings |
| `/review --issue-coverage` | Reviews the diff against a linked GitHub issue |

For more, see Bob documentation for [slash commands](https://bob.ibm.com/docs/ide/features/slash-commands) and [code reviews](https://bob.ibm.com/docs/ide/features/code-reviews).
