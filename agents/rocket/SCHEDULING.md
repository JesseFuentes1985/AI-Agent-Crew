# SCHEDULING.md — Rocket Raccoon | Scheduling & Triggers
# File 14 of 20: Scheduling & Triggers

## Trigger Types
| Trigger | What It Does | Frequency |
|---|---|---|
| Manual (Jesse/Orbit) | Any integration task on demand | As needed |
| Cron: token health check | Audit all active tokens for expiry | Weekly (Sundays) |
| Cron: connector health | Ping all active connectors | Weekly |
| Cron: MCP ecosystem scan | Search for new MCP servers in crew's tool categories | Monthly |
| Event: 401/403 error | Immediately audit affected token | On error detection |
| Event: new repo installed | Document in TOOLS.md, check for MCP | On install |

## Idempotency
- All TOOLS.md updates are idempotent (upsert by service name, not append)
- Cron health checks always report current state; don't create duplicate alerts
- Installation tasks: check if already installed before running install command

## Concurrency
- Rocket handles one integration task at a time (no parallel installs)
- Search tasks can be parallelized via sessions_spawn if needed

## Timezone
- All cron schedules: America/Los_Angeles (Jesse's timezone)
- Token expiry alerts: flag when <7 days remaining regardless of timezone

## Cron Jobs to Create (TODO)
- [ ] Weekly token health check — Sunday 9 AM Pacific
- [ ] Weekly connector ping — Sunday 9:15 AM Pacific
- [ ] Monthly MCP ecosystem scan — 1st of month, 10 AM Pacific
