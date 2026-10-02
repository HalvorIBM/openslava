# Other Labs

The CE Bob Marketplace and lab repository contain labs for a wide range of platforms and use cases beyond the core tracks. This page provides an overview of what's available.

🔗 **Full lab repository:** [https://github.ibm.com/ClientEngineering/bob/tree/main/LABs](https://github.ibm.com/ClientEngineering/bob/tree/main/LABs)

🔗 **APAC lab catalog:** [https://bob-lab-app.29szhis02s11.au-syd.codeengine.appdomain.cloud/](https://bob-lab-app.29szhis02s11.au-syd.codeengine.appdomain.cloud/)

---

## Available Labs

| Lab | Platform / Focus | Description | Lead Time |
|---|---|---|---|
| **Integration Track** | ACE · API Connect · CP4I | API documentation, integration flow analysis, message mapping, connector generation | 1–2 weeks |
| **Automation Track** | BAW · ODM · Ansible · Terraform | Playbook generation, workflow docs, rule extraction, process automation | 2–3 weeks |
| **Agentic AI Track** | watsonx Orchestrate · ADK | Multi-agent architecture, knowledge ingestion, skill authoring, orchestration | 2–3 weeks |
| **DevSecOps with Bob** | Security / Compliance | Security checks, policy enforcement, Bob Findings integration, Snyk/Semgrep MCP | 1–2 weeks |
| **Ansible + Terraform** | Infrastructure / DevOps | IaC generation, playbook automation, z/OS Ansible | 1–2 weeks |
| **IBM AIX / PowerVM** | AIX / Power Systems | AIX administration, PowerVM management, automation | 1–2 weeks |
| **OpenShift with Bob** | Containers / Kubernetes | Container deployment, OpenShift operations | 1–2 weeks |
| **IBM Maximo Script Modernization** | EAM / Automation | Maximo scripting and modernization | 1–2 weeks |
| **IBM MQ Operations with Bob** | Middleware / MQ | MQ troubleshooting, operations, automation | 1–2 weeks |
| **ABAP to Java** | SAP / Modernization | ABAP modernization path exploration | 2–3 weeks |
| **Banking (Python + React)** | Web / Python | Python API + React Carbon UI development | 1–2 weeks |
| **Automotive (C++)** | C++ / Embedded | C++ application modernization | 1–2 weeks |
| **Manufacturing (.NET)** | .NET | .NET application modernization | 1–2 weeks |
| **Telecom (Spring 4 + CXF SOAP)** | Java / SOAP | SOAP to REST modernization | 1–2 weeks |
| **IBM Planning Analytics** | Analytics / TM1 | Planning Analytics script development | 1–2 weeks |
| **AI-Assisted Pipeline Recovery** | DevOps / CI/CD | Pipeline failure diagnosis and recovery | 1–2 weeks |
| **COBOL to Java** | Modernization | COBOL→Java transformation path | 2–3 weeks |

---

## Integration Track (ACE & API Connect)

The Integration track accelerates hybrid integration and API development using IBM Bob.

* **Target Technologies:** App Connect Enterprise (ACE), API Connect, Cloud Pak for Integration (CP4I), IBM MQ
* **Representative Use Cases:**
    * Generating OpenAPI documentation from existing integration flows
    * Analyzing complex ESQL / Java compute nodes for migration
    * Accelerating message mapping and transformation schemas
    * Creating and testing custom connectors and policies
* **Lead Time:** 1–2 weeks with standard integration patterns; 3+ weeks when connecting to client-specific ESB runtimes.

---

## Automation Track (BAW, ODM & Ansible)

Targets business automation analysts and process developers modernizing legacy workflows and business rule engines.

* **Target Technologies:** Business Automation Workflow (BAW), Operational Decision Manager (ODM), Ansible Automation Platform, Terraform
* **Representative Use Cases:**
    * **Rule Extraction:** Extracting and structuring business decision tables from monolithic legacy code
    * **Workflow Documentation:** Auto-generating process flow diagrams and step specifications
    * **Playbook Authoring:** Synthesizing validated Ansible playbooks and Terraform modules from natural language requirements
* **Lead Time:** 2–3 weeks (requires pre-event curation of representative decision tables or workflow definitions).

---

## Agentic AI Track (watsonx Orchestrate & Multi-Agent)

Designed for teams building intelligent agent architectures and custom AI skills.

* **Target Technologies:** watsonx Orchestrate, Agent Development Kit (ADK), vector databases (Milvus/pgvector)
* **Architecture Pattern:**
    * Using Bob to script document chunking, embedding, and vector database ingestion
    * Building specialized domain agents (e.g., Domain Policy Agent, Pricing/Cost Calculator Agent, Authorization Agent, Program Specialist)
    * Wiring agents into an orchestrated supervisory workflow with natural language routing
* **Lead Time:** 2–3 weeks (requires confirmed watsonx Orchestrate tenant and API access).

---

## DevSecOps Track

!!! info "Coming Soon — materials being developed"
    The DevSecOps track is a high-priority addition. IBM Bob's DevSecOps Premium Package covers:

    - **Bob Findings** — automated security vulnerability detection in code
    - **Snyk MCP integration** — real-time dependency scanning
    - **Semgrep integration** — SAST analysis within Bob workflows
    - **Compliance evidence generation** — automated documentation for FedRAMP, PCI-DSS, SOC2 audit cycles
    - **Security workflow guardrails** — BobRules for enforcing secure coding patterns

    **Contact the CE team for current lab materials.** A dedicated lab guide is being developed. Reference: [DevSecOps-with-Bob lab](https://github.ibm.com/ClientEngineering/bob/tree/main/LABs/DevSecOps-with-Bob)

---

## z/OS IT Ops (Ansible Playbook Generation)

This use case is distinct from the Z Modernization track — it targets **Infrastructure & Operations** teams rather than application developers.

**Business problem:** Each Ansible playbook takes ~8 hours to write, modify, or deploy. This consumes a large portion of I&O engineers' time and limits how quickly new services can be provisioned.

**What Bob does:**
- Translates a natural-language infrastructure request into a complete Ansible playbook
- Lints and stores the playbook in Git
- Deploys through a CI/CD pipeline

**Business value:**
- Significant decrease in manual scripting effort
- Accelerated provisioning cycles
- Improved automation scalability without proportional staffing increases

🔗 [DevOps-Ansible-and-Terraform lab](https://github.ibm.com/ClientEngineering/bob/tree/main/LABs/DevOps-Ansible-and-Terraform)

---

## IBM AIX / Power Systems

For clients running AIX or Power Systems, Bob assists with:

- System administration scripting
- PowerVM management automation
- AIX troubleshooting and diagnostics
- HMC (Hardware Management Console) operations

🔗 [IBM AIX-PowerVM lab](https://github.ibm.com/ClientEngineering/bob/tree/main/LABs/IBM%20AIX-PowerVM)

🔗 [IBM HMC for Power Systems with Bob](https://github.ibm.com/ClientEngineering/bob/tree/main/LABs/IBM%20HMC%20for%20Power%20Systems%20with%20Bob)

---

## Suggesting a New Lab

If you've built a lab for a client engagement that could benefit the broader CE community, contribute it to the CE Bob Marketplace:

1. Package your lab in the standard format (README, lab guide markdown, sample code, starting snapshot, endpoint snapshot)
2. Add it to the appropriate section of the CE Bob repo
3. Submit to the Marketplace via the standard contribution process

🔗 [CE Bob Marketplace contribution guide](https://ibm.biz/ce-bob-marketplace)

!!! tip "Build new labs with Bob"
    Use Bob's Bobathon Builder Mode to scaffold a new lab guide. Ask Bob: *"Help me create a new lab guide for [technology / use case]"* — it will generate the structure, objectives, and step-by-step instructions as a first draft.
