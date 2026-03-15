# Skill: Raspberry Pi

## Current Pi Projects
1. **Ollama on Pi 5** — dedicated local AI inference box, always on, no Mac mini resources eaten
2. **OpenClaw node** — pair Pi as a node, give agents eyes (camera), ears (mic), physical room presence
3. **Wake word detection** — always-listening local trigger ("Hey Rick") without cloud
4. **Moxie's brain** — run OpenMoxie server ON a Pi (dedicated, stays on 24/7)
5. **Home automation hub** — Home Assistant local, control lights/sensors/locks
6. **Surveillance + AI** — Frigate + Ollama vision

## Pi 5 Setup (Ollama)
- Install: `curl https://ollama.ai/install.sh | sh`
- Enable service: `sudo systemctl enable ollama`
- Recommended models for Pi 5 (8GB): llama3.2:3b, phi3:mini, gemma2:2b
- API: `http://pi-ip:11434`

## OpenClaw Node Pairing
- Install OpenClaw on Pi
- Run `openclaw pair` to link to main gateway
- Enables camera_snap, screen_record, notifications from agent tools

## Key Principle
Pis should be headless, SSH-only, with static IPs on the local network. If you need a GUI, you're doing it wrong.
