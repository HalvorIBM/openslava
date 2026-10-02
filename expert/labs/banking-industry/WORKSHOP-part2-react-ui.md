# GFM Bank — Build a React Teller UI

**Part 2 of 3** · IBM Bob Workshop

---

## Audience

Frontend and full-stack developers building banking interfaces with React and Vite.

---

## Goal

Demonstrate how IBM Bob can:

- Scaffold a complete React application from a written specification
- Connect a frontend to an existing REST API
- Build a production-ready banking teller interface without any external design system dependency
- Handle authentication, API state, and error handling idiomatically

---

## Bob Mode

> **Required mode: Agent**
>
> Agent mode gives Bob the tools to scaffold, write, and run the application.

---

## Prerequisites

- Part 1 complete — GFM Bank API running on `http://127.0.0.1:8000`
- Node.js 20 LTS installed
- `npm` available in your shell

---

## Lab Files (reference only)

| File | Purpose |
|---|---|
| `gfm-bank/code/teller_client.py` | Defines the operations the UI must replicate |
| `gfm-bank/code/demo_api.py` | API source — use the `/docs` page to explore endpoints |

---

## Step 1 — Test Backend Connectivity

### Why this step?

Before building a frontend, verify the backend is accessible and the credentials work.

### Prompt

```
The GFM Bank API is running at http://127.0.0.1:8000.
Use the teller credentials (username: teller, password: teller123)
to authenticate and retrieve the balance for account with IBAN DE89545769475769453536.
Show me the current balance and the last 5 transactions.
```

---

## Step 2 — Scaffold and Build the Teller UI

### Why this step?

This is the main implementation step. Bob generates a complete React + Vite application that replicates the teller CLI as a browser-based interface.

### Prompt

```
Build a React + Vite teller front-end for GFM Bank.
Connect it to the local API at http://127.0.0.1:8000.

Requirements:
1. Login page — username/password form. Credentials come from a .env file
   (VITE_TELLER_USER and VITE_TELLER_PASS). Default: teller / teller123.
2. After login, show a header with "GFM Bank" and an online/offline
   status indicator that polls /health every 10 seconds.
3. Teller operations — implement all of these on a dashboard:
   - Balance inquiry: IBAN text input → show balance and last 10 transactions
   - Money transfer: source IBAN, destination IBAN, amount → submit → show result
   - Overdraft request: IBAN + requested limit → display a formatted request message
     (the back office sets the actual limit; this just prints the request)
4. Styling: plain CSS — no external component library. Use a clean banking-style
   layout (white background, dark navy header, muted grey card backgrounds).
5. Error handling: show user-friendly messages for API errors (invalid IBAN,
   insufficient funds, network down).

Use React functional components with hooks. Structure the project as:
  src/
    components/   (LoginForm, Header, BalancePanel, TransferForm, OverdraftRequest)
    services/     (api.ts — all fetch calls)
    App.tsx
    main.tsx
```

### What to observe

- Bob reads the API endpoints from `demo_api.py` or the `/docs` page to understand the request/response shapes
- Bob creates a `.env` file, all components, the API service layer, and CSS
- The project runs immediately with `npm run dev`

---

## Step 3 — Run and Test

### Prompt

```
Start the dev server and open it in the browser.
Log in, then look up the balance and transaction history
for IBAN DE89545769475769453536.
```

### What to observe

- Bob runs `npm install` and `npm run dev`
- The login form appears at `http://localhost:5173`
- After login the dashboard shows the balance and transaction table
- The status indicator shows "Online" (green)

---

## Extension: Add a Transaction Table with Sort

Once the basic UI works, try this follow-up prompt:

```
Add a sortable transaction table to the balance panel.
Columns: Date, Amount, Type. Clicking a column header
cycles between ascending and descending sort order.
No external table library — implement with component state.
```

---

## Application Checklist

- [ ] Login form with .env credentials
- [ ] Server status indicator (online/offline)
- [ ] Balance inquiry by IBAN
- [ ] Transaction history (last 10 rows)
- [ ] Money transfer form with confirmation feedback
- [ ] Overdraft request message
- [ ] Error messages for API failures
- [ ] `npm run dev` starts cleanly

---

## Next Steps

→ **Part 3:** Security audit the data pipeline code
