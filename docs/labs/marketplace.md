# CE Bob Marketplace

The **CE Bob Marketplace** is a unified catalog of Bob assets — modes, skills, rules, MCP servers, labs, recipes, and collections — published by CE teams globally and available to install in one click.

🔗 **Access:** [https://ibm.biz/ce-bob-marketplace](https://ibm.biz/ce-bob-marketplace)

---

## Why the Marketplace Matters for Bobathons

> *"An accelerator nobody can find is just a folder."*

Before the Marketplace, CE teams constantly rebuilt the same Bob configurations — modes, skills, prompts — because they lived in repos, Slack threads, and on individual laptops. The Marketplace solves this:

- **Publish once, reuse everywhere** — one catalog, always current
- **A new CE is productive on day one** — no tribal knowledge required
- **Collections install entire engagement kits in one click**

---

## Asset Types

| Type | What It Is | Where It Lives |
|---|---|---|
| **Modes** | How Bob approaches a task (persona, tool access, response style) | `.bob/custom_modes.yaml` |
| **Skills** | What Bob needs to know (workflow instructions, templates, checklists) | `.bob/skills/<name>/` |
| **Rules** | Standards that always apply (coding standards, doc requirements, security guardrails) | `.bob/rules/<name>/` |
| **MCP Servers** | How Bob reaches external systems (Jira, ServiceNow, GitHub, Terraform, etc.) | `.bob/mcp.json` |
| **Labs** | Hands-on exercises | `LABs/` in project root |
| **Recipes & Guides** | Playbooks and how-tos | `Recipes/` in project root |
| **Collections** | Curated kits — every asset an engagement needs, installed in one click | Installs all of the above |

---

## Current Catalog Size

The Marketplace aggregates assets from **4 geo repositories** (WW, EMEA, APAC, Japan, Sales Engineering) into a single shelf:

| Type | Count |
|---|---|
| Modes | 90 |
| Skills | 151 |
| Rules | 16 |
| MCP Servers | 14 |
| Labs | 27 |
| Recipes & Guides | 19 |
| Collections | 21 |
| **Total** | **338+** |

---

## Using the Marketplace for Bobathons

### Find Relevant Assets

In the Bob sidebar, search the Marketplace for:
- `"bobathon"` — Bobathon Builder Mode, Bobathon skills
- `"java modernization"` — Java-specific modes and skills
- `"ibm z"` or `"cobol"` — Z-specific assets
- `"ibm i"` or `"rpg"` — IBM i assets
- `"security"` or `"devsecops"` — Security and compliance assets

### Install a Collection

Collections are the fastest way to get everything an engagement needs:

1. Search for a relevant collection
2. Click **Install** — all included assets are added to the workspace in one action
3. Switch to the relevant mode and start building

### Ask Bob to Suggest Assets

Bob can fingerprint your project and recommend relevant Marketplace assets:

> *"What Marketplace assets would be useful for a Java modernization Bobathon?"*

Bob analyzes your open project and suggests assets that match the tech stack.

---

## Key Marketplace Assets for Bobathon Preparation

| Asset | Type | Use |
|---|---|---|
| **Bobathon Builder** | Mode + Skills | Full Bobathon preparation workflow |
| **Z Architect Mode** | Mode | Used in Z Bobathon labs 1–5 |
| **Z Code Mode** | Mode | Used in Z Bobathon labs 6–7 |
| **IBM i Developer Mode** | Mode | IBM i Bobathon all labs |
| **Java Modernization Mode** | Mode | Java Bobathon all labs |
| **Bob Badge Issuer Lite** | Mode + Skill | Badging at end of event |
| **Security Review Skill** | Skill | DevSecOps track |
| **BobRules Templates** | Rules | Governance and standards |

---

## Mode Hub

The **Bob Mode Hub** is a dedicated catalog for discovering custom modes:

🔗 [http://ibm.biz/modehub](http://ibm.biz/modehub)

---

## Offline Use

The Marketplace works without internet access:

1. Before traveling to a restricted site, pack a `.zip` of the Marketplace
2. On the sealed client site, mount the `.zip` as a local marketplace
3. Full search, detail views, and install work offline

---

## Contributing Assets

If you build a useful mode, skill, or lab during a Bobathon, consider contributing it back:

1. Drop a folder in the CE Bob repo — no forms, no review queue, no ceremony
2. It appears in the Marketplace sidebar for all CE practitioners
3. Others can install and reuse it

Every contributed asset saves the next CE practitioner hours of rebuilding work.
