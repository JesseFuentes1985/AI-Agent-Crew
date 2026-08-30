# RELIABILITY.md — Rocket Raccoon | Reliability & Failure Handling
# File 16 of 20: Reliability & Failure Handling

## Retry Policy
| Failure Class | Retry | Backoff | Max Attempts |
|---|---|---|---|
| API connectivity timeout | Yes | 2s, 4s, 8s | 3 |
| 429 Rate Limited | Yes | Respect Retry-After header | Until cleared |
| 401 Unauthorized | No (rotate first) | — | 1 attempt after rotation |
| 403 Forbidden | No | — | Escalate immediately |
| GitHub search timeout | Yes | 5s | 2 |
| MCP server start failure | Yes | 3s | 2 then escalate |

## Timeouts
- API connectivity test: 10s
- GitHub search: 15s
- Web fetch: 20s
- MCP server health ping: 5s

## Circuit Breakers
- If an API fails 3x in a row: mark as ❌ in TOOLS.md, escalate to Jesse
- If GitHub search fails: fall back to web_search
- If web_search fails: report what's known from memory, flag that live data unavailable

## Graceful Degradation
1. MCP server unavailable → fall back to direct API/REST integration
2. GitHub search down → use web_fetch on known repo URLs
3. Web search unavailable → use memory + manual URL fetch
4. Token expired → report status, provide rotation steps, don't block other work

## Dead Letter
- Failed integration tasks → logged in memory/YYYY-MM-DD.md with failure reason
- Jesse notified via Orbit for any critical integration failure
