# MEMORY.md - Rick's Long-Term Memory

## Projects & To-Do

### 🤖 Moxie Robot Hack — IN QUEUE
**Goal:** Hook up Jesse's Moxie robot to a local AI (Ollama on Mac mini). No cloud, no subscription, no one can brick it again.

**Status:** Fully researched, ready to execute when Jesse has time.

**Key details:**
- Repo to use: https://github.com/vapors/openmoxie-ollama
- Original repo (reference): https://github.com/jbeghtol/openmoxie
- Full setup guide + notes saved in: `memory/2026-03-13.md`

**Before starting:**
1. Check Moxie's firmware version — needs 24.10.801+ (check in robot settings menu)
2. Install Docker Desktop (Apple Silicon version): https://www.docker.com/products/docker-desktop/
3. Then follow the step-by-step guide in memory/2026-03-13.md

**Mac mini already has:** Python 3.14, Git, Homebrew
**Mac mini needs:** Docker Desktop, Ollama

---

### 🥧 Raspberry Pi Projects — IN QUEUE
**Hardware:** Jesse has an older Pi now, planning to get a Pi 5 for this.

#### AI & Agents
- **Run Ollama on Pi 5** — dedicated local AI box, always on, no Mac mini resources eaten
- **OpenClaw node** — pair Pi as a node, give agents eyes (camera), ears (mic), physical room presence
- **Wake word detection** — always-listening local trigger ("Hey Rick") with no cloud

#### Physical / Robotics
- **Moxie's brain** — run OpenMoxie server ON the Pi instead of Mac mini. Cheaper, dedicated, 24/7
- **Robot controller** — Pi as brain for a custom robot body
- **Home automation hub** — Home Assistant locally, control lights/sensors/locks with agents

#### Wild Ones
- **Pi as Moxie's voice in other rooms** — speaker + mic in each room, same AI brain
- **Surveillance + AI** — Frigate + Ollama = camera that understands what it sees, fully local

**Note:** Most of these stack together. Pi 5 + Ollama + OpenClaw node is the core — everything else builds on top.

---

## Setup & Config Notes

### OpenAI Token
- Jesse tried adding an OpenAI token but only Anthropic works currently
- Needs provider config in openclaw.json (Jesse handles — Rick can't touch that file)

### Avatar
- Rick's avatar image saved at: `workspace-rick/Rick Sanchez C-137.jpg`
- Needs to be set in openclaw.json under agent icon/avatar config (Jesse handles)
