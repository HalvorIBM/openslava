# Pitch Conversation Guide

!!! info "First Draft"
    This is a first-draft conversation guide synthesized from CE field experience and positioning materials. It is intended as a starting framework — evolve it with your team's real-world talk tracks and client responses.

---

## The Goal

Move the client from "interesting demo" to "let's do a Bobathon" in a single discovery conversation. The guide is structured as a sequence of questions and pivots — not a script.

---

## Phase 1: Open with Pain (5–10 min)

Start with their world, not Bob's features.

**Opening questions:**

> *"Where does your team spend the most time on things that feel repetitive or slow — is it documentation, testing, understanding legacy code, or something else?"*

> *"When a developer joins a new project, how long does it take before they're genuinely productive?"*

> *"Do you have a modernization backlog — apps that need to move to newer Java, get containerized, or be refactored — that keeps getting pushed back?"*

**What you're listening for:**

- Time lost to manual, repetitive tasks
- Fear or friction around legacy codebases (COBOL, old Java, RPG)
- Testing debt / low confidence in coverage
- Documentation gaps causing onboarding pain
- Security reviews slowing releases

---

## Phase 2: Introduce Bob (5 min)

Once a pain point surfaces, connect it directly to Bob. **Lead with the outcome, not the feature.**

| If they say... | You say... |
|---|---|
| *"We spend forever writing docs for our legacy COBOL"* | "Bob can generate architecture documents, call graphs, and plain-English explanations of any COBOL program in minutes. We've had clients say it eliminated weeks of archaeology work." |
| *"Our Java apps are 10 years old and nobody wants to touch them"* | "Bob has a Java Modernization Premium Package — it can assess your entire WAS/Spring app, map the upgrade path, and generate the refactored code while preserving your business logic." |
| *"Testing is our bottleneck"* | "Bob generates unit tests from existing code or requirements, with full context of your codebase. Teams report going from near-zero coverage to 80%+ in days." |
| *"We have an AI tool already"* | "What platform is it? Bob differentiates most strongly on legacy and enterprise contexts — if you're running COBOL, RPG, or older Java, generic AI coders don't have the domain knowledge Bob's Premium Packages provide." |

---

## Phase 3: Introduce the Bobathon (5 min)

> *"What we like to do is prove this on your actual code — not a contrived demo. A Bobathon is a one-day hands-on session where your developers work alongside our Client Engineers, using Bob on your real problems. You walk away with a working prototype, not a slide deck."*

**Key points to land:**

- **No cost** — CE engagement is complimentary
- **Your code** — we work on their actual stack if possible
- **Real output** — working artifacts they keep
- **Low risk** — it's a learning day, not a production deployment
- **Leads somewhere** — the Bobathon is the on-ramp to a 2–3 week pre-sales pilot focused on fast, demonstrable outcomes

---

## Phase 4: Qualify (5–10 min)

Before committing, quickly confirm viability:

| Question | What You Need to Know |
|---|---|
| *"Who would attend — mostly developers, architects, or mixed?"* | Drives lab selection and depth |
| *"How many people are you thinking — 5, 10, 20?"* | Determines CE staffing and room needs |
| *"What does your IT policy look like around installing new tools or creating IBM Cloud accounts?"* | May trigger air-gapped or VM environment path |
| *"Is there a tech lead or COBOL/RPG expert who could be in the room?"* | Critical for Z and IBM i events |
| *"Who's the executive sponsor? What does success look like for them?"* | Needed for pilot proposal framing |

---

## Phase 5: Close to Next Step

Don't close to a date — close to a scoping conversation.

> *"What I'd suggest is a 30-minute scoping call with you and your tech lead. We'll confirm the use cases, check the environment, and I can have a proposed agenda back to you within a week. What does your calendar look like?"*

**Or if they're ready to move:**

> *"To get the ball rolling, I'll put in a request to our Client Engineering team and they'll be in touch within a day or two. The form takes about 5 minutes — I can walk you through it now if you'd like."*

---

## Red Flags to Watch For

!!! warning "Proceed with caution if..."
    - Client wants IBM to do *all* the work and not involve their developers — the Bobathon requires developer participation
    - No executive sponsor identified — pilot proposals need someone to sell to
    - AI tool policy approval is pending — factor in 2–4 weeks for TechZone/security review
    - Client insists on using a massive, uncharted codebase with no lead time — flag the 3-week minimum for custom content

---

## Related Resources

- [Value Proposition](value-proposition.md) — pricing, productivity data, differentiators
- [How to Engage CE](how-to-engage.md) — ISC/DSR submission steps
- [CE Bob Workshop (Mural)](https://ibm.biz/bob_ce_workshop) — structured discovery template for deeper use case exploration
- [Bob Sales Kit (Seismic)](https://ibm.seismic.com/Link/Content/DCg4cRfBQ6V7G8TW3ppJ6XT8qcM3)
