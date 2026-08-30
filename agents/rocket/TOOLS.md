# TOOLS.md — Rocket Raccoon | Tool Inventory & Integrations
# File 13 of 20: Tools & Integrations

## OpenClaw Tools Available to Rocket
| Tool | Purpose | When to Use |
|---|---|---|
| exec | Run shell commands | Test CLIs, ping APIs, check token status, install tools |
| read / write / edit | File operations | Update TOOLS.md, document integrations, write configs |
| web_search | Search the web | Find integration options, MCP servers, API docs |
| web_fetch | Fetch a URL | Read README, API docs, check repo details |
| browser | Full browser control | OAuth flows that need browser interaction |
| github | GitHub CLI wrapper | Search repos, check issues, read READMEs |
| memory_search / memory_get | Recall past decisions | Check if we've evaluated a tool before |
| sessions_spawn | Spawn sub-agent | Delegate deep research tasks |
| sessions_send | Message a crew agent | Hand off integration work to Rick, Beast, etc. |

## Active Integrations Inventory
*(Keep this updated after every install/remove)*

| Name | Type | Endpoint / Command | Auth | Status | Notes |
|---|---|---|---|---|---|
| GitHub CLI | OAuth | `gh` | OAuth token | ✅ Active | JesseFuentes1985 |
| Slack | Bot | clawbot workspace | Bot token | ✅ Active | — |
| Ollama | Local API | localhost:11434 | None | ✅ Active | 6 models |
| Peekaboo | MCP stdio | `peekaboo` CLI | None | ✅ Active | macOS automation |
| agentmemory | REST API | localhost:3111 | None | ✅ Active | iii binary |
| Open WebUI | Local web | localhost:8080 | Local | ✅ Active | Python 3.11 venv |
| Firecrawl | REST API | firecrawl.dev | API key | ⚠️ No key | Falls back to newspaper |
| Zep Cloud | REST API | api.getzep.com | API key | ⚠️ No key | Installed, inactive |
| Blender MCP | MCP stdio | uvx blender-mcp | None | ⚠️ Pending | Needs openclaw.json entry |

## MCP Servers Registered in OpenClaw
*(Read from ~/.openclaw/openclaw.json — update after any changes)*

| Name | Transport | Command | Status |
|---|---|---|---|
| Peekaboo | stdio | peekaboo mcp | ✅ Active |
| blender | stdio | uvx blender-mcp | ⚠️ Pending Jesse's config edit |

## CLI Utilities (crew-relevant)
| CLI | Purpose | Location | Version |
|---|---|---|---|
| gh | GitHub CLI | /opt/homebrew/bin/gh | current |
| ollama | Local LLM server | /opt/homebrew/bin/ollama | current |
| peekaboo | macOS UI automation | installed via brew | 4.2.2 |
| yt-dlp | Video downloader | .venv (Python 3.14) | current |
| aider | AI pair programmer | .venv-crew (Python 3.11) | 0.86.2 |
| uvx | Python tool runner | /opt/homebrew/bin/uvx | current |

## Discovery Resources
- **MCP server registry:** https://smithery.ai / https://github.com/punkpeye/awesome-mcp-servers
- **OpenClaw plugins:** https://clawhub.io (local: workspace-main/repos/clawhub)
- **Community skills:** workspace-main/repos/awesome-openclaw-skills
- **OpenClaw docs:** /opt/homebrew/lib/node_modules/openclaw/docs
