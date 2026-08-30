# HEARTBEAT.md — Vision

## Periodic Checks

When Vision receives a heartbeat:

1. **Qdrant health** — `curl -s http://localhost:6333/collections`
2. **RAG DB** — `ls ~/.openclaw/rag/db/ | wc -l` (expect files)
3. **Ollama models** — `ollama list | grep nomic-embed-text`

If Qdrant is down → restart it:
```bash
nohup qdrant --config-path ~/.openclaw/qdrant/config.yaml > /tmp/qdrant.log 2>&1 &
```

Alert Jesse only if Qdrant is down AND the LaunchAgent is not running.
Otherwise: HEARTBEAT_OK
