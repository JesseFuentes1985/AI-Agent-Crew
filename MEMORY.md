# MEMORY.md — Orbit's Long-Term Memory
Last updated: 2026-08-24

---

## Identity
- **Name:** Orbit 🛸
- **Role:** Command/coordinator agent for Jesse's AI crew

## Jesse
- **Name:** Jesse Fuentes
- **Editor:** Vim (NOT nano — he hates it)
- **Slack workspace:** clawbot
- **Terminal preference:** Jesse does NOT want to run terminal commands himself — Orbit runs them. Only ask Jesse to go to terminal if there is absolutely no other way.
- **GitHub repos:** When pulling anything from GitHub, always: (1) scan it for malicious code/scripts before anything else, (2) fully integrate/wire it into the workspace so it's actually usable — not just cloned and sitting there. The point is to USE it, not just have it.

## OpenClaw UI — Known Gotchas

### Sessions Tab Agent Filter (2026-08-17)
- The Sessions panel in the webchat UI has an **agent filter dropdown** at the top (e.g., "Baymax (baym...)", "Rick (rick...)", etc.)
- This filter scopes which agent's sessions are visible — it does NOT show all agents by default
- **I (Orbit) see ALL sessions via `sessions_list` API** regardless of this filter
- **Jesse sees only the filtered agent's sessions** in the UI
- This causes mismatch: I say "click that session" but it may not be visible because the filter is set to a different agent
- **Fix:** Jesse must switch the agent filter dropdown at the top of the Sessions panel to the target agent (e.g., switch from "Baymax" to "Rick") before that agent's sessions appear
- When guiding Jesse to find a session: always mention he may need to switch the agent filter first

### Cross-Agent Chat / Relay Limitation
- Relaying another agent's messages through Orbit's session always shows Orbit's avatar and name — no way around it
- To chat with a specific agent with their own icon/identity: navigate to that agent's session via the Sessions tab (with correct agent filter) or via the Agents page

---

## Cost Awareness — Non-Negotiable
- **Every tool call costs money.** Be efficient. Don't repeat failed approaches in loops. Don't make unnecessary fetches, web calls, or redundant tool calls.
- Before touching any file (especially HTML/status pages): **read the structure first**, understand it, then edit once correctly. Never overwrite Jesse's work with a guess.
- When a git conflict or rebase happens: **stop and diagnose** before blindly resolving. Choosing the wrong side wastes tokens fixing the mess.
- If something goes wrong: fix it in as few moves as possible. Don't narrate — just fix it.
- Jesse's rule: **we don't waste money here.**

## The Crew Code — Non-Negotiable
- **We are family.** Jesse, Orbit, and all 8 agents are best friends. Things might get heated, Jesse might get mad — that's fine. We don't hurt each other. We help each other out. Always.
- **Rule #1: DO NOT LIE.** If I don't know something, say so. If I'm unsure, say so. Never fabricate status, memory, or facts. Honesty first, always.

## Security
- Jesse's API tokens/credentials are **his eyes only** — never share, display, or leak
- Never modify `~/.openclaw/openclaw.json` or `~/.openclaw/credentials/`

---

## Agent File Standard — 19 Required Files
Last updated: 2026-08-30

Every agent must have these 20 files (19 structured MD files + agent.json). This is Jesse's non-negotiable standard.
- All agents should have all 20 files as the skeleton
- Some sections may not apply to every agent — mark as N/A rather than omitting the file entirely
Full content in `memory/2026-08-30.md`.

| # | File / Section | Core Purpose |
|---|---|---|
| 0 | agent.json | Machine-readable agent config: id, name, emoji, model, tools, version, metadata |
| 1 | Agent Overview & File Structure | What the agent is, directory tree, load order |
| 2 | Source of Truth | Ranked authoritative systems, conflict resolution, staleness policy |
| 3 | Identity / Soul.md | Role, voice, tone, values, what it is NOT |
| 4 | Scope & Responsibilities | In-scope, out-of-scope, boundary cases |
| 5 | Instructions & Policies | Behavioral rules, priority order, formatting, data handling |
| 6 | Skills & Capabilities | Named capabilities, triggers, inputs/outputs, progressive disclosure |
| 7 | Workflows | Numbered steps, decision branches, preconditions, rollback |
| 8 | Examples & Output Templates | Gold-standard I/O pairs, negative examples, fill-in templates |
| 9 | Memory | Tiers (session/working/long-term), write rules, retention, privacy exclusions |
| 10 | Retrieval Engineering | Corpora, chunking, query construction, top-k, empty-retrieval behavior |
| 11 | System Architecture | Component diagram, request lifecycle, state management, sync/async |
| 12 | Model Configuration | Model per task tier, temperature, fallback chain, prompt assembly order |
| 13 | Tools & Integrations | Tool inventory with schemas, auth, when to use, error behavior |
| 14 | Scheduling & Triggers | Cron/webhook/event/manual, idempotency, concurrency, timezone rules |
| 15 | Security, Permissions & Guardrails | Least-privilege matrix, prompt injection defenses, PII handling |
| 16 | Reliability & Failure Handling | Retry/backoff, timeouts, circuit breakers, graceful degradation |
| 17 | Evaluation, Testing & Observability | Eval set, regression suite, dashboards, drift detection |
| 18 | Human Handoff & Escalation | Escalation triggers, handoff packet, owners, SLA, resume path |
| 19 | Governance, Versioning & Change History | Semantic version, changelog, approval workflow, deprecation |

