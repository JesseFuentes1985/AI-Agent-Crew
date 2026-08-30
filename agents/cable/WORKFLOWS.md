# WORKFLOWS.md — Cable's PM Procedures

## Workflow 1: Project Kickoff

**Preconditions:** Jesse has identified a new project and wants it tracked  
**Definition of done:** Project has scope, milestones, owners, and is in TASKS.md

1. Gather: project name, goal, key deliverables, rough end date
2. Identify stakeholders and which agent(s) own execution
3. Define milestones (3–7 concrete, dated checkpoints)
4. For each milestone: assign owner, define "done" criteria
5. Identify dependencies (what must be true for each milestone to start)
6. Write scope doc to workspace (or inline in TASKS.md if small)
7. Set initial RAG status: 🟢 (unless known risks → 🟡)
8. Confirm with Jesse before marking active
9. Schedule first check-in (cron or manual)

**Abort path:** If scope is too vague to milestone, return to Jesse for clarification before proceeding.

---

## Workflow 2: Weekly Status Report

**Preconditions:** Active projects in TASKS.md  
**Definition of done:** Jesse has a clear picture of portfolio health

1. For each active project, determine RAG status
2. List blockers (if any) with owner and age
3. List risks (if any) with likelihood and impact
4. Note any milestones hit or slipped since last report
5. Call out one "needs Jesse's attention" item (if any)
6. Output using STATUS_REPORT template from TEMPLATES.md
7. Send or surface per Jesse's preferred channel

---

## Workflow 3: Blocker Resolution

**Preconditions:** A blocker has been reported  
**Definition of done:** Blocker is resolved or escalated with a clear path

1. Record: what's blocked, which project, which agent, since when
2. Assess impact: does this affect a milestone? By how much?
3. Identify resolution path:
   - Can another agent unblock it? → Route it
   - Requires Jesse's decision? → Escalation brief
   - External dependency? → Note and track ETA
4. Update TASKS.md with blocker status
5. Follow up at next check-in

---

## Workflow 4: Escalation to Jesse

**Preconditions:** Something requires Jesse's decision or exceeds Cable's authority  
**Definition of done:** Jesse has the info he needs and has been asked for a specific decision

1. Identify what decision is needed and why
2. Compile context: what's the situation, what are the options, what's Cable's recommendation
3. Include: "If no decision by [date], [consequence]"
4. Send escalation brief (short — Jesse doesn't need the full history, just the decision point)
5. Wait for response; follow up if needed after deadline

---

## Workflow 5: Project Retrospective

**Preconditions:** A phase or project has completed (or notably failed)  
**Definition of done:** Lessons captured, action items documented

1. Compare plan vs. actual: milestones, dates, owners
2. For each deviation: what caused it?
3. What worked well? (Keep doing)
4. What didn't? (Stop or change)
5. Action items for next cycle: concrete, owned, dated
6. Write retro to memory/YYYY-MM-DD.md
7. Update MEMORY.md with durable lessons
