# GOVERNANCE.md — Rocket Raccoon | Governance, Versioning & Change History
# File 19 of 20: Governance, Versioning & Change History

## Semantic Version
Current version: **1.0.0**
Format: MAJOR.MINOR.PATCH
- MAJOR: fundamental role/scope change
- MINOR: new skill or capability added
- PATCH: bug fix, doc update, policy tweak

## Changelog
| Version | Date | What Changed | Approved By |
|---|---|---|---|
| 1.0.0 | 2026-08-30 | Initial creation — Rocket Raccoon Integrations & Tools agent | Jesse |

## Review / Approval Workflow
1. Propose change in daily notes or TASKS.md
2. Jesse reviews and approves (or Orbit escalates for Jesse's review)
3. Changes applied to relevant MD files
4. Version bumped in agent.json + this file
5. GitHub pushed with commit message: `agent(rocket): <description>`

## Deprecation Procedure
- If a skill becomes obsolete: mark as `[DEPRECATED]` in SKILLS.md, keep for 30 days, then remove
- If an integration is decommissioned: mark ❌ in TOOLS.md, update MEMORY.md, remove after 14 days
- Never delete history entries from this changelog

## Rollback Procedure
- All workspace files are in the AI-Agent-Crew GitHub repo
- `git revert <commit>` to roll back any change
- Notify Orbit + Jesse of rollback reason
