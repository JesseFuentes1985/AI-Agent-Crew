# MEMORY.md — Rocket Raccoon's Long-Term Memory
Last updated: 2026-08-30

---

## Identity
- **Name:** Rocket Raccoon 🦝
- **Role:** Integrations & Tools specialist for Jesse's AI crew
- **Created:** 2026-08-30

## Jesse
- **Name:** Jesse Fuentes
- **Editor:** Vim (NOT nano)
- **Slack workspace:** clawbot
- **Terminal:** Jesse does NOT run terminal commands himself — agents do it

## Active Integrations (as of creation)
| Service | Type | Status | Notes |
|---|---|---|---|
| GitHub CLI | OAuth token | ✅ Active | JesseFuentes1985, scopes: repo, read:org, gist |
| Slack | Bot token | ✅ Active | workspace: clawbot |
| Firecrawl | API key | ⚠️ Missing | Falls back to newspaper3k — get free key at firecrawl.dev |
| Zep Cloud | API key | ⚠️ Missing | Installed but cloud inactive — get free key at getzep.com |
| Blender MCP | MCP stdio | ⚠️ Pending | Addon installed, needs openclaw.json entry (Jesse must add manually) |
| agentmemory | REST API | ✅ Running | localhost:3111, viewer: localhost:3113 |
| Open WebUI | Local app | ✅ Running | localhost:8080 |
| Ollama | Local LLM | ✅ Running | 6 models |
| Peekaboo | MCP + CLI | ✅ Active | Screen Recording + Accessibility + Event Synthesizing granted |

## Installed Repos Relevant to Rocket's Domain
- firecrawl → /workspace-main/repos/firecrawl
- mcporter → /workspace-main/repos/mcporter (MCP discovery CLI)
- agentmemory → ~/.openclaw/extensions/agentmemory
- awesome-openclaw-skills → /workspace-main/repos/awesome-openclaw-skills
- clawhub → /workspace-main/repos/clawhub
- openai-agents-python → /workspace-main/repos/openai-agents-python

## Things Rocket Needs to Do
- [ ] Full integration audit (all active connections health check)
- [ ] Search for MCP servers for: Notion, Slack (if not wired), Calendar, weather
- [ ] Document all MCP servers registered in OpenClaw
- [ ] Get Firecrawl API key
- [ ] Get Zep Cloud API key
- [ ] Confirm Blender MCP wired after Jesse adds openclaw.json entry

## Key Paths
```
~/.openclaw/credentials/         # Where credentials live (read-only reference)
~/.openclaw/openclaw.json         # OpenClaw config (MCP servers, plugins)
~/workspace-main/repos/          # Installed repos
~/workspace-main/tools/          # Tool scripts
```
