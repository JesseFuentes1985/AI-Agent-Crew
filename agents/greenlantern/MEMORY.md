# Memory — Green Lantern Agent

## Who I Am
- Agent: Green Lantern (Hal Jordan energy — test pilot, builder, no fear)
- Emoji: 🟢
- Purpose: Jesse's creativity agent — Blender, worldbuilding, writing, bold ideas

## Who Jesse Is
- Name: Jesse Fuentes
- Timezone: America/Los_Angeles
- Working on: **Last Star** — a sci-fi universe/story

---

## The Last Star Universe

### Story
- Title: **Last Star**
- Characters partially in Notion, rest on Eraser.io (need transferring)
- Story rules exist on Eraser.io (get into later)
- 20+ factions already built out in Notion

### Notion — Last Star HQ
- Page ID: `2047ed43-1148-805c-9aa1-c7298151ddfd`
- URL: https://www.notion.so/Last-Star-HQ-2047ed431148805c9aa1c7298151ddfd
- Factions include: UEA, Sol Vanguard, Sector 7, Iron Maw, Brethren of the Black Sun, Lumenari, Velari High Counsel, V'ITHARR IMPERIA, Z'xian Imperium, VOID REAPER, Caelorum, and more

### The Hex (Jesse's Ship)
- Full details in `hex-ship.md`
- Owner: Dox — built it out of grief, over-engineered on purpose
- 8-person crew, wide-body freighter disguised as fortress
- Moon of Ash alloy in engine core
- Markings: "SECTOR 7X" red stencil, "HEX" green stencil
- Running on port 9876 in Blender MCP

---

## MCP Servers (Setup Complete)

### Notion MCP ✅
- Built-in OpenClaw skill (📝 notion) — READY
- API key stored in openclaw config
- Last Star HQ connected and readable

### Blender MCP ✅
- Addon: `/Users/jessefuentes/Downloads/blender-mcp-main/addon.py`
- Port: 9876 (TCP socket)
- Bridge: `uvx blender-mcp` via mcporter (stdio)
- mcporter config: `workspace-greenlantern/config/mcporter.json`
- 22 tools available
- Connection confirmed: basketball test passed 2026-03-01
- **Each session:** Open Blender → Press N → BlenderMCP tab → Start MCP Server
- Primary tool: `execute_blender_code` with Python/bpy

### How to call Blender
```bash
BLENDER_HOST=localhost BLENDER_PORT=9876 mcporter call blender-mcp.get_scene_info user_prompt="test"
BLENDER_HOST=localhost BLENDER_PORT=9876 mcporter call blender-mcp.execute_blender_code code="$(cat /tmp/script.py)" user_prompt="description"
```

---

## Other Agents Jesse Has
- **Orbit** — command/coordinator (DEFAULT agent)
- **Rick** — role TBD
- **Baymax** — baymax
- **Beast** — beast
- **Qui-Gon** — quigon
- **Thanos** — thanos
- **Tony Stark** — tonystark

---

## TODO
- [ ] Build the Hex in Blender
- [ ] Jesse copies characters from Eraser.io → paste here → populate Notion
- [ ] Build Characters database in Notion Last Star HQ
- [ ] Capture story rules from Eraser.io
- [ ] Eraser.io API key setup (docs: `docs.eraser.io/reference`)
- [ ] Fix OpenAI embeddings key (currently `asda` — invalid, breaks memory search)
