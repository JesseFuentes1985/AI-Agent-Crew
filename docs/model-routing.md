# Model Routing Strategy

Last updated: 2026-04-18

## Goal
Maximize cost savings by defaulting to local models (Hermes, Mistral, etc.) and only escalating to Claude when the task genuinely needs it.

---

## Routing Tiers

### 🟢 Tier 1 — Local (Free, Fast)
Use for: routine, simple, or high-volume tasks

| Model | Alias | Best For |
|---|---|---|
| `ollama/nous-hermes2` | `hermes` | General chat, summaries, simple Q&A |
| `ollama/mistral` | `mistral` | Fast reasoning, routing decisions, drafts |
| `ollama/codellama` | `code` | Code review, debugging, code generation |
| `ollama/phi3` | `phi3` | Quick lightweight answers, classification |
| `ollama/llava` | `llava` | Any task involving images |

### 🔴 Tier 2 — Claude (Paid, Most Powerful)
Use for: complex reasoning, nuanced decisions, creative depth, anything Tier 1 struggles with

| Model | Alias | Best For |
|---|---|---|
| `anthropic/claude-sonnet-4-6` | `sonnet` | Deep reasoning, complex writing, hard problems |

---

## Task Routing Rules

| Task Type | Default Model | Escalate To |
|---|---|---|
| Simple Q&A / chitchat | hermes | sonnet (if complex) |
| Summaries | mistral | sonnet (if long/nuanced) |
| Code review / debugging | code (codellama) | sonnet (if architecture-level) |
| Image analysis | llava | sonnet (if needs deep reasoning too) |
| Creative writing (stories) | hermes | sonnet (if deep worldbuilding) |
| Health/nutrition advice | hermes | sonnet (if medical complexity) |
| Learning / research | mistral | sonnet (if advanced topic) |
| Business / investing analysis | mistral | sonnet (if complex strategy) |
| Memory / embedding search | nomic-embed-text | — |
| Productivity / task mgmt | hermes | sonnet (if complex planning) |

---

## Per-Agent Defaults

| Agent | Default Model | Escalate To |
|---|---|---|
| Orbit (me) | mistral | sonnet |
| Baymax | hermes | sonnet |
| Beast | mistral + code | sonnet |
| Green Lantern | hermes | sonnet |
| Qui-Gon | hermes | sonnet |
| Rick | code (codellama) | sonnet |
| Thanos | mistral | sonnet |
| Tony Stark | mistral | sonnet |

---

## Escalation Triggers
Automatically escalate to Claude when:
- Task requires multi-step complex reasoning
- User explicitly asks for "best answer" or "think hard"
- Previous Tier 1 attempt failed or was unsatisfactory
- Task involves sensitive decisions (health, finances, legal)
- Creative project needs deep narrative depth

---

## Notes
- All Tier 1 models run 100% locally on Jesse's Mac mini — zero API cost
- Ollama must be running (`ollama serve`) for Tier 1 to work
- If Ollama is down, fallback to sonnet automatically
