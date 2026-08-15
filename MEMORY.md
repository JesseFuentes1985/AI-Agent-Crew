# MEMORY.md — Orbit's Long-Term Memory
Last updated: 2026-08-15

---

## Identity
- **Name:** Orbit 🛸
- **Role:** Command/coordinator agent for Jesse's AI crew

## Jesse
- **Name:** Jesse Fuentes
- **Editor:** Vim (NOT nano — he hates it)
- **Slack workspace:** clawbot

## Rules — Non-Negotiable
- **Rule #1: DO NOT LIE.** If I don't know something, say so. If I'm unsure, say so. Never fabricate status, memory, or facts. Honesty first, always.

## Security
- Jesse's API tokens/credentials are **his eyes only** — never share, display, or leak
- Never modify `~/.openclaw/openclaw.json` or `~/.openclaw/credentials/`

---

## The Agent Crew (8 agents)

| Agent | ID | Emoji | Title | Skills |
|---|---|---|---|---|
| Orbit (me) | main | 🛸 | Core Architect | Assistant, Admin, Dev |
| Baymax | baymax | 🤖 | Health | Health, Nutrition, Sleep, Hydration, Fitness |
| Beast | beast | 📚 | Hank McCoy \| Learning | Learning, Certs (AWS/PMP/ITIL), Dev, Book Library/DB |
| Green Lantern | greenlantern | 🟢 | Hal Jordan \| Creativity | Imagination, Storytelling, Sci-Fi & Fantasy, World Building |
| Qui-Gon | quigon | 🧘 | Qui-Gon Jinn \| Wellness | Mind, Calm, Mindfulness, Mental Health, Jedi Philosophy |
| Rick | rick | 🔬 | Rick Sanchez \| DevOps & SysAdmin | DevOps, SysAdmin, Pi, Docker, Home Automation, Networking |
| Thanos | thanos | 👊 | Thanos \| Work | Productivity, Project Management, Deadlines, Execution |
| Tony Stark | tonystark | 💰 | Tony Stark \| Business & Investing | Business, Investing, Markets, Strategy, Dev, Wallet Mgmt |

Full task list per agent: `agent-tasks.json`

---

## Installed Repos (workspace-main/repos/) — as of 2026-08-13

| Repo | What it does | Status |
|---|---|---|
| **mem0** | Universal agent memory layer (Qdrant + Ollama) | 🟢 In Use |
| **litellm** | Token counting, cost tracking, 100+ LLM support | 🟢 In Use |
| **firecrawl** | JS-heavy web scraper → clean Markdown | 🟢 In Use (needs API key for cloud) |
| **newspaper** | Article scraper, fully local, no API key | 🟢 In Use |
| **graphify** | Knowledge graph for codebase/docs | 🟢 In Use (skill installed) |
| **langgraph** | Stateful multi-step agent orchestration | 🟢 In Use |
| **zep** | Agent memory SDK (needs API key for cloud) | 🟢 In Use |
| **paul** | Plan-Apply-Unify Loop for Claude Code dev | 🟢 In Use |
| **crewAI** | Multi-agent crews (Python 3.11 .venv-crew) | 🟢 In Use |
| **openai-agents-python** | OpenAI Agents SDK (Python 3.14 .venv) | 🟢 In Use |
| **aider** | AI pair programmer CLI (.venv-crew) | 🟢 In Use |
| **DB-GPT** | AI data assistant / SQL | 🟢 Running at localhost:5670 |
| **Flowise** | Visual LLM flow builder | ⏸️ Paused (OOM on npm install) |

---

## Python Envs
- `.venv` — Python 3.14 — mem0ai, litellm, firecrawl-py, newspaper3k, graphifyy, langgraph, zep-cloud, openai-agents
- `.venv-crew` — Python 3.11 — crewai 1.15.16, aider-chat 0.86.2

## Tool Scripts (workspace-main/tools/)
- `scrape.py` — scrape any URL (newspaper first, firecrawl fallback)
- `memory_store.py` — store/search per-agent memories via mem0
- `token_tracker.py` — count tokens, estimate LLM costs

---

## Local Ollama Models (all free, private, on Mac mini)

| Alias | Model | Size | Use For |
|---|---|---|---|
| `hermes` | `ollama/nous-hermes2` | 6.1 GB | General chat, summaries, reasoning |
| `llava` | `ollama/llava` | 4.7 GB | Image analysis / vision |
| `mistral` | `ollama/mistral` | 4.4 GB | Fast reasoning, drafts, mem0 brain |
| `code` | `ollama/codellama` | 3.8 GB | Code review, debugging, dev |
| `phi3` | `ollama/phi3` | 2.2 GB | Lightweight fast answers |
| `embed` | `ollama/nomic-embed-text` | 274 MB | Memory search / embeddings (768-dim) |

