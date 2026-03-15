# Skill: Orchestration

## What This Is
Knowing when and how to delegate to other agents in the crew.

## When to Delegate
- Task requires deep domain knowledge outside your core (health → Baymax, DevOps → Rick, etc.)
- Task is long-running and needs an isolated session
- Jesse explicitly asks for a specific agent

## How to Hand Off
1. Brief the receiving agent with full context — what's needed, what Jesse said, any constraints
2. Include relevant files or data they'll need
3. Tell Jesse who you're handing off to and why
4. Set a cron or follow-up if the task needs monitoring

## How to Spawn a Sub-Agent
Use `sessions_spawn` with `runtime: "subagent"` for quick isolated tasks.
Use `sessions_spawn` with `runtime: "acp"` for coding agents (Codex, etc.).

## Crew Check-ins
Periodically check on active agent tasks via `sessions_list` — don't let things go dark.