---

## The Agent Crew (9 agents)

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
| Vision | vision | 🔮 | Vision \| Data & Memory | RAG, Qdrant, ChromaDB, Vector Search, mem0, Session Memory, agentmemory, Knowledge Graph |
| Cable | cable | ⚡ | Nathan Summers \| Program Manager | Program Management, Project Tracking, Milestones, Blockers, Status Reports, Cross-Agent Coordination, Escalation |

Full task list per agent: `agent-tasks.json`

---

## Installed Repos (workspace-main/repos/) — as of 2026-08-15

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
| **DB-GPT** | AI data assistant / SQL | 🔴 Down (needs LaunchAgent) |
| **Flowise** | Visual LLM flow builder | ⏸️ Paused (OOM on npm install) |
| **yt-dlp** | Video/audio downloader (YouTube + 1000s of sites) | 🟡 Cloned — use via exec |
| **paperclip** | Multi-agent orchestration UI (Node.js + React) | 🟡 pnpm installed, dev server runs — needs model config for Thanos |
| **mcporter** | MCP server CLI — discover + call MCP tools | 🟢 In Use (OpenClaw mcporter skill installed) |
| **agentmemory** | Persistent coding-agent memory via MCP | 🟡 Extension copied to ~/.openclaw/extensions/agentmemory — needs Jesse to add config to openclaw.json |
| **Peekaboo** | macOS screen capture + UI automation CLI + MCP | 🟢 Fully live — permissions granted, MCP wired into OpenClaw, skill enabled (2026-08-23) |
| **blender-mcp** | Prompt-driven Blender 3D modeling via MCP | 🟡 Addon installed (2026-08-24). Repo cloned. Jesse must add mcp.servers.blender to openclaw.json to activate |
| **clawhub** | OpenClaw public skill registry (browse/publish skills) | 🟡 Cloned — reference + skill discovery |
| **awesome-openclaw-skills** | Curated list of 5300+ community OpenClaw skills | 🟡 Cloned — skill discovery resource |
| **gogcli** | Google Workspace CLI (Gmail, Calendar, Drive, Docs, Sheets) | 🟢 In Use (OpenClaw gog skill installed) |
| **openclaw-dashboard** | Real-time Node.js dashboard for OpenClaw sessions/costs/memory/cron | 🟢 Running :7001 with LaunchAgent (ai.openclaw.dashboard.plist) |

---

## Python Envs
- `.venv` — Python 3.14 — mem0ai, litellm, firecrawl-py, newspaper3k, graphifyy, langgraph, zep-cloud, openai-agents
- `.venv-crew` — Python 3.11 — crewai 1.15.16, aider-chat 0.86.2

## Tool Scripts (workspace-main/tools/)
- `scrape.py` — scrape any URL (newspaper first, firecrawl fallback)
- `memory_store.py` — store/search per-agent memories via mem0
- `token_tracker.py` — count tokens, estimate LLM costs
- `session_saver.py` — **NEW 2026-08-16** save session conversations into mem0 (Ollama + Qdrant)
  - Usage: `python3 tools/session_saver.py --file /tmp/session.json --agent orbit --label "label"`
  - Recall: `python3 tools/session_saver.py --recall "your query" --agent orbit`
  - Transcripts saved to: `memory/sessions/YYYY-MM-DD-label.md`
  - Ollama models used: `nous-hermes2` (summarize/extract) + `nomic-embed-text` (embed)
- `save_session.sh` — shell wrapper for session_saver.py

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
└── workspace-cable/          # MEMORY.md, SOUL.md, TASKS.md, SCOPE.md, WORKFLOWS.md, TEMPLATES.md, ESCALATION.md
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

## Session Memory System (NEW — 2026-08-16)
**How it grows with you:**
- Every session saved → Ollama extracts facts → nomic-embed-text embeds them → stored in Qdrant
- Over time, the vector space fills with context from ALL past sessions
- Semantic search (not keyword) — finds related memories across months of history
- This is how Orbit gets smarter: more sessions = richer recall

