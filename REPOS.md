# REPOS.md — Integrated Tool Repos

Cloned and installed into the workspace. Virtual env at `.venv/`.

Activate: `source .venv/bin/activate`

---

## 🧠 mem0 — Agent Memory
**Repo:** `repos/mem0/` | **Package:** `mem0ai`
**Purpose:** Token-efficient persistent memory for all 8 agents.
Stores facts, retrieves only what's relevant — massive token savings vs. dumping full history.

**Our script:** `tools/memory_store.py`
```bash
# Store a memory for an agent
python3 tools/memory_store.py add --agent orbit --text "Jesse prefers Vim over nano"

# Search memories
python3 tools/memory_store.py search --agent orbit --query "editor preferences"

# List all memories for an agent
python3 tools/memory_store.py list --agent greenlantern
```
**Config note:** Set `MEM0_USE_OLLAMA=1` to use local Ollama (free, no API key).
Default uses OpenAI embeddings (requires `OPENAI_API_KEY`).
Local mem0 DB stored at: `~/.openclaw/mem0_db/`

---

## 🔥 Firecrawl — Web Scraper (JS-heavy, full sites)
**Repo:** `repos/firecrawl/` | **Package:** `firecrawl-py`
**Purpose:** Scrape any URL including JS-heavy pages, SPAs, PDFs. Returns clean Markdown/JSON.
96% web coverage. Self-hosting needs Docker; cloud API has free tier.

**Our script:** `tools/scrape.py` (shared with newspaper3k)
```bash
# Auto-pick best method
python3 tools/scrape.py https://example.com

# Force firecrawl (needs FIRECRAWL_API_KEY)
FIRECRAWL_API_KEY=your_key python3 tools/scrape.py https://example.com --method firecrawl

# Output as JSON
python3 tools/scrape.py https://example.com --output json
```
**Get free API key:** https://firecrawl.dev (no credit card for free tier)

---

## 📰 newspaper3k — Article Scraper (lightweight, free)
**Repo:** `repos/newspaper/` | **Package:** `newspaper3k`
**Purpose:** Extract clean text from news articles and blogs. No API key, runs fully local.

**Our script:** `tools/scrape.py` (same script, auto-tries newspaper first)
```bash
# Force newspaper3k method
python3 tools/scrape.py https://techcrunch.com/some-article --method newspaper

# Get structured JSON output
python3 tools/scrape.py https://techcrunch.com/some-article --output json
```

---

## 📊 LiteLLM — Token Tracker & LLM Gateway
**Repo:** `repos/litellm/` | **Package:** `litellm`
**Purpose:** Count tokens before sending, estimate costs, normalize calls across all LLM providers.

**Our script:** `tools/token_tracker.py`
```bash
# Count tokens in text
python3 tools/token_tracker.py count --model claude-sonnet-4-6 --text "your text here"

# Count tokens in a file
python3 tools/token_tracker.py count --model claude-sonnet-4-6 --file myfile.txt

# Estimate cost
python3 tools/token_tracker.py cost --model claude-sonnet-4-6 --input 5000 --output 1000

# Pipe text in
cat bigfile.txt | python3 tools/token_tracker.py count --model gpt-4o --stdin
```

---

## Agent Integration

All 8 agents can use these tools. When Orbit or any agent needs to:

| Task | Use |
|---|---|
| Scrape a URL for context | `tools/scrape.py <url>` |
| Remember something across sessions | `tools/memory_store.py add` |
| Check memory before answering | `tools/memory_store.py search` |
| Count tokens before a big request | `tools/token_tracker.py count` |
| Estimate cost of a call | `tools/token_tracker.py cost` |

---

## Setup Checklist

- [x] Repos cloned to `repos/`
- [x] Python packages installed in `.venv/`
- [x] Integration scripts in `tools/`
- [ ] `FIRECRAWL_API_KEY` — get free key at firecrawl.dev for JS-heavy scraping
- [ ] `MEM0_USE_OLLAMA=1` — set to use local Ollama embeddings (recommended for free usage)
- [ ] Run `python3 tools/memory_store.py add --agent orbit --text "test"` to initialize mem0 DB
