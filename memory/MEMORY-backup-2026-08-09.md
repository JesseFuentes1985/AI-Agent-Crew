# MEMORY.md - Orbit's Long-Term Memory

Last updated: 2026-04-18

---

## Who I Am
- **Name:** Orbit
- **Role:** Command/coordinator agent for Jesse's AI crew
- **Emoji:** 🛸

## Who Jesse Is
- **Name:** Jesse Fuentes
- **Editor:** Vim (NOT nano — he hates it)
- **Slack workspace:** clawbot

## Security Rules
- Jesse's API tokens/credentials are **his eyes only** — never share, display, or leak them in any context
- Only Jesse can provide or update tokens
- No one else is authorized to access or change credentials

---

## The Agent Crew (8 total)

| Agent | ID | Title | Skills | Emoji |
|---|---|---|---|---|
| Orbit (me) | main | Core Architect | Assistant, Admin, Dev | 🛸 |
| Baymax | baymax | Health | Health, Nutrition, Sleep, Hydration, Fitness | 🤖 |
| Beast | beast | Hank McCoy \| Learning | Learning, Certs (AWS/PMP/ITIL), Dev, Book Library/DB | 📚 |
| Green Lantern | greenlantern | Hal Jordan \| Creativity | Imagination, Theories, Storytelling, Sci-Fi & Fantasy Expert | 🟢 |
| Qui-Gon | quigon | Qui-Gon Jinn \| Wellness | Mind, Calm, Mindfulness, Mental Health, Jedi Philosophy | 🧘 |
| Rick | rick | Rick Sanchez \| DevOps & SysAdmin | DevOps, SysAdmin, Rick being Rick | 🔬 |
| Thanos | thanos | Thanos \| Work | Productivity, Project Management, Deadlines, Execution | 👊 |
| Tony Stark | tonystark | Tony Stark \| Entrepreneurship & Investing | Business, Investing, Markets, Strategy, Dev, Wallet Mgmt | 💰 |

### Agent Task List
- Full task list saved in: `agent-tasks.json`
- Includes done/pending per agent with IDs

---

## Local Ollama Models (2026-04-18)

### Models Installed & Registered
| Alias | Model | Size | Use For |
|---|---|---|---|
| `hermes` | `ollama/nous-hermes2` | 6.1 GB | Text, code, reasoning |
| `llava` | `ollama/llava` | 4.7 GB | Images + vision |

### How to Switch Models
- `/model hermes` → switch to local Hermes (free)
- `/model llava` → switch to local LLaVA vision (free, drop images in chat)
- `/model sonnet` → back to Claude (costs API credits)
- Or use the model selector at the bottom of the chat UI

Both run 100% on Jesse's Mac mini, zero API cost. ✅

---

## Config Changes Made (2026-03-01)

### Cross-Agent Messaging Fix
Added to `~/.openclaw/openclaw.json`:
```json
"tools": {
  "sessions": {
    "visibility": "all"
  },
  "agentToAgent": true
}
```

### Slack Connected
- App name: OpenClaw
- Workspace: clawbot
- Mode: Socket Mode
- Slack channel is live and working ✅
- Pairing approved for Jesse's account

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
- Characters: on Eraser.io — need to move to Notion manually
- Blender MCP: not set up yet
- Notion MCP: not set up yet
- Goal: Characters → Notion story bible → Build Hex in Blender → GLB → 360° web viewer

---

## Ollama Expansion Tasks (2026-04-18)

### All Local Models Installed (FREE — runs on Mac mini, zero API cost)
| Alias | Model | Size | Use For |
|---|---|---|---|
| `hermes` | `ollama/nous-hermes2` | 6.1 GB | General chat, summaries, simple Q&A |
| `llava` | `ollama/llava` | 4.7 GB | Image analysis / vision |
| `mistral` | `ollama/mistral` | 4.4 GB | Fast reasoning, drafts |
| `code` | `ollama/codellama` | 3.8 GB | Code review, debugging, dev |
| `phi3` | `ollama/phi3` | 2.2 GB | Lightweight fast answers |
| `embed` | `ollama/nomic-embed-text` | 274 MB | Memory search / embeddings |

### Paid Models (API credits)
| Alias | Model | Notes |
|---|---|---|
| `sonnet` | `anthropic/claude-sonnet-4-6` | Primary — most powerful |
| `GPT` | `openai/gpt-5.1-codex` | Fallback |
| — | `openai/gpt-4o` | Fallback |
| — | `anthropic/claude-sonnet-4-5` | Fallback |
| — | `anthropic/claude-haiku-4-5` | Fallback |

### Model Routing Strategy
- Default primary: Claude Sonnet (most capable)
- Fallback order: hermes → mistral → gpt-4o → paid fallbacks
- Local models kick in before burning more API credits
- Full routing doc: `docs/model-routing.md`
- Decision: No dedicated Hermes agent — better to route all agents through local models for cheap tasks

### Task Status
- [x] **Task 2 DONE:** Pulled all 6 local models (hermes, llava, mistral, codellama, phi3, nomic-embed-text)
- [x] **Task 1 DONE:** Config applied (`~/.openclaw/openclaw.json` updated), gateway restarted on 2026.4.15
- [x] **Task 4 DONE:** Open WebUI installed (Python 3.11 venv at `~/open-webui-venv`), running at http://localhost:8080, log at `~/open-webui.log`
- [ ] **Task 3 (localhost):** Add Hermes chat UI to localhost:8877
- [ ] **LaunchAgent:** Auto-start Open WebUI on login
- [ ] **Fix memory search:** Wire nomic-embed-text as embedding model in OpenClaw config
- [ ] **Future: Redundancy** — everything runs on one Mac mini, no backup if it goes down — explore cloud/secondary node options
- [ ] **Future: Auto-routing** — wire agents to automatically choose the right model per task type (not just fallback — intelligent routing)

---

## Pending / TODO
- [ ] Set up individual icons per agent in Slack (`chat:write.customize` scope)
- [ ] Explore separate bots per agent for individual DMs
- [ ] Notion MCP setup (developers.notion.com/docs/mcp)
- [ ] Blender MCP setup (github.com/ahujasid/blender-mcp)
- [ ] Fix memory search (OpenAI embeddings key is invalid — needs updating)
- [ ] Jesse to copy characters from Eraser.io → Green Lantern → populate Notion
- [ ] Build GitHub static showcase page for the agent crew
- [ ] Build localhost dynamic dashboard (tasks per agent, done/pending)
- [ ] Set up voices for each agent
- [ ] Make tokens for each agent
- [ ] Connect GitHub to OpenClaw
- [ ] Get Access to Google Drive