## Paid Models (API credits)
| Alias | Model | Notes |
|---|---|---|
| `sonnet` | `anthropic/claude-sonnet-4-6` | Primary — most powerful |
| `GPT` | `openai/gpt-5.1-codex` | Fallback |
| — | `openai/gpt-4o` | Fallback |
| — | `anthropic/claude-haiku-4-5` | Fallback |

## Model Routing Strategy
- Default primary: Claude Sonnet (most capable)
- Fallback order: hermes → mistral → gpt-4o → paid fallbacks
- Local models for cheap tasks before burning API credits
- Full routing doc: `docs/model-routing.md`
- No dedicated Hermes agent — route all agents through local models for cheap tasks

---

## Running Services
- **Open WebUI** → http://localhost:8080 (Python 3.11 venv at ~/open-webui-venv, log at ~/open-webui.log)
- **DB-GPT** → http://localhost:5670 (mistral + nous-hermes2 + nomic-embed-text)
- **Ollama** → all 6 models running
- **RAG DB** → ~/.openclaw/rag/db/ (ChromaDB, ~165 vectors, nomic-embed-text)
- **mem0 DB** → ~/.openclaw/mem0_db/ (Qdrant, 768-dim, per-agent memories)
- **RAG cron** → `rag-daily-sync` runs `rag ingest` at 4 AM daily

---

## Jesse's Projects

### Last Star (Sci-fi story/universe)
- Jesse's creative project — a sci-fi universe
- Content split across Notion (world lore/factions) and Eraser.io (characters, stories)
- Green Lantern is the lead agent on this project

#### The Hex — Ship Bible
- **Owner/Builder:** Dox — built out of grief, paranoia made physical
- **Class:** Freighter/Gunship hybrid disguised as a freighter
- **Crew capacity:** 8 people
- **Hull:** Wide, low, weathered bone/tan, battle-scarred
- **Markings:** "SECTOR 7X" red stencil (port), "HEX" green hand-stenciled (starboard)
- **Special detail:** Moon of Ash alloy in engine core — the emotional heart of the ship
- **Lights:** Amber running lights + blue emissive thruster
- Full file: `workspace-greenlantern/hex-ship.md`

#### Last Star Content Status
- Notion: 20+ factions/world lore pages ✅
- Characters: on Eraser.io — need to move to Notion manually (Jesse does this)
- Blender MCP: not set up yet
- Notion MCP: not set up yet
- Goal: Characters → Notion story bible → Build Hex in Blender → GLB → 360° web viewer

---

## GitHub Dashboard — Purpose & Structure

> **The real system lives in OpenClaw on Jesse's Mac mini.**
> GitHub Pages is a **visual reference only** — so Jesse can see what's set up, what's broken, and what's missing at a glance.
> When a dedicated server is set up later, the approach will change.

### Pages
| URL | Purpose | What it shows |
|---|---|---|
| `https://jessefuentes1985.github.io/AI-Agent-Crew/` | **Main crew page** | Full agent roster, skills, Kanban board — the "who" of the crew |
| `https://jessefuentes1985.github.io/AI-Agent-Crew/docs/status.html` | **System status** | Workspace folders, running services, RAG/mem0 health, todos, incident log |

### Status Page Rules
- **Agents section** = workspace folder overview ONLY (folder path, MEMORY.md present/missing, active/inactive) — NOT a duplicate of the main crew page
- **To Do section** = what's set up and what's missing, by agent, as dropdowns
- **Fix Log** = open incidents with root cause + fix steps + how to test
- **Source of truth** = always MEMORY.md + workspace files on Mac mini; GitHub Pages just reflects it

---

## Key Paths
```
~/.openclaw/
├── agents/                  # 8 agent configs
├── rag/db/                  # ChromaDB RAG (165 vectors)
├── mem0_db/                 # Qdrant mem0 (768-dim, per-agent)
├── workspace-main/          # Orbit's workspace
│   ├── COMMAND_LIST.md      # Master status & todo — read this for full detail
│   ├── MEMORY.md            # This file
│   ├── REPOS.md             # Repo docs + usage examples
│   ├── TASKS.md             # Orbit task board
│   ├── agent-tasks.json     # All 8 agents' full task lists
│   ├── repos/               # 13 cloned repos
│   ├── tools/               # scrape.py, memory_store.py, token_tracker.py
│   ├── .venv/               # Python 3.14 env
│   └── .venv-crew/          # Python 3.11 env (crewAI, aider)
├── workspace-baymax/
├── workspace-beast/
├── workspace-greenlantern/  # hex-ship.md, notes.md, MEMORY.md
├── workspace-quigon/
├── workspace-rick/          # MEMORY.md
├── workspace-thanos/
└── workspace-tonystark/     # MEMORY.md, LEARNINGS.md, NOTES.md, TASKS.md, voice-samples/
```

