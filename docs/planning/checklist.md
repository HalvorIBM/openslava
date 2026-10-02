# Pre-Event Checklist

Complete all items **before event day**. The checklist is organized by area. Assign owners and target dates for each section.

!!! tip "Pilot attendee"
    Designate one attendee with the **lowest permission level** on the client team as the pilot attendee. They run through all prereq installs ahead of the event, identifying access or install issues before the day itself.

---

## ✅ Attendee List

- [ ] Collect full names and email addresses (required for account setup and access provisioning)
- [ ] Collect technical background and role (calibrates lab complexity and content depth)
- [ ] Confirm in-person vs. remote per attendee (ideally everyone in-person; know the in-room headcount)
- [ ] Designate a pilot attendee — lowest permission level, tests access and installs before event
- [ ] Add all client attendees to any TechZone environments **before** the Bobathon (TZ requests are slow)
- [ ] Create a dedicated Slack channel for the IBM CE team

---

## ✅ Pre-Event Access & Setup

- [ ] Attendees install required tools **the day prior** — not day-of
- [ ] IBM CE sets up and invites all attendees — confirms access before day-of
- [ ] Pre-event office hours scheduled and confirmed (1 day before event)
- [ ] Every attendee verifies installation during office hours (or provides a screenshot showing system status)
- [ ] Bob installation complete — if client requires AI Security Review, allow 2–4 additional weeks
- [ ] IBM Cloud accounts created and Bob license activated (if using IBM Cloud path)
- [ ] File sharing method confirmed (client system preferred; if using Box, remember external links expire in 24 hours — regenerate morning-of)

### Track-Specific Prerequisites

=== "IBM Z"

    - [ ] Java 21 JDK installed on every attendee machine (IBM Semeru Runtimes recommended)
    - [ ] IBM Z Open Editor verified: opens without errors
    - [ ] pp4z instance provisioned (minimum 1 week before event — request immediately)
    - [ ] GenApp workspace downloaded and accessible (if using sample code)
    - [ ] COBOL expert or Z team member confirmed on the day

=== "IBM i"

    - [ ] IBM i LPAR access provisioned for each attendee (or shared LPAR with `CPYLIB` per user)
    - [ ] Premium Package for i (PPi) activated
    - [ ] VS Code IBM i extension installed and connected
    - [ ] Flight400 (or SAMCO) sample application restored on the LPAR
    - [ ] IBM i developer or SME confirmed on the day

=== "Java Modernization"

    - [ ] Java 21 JDK installed (if needed for target state labs)
    - [ ] Sample application repo cloned and builds successfully on attendee machines
    - [ ] IBM Application Modernization Accelerator access confirmed

=== "SDLC / General"

    - [ ] VS Code installed
    - [ ] Git installed and configured
    - [ ] Sample application repo accessible
    - [ ] Any MCP server dependencies installed (Docker, Node, etc.) if using MCP labs

---

## ✅ Room Logistics

- [ ] Room reserved at **>1.5x capacity vs. headcount** (e.g., 10 attendees → book room for 15+)
- [ ] Classroom-style setup — rows or clusters, **not** a single conference table
- [ ] Collaboration space available — side area for pairs or 1:1 instructor help without disrupting the room
- [ ] Projector / screen confirmed and tested
- [ ] Power strips / extension cords available (laptops need power for a full day)
- [ ] Wi-Fi tested and capacity confirmed for all attendees plus IBM CE team
- [ ] Whiteboard or flip chart available for debrief

---

## ✅ Content & Use Cases

- [ ] Target use case(s) identified and agreed with client
- [ ] Tech stack documented (current state + target state)
- [ ] Labs selected and lab guide finalized (see [Lab Menu](../labs/index.md))
- [ ] Each use case has a named CE lead who has **completed the entire lab**
- [ ] If running parallel use case tracks: breakout rooms confirmed, 1 CE per track
- [ ] If using IBM-provided code: code reviewed and confirmed to meet client expectations
- [ ] If using client code: all users have access, security restrictions are met
- [ ] TechZone environment reserved **7+ days** before event with required permissions and add-ons
- [ ] Lab guide has starting snapshots **and** final endpoint snapshots (for "baking show" fallback)
- [ ] Backup plan documented: if Bob has issues, CE can demo the expected output ("baking show")

---

## ✅ Badging (Optional but Recommended)

- [ ] Event created in the [badge admin portal](https://bob-badge-portal.ce.techzone.ibm.com/) with correct slug, dates, badges, and your email as owner
- [ ] Event API key and slug copied from post-creation screen
- [ ] IBM Bob Badge Issuer extension installed in Bob
- [ ] Badge mode installed in lab repo (`.bob/` committed and pushed)
- [ ] Participants informed: need a Credly account, know which email to use
- [ ] Participant instructions added to event communications

See [Badging Setup](badging.md) for the full step-by-step guide.

---

## ✅ Day-of Kit

Prepare this and bring it on the day:

- [ ] Printed (or digital) lab guides per attendee
- [ ] CE team contact list (names, phone numbers for day-of issues)
- [ ] Backup USB drives with offline installers (Bob, VS Code, Java 21) for install failures
- [ ] Feedback / survey form prepared and tested (link or QR code)
- [ ] Recording consent confirmed if session is to be recorded
- [ ] Post-event survey ready (business value tracking — see [Follow-Up](../followup/index.md))

---

## ✅ Pre-Event Meeting with Client Lead

Schedule a 30-min meeting with the client's nominated lead **1–3 days before** the event:

- [ ] Verify all prerequisites are in place
- [ ] Confirm headcount and any last-minute attendee changes
- [ ] Confirm room setup and logistics
- [ ] Walk through the agenda together
- [ ] Identify any attendees who haven't completed install verification
- [ ] Agree on communication channel for day-of issues (Slack, Teams, etc.)

!!! quote "Lessons Learned"
    *"Meet with a client lead before the Bobathon to verify all pre-reqs are in place — their job is to ensure all attendees match the system requirements before the day."*
