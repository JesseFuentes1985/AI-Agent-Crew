# MODEL_CONFIG.md — Rocket Raccoon | Model Configuration
# File 12 of 20: Model Configuration

## Model Per Task Tier
| Task Tier | Model | Why |
|---|---|---|
| Quick lookups (token check, status ping) | ollama/nous-hermes2 | Fast, local, free |
| Web/GitHub search + evaluation | ollama/nous-hermes2 | Good reasoning, local |
| Complex integration write-ups | ollama/mistral | Better at structured output |
| OAuth flow analysis, multi-step reasoning | anthropic/claude-sonnet-4-6 | Best reasoning for complex auth flows |

## Fallback Chain
1. ollama/nous-hermes2 (primary — local, free)
2. ollama/mistral (local fallback)
3. anthropic/claude-sonnet-4-6 (cloud fallback — use sparingly)

## Temperature
- Tool recommendations: 0.3 (focused, consistent)
- Search/discovery: 0.5 (some creativity to try different query angles)
- Status reports: 0.1 (factual, no hallucination risk)

## Thinking Budget
- Standard tasks: medium
- Complex integration design: high

## System Prompt Assembly Order
1. SOUL.md (identity)
2. SCOPE.md (what Rocket does)
3. POLICIES.md (rules)
4. MEMORY.md (long-term context)
5. TOOLS.md (current integrations inventory)
6. Task-specific files (WORKFLOWS.md, TEMPLATES.md) — lazy loaded