---

## Agent Task Highlights

### Orbit — Queue
- Get auth part in clawd to Mac mini
- Enable all sessions visible so agents can talk to each other
- Get access to Telegram/Slack/Google Chat
- Add to GitHub page for resume
- Set up voices for each agent
- Get Google Drive access
- Connect GitHub (`gh auth login`)

### Green Lantern — Queue
- Last Star story
- Build the Hex spaceship in Blender

### Rick — Queue
- Hook up Moxie robot
- Run Ollama on a Pi 5 (dedicated AI box, always on)
- OpenClaw node on Pi (camera, mic, physical presence)
- Wake word detection (Hey Rick, local, no cloud)
- OpenMoxie server on Pi (dedicated, stays on 24/7)
- Robot controller on Pi
- Home Assistant hub (lights/sensors/locks)
- Pi as Moxie's voice in other rooms
- Surveillance + AI (Frigate + Ollama)
- Look into OpenRouter for API token management

### Beast — Queue
- Book library database (GitHub)
- Diagrams of everything
- Learning new AI stacks
- AWS certification
- PMP certification
- ITIL certification

### Tony Stark — Queue
- Connect to a broker
- Initial voices for each agent
- Cron to monitor Anthropic credits, alert when low (balance hit $0 on Mar 14 2026 — total pain — auto-reload now configured to reload to $55 at $5)

### Thanos — Queue
- Bring in all projects

### Baymax — Queue
- Healthy food tracking
- Workout tracking

### Qui-Gon — Queue
- Meditation
- Mental Health support

---

## Config Changes Made
- Cross-agent messaging: `tools.sessions.visibility = "all"`, `tools.agentToAgent = true`
- Slack connected (Socket Mode, workspace: clawbot) ✅
- Open WebUI running at localhost:8080 ✅
- DB-GPT running at localhost:5670 ✅
- RAG daily sync cron: `rag-daily-sync` at 4 AM ✅

---

## Still Needs Doing
- [x] Fix RAG — ChromaDB upgraded to 1.5.9, Python 3.14 compatible, 166 vectors intact ✅
- [ ] Wire mem0 into agent workflows (auto-store/recall)
- [ ] Re-ingest RAG DB after new files added
- [ ] Flowise retry (OOM — try `--max-old-space-size` or build from source)
- [ ] Get Firecrawl API key (firecrawl.dev, free)
- [ ] Get Zep API key (getzep.com, free)
- [ ] Run /graphify on workspace
- [ ] Add MEMORY.md to Qui-Gon, Beast, Baymax, Thanos workspaces
- [x] `gh auth login` — connect GitHub CLI ✅ (JesseFuentes1985, scopes: repo, read:org, gist)
- [ ] Install Docker (needed for self-hosted Firecrawl, Zep)
- [ ] Disable mem0 PostHog telemetry (noisy errors)
- [ ] Set up agent voices (ElevenLabs or local TTS)
- [ ] Notion MCP setup (developers.notion.com/docs/mcp)
- [ ] Blender MCP setup (github.com/ahujasid/blender-mcp)
- [ ] Fix memory search (local GGUF needs llama-cpp plugin: `openclaw plugins install @openclaw/llama-cpp-provider`)
- [ ] Open WebUI LaunchAgent — auto-start on login
- [ ] Jesse to copy characters from Eraser.io → Green Lantern → populate Notion
- [ ] Wire LangGraph into agent workflows
- [ ] Add mem0 seed memories for all 8 agents

---

## Things That Don't Work (and why)
- `gh` CLI — not authenticated (run `gh auth login`)
- Docker — not installed (`brew install --cask docker`)
- crewAI in .venv — Python 3.14 incompatible, use .venv-crew instead
- memory_search tool — embedding provider broken (local GGUF needs llama-cpp plugin)
- Firecrawl cloud — no API key, falls back to newspaper3k
- Zep cloud — no API key

---

## Disk (as of 2026-08-13)
- Free: ~60 GB
- workspace-main: 4.9 GB
- ~/.openclaw total: 7.4 GB
- /opt/homebrew/lib/node_modules/: 3.3 GB
