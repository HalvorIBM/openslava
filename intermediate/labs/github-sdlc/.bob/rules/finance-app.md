# Finance App — Project Location

The application lives in `finance-app/` inside this workspace. All commands that operate on the application must run from that directory.

**ALWAYS use `finance-app/` as the working directory for:**
- `git` commands (init, add, commit, push, checkout, …)
- `npm` commands (install, start, run, …)
- any other commands that target the application

**NEVER run these commands from the workspace root.** Check the current working directory before executing. If in doubt, `cd finance-app` first.
