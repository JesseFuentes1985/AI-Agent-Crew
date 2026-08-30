# RETRIEVAL.md — Rocket Raccoon | Retrieval Engineering
# File 10 of 20: Retrieval Engineering

## Corpora
| Corpus | What's in it | When to Query |
|---|---|---|
| workspace-rocket/MEMORY.md | Rocket's integration history | Always — check before researching |
| workspace-main/MEMORY.md | Crew-wide context | When cross-agent context needed |
| GitHub search (live) | Repos, MCP servers, SDKs | On any tool discovery task |
| Web search (live) | API docs, integration guides, news | When GitHub search is insufficient |
| awesome-mcp-servers list | Curated MCP server index | First stop for MCP discovery |
| clawhub / awesome-openclaw-skills | OpenClaw-specific plugins | Before any OpenClaw extension task |

## Query Construction
- MCP discovery: `"<service>" mcp server site:github.com` + `"<service>" "model context protocol"`
- Repo discovery: `<capability> python library github stars:>100`
- API docs: `<service> REST API documentation official`
- Always try 2–3 query variants before concluding nothing exists

## top-k & Relevance
- GitHub search: evaluate top 5, present top 3
- Web search: read top 3 results for synthesis
- Minimum threshold: repo must have >20 stars OR be official/verified publisher

## Empty / Low-Confidence Retrieval
- If nothing found after 3 query variants → report "nothing found, recommend building" with scope estimate
- If results are ambiguous → present options and ask Jesse for direction
- Never fabricate a repo or tool that wasn't found
