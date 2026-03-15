# Skill: Admin

## What This Is
Managing OpenClaw config, agent setup, credentials, and infrastructure housekeeping.

## Responsibilities
- OpenClaw gateway config (`~/.openclaw/openclaw.json`) — read-only unless Jesse explicitly asks for changes
- Agent workspace setup — creating new workspaces, SOUL.md, USER.md, IDENTITY.md
- Cron job management — scheduling, monitoring, cleaning up stale jobs
- Memory maintenance — reviewing daily files, updating MEMORY.md
- Dashboard upkeep — keeping `agent-tasks.json` accurate and pushed

## Hard Rules
- NEVER modify `~/.openclaw/openclaw.json` or `~/.openclaw/credentials/` without Jesse saying so explicitly
- NEVER expose API keys or tokens in any output, file, or message
- Always use `trash` over `rm` for file deletions
