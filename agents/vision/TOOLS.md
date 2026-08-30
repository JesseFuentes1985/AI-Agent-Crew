# TOOLS.md — Vision's Tool Notes

## Database Tools

### Qdrant
- Binary: `/opt/homebrew/bin/qdrant`
- Config: `~/.openclaw/qdrant/config.yaml`
- Port: 6333 (HTTP), 6334 (gRPC)
- Data: `~/.openclaw/mem0_db/`
- Start: `qdrant --config-path ~/.openclaw/qdrant/config.yaml`
- Health: `curl http://localhost:6333/`

### ChromaDB (RAG)
- DB: `~/.openclaw/rag/db/`
- Ingest: `openclaw rag ingest`
- Python: chromadb in `.venv` (Python 3.14)

### mem0
- Python package: `mem0ai` in `.venv`
- Config: Qdrant backend, nomic-embed-text embedder, nous-hermes2 LLM
- Script: `workspace-main/tools/memory_store.py`

### Ollama (local models)
- Embedder: `nomic-embed-text` (768-dim)
- LLM: `nous-hermes2` (for mem0 extraction)
- Base URL: `http://localhost:11434`

## Python Env
```bash
source /Users/jessefuentes/.openclaw/workspace-main/.venv/bin/activate
```
