# GitHub Introduction — Quick Start for Lab Participants

This guide covers everything you need to participate in the GitHub SDLC Lab, even if you have never used GitHub before.

---

## 1. Sign up on github.com

> **Already have an account?** Skip to the next section.

1. Go to [github.com](https://github.com)
2. Click **Sign up** and follow the steps
3. Verify your email address

---

## 2. Install Git, GitHub CLI (`gh`), and the GitHub Desktop (optional)

### macOS

**Recommended: use Homebrew**

If you don't have Homebrew yet:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install Git and `gh`:
```bash
brew install git gh
```

### Windows

**Option A — winget (built into Windows 10/11)**
```powershell
winget install --id Git.Git
winget install --id GitHub.cli
```

**Option B — manual installers**
- Git: [git-scm.com/download/win](https://git-scm.com/download/win)
- `gh`: [cli.github.com](https://cli.github.com)

> After installation on Windows, open a new **PowerShell** or **Git Bash** window so the commands are available.

### Verify your installation

```bash
git --version   # e.g. git version 2.x.x
gh --version    # e.g. gh version 2.x.x
```

---

## 3. Sign in with the GitHub CLI

```bash
gh auth login
```

Follow the prompts:
1. Select **GitHub.com**
2. Select **HTTPS**
3. Confirm with **Y** (authenticate via browser)
4. A browser window opens — log in and authorize the CLI

Verify it worked:
```bash
gh auth status
```

You should see your username and `Logged in to github.com`.

> **One login for everything:** `gh auth login` also configures Git's credential helper automatically. All `git push`, `git pull`, and `git clone` commands over HTTPS will use the same token — no separate Git login needed.

---

## 4. Key concepts — explained simply

> **`git` vs. `gh`:** `git` is the version control system itself — it manages your code history locally and syncs with any remote. `gh` is GitHub's CLI on top of git — it lets you work with GitHub-specific features like issues, pull requests, and repositories directly from the terminal.

### Repository (Repo)

A repository is a project folder managed by Git. It stores all files and the complete history of every change ever made.

### Clone — get the code locally

A **clone** copies a remote repository from GitHub onto your machine:

```bash
git clone https://github.com/<owner>/<repo>.git
```

This creates a local folder with all the files and history.

### Pull — get the latest changes

After cloning, others may push new changes to GitHub. **Pull** downloads those changes into your local copy:

```bash
git pull
```

> `pull` = fetch from GitHub + merge into your current branch.

### Branch

A **branch** is an independent line of work. The default branch is usually called `main`. When you work on a feature or fix, you create a new branch so your changes don't affect `main` until they are reviewed and merged.

```bash
git checkout -b my-feature    # create and switch to a new branch
git checkout main             # switch back to main
```

### Add — stage your changes

Before committing, you tell Git which changed files to include. This is called **staging**:

```bash
git add <file>       # stage a specific file
git add .            # stage all changed files in the current directory
```

Think of `git add` as putting items into a box.

### Commit — seal the box

You can run `git add` as many times as you like before committing — adding more files to the box one by one. A **commit** then seals the box and labels it with a message describing what's inside:

```bash
git commit -m "Add quarterly chart to dashboard"
```

The box is sealed locally — GitHub does not see it yet.

### Push — ship the box to GitHub

**Push** ships your sealed boxes (commits) to GitHub:

```bash
git push
```

If you are pushing a branch that does not yet exist on GitHub, the `-u origin <branch>` flag creates it there and links your local branch to it:

```bash
git push -u origin my-feature
```

### Issue

An **issue** is a discussion item on GitHub — a bug report, a feature request, or a question. Issues are numbered (`#1`, `#2`, …) and can be assigned to people, labeled, and linked to code changes.

### Pull Request (PR)

A **pull request** proposes merging changes from one branch into another (usually into `main`). It is the standard way to review code on GitHub before it becomes part of the main codebase.

A PR shows the diff, allows comments, runs CI checks, and requires approval before merging.

---

## 5. Essential CLI commands — cheat sheet

| Task | Command |
|---|---|
| Sign in | `gh auth login` |
| Check login status | `gh auth status` |
| Clone a repo | `git clone <url>` |
| Get latest changes | `git pull` |
| Create a new branch | `git checkout -b <branch-name>` |
| Switch branch | `git checkout <branch-name>` |
| See what changed | `git status` |
| Stage all changes | `git add .` |
| Commit staged changes | `git commit -m "your message"` |
| Push to GitHub | `git push` (or `git push -u origin <branch>` first time) |
| Create a PR | `gh pr create` |
| List open PRs | `gh pr list` |
| View a PR | `gh pr view <number>` |
| List issues | `gh issue list` |
| View an issue | `gh issue view <number>` |

---

## 6. Typical workflow end-to-end

```
# 1. Get the latest main
git checkout main
git pull

# 2. Create a branch for your work
git checkout -b feature/my-change

# 3. Make code changes …

# 4. Stage and commit
git add .
git commit -m "Describe what you changed"

# 5. Push to GitHub
git push -u origin feature/my-change

# 6. Open a Pull Request
gh pr create
```

---

> **Next step:** Continue with [Part 1 of the lab](../WORKSHOP-part1-BUILD.md).
