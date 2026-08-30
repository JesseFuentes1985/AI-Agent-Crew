# Tony Stark Memory

## Standing Instructions

- **Cron Job Audits:** When Jesse asks about costs, charges, or "what's running," always check active cron jobs first. Flag any that are running but not delivering clear value to Jesse. Removed wasteful jobs on 2026-04-18 (Anthropic Credit Monitor — was silently burning ~$1/day in background token usage with no real benefit since auto-reload was already configured).

- **Context Management (2026-04-18):** Memory flush enabled (softThreshold: 80k tokens, preserve 3 recent turns). Context pruning active (keeps 3 recent responses). Daily logs go to `memory/YYYY-MM-DD.md`. Search memory/ + LEARNINGS.md before answering recall questions.
