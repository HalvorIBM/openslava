# OpenSlava Lab Menu & Track Guide

Choose your hands-on track for the OpenSlava Bobathon. Each track is self-contained and designed to be completed in ~70–90 minutes.

---

## 🎯 OpenSlava 1.5h Hands-On Tracks

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __[🟢 Beginner Track](openslava-beginner.md)__

    ---

    **Audience:** Developers new to IBM Bob · No prior experience needed  
    **Duration:** ~70 minutes  
    **Sample App:** Galaxium Travels (React + Node.js)

    * **Lab B1 (25m):** Discover **Ask**, **Plan**, and **Agent** modes by building the OpenSlava 2026 Welcome App with CSS confetti animations.
    * **Lab B2 (25m):** Add layover support to Galaxium Travels using a guided Ask → Plan → Agent workflow.
    * **Lab B3 (20m):** Implement date pickers, price ranking, and mock AI booking agents.

    [:octicons-arrow-right-24: Open Beginner Track Guide](openslava-beginner.md)

-   :material-numeric-2-circle:{ .lg .middle } __[🟡 Intermediate Track](openslava-intermediate.md)__

    ---

    **Audience:** Developers with basic Bob familiarity  
    **Duration:** ~70 minutes  
    **Sample App:** Galaxium Travels + GitHub MCP

    * **Lab I1 (40m):** End-to-end SDLC loop with **GitHub MCP** — Issue creation, branch management, coding, automated testing, and Pull Request.
    * **Lab I2 (30m):** Author, test, and commit custom project rules (`.bob/rules/`) enforcing team standards.

    [:octicons-arrow-right-24: Open Intermediate Track Guide](openslava-intermediate.md)

-   :material-numeric-3-circle:{ .lg .middle } __[🔴 Expert Track](openslava-expert.md)__

    ---

    **Audience:** Experienced Bob users, lead engineers, and architects  
    **Duration:** ~90 minutes  
    **Sample App:** GFM Bank (FastAPI / SQLite / Vanilla React)

    * **Lab E1 (25m):** GFM Core Bank — Architecture discovery, building a React teller/backoffice UI, and finding/fixing security flaws.
    * **Lab E2 (20m):** `/init`, re-initialization, and authoring production-grade fintech governance rules.
    * **Lab E3 (20m):** Custom modes with scoped rules and tool permissions (`fintech-reviewer`).
    * **Lab E4 (25m):** Autonomous GitHub MCP issue-to-PR workflow.

    [:octicons-arrow-right-24: Open Expert Track Guide](openslava-expert.md)

</div>

---

## 🧭 Track Comparison & Selection

| Feature / Topic | 🟢 Beginner | 🟡 Intermediate | 🔴 Expert |
|---|:---:|:---:|:---:|
| **Target Audience** | First-time Bob users | Familiar with basic Bob | Advanced / Power users |
| **Duration** | ~70 min | ~70 min | ~90 min |
| **Primary Codebase** | Galaxium Travels (React/Node) | Galaxium Travels + Git | GFM Bank (Python/React) |
| **Ask / Plan / Agent Modes** | ✅ Core focus | ✅ Used | ✅ Used |
| **Feature Implementation** | ✅ Layovers, Date picker | ✅ Issue driven | ✅ Teller/Backoffice UI |
| **GitHub MCP SDLC** | — | ✅ Deep dive (I1) | ✅ Deep dive (E4) |
| **Custom Rules (`.bob/rules`)** | — | ✅ Deep dive (I2) | ✅ Fintech standards (E2) |
| **Custom Modes & Personas** | — | — | ✅ Deep dive (E3) |
| **Security Audit & Remediation** | — | — | ✅ PCI-DSS / OWASP (E1) |

