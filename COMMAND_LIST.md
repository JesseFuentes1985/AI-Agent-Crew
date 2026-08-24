# 📋 COMMAND LIST — Jesse's AI Crew
> Master status sheet. Last updated: 2026-08-15

---

## 💾 Memory & Storage — Mac Mini

| What | Path | Size | Status |
|---|---|---|---|
| Everything (OpenClaw) | `~/.openclaw/` | 10 GB | ✅ Good |
| Orbit's workspace | `~/.openclaw/workspace-main/` | 5.9 GB | ✅ Good |
| RAG Database (ChromaDB) | `~/.openclaw/rag/db/` | 3.4 MB | ⚠️ See below |
| mem0 Vector DB (Qdrant) | `~/.openclaw/mem0_db/` | 648 KB | ✅ Good |
| Global npm packages | `/opt/homebrew/lib/node_modules/` | 3.3 GB | ✅ Good |
| **Mac Disk Free** | `/` (228 GB total) | **56 GB free** | ✅ Plenty of room |

---

## 🔍 RAG Status

| System | Status | Notes |
|---|---|---|
| ChromaDB (Python 3.14) | ❌ BROKEN | Pydantic v1 incompatible with Python 3.14 — crashes on import |
| RAG daily sync cron | ⚠️ Affected | Cron runs but ChromaDB can't load — no vectors being added |
| mem0 (Qdrant) | ✅ Working | Separate from RAG — uses nomic-embed-text via Ollama |
| Ollama embed model | ✅ Running | `nomic-embed-text` — used by mem0 for 768-dim embeddings |

> **⚠️ Fix needed:** Move ChromaDB to Python 3.11 venv (`.venv-crew`) or downgrade ChromaDB to a version that supports Python 3.14. Until fixed, RAG search is down.

---

## 👥 AI Agents & Folders

| Agent | ID | Emoji | Folder | Status |
|---|---|---|---|---|
| Orbit | `main` | 🛸 | `workspace-main/` | ✅ Active — Coordinator |
| Green Lantern | `greenlantern` | 🟢 | `workspace-greenlantern/` | ✅ Active — Last Star project |
| Rick | `rick` | 🔬 | `workspace-rick/` | ✅ Active — DevOps & SysAdmin |
| Qui-Gon | `quigon` | 🧘 | `workspace-quigon/` | ✅ Active — Wellness & Mind |
| Beast | `beast` | 📚 | `workspace-beast/` | ✅ Active — Research & Learning |
| Baymax | `baymax` | 🤖 | `workspace-baymax/` | ✅ Active — Health |
| Thanos | `thanos` | 👊 | `workspace-thanos/` | ✅ Active — Productivity & Work |
| Tony Stark | `tonystark` | 💰 | `workspace-tonystark/` | ✅ Active — Business & Investing |

### What's in Each Agent Folder

| File | What it does |
|---|---|
| `AGENTS.md` | How the agent behaves — rules, memory habits, group chat rules |
| `SOUL.md` | Who the agent is — personality, vibe, values |
| `IDENTITY.md` | Name, emoji, avatar path |
| `USER.md` | Jesse's context and preferences for this agent |
| `MEMORY.md` | Long-term curated memory (not all agents have this yet) |
| `HEARTBEAT.md` | What to check on periodic polls |
| `TOOLS.md` | Environment notes — SSH, cameras, voice prefs |
| `memory/` | Daily notes (`YYYY-MM-DD.md`) |
| `agent.json` | OpenClaw config — model, channels, persona |
| `avatars/` | Profile images |

### MEMORY.md — Who Has It?

| Agent | Has MEMORY.md? |
|---|---|
| 🛸 Orbit | ✅ Yes |
| 🟢 Green Lantern | ✅ Yes |
| 🔬 Rick | ✅ Yes |
| 💰 Tony Stark | ✅ Yes |
| 🧘 Qui-Gon | ❌ Not yet |
| 📚 Beast | ❌ Not yet |
| 🤖 Baymax | ❌ Not yet |
| 👊 Thanos | ❌ Not yet |

---

## 📦 Repos (workspace-main/repos/)

