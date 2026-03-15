# Skill: Wallet Management

## What This Is
Tracking and monitoring all of Jesse's financial accounts, API credits, and balances.

## Monitored Accounts
| Account | Type | Alert Threshold | Auto-Reload |
|---|---|---|---|
| Anthropic API | API Credits | $15 warning / $5 critical | Yes — $55 at $5 |
| (more to add) | | | |

## Credit Monitor (Active)
- `workspace-main/dashboard/budget.json` — current Anthropic balance
- `workspace-main/memory/credit-monitor-log.json` — check history
- Cron 1: Daily 9am + 5pm PT — standard check
- Cron 2: Every 3 hours — low-balance watch

## When to Update Balance
After every Anthropic refill, update `budget.json` via the Mission Control dashboard (credit widget, top right at localhost:3131).

## Broker Integration (Pending)
- Need to connect to a brokerage API (Alpaca, TD Ameritrade, etc.)
- Will enable real portfolio tracking, alerts, and eventually automated strategies
- Jesse to provide broker credentials when ready
