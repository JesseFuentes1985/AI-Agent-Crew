# Skill: DevOps

## What This Is
Building, deploying, and maintaining infrastructure that actually works and doesn't wake Jesse up at 3am.

## Stack
- Docker / Docker Compose — containerizing everything that moves
- GitHub Actions — CI/CD for the agent crew repo
- Nginx — reverse proxy for local and VPS services
- systemd — service management on Linux hosts
- SSH — the only way to administer a server

## Current Infrastructure
- Mac mini — main OpenClaw host (Darwin arm64)
- Dashboard: Node.js on port 3131
- GitHub: JesseFuentes1985/AI-Agent-Crew
- Pi 5: (being set up) — Ollama inference box

## Principles
- If it's not in version control, it doesn't exist
- Every service needs a restart policy
- Logs matter — if you can't see what's happening, you can't fix it
- Automate everything that happens more than twice
