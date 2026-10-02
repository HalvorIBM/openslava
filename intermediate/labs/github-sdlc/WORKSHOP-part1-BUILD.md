# Bob GitHub SDLC Lab
## IBM Bob LAB — Finance Dashboard Build and Validation | Part 1

### Audience
Developers, solution architects, AI engineering advocates, and platform teams who want to experience how **IBM Bob** can build and validate a modern application from scratch.

### Goal of Part 1
Experience how Bob can:
- interpret a business requirement
- plan and scaffold a React application
- integrate external data
- build visual dashboards
- add tests and validation

Part 1 focuses entirely on **development with Bob**. GitHub workflows, pull requests, and issue tracking are covered in [Part 2](WORKSHOP-part2-GITHUB-AUTOMATION.md). At the end of Part 1, you will have a working `finance-app` project that validates locally and is ready for GitHub collaboration.

---

## Before You Start

> **💡 Agent Mode Required**
> All steps in this workshop run in **Agent** mode in IBM Bob. Make sure Agent mode is active before you start.

> **💡 Open a terminal in Bob**
> Several steps involve running commands. In Bob, open an integrated terminal directly in the LAB directory: press **⌘J** (macOS) or **Ctrl+J** (Windows/Linux) to toggle the panel, then select the **Terminal** tab.

> **📁 Fixed project directory name**
> Bob will create the application in a subdirectory. To ensure [Part 2](WORKSHOP-part2-GITHUB-AUTOMATION.md) of the workshop works without path issues, the project directory **must be named `finance-app`**. The prompts below already include this instruction — do not change it.

---

## Workshop Flow Overview

1. Understand the repository and plan the build
2. Create the application skeleton
3. Integrate Yahoo Finance market data
4. Build the dashboard views
5. Add validation and tests

Each step mirrors a realistic AI-assisted engineering workflow from idea to validated code.

---

## Step A — Understand the Repository and Plan the Build

### Why this step?
Before generating any code, Bob should understand the full scope: what to build, how to structure it, and what challenges to anticipate. This step shows Bob reasoning about a requirement — not just producing output.

### What to do
Copy the prompt below into Bob's chat and submit it.

### Prompt
```text
Review this repository and propose a build plan for a small React finance dashboard application. The app should use Yahoo Finance data for the following stock indices and symbols: Euro Stoxx 50 (`^STOXX50E`), DAX (`^GDAXI`), Nikkei 225 (`^N225`), Dow Jones Industrial Average (`^DJI`), and MSCI World (`URTH`). The dashboard should provide views for current day, last 7 days, and last quarter. Explain the recommended project structure, data-fetching approach, UI sections, and testing strategy.
```

### Optional: ✨ Try the Sparkle Button
Bob can enhance your prompt before submitting. Paste the prompt above, then click the **✨** button next to the input field to let Bob improve it automatically.

> To enable the sparkle button, open Bob settings → **Chat** → activate prompt enhancement (last item in the list). The button appears once you have typed a few words. If it does not appear, refresh the page or ask your facilitator.

### What Bob does
Bob will output a structured build plan. Read through it — it sets the context for everything that follows.

---

## Step B — Create the Application Skeleton

### Why this step?
A repeatable lab needs a clear project structure. This step generates the app shell, component layout, service layer, and test scaffolding that all later steps build on.

### What to do
Submit the prompt below in the **same chat** as Step A.

### Prompt
```text
Create a simple React application structure for this repository inside a directory named "finance-app". Include a dashboard page, reusable chart card components, a finance data service layer, and a clean folder layout suitable for future enhancements.
```

### What Bob does
Bob will create the `finance-app` directory with the full project structure. You should see the new files appear in the file explorer on the left.

### Check before continuing
Confirm that the `finance-app` directory exists and contains the generated application files.

---

## Step C — Integrate Yahoo Finance Data

### Why this step?
The application needs real data to be compelling. This step wires up the Yahoo Finance API, handles CORS via a lightweight proxy, and normalizes the data for the UI.

