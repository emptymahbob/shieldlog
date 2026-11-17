# Agentic workflow evidence

This file documents how Claude Code / Cursor agentic tools were used while building ShieldLog.

## Tools used

| Tool | Where | Purpose |
|------|-------|---------|
| Project rules (`CLAUDE.md`) | repo root | Commands, stack, defensive scope rules |
| Skill | `skills/verify-finding/SKILL.md` | Checklist to verify create/edit/delete after changes |
| Hook | `.cursor/hooks/pre-commit-checklist.sh` | Pre-commit checklist for required files / secrets |
| Plan → implement → verify | each feature | Dashboard, CRUD forms, seed data |
| Parallel session (suggested) | branch `ui-polish` + `feature/status-filters` | UI CSS polish in parallel with a filter feature, then merge |

## Parallel work (do this before submit if you have time)
1. Create branch `feature/status-filters` and add a status filter dropdown on the dashboard.
2. In a second session/branch `ui-polish`, improve empty states / mobile spacing.
3. Merge both into `main` and fix any conflicts in `templates/dashboard.html`.

## MCP note
Playwright MCP (or browser tools) can be used for UI checks against `http://127.0.0.1:5000`. If you run those checks, mention them in the README “agentic tools” section.
