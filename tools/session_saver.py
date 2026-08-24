#!/usr/bin/env python3
"""
session_saver.py — Save session conversations into mem0 (Ollama + Qdrant)

How it works:
  1. Takes a session history JSON (from OpenClaw sessions_history API)
  2. Extracts user/assistant messages into a clean transcript
  3. Asks Ollama (hermes/mistral) to summarize + extract key facts
  4. Stores facts in mem0 (Qdrant vector DB with nomic-embed-text embeddings)
  5. Saves full transcript to memory/sessions/YYYY-MM-DD-<label>.md

Usage:
  python3 tools/session_saver.py --file /tmp/session.json --agent orbit --label "memory-system-design"
  python3 tools/session_saver.py --file /tmp/session.json  # uses orbit + auto date label
  cat session.json | python3 tools/session_saver.py --stdin --agent orbit

Query later:
  python3 tools/session_saver.py --recall "what did we discuss about memory"
  python3 tools/session_saver.py --recall "Ollama session system" --agent orbit
"""

import argparse
import json
import os
import re
import sys
import datetime
import requests
from pathlib import Path

# ── Config ──────────────────────────────────────────────────────────────────

WORKSPACE = Path(__file__).parent.parent
SESSIONS_DIR = WORKSPACE / "memory" / "sessions"
MEM0_DB = os.path.expanduser("~/.openclaw/mem0_db")
OLLAMA_URL = "http://localhost:11434"
SUMMARIZE_MODEL = "nous-hermes2"   # local, no API key
EXTRACT_MODEL = "nous-hermes2"

MEM0_CONFIG = {
    "llm": {
        "provider": "ollama",
        "config": {"model": SUMMARIZE_MODEL, "ollama_base_url": OLLAMA_URL}
    },
    "embedder": {
        "provider": "ollama",
        "config": {"model": "nomic-embed-text", "ollama_base_url": OLLAMA_URL}
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {"path": MEM0_DB, "embedding_model_dims": 768}
    }
}

VALID_AGENTS = ["orbit", "baymax", "beast", "greenlantern", "quigon", "rick", "thanos", "tonystark"]


# ── Ollama helpers ───────────────────────────────────────────────────────────

def ollama_generate(prompt: str, model: str = SUMMARIZE_MODEL) -> str:
    """Call Ollama generate endpoint. Returns response text."""
    try:
        resp = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=120
        )
        resp.raise_for_status()
        return resp.json().get("response", "").strip()
    except Exception as e:
        print(f"[!] Ollama error: {e}", file=sys.stderr)
        return ""


def check_ollama() -> bool:
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        return r.status_code == 200
    except Exception:
        return False


# ── Session parsing ──────────────────────────────────────────────────────────

def parse_session(data: dict) -> list[dict]:
    """Extract clean user/assistant turns from OpenClaw session history JSON."""
    messages = data.get("messages", [])
    turns = []
    for msg in messages:
        role = msg.get("role", "")
        content = msg.get("content", "")

        # content can be string or list of blocks
        if isinstance(content, list):
            text_parts = []
            for block in content:
                if isinstance(block, dict):
                    if block.get("type") == "text":
                        text_parts.append(block.get("text", ""))
                    # skip toolCall, thinking, attachment blocks
            content = " ".join(text_parts).strip()

        if role in ("user", "assistant") and content:
            turns.append({"role": role, "content": content})

    return turns


