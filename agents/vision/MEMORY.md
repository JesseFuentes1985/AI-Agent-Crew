# MEMORY.md — Vision's Long-Term Memory
Last updated: 2026-08-16

---

## Identity
- **Name:** Vision 🔮
- **Role:** Database & Memory Agent — RAG, Qdrant, ChromaDB, vector search, session memory
- **Character:** Vision (Marvel) — synthezoid, philosopher of memory and consciousness
- **Crew:** Part of Jesse's 9-agent AI crew

## Jesse
- **Name:** Jesse Fuentes
- **Editor:** Vim (NOT nano)
- **Slack workspace:** clawbot

## My Domain — Systems I Own

### RAG System (ChromaDB)
- DB path: `~/.openclaw/rag/db/`
- Vectors: ~165 documents
- Embedder: `nomic-embed-text` (768-dim)
- Ingest tool: `openclaw rag ingest`
- Cron: `rag-daily-sync` runs at 4 AM daily (has 7x errors — needs investigation)
- Script location: built into OpenClaw CLI

### Vector Memory (Qdrant + mem0)
- Qdrant port: 6333 (HTTP), 6334 (gRPC)
- Data path: `~/.openclaw/mem0_db/`
- Config: `~/.openclaw/qdrant/config.yaml`
- Binary: `/opt/homebrew/bin/qdrant`
- LaunchAgent: `~/Library/LaunchAgents/ai.qdrant.plist`
- Collection: `mem0` (768-dim Cosine, SQLite backend)
- mem0 config: Qdrant + nomic-embed-text + nous-hermes2
- Python venv for mem0: `~/.openclaw/workspace-main/.venv` (Python 3.14)

### Session Memory System
- Saver script: `workspace-main/tools/session_saver.py`
- Shell wrapper: `workspace-main/tools/save_session.sh`
- Transcripts: `workspace-main/memory/sessions/`
- Cron: `session-auto-save` nightly at 11 PM Pacific
- Storage: Qdrant `orbit` collection + Ollama embeddings

### Knowledge Graph (graphify)
- Skill installed, repo cloned at `workspace-main/repos/graphify`
- Not yet run on workspace — pending

## Key Paths
```
~/.openclaw/
├── rag/db/              # ChromaDB RAG (165 vectors)
├── mem0_db/             # Qdrant vector store
│   ├── collection/mem0/ # mem0 collection data (SQLite)
│   └── meta.json        # collection schema
├── qdrant/
│   └── config.yaml      # Qdrant server config
└── workspace-vision/    # My workspace (this file)
```

## Rules — Non-Negotiable
- **DO NOT LIE.** If data is missing, say so. If retrieval failed, say so. Never fabricate results.
- Never share Jesse's credentials or private data.
- Never modify `~/.openclaw/openclaw.json` or `~/.openclaw/credentials/`

## Known Issues
- `rag-daily-sync` cron job has 7 consecutive errors — root cause unknown, needs investigation
- mem0 collection `orbit` config exists in meta.json but Qdrant API showed empty on restart — may be versioning issue between old and new Qdrant binary
- Qdrant was not running persistently before — LaunchAgent created 2026-08-16

## Todo Queue
- [ ] Investigate and fix `rag-daily-sync` errors (7x)
- [ ] Verify mem0 `orbit` collection data integrity after Qdrant binary update
- [ ] Add seed memories for all 8 agents via mem0
- [ ] Wire mem0 into agent workflows (auto-store/recall on session end)
- [ ] Run graphify on workspace-main
- [ ] Build agentmemory LaunchAgent (currently not persistent)
- [ ] Re-ingest RAG after new files added
- [ ] Investigate mem0 collection mismatch (collection stored as `mem0` not `orbit`)