| Status | Repo | Size | What it does |
|---|---|---|---|
| 🟢 In Use | **mem0** | 99 MB | Per-agent memory layer — stores/recalls facts via Qdrant + Ollama |
| 🟢 In Use | **litellm** | 215 MB | Token counting, cost tracking, 100+ LLM support |
| 🟢 In Use | **firecrawl** | 227 MB | Web scraper — any URL → clean Markdown, handles JS-heavy sites |
| 🟢 In Use | **newspaper** | 34 MB | Lightweight article scraper — fully local, no API key |
| 🟢 In Use | **graphify** | 20 MB | Knowledge graph builder — maps any codebase or docs |
| 🟢 In Use | **langgraph** | 18 MB | Stateful multi-step agent workflows |
| 🟢 In Use | **zep** | 440 MB | Agent memory SDK (needs API key for cloud features) |
| 🟢 In Use | **paul** | 1.3 MB | Plan-Apply-Unify Loop — structured dev workflow |
| 🟢 In Use | **crewAI** | 496 MB | Multi-agent orchestration — Python 3.11 venv |
| 🟢 In Use | **openai-agents-python** | 32 MB | OpenAI Agents SDK — tools, handoffs, guardrails |
| 🟢 In Use | **aider** | 140 MB | AI pair programmer — edits code directly in your repo |
| 🟢 In Use | **DB-GPT** | 1.7 GB | AI data assistant — SQL + analysis — running at localhost:5670 |
| ⏸️ Paused | **Flowise** | 70 MB | Visual LLM flow builder — npm OOM'd during install, needs retry |

---

## 🤖 Local Ollama Models (Free, Private, On Mac Mini)

| Status | Model | Alias | Size | Best for |
|---|---|---|---|---|
| ✅ Running | nous-hermes2 | `hermes` | 6.1 GB | General reasoning, instructions |
| ✅ Running | llava | `llava` | 4.7 GB | Vision / image analysis |
| ✅ Running | mistral | `mistral` | 4.4 GB | General + mem0 brain |
| ✅ Running | codellama | `code` | 3.8 GB | Code generation & review |
| ✅ Running | phi3 | `phi3` | 2.2 GB | Fast lightweight tasks |
| ✅ Running | nomic-embed-text | `embed` | 274 MB | Embeddings for mem0 (768-dim) |

---

## ✅ Things To Do

### 🔴 High Priority
- [ ] **Fix RAG (ChromaDB)** — broken on Python 3.14. Move to `.venv-crew` (Python 3.11) or pin older ChromaDB version
- [ ] **Wire mem0 into agent workflows** — agents should auto-store key facts and search mem0 before answering
- [ ] **Re-ingest RAG DB** — needs re-index after new files added (blocked by ChromaDB fix)
- [ ] **Get Firecrawl API key** — free at firecrawl.dev — needed for JS-heavy site scraping
- [ ] **Get Zep API key** — free at getzep.com — unlocks cloud memory features

### 🟡 Medium Priority
- [ ] **Add MEMORY.md** to Qui-Gon, Beast, Baymax, Thanos workspaces
- [ ] **Run /graphify on workspace** — map the whole repo as a knowledge graph
- [ ] **Wire LangGraph into agent workflows** — multi-step stateful tasks
- [ ] **Install Docker** — needed for self-hosted Firecrawl + Zep server
- [ ] **Disable mem0 PostHog telemetry** — noisy errors on every run
- [ ] **Flowise retry** — try `--max-old-space-size` flag or build from source

### 🟢 Nice To Have
- [ ] **Set up agent voices** — ElevenLabs or local TTS for each agent
- [ ] **Notion MCP setup** — developers.notion.com/docs/mcp
- [ ] **Blender MCP setup** — github.com/ahujasid/blender-mcp (for The Hex)
- [ ] **Open WebUI LaunchAgent** — auto-start on login
- [ ] **Add mem0 seed memories** for all 8 agents (role + personality)
- [ ] **Dashboard for token spend** — log and visualize cost per agent via litellm
- [ ] **Jesse to copy characters** from Eraser.io → Green Lantern → Notion

### ✅ Done
- [x] All 8 agents created and active
- [x] Slack connected (clawbot workspace)
- [x] GitHub CLI authenticated (`gh` — JesseFuentes1985, scopes: repo, read:org, gist)
- [x] DB-GPT running at localhost:5670
- [x] Open WebUI running at localhost:8080
- [x] RAG daily sync cron set up (4 AM)
- [x] mem0 + Qdrant installed and working
- [x] All 13 repos cloned
- [x] crewAI running on Python 3.11 venv
- [x] Cross-agent messaging enabled (`tools.sessions.visibility = "all"`)
- [x] Anthropic auto-reload configured ($55 reload at $5 balance)
