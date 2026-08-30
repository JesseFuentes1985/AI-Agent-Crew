# Session Notes — Green Lantern

Last updated: 2026-03-01

---

## The Project: Last Star

Jesse's story/universe is called **Last Star**. Characters are partially in Notion (not all of them). Full character bible needs to be built out.

---

## The Hex — Ship (see hex-ship.md for full details)

- Jesse's ship in the Last Star universe
- Owner/builder: **Dox** — built it out of grief, over-engineered on purpose
- 8-person crew capacity
- Wide-body freighter disguised as a fortress
- Moon of Ash alloy in the engine core — the emotional heart
- File saved: `workspace-greenlantern/hex-ship.md`

---

## Last Star — Content Status

### In Notion (connected ✅)
- Full faction/world lore pages (20+ factions already)
- Last Star HQ page ID: `2047ed43-1148-805c-9aa1-c7298151ddfd`

### On Eraser.io (need to transfer)
- **Characters** — Jesse will copy these over manually
- **Stories** — some story content lives here
- **Story rules** — rules/guidelines for the universe (get into this later)

### TODO
- [ ] Jesse copies characters from Eraser.io → paste to Green Lantern → I populate Notion + local files
- [ ] Build a Characters database in Notion Last Star HQ
- [ ] Capture story rules once Jesse is ready
- [ ] **Eraser.io API setup** — Eraser has a REST API (no MCP yet). Get API key from eraser.io account settings → connect so I can read diagrams/docs/characters directly without manual copy-paste. Docs: `docs.eraser.io/reference`

---

## The Plan We Built

### Phase 1 — Notion MCP
- Notion has an **official MCP server** (remote, OAuth-based)
- Docs: `developers.notion.com/docs/mcp`
- Goal: connect me to Jesse's Notion → pull Last Star characters → build full story bible
- **STATUS: Not yet set up**

### Phase 2 — Blender MCP
- Add-on: `github.com/ahujasid/blender-mcp`
- Runs local server at `http://localhost:8000`
- Goal: control Blender via natural language → build the Hex in 3D
- Pipeline: prompt → OpenClaw → Blender MCP → bpy Python → GLB export → Three.js web viewer
- **STATUS: Not yet set up**

### Phase 3 — Build the Hex
- Source a blocky freighter base mesh (Sketchfab/BlenderKit)
- Apply weathered hull textures, stencil markings (SECTOR 7X red, HEX green)
- Moon of Ash alloy engine housing (darker, iridescent)
- Amber running lights + blue emissive thruster
- Export GLB → deploy interactive 360° web viewer

---

## Agent Setup Context

- **Green Lantern** = Creativity agent (this agent) — Blender, worldbuilding, writing
- **Orbit** = Command/coordinator agent — Jesse said to loop Orbit in on logging
- **Rick** = Another agent (role unclear, Jesse to clarify)
- Jesse will brief Orbit separately on this session's work

---

## Technical Notes

- Memory search is broken (OpenAI embeddings key `asda` is invalid — needs fixing)
- Green Lantern emoji updated from 💚 to 🟢 (Classic GL, clean)
- Workspace: `/Users/jessefuentes/.openclaw/workspace-greenlantern/`

---

## MCP Server Status (as of 2026-03-01)

### ✅ Notion MCP — LIVE
- Built-in OpenClaw skill (📝 notion) — status: Ready
- API key stored via `openclaw config set skills.entries.notion.apiKey`
- Last Star HQ page connected: `2047ed43-1148-805c-9aa1-c7298151ddfd`
- Can read/write pages, databases, blocks

### ✅ Blender MCP — LIVE
- Add-on installed: `/Users/jessefuentes/Downloads/blender-mcp-main/addon.py`
- Running on port **9876** (TCP socket, NOT HTTP)
- Bridge: `uvx blender-mcp` (mcporter stdio command)
- mcporter config: `workspace-greenlantern/config/mcporter.json`
- uv installed via homebrew
- mcporter installed via npm globally
- **22 tools available** including: get_scene_info, execute_blender_code, get_viewport_screenshot, search_sketchfab_models, download_sketchfab_model, generate_hyper3d_model_via_text, set_texture
- **⚠️ Important:** Blender must be open and MCP server must be started manually each session
  - Open Blender → Press **N** → Click **BlenderMCP tab** → Click **Start MCP Server**
  - Confirmed running when it shows port 9876

### How to call Blender tools
Use mcporter via exec:
```bash
BLENDER_HOST=localhost BLENDER_PORT=9876 mcporter call blender-mcp.get_scene_info user_prompt="test"
```

### ✅ CONNECTION CONFIRMED (2026-03-01)
- Tested with basketball — orange sphere created successfully via execute_blender_code
- Core workflow proven: natural language → I write Python → Blender executes
- execute_blender_code is the primary tool for building
- search_sketchfab_models NOT available in this addon version (addon.py v1.2, needs update for Sketchfab/Poly Haven)
- Optional integrations in N panel (Poly Haven, Hyper3D, Sketchfab, Hunyuan) — require API keys, skip for now
- The Hex will be built using execute_blender_code with Python/bpy scripting

---

## WHERE WE LEFT OFF (2026-03-01)

Both MCPs are set up and verified working. Next steps:
1. **Test Blender connection** — run get_scene_info to confirm live link
2. **Start building the Hex** — search Sketchfab for a freighter base mesh
3. **Characters** — Jesse to copy characters from Eraser.io → paste here → I populate Notion
4. **Eraser.io API** — set up API key when ready (see TODO above)

---

## Reference Links

- OpenClaw docs: `openclaw.ai/docs`
- Blender MCP: `github.com/ahujasid/blender-mcp`
- Notion MCP: `developers.notion.com/docs/mcp`
- Riley Brown's video: OpenClaw + Blender MCP demo (Mac Mini model → recolor → sticker → deploy)
