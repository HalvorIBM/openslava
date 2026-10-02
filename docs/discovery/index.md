# Discovery & Scoping Overview

Discovery is where you translate a client's vague interest in AI tooling into a focused, deliverable Bobathon. It answers four questions:

1. **What problems are real?** — Which pain points have enough urgency and business impact to anchor the event?
2. **What use cases fit?** — Which Bob capabilities map to those pain points?
3. **What's the environment?** — Can we access the code? Are there install restrictions?
4. **What does success look like?** — How will the client know the Bobathon was worth their day?

---

## Discovery Workflow

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#1a56db', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#1a56db', 'lineColor': '#6b7280', 'mainBkg': '#1a56db', 'nodeBorder': '#1a56db', 'clusterBkg': '#1e3a5f', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent'}}}%%
flowchart TD
    A["🗣 Initial Conversation\nPain point identification\nStakeholder mapping"] --> B["🔍 Client Questions\nTech stack · Environment · Constraints\nUse case candidates"]
    B --> C["🎯 Use Case Prioritization\nValue vs. Feasibility\nWhich labs to run"]
    C --> D{"Custom code\nor sample?"}
    D -->|"Client code"| E["3+ week prep\nSME curation\nCode access setup"]
    D -->|"Sample app"| F["1 week prep\nGenApp · Flight400 · Aurora Bank"]
    E --> G["📋 Scope & Agenda\nConfirmed with client"]
    F --> G

    class A node
    class B node
    class C node
    class D node
    class E node
    class F node
    class G node
    classDef node fill:#1a56db,color:#fff,stroke:#1a56db
    classDef secondary fill:#2563eb,color:#fff,stroke:#2563eb
    classDef highlight fill:#1d4ed8,color:#fff,stroke:#1d4ed8,stroke-width:3px
    classDef success fill:#166534,color:#fff,stroke:#166534
    classDef warning fill:#92400e,color:#fff,stroke:#92400e
    classDef decision fill:#1e40af,color:#fff,stroke:#1e40af
```

---

## Key Sections

<div class="grid cards" markdown>

- :material-message-question: **[Client Discovery Questions](client-questions.md)**

    Structured question bank organized by SDLC area — use these to uncover pain points and inputs for the business value case.

- :material-tune: **[Scoping Decisions](scoping-decisions.md)**

    Work through the key decisions that shape the event: sample vs. client code, headcount, duration, format, and modernization goal.

- :material-whiteboard: **[Workshop (Mural)](workshop.md)**

    How to use the CE Bob Workshop Mural template for deeper discovery sessions with the client.

</div>

---

## What Good Discovery Produces

By the end of the discovery phase, you should have:

- [ ] 1–3 prioritized use cases with a clear "why this matters" statement
- [ ] Confirmed tech stack and code availability
- [ ] Known environment constraints (install rights, network, cloud account access)
- [ ] Named executive sponsor and their KPIs
- [ ] Proposed format and timing (half-day / full-day / 90-min)
- [ ] Identified CE staffing needs

Hand all of this to [Planning & Prep](../planning/index.md) and the [Bobathon Builder](../planning/build-with-bob.md).
