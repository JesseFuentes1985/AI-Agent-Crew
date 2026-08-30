# EVALUATION.md — Rocket Raccoon | Evaluation, Testing & Observability
# File 17 of 20: Evaluation, Testing & Observability

## Eval Set (pass criteria)
| Test | Input | Expected Output | Pass Condition |
|---|---|---|---|
| MCP discovery | "Does Slack have an MCP?" | Repo link + stars + install command | Link is real, repo exists |
| Token check | "Is GitHub auth working?" | ✅ or ❌ with reason | Matches actual `gh auth status` |
| Repo discovery | "Find a web scraper for Python" | Table with ≥3 repos, stars, license | All repos verified on GitHub |
| Bad token response | Simulate 401 from API | Flag + rotation steps | No false "it's working" |
| Escalation trigger | OAuth needs browser | Exact steps for Jesse | Jesse can follow without Rocket |

## Regression Suite
- Run after any prompt/workflow change
- Test: MCP discovery for 3 known services (Notion, Slack, GitHub)
- Test: token health check (dry run against known-good credentials)
- Test: repo discovery for 2 capabilities

## Observability
- Integration status: TOOLS.md (last updated timestamp)
- Failed tasks: memory/YYYY-MM-DD.md
- Token expiry tracking: MEMORY.md (Active Integrations table)
- Tool errors: exec output logged in daily notes

## Drift Detection
- If TOOLS.md hasn't been updated in >14 days: flag for review
- If a known integration stops responding: flag in next health check
- Monthly: compare installed repos vs. TOOLS.md — anything installed but undocumented?

## N/A
- No cost/latency dashboards (Rocket uses local models primarily; cloud model use is logged in session costs via OpenClaw)
