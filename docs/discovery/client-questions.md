# Client Discovery Questions

!!! info "First Draft"
    This question bank is synthesized from the CE Bob Workshop Mural template and field experience. Use it as a starting point — not a rigid interview script. Tune questions to your client's context and the use cases you're exploring.

Use the [CE Bob Workshop (Mural)](https://ibm.biz/bob_ce_workshop) for structured facilitation of these questions in a working session with the client.

---

## General Developer Workflow & Productivity

These questions apply to any Bobathon type and help establish baseline pain.

**Qualitative:**

- Where do your developers spend the most time on things that feel repetitive or manual?
- How many tools does a developer switch between in a typical workflow, and where does that cause friction?
- Have you adopted AI coding assistants already? Where do they help, and where do they fall short?
- How difficult is onboarding today for new developers entering legacy codebases?

**Quantitative:**

- What is your average lead time from idea → production?
- What % of development time is spent on low-value vs. high-value tasks?
- What is your developer fully-loaded hourly rate? *(Used in ROI calc)*
- Total engineering hours per year on the tasks you're discussing?

---

## Codebase & System Complexity

- How complex are your codebases? (Monolith, microservices, multi-repo, legacy)
- What types of changes require updates across multiple files or systems?
- What % of codebases have adequate documentation today?
- How long does it take to onboard a new developer onto a project?

---

## Application Modernization

Relevant for Java, IBM i, and Z tracks.

**Qualitative:**

- How risky is each modernization effort perceived to be?
- How does legacy tech limit innovation or delivery speed?
- What skills gaps cause modernization delays?
- How important is modernization to your business strategy (scalability, cloud adoption, risk reduction)?

**Quantitative:**

- How much legacy code (KLOC or # of apps) requires refactoring or rewriting?
- What is the average time per modernization task today?
- How much of your engineering budget is spent on legacy maintenance?
- How often do modernization projects miss deadlines or exceed cost estimates?

---

## Testing & Quality

**Qualitative:**

- How confident are teams in test coverage and code quality?
- Do developers trust existing automated testing tools?
- How often does testing bottleneck releases?

**Quantitative:**

- How many hours per sprint do developers spend writing, running, and fixing tests?
- What is your average defect escape rate (bugs found in later stages or production)?
- What are the costs of production incidents attributed to insufficient testing?
- How many test suites exist today, and what % are automated vs. manual?

---

## Documentation & Knowledge Capture

**Qualitative:**

- Is documentation seen as valuable or a burden?
- How does knowledge loss affect projects during turnover?
- How much time is spent rediscovering or re-learning undocumented logic?

**Quantitative:**

- How many hours per week are spent creating or maintaining documentation?
- How long does it take to onboard a new developer onto a project?
- What % of codebases have adequate documentation today?

---

## Security & Compliance

**Qualitative:**

- How confident are security teams in the consistency of secure coding practices?
- How often do compliance blockers delay releases?
- What areas feel risky (crypto, authentication, APIs, data handling)?

**Quantitative:**

- How many hours per project go into security reviews or compliance tasks?
- How many vulnerabilities are discovered per release cycle?
- What is your typical time to remediate vulnerabilities?
- How long do compliance cycles (FedRAMP, PCI, SOC2, internal audit) take today?

---

## Bug Fixing & Incident Response

**Qualitative:**

- Do developers feel confident navigating unfamiliar codebases?
- What recurring issues cause repetitive debug cycles?
- How do unresolved bugs impact customer experience or brand trust?

**Quantitative:**

- How many bugs are opened per month, and how many are Sev1/Sev2?
- What is the average MTTR?
- How many engineering hours go into debugging per week?
- What is the average cost of a critical incident?

---

## Architecture, Environment & Tools

- What does your current DevOps/toolchain landscape look like (IDEs, CI/CD, security, observability)?
- Are you managing multicloud or hybrid environments?
- Where do security checks occur today — code writing, PR review, pipelines, or production?
- Do developers have clear guardrails and standards when introducing changes?

---

## AI Readiness (Optional)

Use these to gauge where the client is in their AI journey and any blockers.

- What are your AI goals? What do you want your AI position to be in 2 years?
- How does Trustworthy AI, AI Ethics, Compliance, and Security affect your decision to engage this technology?
- What internal or external barriers are currently holding you back from AI adoption?
- What is currently making your AI initiatives successful (if any)?
- Do you have an AI tool approval or security review process? How long does it typically take?

---

## Environment & Access (Required Before Scoping)

| Question | Why It Matters |
|---|---|
| Do attendees have admin rights to install tools? | Determines if we need VM or CE laptop fallback |
| Can attendees create an IBM Cloud account, or is that blocked? | Affects environment path |
| Any air-gapped or no-internet restrictions on the day? | May require pre-configured VMs |
| Is the client codebase accessible in VS Code? | Required if using client code |
| How large is the codebase? (# programs / KLOC) | Scanner size limits apply for local environments |
| Are there AI tool usage policies or approval requirements already in place? | May add 2–4 weeks |

---

## Capturing Outputs

Use the **Business Value Questioning** canvas in the [CE Bob Workshop (Mural)](https://ibm.biz/bob_ce_workshop) to record answers and build toward an MVP Statement:

> *With [description of the Bobathon scope], if we provide [target users] a way to [capability], by measuring [metric], we will address the risk of [pain], and we'll know we've arrived if [target outcome].*