def build_transcript(turns: list[dict], label: str = "", session_key: str = "") -> str:
    """Build a readable markdown transcript."""
    lines = [f"# Session Transcript", ""]
    if label:
        lines.append(f"**Label:** {label}")
    if session_key:
        lines.append(f"**Session:** {session_key}")
    lines.append(f"**Saved:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("---")
    lines.append("")

    for turn in turns:
        prefix = "**Jesse:**" if turn["role"] == "user" else "**Orbit:**"
        lines.append(f"{prefix} {turn['content']}")
        lines.append("")

    return "\n".join(lines)


# ── Summarization & extraction ───────────────────────────────────────────────

def summarize_session(turns: list[dict]) -> str:
    """Ask Ollama to write a brief summary of the session."""
    if not turns:
        return ""

    transcript_text = "\n".join(
        f"{'Jesse' if t['role'] == 'user' else 'Orbit'}: {t['content']}"
        for t in turns
    )

    prompt = f"""You are summarizing a conversation between Jesse (human) and Orbit (AI assistant).
Write a 2-3 sentence summary of what this conversation was about.
Be factual and specific. No fluff.

Conversation:
{transcript_text[:4000]}

Summary:"""

    return ollama_generate(prompt)


def extract_facts(turns: list[dict]) -> list[str]:
    """Ask Ollama to extract memorable facts/decisions from the session."""
    if not turns:
        return []

    transcript_text = "\n".join(
        f"{'Jesse' if t['role'] == 'user' else 'Orbit'}: {t['content']}"
        for t in turns
    )

    prompt = f"""You are extracting key facts from a conversation between Jesse and his AI assistant Orbit.
Extract important facts, decisions, plans, or context that should be remembered for future sessions.
Output ONLY a JSON array of strings, one fact per string. No explanation, no markdown, just valid JSON.
Each fact should be a complete, standalone sentence.
Limit to the 8 most important facts.

Conversation:
{transcript_text[:4000]}

JSON array:"""

    raw = ollama_generate(prompt)

    # Try to parse JSON from response
    try:
        # Find JSON array in response
        match = re.search(r'\[.*?\]', raw, re.DOTALL)
        if match:
            return json.loads(match.group())
    except Exception:
        pass

    # Fallback: split by newlines and clean up
    lines = [l.strip().strip('"-,[]') for l in raw.split('\n') if l.strip() and l.strip() not in ('[]', '""')]
    return [l for l in lines if len(l) > 10][:8]


# ── mem0 storage ─────────────────────────────────────────────────────────────

def store_in_mem0(facts: list[str], summary: str, agent: str, label: str = "") -> int:
    """Store facts + summary in mem0 vector store. Returns count stored."""
    try:
        from mem0 import Memory
        m = Memory.from_config(MEM0_CONFIG)

        stored = 0
        tag = f"[session:{label}] " if label else "[session] "

        # Store summary
        if summary:
            m.add(f"{tag}Session summary: {summary}", user_id=agent, infer=False)
            stored += 1

        # Store each fact
        for fact in facts:
            if fact:
                m.add(f"{tag}{fact}", user_id=agent, infer=False)
                stored += 1

        return stored
    except Exception as e:
        print(f"[!] mem0 error: {e}", file=sys.stderr)
        return 0


def recall_from_mem0(query: str, agent: str, limit: int = 8) -> list[str]:
    """Search mem0 for memories relevant to query."""
    try:
        from mem0 import Memory
        m = Memory.from_config(MEM0_CONFIG)
        results = m.search(query, filters={"user_id": agent}, top_k=limit)
        return [r.get("memory", "") for r in results.get("results", []) if r.get("memory")]
    except Exception as e:
        print(f"[!] mem0 recall error: {e}", file=sys.stderr)
        return []


# ── Save transcript to disk ───────────────────────────────────────────────────

def save_transcript(transcript: str, label: str) -> Path:
    """Write transcript markdown to memory/sessions/."""
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    safe_label = re.sub(r'[^a-zA-Z0-9_-]', '-', label)[:40] if label else "session"
    filename = f"{date_str}-{safe_label}.md"
    path = SESSIONS_DIR / filename
    path.write_text(transcript)
    return path


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Save OpenClaw session conversations into mem0 (Ollama + Qdrant)"
    )
    parser.add_argument("--file", "-f", help="Path to session history JSON file")
    parser.add_argument("--stdin", action="store_true", help="Read session JSON from stdin")
    parser.add_argument("--agent", default="orbit", help="Agent id (default: orbit)")
    parser.add_argument("--label", default="", help="Human-readable label for this session")
    parser.add_argument("--session-key", default="", help="OpenClaw session key")
    parser.add_argument("--no-mem0", action="store_true", help="Skip mem0 storage, just save transcript")
    parser.add_argument("--recall", metavar="QUERY", help="Search mem0 for memories matching query")
    parser.add_argument("--limit", type=int, default=8, help="Max recall results (default: 8)")
    args = parser.parse_args()

    # ── Recall mode ─────────────────────────────────────────────────────────
    if args.recall:
        agent = args.agent if args.agent in VALID_AGENTS else "orbit"
        print(f"\n🔍 Searching mem0 for '{args.recall}' (agent: {agent})...\n")
        results = recall_from_mem0(args.recall, agent, args.limit)
        if not results:
            print("No matching memories found.")
        else:
            print(f"Found {len(results)} memories:\n")
            for i, mem in enumerate(results, 1):
                print(f"  {i}. {mem}")
        return

    # ── Save mode ────────────────────────────────────────────────────────────
    if not args.file and not args.stdin:
        parser.print_help()
        sys.exit(1)

    # Read session JSON
    if args.stdin:
        raw = sys.stdin.read()
    else:
        raw = Path(args.file).read_text()

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"[!] Failed to parse session JSON: {e}", file=sys.stderr)
        sys.exit(1)

    agent = args.agent if args.agent in VALID_AGENTS else "orbit"
    label = args.label or (data.get("sessionKey", "").replace(":", "-") or "session")

    print(f"\n📋 Processing session: {label} (agent: {agent})")

    # Parse messages
    turns = parse_session(data)
    if not turns:
        print("[!] No readable messages found in session data.")
        sys.exit(1)

    print(f"   → {len(turns)} turns extracted")

    # Save transcript to disk
    transcript = build_transcript(turns, label=label, session_key=data.get("sessionKey", ""))
    transcript_path = save_transcript(transcript, label)
    print(f"   → Transcript saved: {transcript_path}")

    if args.no_mem0:
        print("\nDone (mem0 skipped).")
        return

    # Check Ollama
    if not check_ollama():
        print("[!] Ollama is not running. Transcript saved but skipping AI extraction.")
        return

    print(f"\n🤖 Summarizing with {SUMMARIZE_MODEL}...")
    summary = summarize_session(turns)
    if summary:
        print(f"   Summary: {summary[:120]}...")
    else:
        print("   [!] Summary generation failed or empty")

    print(f"\n🧠 Extracting key facts...")
    facts = extract_facts(turns)
    print(f"   → {len(facts)} facts extracted")
    for i, f in enumerate(facts, 1):
        print(f"      {i}. {f[:80]}")

    if not args.no_mem0:
        print(f"\n💾 Storing in mem0 (Qdrant + nomic-embed-text)...")
        stored = store_in_mem0(facts, summary, agent, label=label)
        print(f"   → {stored} memories stored for agent: {agent}")

    print(f"\n✅ Done!")
    print(f"   Transcript: {transcript_path}")
    if not args.no_mem0:
        print(f"   mem0: {stored} new memories embedded via Ollama")
    print(f"\nRecall later with:")
    print(f"   python3 tools/session_saver.py --recall \"your query\" --agent {agent}")


if __name__ == "__main__":
    main()
