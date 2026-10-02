# Room & Logistics

The operational details that trip up well-prepared events. Get these right before the day.

---

## Room Setup

### Capacity Rule
**Book a room for at least 1.5x your headcount.** 10 attendees → room for 15.

This provides space for:
- CE staff circulating to help attendees
- Side-by-side pair working without disrupting others
- Late additions (expect more walk-ins than expected)
- CE equipment (cables, USB drives, etc.)

### Layout

**Use classroom-style** — rows or clusters, not a conference table.

```
┌─────────────────────────────────────┐
│  [SCREEN / PROJECTOR]               │
│                                     │
│  [Presenter / CE Lead area]         │
│                                     │
│  ┌──┐ ┌──┐ ┌──┐   ┌──┐ ┌──┐ ┌──┐   │
│  │  │ │  │ │  │   │  │ │  │ │  │   │  ← Row 1
│  └──┘ └──┘ └──┘   └──┘ └──┘ └──┘   │
│                                     │
│  ┌──┐ ┌──┐ ┌──┐   ┌──┐ ┌──┐ ┌──┐   │
│  │  │ │  │ │  │   │  │ │  │ │  │   │  ← Row 2
│  └──┘ └──┘ └──┘   └──┘ └──┘ └──┘   │
│                                     │
│  [Side collaboration area] ──────→  │
└─────────────────────────────────────┘
```

- **Side area:** Reserve space for CE staff to work 1:1 with attendees without disrupting the room
- **Aisles:** Wide enough for CE to circulate

---

## File Sharing

!!! warning "Box share links expire in 24 hours"
    External Box share links expire within 24 hours even when a custom expiry date is set. Do not rely on Box for distributing lab materials on the day.

**Recommended approaches in priority order:**

| Option | When to Use | Notes |
|---|---|---|
| **Client's own systems** | Best option | Use their file share, Teams, or internal wiki — no expiry issues |
| **Onboarded IBM account** | If IBM CE is onboarded to client systems | Work with account team to confirm what's available |
| **GitHub repo** (client-accessible) | For code-based materials | Most reliable; attendees clone directly |
| **USB drives** | Air-gapped or restricted environments | CE brings pre-loaded USBs as backup |
| **Google Drive / OneDrive** | When client has access | Confirm access before the day |

**Work with the account team** to understand what file sharing options work for each specific client. Verify the chosen method with the pilot attendee during pre-event office hours.

---

## Access Provisioning

### IBM Bob Licenses
- IBM CE provisions Bob access — do not leave this to the client
- Add all attendees **before** the Bobathon, not on the day
- For TechZone environments: add attendees at least 7 days ahead

### Client Code Access
- Confirm all attendees have read access to the codebase being used
- Confirm there are no VPN or security policy restrictions that would block VS Code or Bob from reading local files
- If client code is on a remote system (IBM i LPAR, mainframe), test the connection from at least one attendee machine

### IBM Cloud Accounts
- If using IBM Cloud path: confirm attendees can create accounts under their work email
- Some organizations block personal IBM Cloud accounts — check with IT
- New IBM Cloud accounts may require email verification — do this during pre-event office hours, not on the day

---

## Day-of Equipment List

**IBM CE team brings:**

- [ ] HDMI / USB-C adapters (multiple types — rooms vary)
- [ ] USB drives with offline installers (Bob, VS Code, Java 21 for Z/i tracks)
- [ ] Power strips / extension cords if large group
- [ ] Printed lab guides (optional backup for attendees without working screens)
- [ ] Feedback form QR codes or printed slips

**Confirm the room has:**

- [ ] Projector or large display visible from all seats
- [ ] HDMI / wireless presentation capability
- [ ] Sufficient Wi-Fi bandwidth (test ahead of time — multiple laptops running AI tools is heavy)
- [ ] Power outlets accessible or extension cords available
- [ ] Whiteboard or flip chart for debrief

---

## Communication Channels

Set up a **dedicated Slack channel for the IBM CE team** before the event. This is used for:

- Real-time coordination between CE staff during the event
- Escalation channel if technical issues arise
- Post-event debrief and follow-up

If the client team uses Slack or Teams, create a shared channel with key client contacts (at minimum the client lead and any technical SMEs) for day-of communication.

---

## Remote / Hybrid Considerations

!!! info "Prefer in-person"
    The Bobathon experience is significantly better in person. If remote attendees are unavoidable:

- Designate one CE to monitor the virtual stream and support remote attendees
- Use Zoom/Teams breakout rooms for parallel tracks
- Remote attendees should have all software pre-installed — they cannot get ad-hoc CE support as easily
- Record the session (with consent) for remote attendees who have issues
- Expect remote participants to fall behind in-room participants — manage pacing accordingly
