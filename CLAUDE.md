# ShieldLog — Claude Code project guide

## What this is
ShieldLog is a small **defensive** security finding tracker. Analysts can log phishing reports, misconfigurations, access alerts, and similar findings, then update severity and status.

This project is intentionally small for a Claude Code course submission. Prefer simple, readable changes over new frameworks.

## Stack
- Python 3.10+
- Flask + Flask-SQLAlchemy
- SQLite (`shieldlog.db` created on first run)

## Commands
```bash
# Create venv (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install
pip install -r requirements.txt

# Run
python run.py
# App: http://127.0.0.1:5000
```

## Project rules
1. Keep the scope defensive: tracking/reporting findings only. No exploit code, scanners, or attack tooling.
2. Prefer plan → implement → verify for each feature.
3. After route or model changes, restart the app and click through create / edit / delete.
4. Do not commit secrets, API keys, or real incident data. Use sample findings only.
5. Keep UI templates in `templates/` and styles in `static/style.css`.
6. Update `docs/DATA_MODEL.md` if entities or relationships change.
7. Update README feature status when something is finished or deferred.

## Key paths
- `run.py` — entrypoint
- `app/models.py` — Finding entity
- `app/routes.py` — dashboard + CRUD
- `docs/DATA_MODEL.md` — data model
- `skills/verify-finding/SKILL.md` — agent skill for verifying a finding form
- `.cursor/hooks/pre-commit-checklist.sh` — lightweight hook checklist

## Agentic workflow notes
- Use a subagent/explore pass before large refactors.
- Use the `verify-finding` skill after UI form changes.
- Parallel work example: one branch for UI polish, one for model/status filters; merge cleanly into main.
