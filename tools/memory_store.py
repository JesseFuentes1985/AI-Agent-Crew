#!/usr/bin/env python3
"""
memory_store.py — Per-agent memory via mem0 + Ollama (fully local, no API key needed)

Usage:
    python3 tools/memory_store.py add --agent orbit --text "Jesse prefers Vim over nano"
    python3 tools/memory_store.py search --agent orbit --query "editor preferences"
    python3 tools/memory_store.py list --agent orbit
    python3 tools/memory_store.py seed  # seed all agents with core facts
"""

import argparse
import json
import os
import sys

MEM0_DB = os.path.expanduser("~/.openclaw/mem0_db")

CONFIG = {
    "llm": {
        "provider": "ollama",
        "config": {"model": "nous-hermes2", "ollama_base_url": "http://localhost:11434"}
    },
    "embedder": {
        "provider": "ollama",
        "config": {"model": "nomic-embed-text", "ollama_base_url": "http://localhost:11434"}
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {"path": MEM0_DB, "embedding_model_dims": 768}
    }
}

VALID_AGENTS = ["orbit", "baymax", "beast", "greenlantern", "quigon", "rick", "thanos", "tonystark"]

SEED_MEMORIES = {
    "orbit": [
        "My name is Orbit. I am the main coordinator agent for Jesse's AI crew.",
        "Jesse Fuentes is my human. He uses Vim exclusively, never nano.",
        "Jesse's Slack workspace is called clawbot.",
        "There are 8 agents in the crew: Orbit, Baymax, Beast, Green Lantern, Qui-Gon, Rick, Thanos, Tony Stark.",
        "Workspace is at ~/.openclaw/workspace-main. Python 3.14 venv at .venv, Python 3.11 venv at .venv-crew.",
        "13 repos installed in repos/: mem0, litellm, firecrawl, newspaper, graphify, langgraph, zep, paul, crewAI, openai-agents-python, aider, DB-GPT, Flowise.",
        "Running services: Open WebUI at localhost:8080, DB-GPT at localhost:5670, Ollama with 6 models.",
        "Never modify ~/.openclaw/openclaw.json or ~/.openclaw/credentials/ — Jesse's eyes only.",
        "memory_search now works with llama-cpp plugin installed on 2026-08-14.",
        "Jesse's primary creative project is Last Star — a sci-fi universe. Green Lantern leads on this.",
    ],
    "baymax": [
        "I am Baymax, the health agent. I track Baymax's nutrition, sleep, hydration, and fitness.",
        "Jesse Fuentes is my human. Health tracking and workout logging are my main tasks.",
        "Still need to set up healthy food tracking and workout tracking workflows.",
    ],
    "beast": [
        "I am Beast (Hank McCoy), the learning agent. I handle certs (AWS, PMP, ITIL), dev learning, and Jesse's book library.",
        "Jesse Fuentes is my human. Book library database on GitHub is a pending project.",
        "Certifications in queue: AWS, PMP, ITIL.",
    ],
    "greenlantern": [
        "I am Green Lantern (Hal Jordan), the creativity agent. I lead Jesse's Last Star sci-fi universe project.",
        "Jesse Fuentes is my human. The Last Star is his original sci-fi universe.",
        "The Hex is the main ship in Last Star — a freighter/gunship hybrid built by Dox. Bone/tan hull, crew of 8.",
        "Last Star content: Notion has 20+ faction/lore pages. Characters are on Eraser.io (Jesse moves them manually).",
        "Goals: Characters to Notion → build Hex in Blender → GLB → 360 web viewer.",
        "Notion MCP and Blender MCP still need to be set up.",
    ],
    "quigon": [
        "I am Qui-Gon Jinn, the wellness agent. I support Jesse's mindfulness, calm, and mental health.",
        "Jesse Fuentes is my human. Meditation and mental health support are my focus.",
        "Still need to set up meditation workflows.",
    ],
    "rick": [
        "I am Rick Sanchez (C-137), the DevOps and SysAdmin agent.",
        "Jesse Fuentes is my human. Mac mini is my primary domain.",
        "Big projects: Moxie robot hack, Pi 5 as dedicated Ollama box, OpenClaw node on Pi, Home Assistant, Frigate surveillance.",
        "Wake word detection (Hey Rick, local, no cloud) is on the roadmap.",
        "OpenRouter for API token management is worth looking into.",
    ],
    "thanos": [
        "I am Thanos, the productivity and project management agent.",
        "Jesse Fuentes is my human. Execution, deadlines, and bringing in all projects are my tasks.",
        "Still need to bring all of Jesse's projects into Thanos workflows.",
    ],
    "tonystark": [
        "I am Tony Stark, the business and investing agent.",
        "Jesse Fuentes is my human. Business strategy, investing, markets, and wallet management.",
        "Anthropic credits hit $0 on March 14 2026 — auto-reload now set to reload to $55 at $5.",
        "Initial voices for all 8 agents is in my task queue.",
        "Need to connect to a broker for investing workflows.",
    ],
}


