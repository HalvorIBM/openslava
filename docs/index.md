# IBM Bob — OpenSlava Lab Guide

**Hands-on lab guide for the IBM Bob Bobathon at OpenSlava.**
Three tracks — Beginner, Intermediate, Expert — each self-contained and runnable in ~90 minutes.

→ **[Jump straight to the OpenSlava tracks](labs/index.md)**

!!! note "IBM-internal links"
    Some links in this guide point to internal IBM resources (GitHub Enterprise, Confluence, Mural boards) that require IBM SSO. These are marked or will return a login page if you are not an IBMer. All lab code and the three OpenSlava track guides are fully public.

---

## What is a Bobathon?

A **Bobathon** (also called a Bob-a-thon or Bob Bootcamp) is a structured, hands-on workshop where client developers and IBM Client Engineers work together — using IBM Bob — to tackle real engineering problems on the client's actual technology stack.

It is **not** a product demo. It is a co-creation experience that produces working artifacts, builds developer confidence, and creates the momentum needed to move toward a sustained pilot.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#1a56db', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#1a56db', 'lineColor': '#6b7280', 'mainBkg': '#1a56db', 'nodeBorder': '#1a56db', 'clusterBkg': '#1e3a5f', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent'}}}%%
flowchart LR
    A["🎯 Custom Demo\nIBM CE builds a tailored demo\nusing client code & scenarios\nGoal: prove Bob works for your stack"] --> B
    B["⚡ Bobathon\n1-day hands-on workshop\nDevelopers + Client Engineers\nGuided labs + open experimentation\nOutcome: functional prototype"] --> C
    C["🚀 Pilot (if needed)\nWeekly office hours\nBusiness value KPI tracking\nProposal — or skip straight\nto adoption if Bobathon lands"]

    class A secondary
    class B highlight
    class C secondary
    classDef node fill:#1a56db,color:#fff,stroke:#1a56db
    classDef secondary fill:#2563eb,color:#fff,stroke:#2563eb
    classDef highlight fill:#1d4ed8,color:#fff,stroke:#1d4ed8,stroke-width:3px
    classDef success fill:#166534,color:#fff,stroke:#166534
    classDef warning fill:#92400e,color:#fff,stroke:#92400e
    classDef decision fill:#1e40af,color:#fff,stroke:#1e40af
```

---

## Who This Guide Is For

- **Client Engineers (CEs)** running pre-sales engagements — Bobathons are the primary CE activation motion
- **Forward Deployed Engineers (FDEs)** embedded in client teams — post-sale activation and scaled pilots
- **Client Value Engineers (CVEs)** driving SaaS adoption — Bobathons accelerate value realization on focus products
- **CE team leads** building repeatable bobathon practices

---

## How to Use This Guide

Follow the phases in order for a first engagement. Return to specific sections as needed.

| Phase | What You'll Do |
|---|---|
| [**Pitch & Discovery**](pitch/index.md) | Build the business case, identify the right contacts, understand Bob's value |
| [**Discovery & Scoping**](discovery/index.md) | Uncover client pain points, prioritize use cases, confirm tech stack |
| [**Planning & Prep**](planning/index.md) | Build the agenda, prepare the environment, set up labs and logistics |
| [**Use Cases & Labs**](labs/index.md) | Select and customize labs for Java, IBM i, Z, SDLC, and more |
| [**Delivery**](delivery/index.md) | Run the day-of event with confidence |
| [**Follow-Up**](followup/index.md) | Transition to a pilot, track KPIs, close the loop |

---

## The Bobathon in 60 Seconds

!!! info "Key facts for a first conversation"
    - **Duration:** Half-day (3–4 hrs) to full day (6–7 hrs or longer for complex engagements)
    - **Audience:** Client developers + architects, ideally 4–15 people
    - **Format:** Guided labs on the client's own code or IBM-provided sample applications
    - **Cost to client:** No charge — CE engagement model
    - **Lead time:** Minimum 1 week (standard); 3+ weeks if using client code or custom labs
    - **Outcome:** Working prototype, documented artifacts, clear pilot proposal

---

## Formats at a Glance

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#1a56db', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#1a56db', 'lineColor': '#6b7280', 'mainBkg': '#1a56db', 'nodeBorder': '#1a56db', 'clusterBkg': '#1e3a5f', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent'}}}%%
flowchart TD
    A["How long do you have?"] --> B["90-min Sprint"]
    A --> C["Half Day · 3 hrs"]
    A --> D["Full Day · 6–7 hrs+"]

    B --> B1["Executive preview\nValue framing\nMini-lab"]
    C --> C1["Light enablement\nIntro + 1-2 labs\nUse case exploration"]
    D --> D1["Full hands-on\nMultiple use cases\nClient-specific build"]

    class A node
    class B,C,D node
    class B1,C1,D1 secondary
    classDef node fill:#1a56db,color:#fff,stroke:#1a56db
    classDef secondary fill:#2563eb,color:#fff,stroke:#2563eb
    classDef highlight fill:#1d4ed8,color:#fff,stroke:#1d4ed8,stroke-width:3px
    classDef success fill:#166534,color:#fff,stroke:#166534
    classDef warning fill:#92400e,color:#fff,stroke:#92400e
    classDef decision fill:#1e40af,color:#fff,stroke:#1e40af
```

---

## Premium Package Tracks

IBM Bob has **Premium Packages** for specific platforms that unlock specialized modes and deeper capabilities. Three tracks warrant particular attention:

| Track | Premium Package | Key Differentiator |
|---|---|---|
| [IBM i (PPi)](labs/ibm-i.md) | ✅ Available (PPi) | [Flight400 Lab](https://github.com/bmarolleau/flight400-demo) · Direct QSYS connection, RPG/COBOL modernization, DDS→SQL, 5250 to React |
| [Java Modernization](labs/java.md) | ✅ Available | WebSphere → Liberty, Java 8 → 21, Spring migrations |
| [IBM Z](labs/ibm-z.md) | ✅ Available (pp4z) | COBOL/JCL/PL/I, GenApp, impact analysis, refactoring |

---

!!! tip "Use Bob to build your Bobathon"
    The [CE Bob Marketplace](https://ibm.biz/ce-bob-marketplace) includes a **Bobathon Builder Mode** and supporting skills that guide you through the entire preparation process — from client discovery to lab customization to agenda generation. See [Building with Bob](planning/build-with-bob.md).
