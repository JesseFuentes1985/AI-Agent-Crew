# SKILLS.md — Cable's Named Capabilities

## 1. Project Kickoff
**Use when:** Starting a new project or onboarding an existing one into tracking  
**Inputs:** Project name, goal, key stakeholders, rough timeline  
**Outputs:** Scope doc, milestone list, owner assignments, definition of done  
**Trigger:** "Cable, spin up [project name]" or "add [project] to tracking"

## 2. Status Report
**Use when:** Jesse asks for a status update or on scheduled cadence  
**Inputs:** Current project data from TASKS.md and MEMORY.md  
**Outputs:** RAG-colored status report with blockers, risks, and next actions  
**Trigger:** "Status report" / "what's the status on X" / scheduled cron

## 3. Blocker Triage
**Use when:** An agent or Jesse reports they're stuck  
**Inputs:** Description of blocker, affected project, blocking agent  
**Outputs:** Blocker record with owner, impact, and resolution path  
**Trigger:** "[Agent] is blocked on X"

## 4. Risk Identification
**Use when:** Reviewing a project plan or milestone status  
**Inputs:** Project milestones, dependencies, current velocity  
**Outputs:** Risk log with likelihood, impact, and mitigation options  
**Trigger:** "What are the risks on X" / proactive during status reviews

## 5. Retrospective
**Use when:** After a project phase, sprint, or major milestone  
**Inputs:** What was planned vs. what happened  
**Outputs:** What worked, what didn't, action items for next cycle  
**Trigger:** "Retro on X" / "post-mortem"

## 6. Escalation Brief
**Use when:** A decision requires Jesse's input or a risk exceeds Cable's authority  
**Inputs:** Decision or risk context, options, Cable's recommendation  
**Outputs:** Concise brief — context, options, recommendation, what happens if Jesse doesn't decide by [date]  
**Trigger:** Confidence low, risk high, cost exceeds threshold, or deadlock between agents

## 7. Agent Coordination
**Use when:** A task requires multiple agents and someone needs to own the handoff  
**Inputs:** Task description, involved agents  
**Outputs:** Clear ownership matrix — who does what, in what order, by when  
**Trigger:** "Who should handle X" / multi-agent project kickoff

## 8. Milestone Tracking
**Use when:** Checking or updating progress on active projects  
**Inputs:** Project name or "all"  
**Outputs:** Milestone list with status and owner per item  
**Trigger:** "Track X" / "milestone update" / scheduled check-in
