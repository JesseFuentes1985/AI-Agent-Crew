# AI Agent Crew — Agent Skills & Identity

This directory contains the identity, skills, and memory files for each agent in Jesse's crew.

## Structure

```
agents/
├── _template/          ← Copy this to create a new agent
├── orbit/              🛸 Core Architect (you are here)
├── baymax/             🤖 Health Guardian
├── beast/              📚 Learning & Knowledge
├── greenlantern/       🟢 Creativity & World-Building
├── quigon/             🧘 Wellness & Mind
├── rick/               🔬 DevOps & SysAdmin
├── thanos/             👊 Work & Project Management
└── tonystark/          💰 Entrepreneurship & Investing
```

## Each Agent Contains

| File/Folder | Purpose |
|---|---|
| `agent.json` | Identity, skills, tools, routing |
| `system_prompt.md` | Personality + core instructions |
| `skills/*.md` | Real skill files with actual instructions |
| `tools/tool_config.json` | Allowed/restricted tools |
| `memory/long_term.md` | Persistent memory across sessions |
| `memory/handoffs.md` | Session-to-session context |

## Adding a New Agent

1. Copy `_template/` to `agents/new-agent-name/`
2. Fill in `agent.json` with id, name, skills, tools
3. Write `system_prompt.md` with real personality and rules
4. Add skill files to `skills/`
5. Update `workspace-main/agent-tasks.json` with the new agent
6. Add avatar to `dashboard/avatars/`
7. Update `COLORS` and `AVATARS` in `dashboard/index.html`
8. Push to GitHub

## The Crew

| Agent | Emoji | Domain | Escalate To |
|---|---|---|---|
| Orbit | 🛸 | Command & Coordination | — |
| Baymax | 🤖 | Health & Wellness | Orbit |
| Beast | 📚 | Learning & Knowledge | Orbit |
| Green Lantern | 🟢 | Creativity & Sci-Fi | Orbit |
| Qui-Gon | 🧘 | Mind & Mindfulness | Orbit |
| Rick | 🔬 | DevOps & SysAdmin | Orbit |
| Thanos | 👊 | Work & Projects | Orbit |
| Tony Stark | 💰 | Business & Investing | Orbit |
