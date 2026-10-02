# GFM Bank — Security Audit & Remediation

**Part 3 of 3** · IBM Bob Workshop

---

## Audience

Security engineers, DevSecOps professionals, and developers responsible for secure coding practices in banking and financial services applications.

---

## Goal

Demonstrate how IBM Bob can:

- Discover security vulnerabilities in code
- Categorise issues by severity and type (OWASP, CWE)
- Generate compliance-ready security audit reports
- Propose and apply secure code fixes
- Verify remediation effectiveness

We audit the **GFM Bank data pipeline** code, which contains intentional security vulnerabilities for training purposes.

---

## Bob Mode

> **Required mode: Agent**
>
> Agent mode lets Bob read all files, generate reports, and write the fixed versions.

---

## Lab Files

| File | Purpose |
|---|---|
| `security-audit/code/data_pipeline.py` | Batch data ingestion pipeline — contains intentional vulnerabilities |
| `security-audit/code/synthetic_generator.py` | Synthetic data generator — contains intentional vulnerabilities |

> **Note:** These files contain **intentional security vulnerabilities** for educational purposes only. Do not run them in a production or networked environment.

---

## Workshop Flow

1. Discover vulnerabilities across both files
2. Generate a formal security audit report
3. Document the top-5 critical findings in detail
4. Apply secure fixes and produce remediated files
5. Verify remediation completeness

---

## Step A — Discover Vulnerabilities

### Prompt

```
Analyse data_pipeline.py and synthetic_generator.py for security vulnerabilities.

For each vulnerability found, provide:
1. File and line number
2. Vulnerability type and OWASP / CWE category
3. Description of the security risk
4. Potential attack scenario
5. Severity rating (Critical / High / Medium / Low) with justification
```

### Expected findings

**`data_pipeline.py`**

| # | Vulnerability | CWE | Severity |
|---|---|---|---|
| 1 | Hardcoded database credentials | CWE-798 | Critical |
| 2 | SQL injection via f-string formatting | CWE-89 | Critical |
| 3 | Command injection via `shell=True` | CWE-78 | Critical |
| 4 | Insecure deserialization (`pickle.loads`) | CWE-502 | Critical |
| 5 | SSL verification disabled (`verify=False`) | CWE-295 | High |
| 6 | Overly permissive file mode (`0o777`) | CWE-732 | Medium |

**`synthetic_generator.py`**

| # | Vulnerability | CWE | Severity |
|---|---|---|---|
| 7 | Hardcoded JWT secret | CWE-798 | Critical |
| 8 | Insecure randomness for tokens | CWE-330 | High |
| 9 | Arbitrary code execution via `exec()` | CWE-94 | Critical |
| 10 | Weak password hashing (MD5) | CWE-328 | High |
| 11 | Secrets written to disk in plaintext | CWE-312 | High |
| 12 | Command injection via string concatenation | CWE-78 | Critical |

---

## Step B — Generate Security Audit Report

### Prompt

```
Generate a comprehensive SECURITY_AUDIT_REPORT.md that includes:

1. Executive Summary
   - Files analysed
   - Vulnerability count by severity
   - Overall risk assessment
   - Top 3 recommendations

2. Vulnerability Inventory
   For each finding:
   - Unique ID (e.g. VULN-001)
   - File and line number
   - Title
   - CWE / OWASP classification
   - Severity (Critical / High / Medium / Low)
   - Description
   - Attack scenario
   - Business impact for a banking system
   - Remediation recommendation

3. Risk Matrix — vulnerabilities plotted by severity × likelihood

4. Remediation Roadmap — prioritised fix order with effort estimates

5. Secure Coding Guidelines — language-specific Python recommendations
   to prevent recurrence

Save as SECURITY_AUDIT_REPORT.md in the current directory.
```

---

## Step C — Document the Top 5 Critical Findings

### Prompt

```
For the 5 most critical vulnerabilities, create detailed remediation guidance:

1. SQL Injection in data_pipeline.py
   - Show the vulnerable code
   - Explain why it is vulnerable
   - Demonstrate a plausible exploit input
   - Show the secure fix using parameterised queries

2. Command Injection (shell=True)
   - Identify all instances
   - Explain the injection risk
   - Provide secure subprocess alternatives

3. Insecure Deserialization (pickle)
   - Explain the remote code execution risk
   - Show how an attacker could craft a malicious pickle
   - Recommend safe alternatives (JSON, msgpack)

4. Hardcoded Secrets
   - List all hardcoded credentials and keys
   - Explain exposure risks (version control, logs)
   - Show how to use environment variables or a secrets manager

5. Code Injection via exec()
   - Explain the arbitrary execution risk
   - Provide safe alternatives for user-supplied transforms
     (e.g. restricted operator application, allowlisted operations)
```

---

## Step D — Apply Secure Fixes

### Prompt

```
Fix all security vulnerabilities in data_pipeline.py and synthetic_generator.py.

For each fix:
- Apply the secure coding pattern
- Add a brief comment explaining the security improvement
- Ensure the fix does not break the existing logic

Specifically:
- Replace f-string SQL with parameterised queries
- Replace shell=True with subprocess argument lists
- Remove or externalise all hardcoded credentials (use os.environ.get)
- Replace pickle with JSON for serialisation
- Enable SSL verification
- Change file permissions to 0o600
- Replace MD5 with hashlib.sha256 or bcrypt
- Replace random with the secrets module
- Remove exec() and replace with a safe functional equivalent
- Use os.environ.get for the JWT secret

Save as:
  data_pipeline_secure.py
  synthetic_generator_secure.py
```

---

## Step E — Verify Remediation

### Prompt

```
Review the fixed files and verify that:

1. Every vulnerability in the audit report has been addressed
2. No new issues were introduced in the fixes
3. The code still performs its intended function

Generate REMEDIATION_VERIFICATION.md with:
- A checklist mapping each VULN-ID to its fix status
- Any remaining concerns or hardening recommendations
- Suggestions for automated security testing (SAST, dependency scanning)
```

---

## Vulnerability Reference

### OWASP Top 10 coverage

| Category | Relevant findings |
|---|---|
| A02 — Cryptographic Failures | MD5 hashing, hardcoded secrets, plaintext secret files |
| A03 — Injection | SQL injection, command injection, code injection (`exec`) |
| A04 — Insecure Design | `exec` for user-supplied transforms |
| A05 — Security Misconfiguration | Disabled SSL, permissive file modes |
| A07 — Authentication Failures | Hardcoded credentials |
| A08 — Data Integrity Failures | Pickle deserialization |

---

## Expected Outputs

| File | Description |
|---|---|
| `SECURITY_AUDIT_REPORT.md` | Full vulnerability inventory, risk matrix, remediation roadmap |
| `data_pipeline_secure.py` | Fully remediated pipeline |
| `synthetic_generator_secure.py` | Fully remediated generator |
| `REMEDIATION_VERIFICATION.md` | Fix checklist and further recommendations |

---

## Reflection Questions

1. Which vulnerability was easiest for Bob to find? Which required the most detailed prompt?
2. How does Bob's output compare to a traditional SAST scanner (e.g. Bandit, Semgrep)?
3. What additional steps would a real PCI-DSS audit require beyond what Bob produced here?
