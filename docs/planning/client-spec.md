# Client Context Spec Template

!!! info "First Draft — evolve with your team"
    This template is a starting point. Fill in what you know from discovery conversations and scoping calls. You don't need every field — partial context is better than none.

## How to Use This Template

1. **Copy this file** into your working folder as `client-spec.md`
2. **Fill in what you know** — even a half-filled spec dramatically improves Bob's output
3. **Open the Bobathon Builder repo** in Bob and tell it:

```
"I want to build a Bobathon for a client. 
I've captured the context in client-spec.md — 
please read that file and then run the setup_new_bobathon workflow."
```

Bob will read your spec, skip questions it can already answer, and ask only about gaps.

---

## The Template

Copy everything below the divider into your `client-spec.md` file.

---

```markdown
# Bobathon Client Context Spec
# ============================================================
# Fill in what you know. Leave fields blank if unknown — 
# Bob will ask during the intake workflow.
# ============================================================

## Client Basics

- **Company name:** [e.g. Acme Financial Services]
- **Industry / market segment:** [e.g. Banking / Financial Services]
- **Primary contact name:** [Name]
- **Primary contact email:** [email@company.com]
- **Account team contact:** [IBM contact name]
- **Opportunity / engagement ID:** [if applicable]

---

## Application Context

<!-- What application(s) will participants work on during the Bobathon? -->

- **Application name / description:** [e.g. Core banking transaction processing system]
- **What does it do?** [2–3 sentences describing the application's purpose and users]
- **Current state:** [e.g. Java 8, Spring Boot 1.5, deployed on WebSphere, Oracle DB]
- **Target / desired state:** [e.g. Java 21, Spring Boot 3, Liberty, PostgreSQL]
- **Codebase size (rough):** [e.g. ~50 Java classes, 200K LOC, 30 COBOL programs]
- **Code access on the day:** [Client repo / Sample app provided / TBD]
  - If client repo: URL and access method: [URL / VPN / SSH]

---

## Technology Stack

<!-- Be as specific as possible — this drives all lab customization -->

- **Primary language(s):** [e.g. Java, COBOL, RPG, Python, TypeScript]
- **Frameworks / runtimes:**
  - [e.g. Spring Boot 1.5, Struts, WAS Liberty]
  - [e.g. React 17, Angular 14]
- **Database(s):** [e.g. Oracle 19c, DB2, PostgreSQL, MySQL]
- **Infrastructure / cloud:** [e.g. On-prem WAS, AWS EKS, OpenShift, IBM Cloud]
- **Version control:** [e.g. GitHub Enterprise, GitLab, Bitbucket, RDz]
- **CI/CD toolchain:** [e.g. Jenkins, GitHub Actions, UCD]
- **IDE in use today:** [e.g. Eclipse, IntelliJ, RDz, VS Code, IBM i Developer]
- **Other key tools:** [e.g. Jira, Confluence, ServiceNow, SonarQube, Dynatrace]

### Special Platform Flags

- [ ] **IBM Z / Mainframe** — COBOL/JCL/PL/I (requires pp4z Premium Package)
- [ ] **IBM i / AS400** — RPG/COBOL/CL (requires PPi Premium Package)
- [ ] **Java EE / WebSphere** — Java Modernization Premium Package
- [ ] **Air-gapped / restricted network** — No internet access on the day
- [ ] **Admin rights restricted** — Attendees cannot install software

---

## Developer Pain Points

<!-- What problems does the development team face every day?
     These become the use cases for the Bobathon. -->

Rank from most to least painful:

1. **[Pain point 1]** — [Brief description, estimated time lost per week/sprint]
   - e.g. "Documenting legacy COBOL programs — ~2 days per sprint"
2. **[Pain point 2]** — [Brief description]
3. **[Pain point 3]** — [Brief description]

### Context Questions (fill in what you know)

- Where do developers spend the most time on repetitive / manual tasks?
  [Answer]

- How long does it take to onboard a new developer onto the codebase?
  [Answer]

- What is the modernization backlog? (apps that need updating, platforms to migrate)
  [Answer]

- What does the current DevOps / toolchain landscape look like?
  [Answer]

- Are there AI tools in use today? If so, what and where do they fall short?
  [Answer]

---

## Prioritized Use Cases

<!-- 1–3 use cases for the Bobathon. Be specific. -->
<!-- See docs/discovery/client-questions.md for discovery prompts. -->

### Use Case 1 (High Priority)
- **Name:** [e.g. COBOL documentation generation]
- **Description:** [What Bob will help them do]
- **Business impact:** [e.g. Reduces documentation time from 2 days to 2 hours per program]
- **Bob capability:** [e.g. Z Architect mode — Technical Design Document]
- **Estimated lab time:** [e.g. 30 min]

### Use Case 2 (High Priority)
- **Name:** [e.g. Impact analysis before a field change]
- **Description:** [What Bob will help them do]
- **Business impact:** [e.g. Reduces change analysis risk; currently done manually over 3 days]
- **Bob capability:** [e.g. Z Architect mode — Impact Analysis Lab]
- **Estimated lab time:** [e.g. 30 min]

### Use Case 3 (Medium Priority — if time allows)
- **Name:** [e.g. Unit test generation for untested modules]
- **Description:** [What Bob will help them do]
- **Business impact:** [e.g. Increases test coverage from ~10% to >60%]
- **Bob capability:** [e.g. Z Code mode — test generation]
- **Estimated lab time:** [e.g. 45 min]

---

## Participants

- **Expected headcount:** [e.g. 8–12]
- **Roles attending:**
  - [e.g. 6 COBOL developers]
  - [e.g. 2 tech leads / architects]
  - [e.g. 1 DevOps engineer]
- **Skill levels:**
  - [e.g. COBOL: 5 experienced (10+ yrs), 3 junior (<2 yrs)]
  - [e.g. AI tooling experience: mostly none]
- **Format:** [ ] In-person  [ ] Remote  [ ] Hybrid
- **Named pilot attendee (lowest permissions):** [Name]
- **Client lead (logistics / prereqs):** [Name]
- **Domain SME available on the day?** [e.g. Yes — Jane Smith, senior COBOL developer]

---

## Event Logistics

- **Preferred date / date range:** [e.g. Week of July 14]
- **Preferred duration:** [ ] 90-min sprint  [ ] Half-day (3hr)  [ ] 4-hr (Z standard)  [ ] Full day (6hr)
- **Location:** [City / building / virtual]
- **Time zone:** [e.g. US/Eastern]

### Environment Constraints

- **Can attendees install software?** [ ] Yes  [ ] No  [ ] With IT approval
- **Can they create an IBM Cloud account?** [ ] Yes  [ ] No  [ ] Unknown
- **Network restrictions on the day?** [ ] None  [ ] Proxy/firewall  [ ] Air-gapped
- **AI tool policy / security review required?** [ ] Yes (allow 2–4 extra weeks)  [ ] No  [ ] Unknown
- **Preferred environment path:**
  [ ] IBM Cloud account  [ ] Pre-configured VM  [ ] CE-provided laptops  [ ] TBD

---

## Success Criteria

<!-- How will the client (and you) know the Bobathon was successful? -->

- **Immediate (end of day):**
  1. [e.g. Every developer can independently generate a TDD for a COBOL program]
  2. [e.g. At least one impact analysis completed on a real change candidate]
  3. [e.g. Positive developer reaction — >4/5 satisfaction]

- **Short-term (1–2 weeks):**
  1. [e.g. At least 3 developers using Bob independently on their backlog]
  2. [e.g. Pilot scope agreed]

- **Long-term (pilot outcome):**
  1. [e.g. Measurable reduction in documentation time]
  2. [e.g. Exec sponsor approves commercial licensing discussion]

---

## Executive Sponsor

- **Name / role:** [e.g. VP of Application Development]
- **Primary KPI they care about:** [e.g. Reduce cost of mainframe maintenance by 20%]
- **Will they attend the Bobathon?** [ ] Yes  [ ] No  [ ] Exec briefing instead
- **Key messages for the pilot proposal:**
  [e.g. "Speed up modernization roadmap"; "Reduce dependency on scarce COBOL expertise"]

---

## Additional Context

<!-- Anything else that would help Bob generate better materials:
     - Compliance requirements (HIPAA, PCI, FedRAMP)
     - Cultural / language considerations
     - Prior failed AI tool evaluations
     - Executive politics or sensitivities
     - Related IBM engagements in flight
     - Specific code patterns or naming conventions to be aware of -->

[Notes]

---

## CE Team

- **CE Lead:** [Name / email]
- **Additional CE support:** [Names]
- **Planned IBM Slack channel:** [channel name]
- **DSR submitted?** [ ] Yes — ID: [DSR-XXXX]  [ ] Pending

---
*Created: [date] | Updated: [date] | Status: [ ] Draft  [ ] Ready for Builder*
```
