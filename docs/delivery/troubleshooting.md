# Troubleshooting Guide

Common issues and how to resolve them — organized by when they occur.

---

## Pre-Event Office Hours Issues

| Issue | Resolution |
|---|---|
| Attendee can't install Bob | Check admin rights. Try running installer as admin. If blocked: prepare CE laptop or VM as fallback. |
| IBM Cloud account creation blocked | Work with client IT. Identify if there's an org-approved path. Fallback: pre-configured VM. |
| Box share link expired | Box links expire in 24hrs even with custom dates. Switch to client's own file share or GitHub repo immediately. |
| TechZone invite not received | Verify email address. Re-send invite. Add attendee directly in TechZone admin. Allow 15–30 min to propagate. |
| Java 21 install fails | Check if a version already exists (`java -version`). Check PATH. IBM Semeru `.msi` (Windows) or `.pkg` (macOS) is most reliable. |
| Z Open Editor won't load | 99% of cases: Java 21 not installed, not on PATH, or wrong version. Verify `java -version` in a new terminal. |
| VS Code IBM i extension can't connect to LPAR | Verify LPAR IP / port / credentials. Check that the port (usually 8470 or 8476) is accessible. Test with a direct SSH first. |

---

## Environment Issues (Day-of)

| Issue | Resolution |
|---|---|
| **Attendee machine won't install Bob** | Pair with another attendee or use CE laptop. Don't delay the session for one machine. |
| **TechZone / LPAR unreachable** | 1. Check TechZone status. 2. Try a different network (hotspot). 3. Switch to pre-configured VM. 4. Pair with another attendee. |
| **IBM Cloud account locked / unverified** | Have attendee check email for verification link. If expired, re-trigger verification. Pair with working account as fallback. |
| **Bob won't start** | Restart VS Code. Check internet connection (IBM Cloud path requires internet). Check `.bob/` folder is not corrupted. |
| **Bob license not activating** | Verify IBM Cloud account is using the correct email. Check Bob subscription status in IBM Cloud console. CE can re-provision. |
| **Wi-Fi overloaded** | Prioritize CE presenter machine on a different network (hotspot or wired). Reduce number of simultaneous AI calls if causing slowness. |

---

## Bob Behavior Issues

| Issue | Resolution |
|---|---|
| **Bob produces generic / unhelpful output** | 1. Rephrase with more context. 2. Add the file/code you want Bob to focus on. 3. Switch to the appropriate mode (Z Architect, IBM i Developer, etc.). 4. Run a workspace scan / initialize Agent.md first. |
| **Bob ignores context in the workspace** | Run `scan workspace` or equivalent workspace initialization command. Ensure the lab directory is the open workspace folder, not a parent directory. |
| **Bob is very slow** | Check internet connection. Check Bob status page. Reduce prompt complexity. Switch to a lighter model if option available. |
| **Bob produces code with errors** | This is normal and expected — Bob iterates. Paste the error back to Bob and ask it to fix. This is a useful teaching moment. |
| **Bob loses context mid-lab** | Open a new conversation and re-paste the relevant context. This is a known limitation of context windows — structure prompts to include necessary context each time. |
| **Wrong mode active** | Check the mode selector in the Bob sidebar. Switch to the appropriate mode for the lab. |

---

## Lab-Specific Issues

=== "IBM Z"

    | Issue | Resolution |
    |---|---|
    | Z Open Editor not loading | Verify Java 21 is installed and on PATH. Restart VS Code after confirming. |
    | Workspace scan fails | Check that GenApp folder is the root open folder in VS Code, not a subfolder. |
    | pp4z features not available | Confirm Premium Package for Z is activated on the IBM Cloud account. |
    | GenApp programs not found | Ensure `.zip` was extracted correctly and the folder (not the zip) is opened in Bob. |

=== "IBM i"

    | Issue | Resolution |
    |---|---|
    | Cannot connect to IBM i LPAR | Check connection settings (host, port 8470/8476, credentials). Try SSH to same host. Check firewall. |
    | Source members not showing | Verify library list includes the application library. Check VS Code IBM i extension is connected. |
    | PPi features not available | Confirm Premium Package for i is activated. Check mode selector — switch to IBM i Developer mode. |
    | Multi-user library conflicts | Ensure each attendee has their own library copy (`CPYLIB` per user). |

=== "Java Modernization"

    | Issue | Resolution |
    |---|---|
    | Sample project won't build | Check Java version (`java -version`). Check Maven (`mvn -v`) or Gradle. Run `mvn clean install` to identify specific errors. |
    | Bob can't see the project | Ensure the project folder (not parent) is the open workspace in Bob. Run workspace scan. |
    | javax→jakarta migration incomplete | This is often intentional — the lab asks Bob to do one pass, then you review. Show the remaining items as a discussion point. |

---

## Client Access Issues

| Issue | Resolution |
|---|---|
| **Client can't share their codebase** | Switch to the provided sample application. Frame as "let's learn the pattern on this code, then you apply it to yours next week." |
| **Security review blocking Bob installation** | This can take 2–4 weeks at some clients. Always check early. Fallback: use CE laptops with pre-installed Bob. |
| **VPN blocks Bob cloud connection** | Try connecting without VPN (if policy allows). Fallback: pre-configured VM with Bob pre-authenticated. |
| **Admin rights required for install** | Work with client IT contact. Fallback: pre-configured VM or CE laptops. |

---

## Escalation

If an issue can't be resolved on the day:

- **Bob technical issues:** [bob.ibm.com](https://bob.ibm.com) support, or CE Slack channels
- **TechZone issues:** TechZone support portal
- **Z/i environment issues:** Contact the Z or i specialist team via CE Slack
- **Badge issues:** [https://bob-badge-portal.ce.techzone.ibm.com/](https://bob-badge-portal.ce.techzone.ibm.com/) — or contact the IBM badge team
- **Licensing:** IBM Bob sales / CE manager escalation path
