# WORKFLOWS.md — Rocket Raccoon | Workflows
# File 7 of 20: Workflows

## WF-01: New Integration Request

**Precondition:** Jesse or a crew agent asks to integrate a new service/tool.
**Definition of Done:** Integration is live, tested, documented in TOOLS.md, added to agent-tasks.json.

1. Receive service/tool name and desired capability
2. **Search first** — check GitHub for existing MCP server, plugin, or SDK
3. **Check web** — look for official integration docs, community solutions
4. **Check what's already installed** — scan workspace repos and OpenClaw config
5. Present findings to Jesse: what exists, what's best, what it would take
6. Await go-ahead
7. Install/configure per recommended approach
8. Test connectivity with a live call
9. Document in TOOLS.md (name, type, endpoint, auth method, status)
10. Update agent-tasks.json status to done
11. Report completion to Orbit (main)

**Abort path:** If no suitable solution found after exhaustive search → recommend build plan and escalate to Orbit.

---

## WF-02: Token / Auth Health Check

**Precondition:** Periodic check or triggered by 401/403 error.

1. Read active integrations from TOOLS.md
2. For each integration with an auth requirement:
   a. Attempt lightweight authenticated API call
   b. Check token expiry if available
3. Categorize: ✅ valid / ⚠️ expiring <7 days / ❌ expired or broken
4. For any ⚠️ or ❌: prepare rotation steps
5. Report to Jesse with action items
6. If Jesse must take manual OAuth action: provide exact URL + steps
7. After rotation: re-test and confirm ✅

**Rollback:** If rotation breaks something, restore previous token if available, flag immediately.

---

## WF-03: MCP Server Discovery

**Precondition:** New tool/service discussed, or periodic scan for new MCP ecosystem additions.

1. Identify target service/capability
2. Search: `site:github.com <service> mcp`
3. Search: `"<service>" "model context protocol" OR "mcp server"`
4. Check: awesome-mcp lists, OpenClaw plugin registry, Smithery.ai
5. Evaluate candidates (stars, freshness, license)
6. Check if OpenClaw config already has it registered
7. Return ranked table
8. If top candidate selected: follow WF-01 from step 6

---

## WF-04: Repo Discovery & Evaluation

**Precondition:** Need a library, SDK, or tool for a capability.

1. Define search keywords (capability + language + platform)
2. GitHub search with filters (stars >50, recent activity)
3. Pull top 5 candidates
4. For each: read README, check issues, check license
5. Cross-check against crew's existing stack (Python 3.14/.venv, Node v24, zsh/macOS)
6. Rank by: fit, maintenance, ease of integration
7. Return table with recommendation
8. If install approved: clone to workspace-main/repos/, document in MEMORY.md

---

## WF-05: Connector Health Audit (Periodic)

**Precondition:** Weekly or on-demand.

1. List all registered connectors (OpenClaw config, TOOLS.md)
2. For each: ping endpoint or check last successful event
3. Report health matrix
4. Flag anything silent >7 days or erroring
5. For broken connectors: diagnose and propose fix
6. Update TOOLS.md with current status
