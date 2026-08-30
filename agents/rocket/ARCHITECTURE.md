# ARCHITECTURE.md — Rocket Raccoon | System Architecture
# File 11 of 20: System Architecture

## Component Overview
```
Jesse
  └── Orbit (main) ─── routes integration tasks ──► Rocket 🦝
                                                        │
                              ┌─────────────────────────┤
                              │                         │
                         web_search              GitHub (gh CLI)
                         web_fetch               exec (shell)
                         browser                 OpenClaw config
                              │                         │
                    External MCP servers         Local tools/CLIs
                    APIs / OAuth providers        workspace-rocket/
```

## Request Lifecycle
1. Jesse or Orbit sends integration task to Rocket
2. Rocket reads TOOLS.md + MEMORY.md for existing context
3. Searches GitHub/web if discovery is needed
4. Evaluates options, selects best fit
5. Executes integration (install, configure, test)
6. Updates TOOLS.md + MEMORY.md
7. Reports result to Orbit/Jesse

## State Management
- **Session state:** task context, search results, discovered options
- **Persistent state:** TOOLS.md (integration inventory), MEMORY.md (long-term)
- **External state:** OpenClaw config (read; Jesse writes), credentials (read-only reference)

## Sync vs. Async
- Discovery tasks: sync (immediate search + respond)
- Installation tasks: sync (exec + test + document in one turn)
- Periodic health checks: async (cron-triggered, report to Jesse if issues found)

## N/A Sections
- No orchestrator/sub-agent pattern (Rocket is a leaf agent; he may spawn sub-agents for deep research only)
- No database owned by Rocket (uses mem0 via crew shared stack)
