# Fork & Origin Notes

Records of all external source material included in this workspace, forked dates, licences, and any modifications made.

---

## galaxium-travels/

| Field | Value |
|---|---|
| **Origin** | `https://github.com/IBM/galaxium-travels` |
| **Forked** | 2026-10-01 |
| **Licence** | Apache-2.0 |
| **Modifications** | None — unmodified clone |
| **Notes** | Interplanetary flight booking demo app. React 19 / TypeScript / Vite 7 / Tailwind frontend; Python 3 / FastAPI / FastMCP backend; Java 17 / Spring Boot hold service. Start with `./start.sh`. |

---

## labs/github-sdlc/

| Field | Value |
|---|---|
| **Origin** | `git@github.ibm.com:ClientEngineering/bob` · path `LABs/Github-SDLC` |
| **Forked** | 2026-10-01 |
| **Licence** | MIT (see `labs/github-sdlc/LICENSE`) |
| **Original author** | ticlazau (IBM Client Engineering) |
| **Modifications** | None — unmodified sparse-checkout copy |
| **Notes** | Two-part React finance dashboard lab. Part 1: build locally with Bob. Part 2: GitHub MCP automation (issues → branch → PR). |

---

## labs/banking-industry/

| Field | Value |
|---|---|
| **Origin** | Original work created for this workspace |
| **Created** | 2026-10-01 |
| **Licence** | Original — freely usable for IBM Bobathon events |
| **Based on** | GFM Bank concept from IBM Client Engineering; rebuilt from scratch with no copied code |
| **Modifications** | Completely rewritten. IBM Carbon removed; plain CSS React UI (Part 2). Seed script replaces binary `.db` file. All three parts restructured as standalone Markdown workshop guides. |
| **Notes** | Three-part workshop: (1) architecture understanding, (2) React teller UI, (3) security audit. Python 3.9+ compatible. No external design system dependency. |

---

## Excluded (internal IBM repos, no open licence)

The following labs exist in `github.ibm.com/ClientEngineering/bob` but were **not** included because they carry no explicit open-source licence:

- `LABs/Banking Industry (Java Modernization - Spring Boot 1.5)` — replaced by our own banking-industry lab
- All other `LABs/` directories not listed above

Facilitators with IBM SSO access can reference the original repo directly.