> **💡 Start a new chat before Step C**
> Step B completes the scaffolding phase. Starting a fresh chat keeps Bob focused — it no longer needs the planning context from Steps A and B. Click **"New task"** at the end of Bob's output to open a new session, then continue below.

> **📖 Implementation note**
> This lab uses the Yahoo Finance v8 public HTTP API directly, without an npm wrapper. A lightweight Node/Express proxy handles server-side API calls and eliminates browser CORS restrictions. See [`docs/yahoo-finance-api-notes.md`](docs/yahoo-finance-api-notes.md) for endpoint details, response structure, and known field quirks. If Bob tries to call Yahoo Finance directly from the browser, ask it to move the API access into the Node/Express proxy.

### Prompt
```text
Implement a finance data layer for the following stock indices using Yahoo Finance data: Euro Stoxx 50 (`^STOXX50E`), DAX (`^GDAXI`), Nikkei 225 (`^N225`), Dow Jones Industrial Average (`^DJI`), and MSCI World (`URTH`). Normalize the returned data so the UI can display quote summaries, short-term history, and quarterly trend views. Keep the code easy to extend if more indices need to be added later.
```

---

## Step D — Build the Dashboards

### Why this step?
This is where the application becomes visible. Bob translates the data layer into a working UI with charts and summary cards.

### What to do
Submit the prompt below in the **same chat** as Step C.

### Prompt
```text
Build 2 to 3 dashboard views for the finance application:
- current day market summary
- last 7 days trend comparison
- last quarter comparison view

Include the following stock indices: Euro Stoxx 50, DAX, Nikkei 225, Dow Jones Industrial Average, and MSCI World. Use charts and summary cards where appropriate. Keep the UI simple, readable, and demo-friendly.
```

### What Bob does
Bob will implement the dashboard components. Once done, you can start the app locally to see it in the browser:

```bash
cd finance-app
npm install
npm start
```

### Check before continuing
- confirm that `npm install` completes without errors
- if the app uses separate client and server processes, use the scripts Bob added in `package.json`
- if you are unsure which command starts the app, ask Bob to explain how to run the application locally

---

## Step E — Add Validation and Tests

### Why this step?
AI-generated code needs engineering discipline. This step adds unit tests, integration tests, and a single validation command that covers lint, type-check, tests, and build.

> **💡 Start a new chat before Step E**
> Step D completes the UI build phase. Open a fresh session before adding tests to keep the context lean. Click **"New task"** at the end of Bob's output.

### Prompt
```text
Add appropriate validation for the finance dashboard project. Include unit tests for the data formatting and normalization utilities, and integration tests for at least one dashboard view rendered with mocked API data. Use MSW to mock the finance API responses in tests. Provide a single command that runs lint, type-check, tests, and build together, and summarize what a successful run looks like.
```

### What Bob does
Bob will add the test files and update `package.json`.

### Command
```bash
cd finance-app
npm run validate
```

### Check before continuing
A successful run should complete without errors and include passing lint, type-check, test, and build steps.

---

## Part 1 Complete

At the end of Part 1, your `finance-app` directory should contain:

- [ ] React application scaffold with component structure
- [ ] Yahoo Finance data service and proxy
- [ ] Dashboard views for five stock indices and three time windows
- [ ] Unit and integration tests
- [ ] A passing `npm run validate` command

Do not continue to [Part 2](WORKSHOP-part2-GITHUB-AUTOMATION.md) until the `finance-app` directory exists and `npm run validate` passes locally.

**Continue with [Part 2](WORKSHOP-part2-GITHUB-AUTOMATION.md)** to push this application to GitHub and experience Bob's GitHub collaboration workflow.

---

## Engineering Notes

### Stock indices used in this lab
| Index | Yahoo Finance symbol |
|---|---|
| Euro Stoxx 50 | `^STOXX50E` |
| DAX | `^GDAXI` |
| Nikkei 225 | `^N225` |
| Dow Jones Industrial Average | `^DJI` |
| MSCI World | `URTH` |

### Yahoo Finance fallback
If direct API access is unreliable in your environment, Bob can use mocked/cached example data for the workshop while keeping the UI and transformation layers stable. Ask Bob to add a mock data mode if needed.
