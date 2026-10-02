# GFM Bank — Core Banking Architecture & Code Understanding

**Part 1 of 3** · IBM Bob Workshop

---

## Audience

Banking software engineers, solution architects, and developers working with core banking systems, REST APIs, and financial transaction processing.

---

## Goal

Demonstrate how IBM Bob can:

- Understand complex banking system codebases
- Analyse API architecture and data flows
- Generate professional engineering artefacts (Mermaid diagrams, documentation)
- Reason about financial transaction logic and data integrity
- Produce architecture documentation suitable for stakeholders

We use the **GFM Bank Core Banking System** — a realistic demo application with a FastAPI backend, a teller CLI, and a back-office CLI.

---

## Bob Mode

> **Required mode: Agent**
>
> Switch to Agent mode before starting. This gives Bob full read, edit, and command access to analyse and document the codebase.

---

## Lab Files

| File | Purpose |
|---|---|
| `code/demo_api.py` | FastAPI backend — accounts, transactions, transfers, role-based auth |
| `code/seed_db.py` | Database initialiser — creates tables and seeds sample data |
| `code/teller_client.py` | Teller CLI — balance inquiry, transfers, overdraft requests |
| `code/backoffice_client.py` | Back-office CLI — customer lookup, overdraft management, fee reversals |
| `code/requirements.txt` | Python dependencies |

---

## Setup

```bash
cd labs/banking-industry/gfm-bank
./start.sh
```

This installs dependencies, seeds `corebank.db`, and starts the API on `http://127.0.0.1:8000`.

Interactive API docs: `http://127.0.0.1:8000/docs`

---

## Workshop Flow

1. Understand the codebase structure
2. Generate architecture documentation with Mermaid diagrams
3. Document functional requirements
4. Analyse the data pipeline and transaction flow
5. Identify system invariants and assumptions
6. Produce a comprehensive `ARCHITECTURE.md`

---

## Step A — Understand the Code

### Why this step?

Before extending or auditing financial software, engineers must fully understand how it works: API endpoints, transaction logic, role-based access control, and data integrity mechanisms. This step shows Bob can perform a deep technical read of banking code, not just summarise files.

### Prompt

```
Can you describe what this software does?
Include the software architecture and show me a Mermaid diagram.
```

### Enhanced prompt

```
Analyse the GFM Bank Core Banking codebase and explain:

1. API Architecture — how the FastAPI backend handles authentication (OAuth2),
   account management, and transaction processing
2. Role-Based Access Control — how TELLER and BACKOFFICE roles differ in
   permissions and capabilities
3. Transaction Processing — the transfer logic including balance verification,
   overdraft handling, and the two-leg debit/credit pattern
4. Data Model — the relationship between users, customers, accounts, and transactions
5. Client Applications — how teller_client.py and backoffice_client.py interact
   with the API

Also create Mermaid diagrams for:
- System architecture showing all components
- API endpoint structure and authentication flow
- Transaction processing sequence
- Data model (ER diagram)

State any key invariants, business rules, and assumptions made by the code.
```

---

## Step B — Generate Architecture Document

### Why this step?

Enterprise banking systems require formal architecture documentation for regulatory compliance, onboarding, integration planning, and change management.

### Prompt

```
Based on your analysis, create a comprehensive ARCHITECTURE.md that includes:

1. Executive Summary — one-paragraph system overview
2. System Architecture — high-level Mermaid component diagram
3. Component Descriptions — detailed explanation of each module
4. API Reference — all endpoints with purposes and access controls
5. Data Model — ER diagram using Mermaid
6. Transaction Flow — sequence diagram for a money transfer
7. Security Model — authentication, authorisation, and data protection
8. Functional Requirements — list of supported business operations
9. Non-Functional Requirements — performance and reliability considerations
10. Assumptions and Constraints — technical and business limitations

Save this as ARCHITECTURE.md in the current directory.
```

---

## Step C — Data Pipeline Analysis

### Why this step?

Understanding how data flows through a banking system is critical for performance optimisation, debugging transaction issues, and ensuring audit compliance.

### Prompt

```
Create a detailed data pipeline analysis covering:

1. Request Lifecycle — from HTTP request to database commit
2. Transaction States — how transfers move through validation, execution, and confirmation
3. Error Handling — what happens when a transaction fails at each stage
4. Consistency Guarantees — how the system ensures ACID properties
5. Audit Trail — what information is stored for compliance

Include a Mermaid flowchart showing the complete data pipeline
from client request to persisted transaction.
```

---

## Step D — Functional Requirements Extraction

### Prompt

```
Extract and document all functional requirements from the codebase:

1. Teller Operations
   - What can a teller do?
   - What information can they access?
   - What are the limitations?

2. Back-Office Operations
   - What administrative functions are available?
   - What operations require the BACKOFFICE role?

3. Business Rules
   - Overdraft limits and enforcement
   - Transfer validation rules
   - Fee reversal constraints

Format this as a structured requirements document with acceptance criteria.
```

---

## Step E — System Invariants

### Prompt

```
Identify and document all system invariants and assumptions:

1. Data Invariants — rules that must always hold true in the database
2. Business Invariants — financial rules that cannot be violated
3. Security Invariants — access control rules that must always be enforced
4. Technical Assumptions — what the code assumes about its environment

For each invariant: state the rule, where in the code it is enforced,
and what could go wrong if it were violated.
```

---

## Expected Outcome

By the end of this lab you should have:

- `ARCHITECTURE.md` — complete documentation with diagrams, API reference, data model, transaction flow, security model, and requirements
- A clear understanding of how Bob analyses and documents complex financial codebases

---

## Next Steps

→ **Part 2:** Build a React teller UI connected to this API
→ **Part 3:** Security audit and remediation
