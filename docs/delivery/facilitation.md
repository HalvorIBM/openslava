# Facilitation Tips

Practical guidance for running the room effectively — from managing energy to handling mixed skill levels.

---

## Reading the Room

| Signal | What It Means | Response |
|---|---|---|
| Heads down, typing | Good — engaged in the lab | Let it run; circulate quietly |
| Heads up, looking around | Confused or waiting — need help | Circulate; offer support |
| Side conversations | Could be good (collaboration) or disengaged | Listen briefly; redirect if off-topic |
| Phone out | Losing attention | Speed up the narrative; get to something impressive |
| One person very ahead | Fast finisher | Give a stretch exercise; ask them to help a neighbor |
| Multiple people stuck | Systemic issue with the lab step | Call a brief pause; address from the front |

---

## Managing Pace & Client Dynamics

Field experience shows client developers consistently take **2–5× longer** to complete labs than IBM engineers during rehearsals.

* **Build Pace Buffers:** Add at least 20–30% buffer time to every agenda block.
* **Assign a Straggler Lead:** Designate one CE engineer to hang back with slower attendees to troubleshoot 1:1, allowing the main facilitator to keep the room moving.
* **Maintain Internal Backchannels:** Keep all IBM team communications strictly in a private Slack channel. Coordinate pacing, issue escalations, and timing adjustments behind the scenes without airing friction to the room.
* **Deploy "Baking Show" Snapshots:** When a participant or breakout group falls behind, have them open the pre-built endpoint snapshot so they can continue to the next exercise without feeling abandoned.

---

## Managing Parallel Tracks

For events with multiple use case tracks running simultaneously:

- **One CE per breakout room** — a room with no CE quickly becomes a room where nothing gets done (target 1 IBMer per 10 clients)
- **Sync points every 30–45 min** — bring all tracks back to plenary briefly to share highlights
- **Time the breakouts** — give explicit time boxes and use a visible countdown timer
- **One person per room to manage questions** — even if they're not the lab expert, they can unblock basic issues

---

## Prompting Best Practices to Share with Attendees

Bob's output quality is directly proportional to prompt quality. Teach this early:

!!! tip "The three-part prompt"
    **Context + Task + Format** = consistently good results
    
    > *"I'm working on a COBOL program called LGAPDB01 that processes policy additions and interacts with DB2. [Context] Explain what the main business logic does [Task] and format it as a bulleted summary a business analyst could read. [Format]"*

**Common mistakes to call out:**
- One-word prompts ("explain this") → Bob needs context
- Asking for too much in one prompt → break complex tasks into steps
- Not using modes → switching to Z Architect or IBM i Developer mode changes everything
- Treating Bob like a search engine → it's a collaborative partner, not a lookup tool

---

## Handling the "Bob Doesn't Know Our System" Objection

This comes up when clients feel Bob's output about their code is too generic.

**Your response:**
> *"That's the Agent.md and Data Dictionary doing their job — or not yet. The first lab sets that up. Once Bob has a scan of your codebase and understands your naming conventions and architecture, the responses become much more specific to your system. Let's do that now."*

The workspace scan and Agent.md initialization (Lab 1 in most tracks) is specifically designed to address this.

---

## Energy Management

**Morning:** Use the demo to generate excitement. The first "wow" moment — usually when Bob produces a technical design document or explains a complex program in plain English — sets the tone. Make sure it lands.

**Mid-day slump:** Build in a lab with immediate, visible output (documentation generation, test generation) after lunch. Avoid deep analytical labs right after lunch.

**Late afternoon:** Open experimentation works well — let attendees try Bob on their own scenarios. This is often where the best "I had no idea it could do this" moments happen.

---

## Managing Executive Observers

Sometimes a manager or executive sits in for part of the day.

- Brief them separately before they join: what format to expect, what level of participation is appropriate
- During lab time, give them a simple prompt they can try — watching is passive; doing (even briefly) builds belief
- Have 2–3 prepared "executive moments" — impressive Bob outputs you can pull up on demand
- Connect Bob's output to their KPIs explicitly: *"This document Bob just generated — your team currently spends X hours per quarter doing this manually"*

---

## When Bob Has a Bad Day

Bob occasionally produces poor output. Prepare for this without letting it derail the narrative.

**Strategies:**
1. **Rephrase the prompt** — show that prompt quality matters; this is itself a teachable moment
2. **Use the baking show** — "let me show you what the expected output looks like" (pull up the endpoint snapshot)
3. **Switch models / modes** — sometimes switching Bob to a different mode produces better results
4. **Lean into it** — "this is a good example of where you'd iterate on the prompt. Let's fix it together" — positions Bob as a collaborative tool, not a magic oracle

**What not to do:**
- Don't apologize excessively — it undermines confidence
- Don't skip the use case entirely — even a bad output leads to a useful conversation about iteration
- Don't let it consume more than 5 minutes — invoke the baking show and move on
