# Session: 2026-04-18 17:06:51 UTC

- **Session Key**: agent:main:main
- **Session ID**: 3e46fc4d-035d-41e9-919b-3fc1f12290e0
- **Source**: webchat

## Conversation Summary

assistant: On it — let me check the current config first, then wire it in.
assistant: Let me check the schema for how Ollama should be configured as a plugin/provider:
assistant: Got everything I need. Patching the config now to enable the Ollama plugin, then I'll also add `nous-hermes2` to the available models and set it as a fallback:
assistant: Config patched. Now restarting to load the Ollama plugin:
assistant: Restarting... I'll be back in a sec. Once I'm back up here's what you'll have:

---

## ✅ What Just Got Set Up

- **Ollama plugin** enabled in OpenClaw — it auto-discovers your local models
- **`nous-hermes2`** registered with alias **`hermes`**
- Ollama runs at `localhost:11434` — no API key, totally free

## How to Use It

**Switch any session to Hermes:**
```
/model hermes
```

**Or kick off a subagent using it** — like spinning up Rick or Beast on `ollama/nous-hermes2` for code tasks to save API credits.

**File reading with it right now:**
```bash
cat yourfile.py | ollama run nous-hermes2 "Review this"
git diff | ollama run nous-hermes2 "Summarize these changes"
```

## 👁️ Vision — Want Images Too?

Run this and I'll wire up a vision model alongside it:
```bash
ollama pull llava
```

That'll let any agent analyze images locally, zero cost.
assistant: Audio reply
user: System: [2026-04-18 10:02:23 PDT] Gateway restart restart ok (gateway.restart)
System: Ollama is live! nous-hermes2 registered as 'hermes' — use /model hermes to switch to it anytime.
System: Run: openclaw doctor --non-interactive

Read HEARTBEAT.md if it exists (workspace context). Follow it strictly. Do not infer or repeat old tasks from prior chats. If nothing needs attention, reply HEARTBEAT_OK.
When reading HEARTBEAT.md, use workspace file /Users/jessefuentes/.openclaw/workspace-main/HEARTBEAT.md (exact case). Do not read docs/heartbeat.md.
Current time: Saturday, April 18th, 2026 - 10:02 AM (America/Los_Angeles) / 2026-04-18 17:02 UTC
assistant: HEARTBEAT_OK
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sat 2026-04-18 10:04 PDT] ok cool done
assistant: You pulled `llava` too — let's register it right now.
assistant: You're fully loaded now. Here's your local AI arsenal:

---

## 🔥 Local Models Ready

| Alias | Model | Size | Use For |
|---|---|---|---|
| `hermes` | `ollama/nous-hermes2` | 6.1 GB | Text, code, reasoning |
| `llava` | `ollama/llava` | 4.7 GB | **Images + text** |

---

## How to Use Them

**Switch to Hermes (free, local):**
```
/model hermes
```

**Switch to LLaVA (vision):**
```
/model llava
```

**Drop an image in chat** while on `/model llava` and it'll describe/analyze it — screenshots, photos, diagrams, whatever.

**Back to Claude:**
```
/model sonnet
```

---

Both models run 100% on your Mac mini, zero API cost. Hermes is solid for code review and drafts. LLaVA handles anything visual. 🛸
assistant: Audio reply
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sat 2026-04-18 10:06 PDT] I am confused how do I switch them
assistant: Super easy — two ways:

---

## Option 1: Type it in chat (fastest)

Just type this directly in the chat box:
```
/model hermes
```
or
```
/model llava
```
or back to me:
```
/model sonnet
```

That switches the active model for the current session right then and there.

---

## Option 2: The dropdown in the UI

Look at the bottom of the chat — there should be a model selector. You can click it and pick from the list. `hermes` and `llava` should show up there now.

---

**Quick cheat sheet:**
- 🆓 `hermes` → free local, good for code/text
- 🆓 `llava` → free local, good for images
- 💰 `sonnet` → Claude (costs API credits, most powerful)

Want me to test it right now? Type `/model hermes` and then ask it something — I'll stay quiet and let it answer. 😄
assistant: Audio reply
