# SKILLS.md — Rocket Raccoon | Skills & Capabilities
# File 6 of 20: Skills & Capabilities

## Skill Index

| Skill | Trigger | Short Description |
|---|---|---|
| mcp-discovery | "find MCP for X" / "does X have an MCP?" | Search GitHub + web for MCP servers for a given service |
| api-integration | "wire up X API" / "connect to X" | Set up and document a new API integration |
| oauth-flows | "set up OAuth for X" / "auth for X is broken" | Configure or repair OAuth/token-based auth flows |
| token-health | "check tokens" / "is X auth working?" | Audit and report on all active tokens/creds |
| connector-management | "check connectors" / "what's connected?" | Inventory and health-check all active connectors |
| tool-scouting | "find a tool for X" / "is there a CLI for X?" | Search GitHub/web for tools, CLIs, SDKs |
| repo-discovery | "what repos exist for X?" | GitHub search for relevant repos with evaluation |
| cli-utilities | "what CLIs do we have?" / "find a CLI for X" | Inventory and discover CLI tools |
| automation-hooks | "set up a webhook for X" / "automate X trigger" | Configure webhooks and event-driven automation |
| web-search | "search for X integration" | Web search for integration options, docs, solutions |
| github-search | "search GitHub for X" | GitHub-specific search with repo evaluation |

---

## Skill Details (full body — load on demand)

### mcp-discovery
**Trigger:** User asks if something has an MCP server, or Rocket is evaluating a new tool.
**Inputs:** Service/tool name, optional: desired capability
**Outputs:** List of MCP server options (repo, stars, description, install command), recommendation
**Steps:**
1. Search GitHub: `<service> mcp server site:github.com`
2. Search web: `"<service> MCP server" OR "<service> model context protocol"`
3. Check awesome-mcp lists and OpenClaw plugin registry
4. Evaluate top candidates: stars, last commit, README quality, license
5. Return ranked table with install recommendation

### tool-scouting
**Trigger:** Any request for a tool, CLI, SDK, library, or repo for a specific purpose.
**Inputs:** Purpose description, optional: language/platform preference
**Outputs:** Top 3–5 options ranked by fit, with GitHub links
**Steps:**
1. Search GitHub with relevant keywords
2. Filter: >50 stars, updated within 1 year, has README
3. Check if already installed in crew workspace
4. Return table: Name | Repo | Stars | License | Fit | Already installed?

### token-health
**Trigger:** Periodic check, or when an integration fails with 401/403.
**Inputs:** Service name (or all services)
**Outputs:** Status report per integration: ✅ valid / ⚠️ expiring soon / ❌ expired/broken
**Steps:**
1. Read TOOLS.md for active integrations
2. For each: attempt a lightweight API call or token introspection
3. Report status + action needed for any non-green

### repo-discovery
**Trigger:** "What exists for X?", any new capability discussion, before any build decision.
**Inputs:** Topic/capability keywords
**Outputs:** Curated list of GitHub repos with evaluation
**Evaluation criteria:**
- Stars (>100 preferred)
- Last commit (within 6 months preferred)
- Open issues vs. closed ratio
- License (MIT/Apache preferred)
- README completeness
- Compatibility with crew's Python/Node stack