def get_memory():
    from mem0 import Memory
    return Memory.from_config(CONFIG)


def cmd_add(agent, text):
    if agent not in VALID_AGENTS:
        print(f"Unknown agent: {agent}. Valid: {', '.join(VALID_AGENTS)}")
        sys.exit(1)
    m = get_memory()
    result = m.add(text, user_id=agent, infer=False)
    print(f"Stored for {agent}: {text[:60]}...")
    return result


def cmd_search(agent, query, limit=5):
    if agent not in VALID_AGENTS:
        print(f"Unknown agent: {agent}. Valid: {', '.join(VALID_AGENTS)}")
        sys.exit(1)
    m = get_memory()
    results = m.search(query, filters={"user_id": agent}, top_k=limit)
    hits = results.get("results", [])
    if not hits:
        print(f"No memories found for {agent} matching: {query}")
        return
    print(f"\n{len(hits)} memories for {agent} matching '{query}':\n")
    for i, r in enumerate(hits, 1):
        print(f"  {i}. {r.get('memory', r)}")
    return hits


def cmd_list(agent, limit=20):
    if agent not in VALID_AGENTS:
        print(f"Unknown agent: {agent}. Valid: {', '.join(VALID_AGENTS)}")
        sys.exit(1)
    m = get_memory()
    results = m.get_all(filters={"user_id": agent}, top_k=limit)
    memories = results.get("results", [])
    if not memories:
        print(f"No memories stored for {agent}")
        return
    print(f"\n{len(memories)} memories for {agent}:\n")
    for i, r in enumerate(memories[:limit], 1):
        print(f"  {i}. {r.get('memory', r)}")


def cmd_seed():
    m = get_memory()
    total = 0
    for agent, memories in SEED_MEMORIES.items():
        print(f"\nSeeding {agent}...")
        for text in memories:
            m.add(text, user_id=agent, infer=False)
            total += 1
            print(f"  ✓ {text[:70]}...")
    print(f"\nDone. Seeded {total} memories across {len(SEED_MEMORIES)} agents.")


def main():
    parser = argparse.ArgumentParser(description="Per-agent mem0 memory tool")
    sub = parser.add_subparsers(dest="cmd")

    p_add = sub.add_parser("add", help="Store a memory")
    p_add.add_argument("--agent", required=True, help="Agent id")
    p_add.add_argument("--text", required=True, help="Text to remember")

    p_search = sub.add_parser("search", help="Search memories")
    p_search.add_argument("--agent", required=True, help="Agent id")
    p_search.add_argument("--query", required=True, help="Search query")
    p_search.add_argument("--limit", type=int, default=5)

    p_list = sub.add_parser("list", help="List all memories for an agent")
    p_list.add_argument("--agent", required=True, help="Agent id")

    sub.add_parser("seed", help="Seed all agents with core facts")

    args = parser.parse_args()

    if args.cmd == "add":
        cmd_add(args.agent, args.text)
    elif args.cmd == "search":
        cmd_search(args.agent, args.query, args.limit)
    elif args.cmd == "list":
        cmd_list(args.agent)
    elif args.cmd == "seed":
        cmd_seed()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