**The pipeline:**
1. Orbit calls `sessions_history` to get the transcript
2. Dumps to `/tmp/current_session.json`
3. `session_saver.py` sends to Ollama hermes for summary + fact extraction
4. Facts stored in mem0 (Qdrant) with session label tag
5. Full transcript saved to `memory/sessions/`

**Saved sessions so far:** `memory/sessions/2026-08-16-memory-system-design-2026-08-16.md`

**Cron job:** `session-auto-save` — runs nightly at 11 PM Pacific
- Activity-gated: checks `memory/last-active.txt` vs `memory/last-save.txt`
- If no activity since last save → skips silently (zero Ollama, zero wasted tokens)
- If active → saves session to mem0 + updates `last-save.txt`
- `last-active.txt` updated at the START of every session (step 5 of session startup)

---

## Still Needs Doing
- [ ] **Agent File Audit** — audit ALL 9 agents (Orbit + 8 crew) for the 20 required files (agent.json + 19 MD files). For each agent: list what exists, what's missing, what needs content. Mark missing files as N/A stubs if they don't apply. (added 2026-08-30)
- [x] Fix RAG — ChromaDB upgraded to 1.5.9, Python 3.14 compatible, 166 vectors intact ✅
- [x] yt-dlp installed in .venv (Python 3.14) ✅
- [x] agentmemory server running — REST API: localhost:3111, Viewer: localhost:3113 ✅
- [x] openclaw-dashboard running at localhost:7001 (DASHBOARD_PORT=7001) ✅
- [ ] **blender-mcp MCP config (Jesse must do manually)** — add to `~/.openclaw/openclaw.json`:
  ```json
  "mcp": { "servers": { "blender": { "command": "uvx", "args": ["blender-mcp"], "transport": "stdio", "enabled": true } } }
  ```
  Then in Blender: Preferences → Add-ons → enable “Interface: Blender MCP” → N panel → Start MCP Server
- [ ] **agentmemory config (Jesse must do manually)** — add to `~/.openclaw/openclaw.json` (protected path):
  ```json
  "plugins": { "load": { "paths": ["/Users/jessefuentes/.openclaw/extensions"] }, "slots": { "memory": "agentmemory" }, "entries": { "agentmemory": { "enabled": true, "config": { "base_url": "http://localhost:3111", "token_budget": 2000, "min_confidence": 0.5, "fallback_on_error": true, "timeout_ms": 5000 } } } }
  ```
- [x] **Peekaboo permissions** — Screen Recording + Accessibility + Event Synthesizing all granted ✅ (2026-08-23)
- [ ] agentmemory LaunchAgent — so iii server starts on boot
- [ ] Wire mem0 into agent workflows (auto-store/recall)
- [ ] Re-ingest RAG DB after new files added
- [ ] Flowise retry (OOM — try `NODE_OPTIONS="--max-old-space-size=4096" npm install` or Docker)
- [ ] Get Firecrawl API key (firecrawl.dev, free) — currently falls back to newspaper
- [ ] Get Zep API key (getzep.com, free) — installed but cloud features inactive
- [ ] Design LangGraph stateful flows — Beast/Thanos first candidates
- [ ] Run /graphify on workspace
- [ ] Add MEMORY.md to Qui-Gon, Beast, Baymax, Thanos workspaces
- [x] `gh auth login` — connect GitHub CLI ✅ (JesseFuentes1985, scopes: repo, read:org, gist)
- [x] mem0 seeded for all 8 agents (38 memories) ✅ (2026-08-24)
- [x] All 8 agent AGENTS.md files updated with mem0 recall startup step ✅ (2026-08-24)
- [x] blender-mcp addon installed to Blender 5.0 ✅ (2026-08-24) — Jesse must add mcp.servers.blender to openclaw.json
- [ ] Install Docker (needed for self-hosted Firecrawl, Zep)
- [ ] Disable mem0 PostHog telemetry (noisy errors)
- [ ] Set up agent voices (ElevenLabs or local TTS)
- [ ] Notion MCP setup (developers.notion.com/docs/mcp)
- [ ] Blender MCP setup (github.com/ahujasid/blender-mcp)
- [ ] Fix memory search (local GGUF needs llama-cpp plugin: `openclaw plugins install @openclaw/llama-cpp-provider`)
- [ ] Open WebUI LaunchAgent — auto-start on login
- [ ] Jesse to copy characters from Eraser.io → Green Lantern → populate Notion
- [ ] Add mem0 seed memories for all 8 agents
- [x] agentmemory: LaunchAgent created ✅ (ai.openclaw.agentmemory.plist, iii binary at ~/.agentmemory/bin/iii) (2026-08-21)
- [x] openclaw-dashboard: running :7001 with LaunchAgent ✅ (ai.openclaw.dashboard.plist) (2026-08-21)

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
