# ShieldLog

Small **defensive cybersecurity** web app for logging and triaging security findings (phishing reports, misconfigurations, access alerts, and more).

Built as a Claude Code / agentic-workflow course submission. Stack is Python (Flask) + SQLite instead of PHP/Laravel.

## How to run

```powershell
cd shieldlog-course-project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000).

Sample findings are seeded on first launch.

## Features

| Feature | Status |
|---------|--------|
| Dashboard with summary counts | Done |
| Create / view / edit / delete findings | Done |
| Categories, severity, status | Done |
| SQLite persistence + seed data | Done |
| Data model doc | Done (`docs/DATA_MODEL.md`) |
| CLAUDE.md project rules | Done |
| Status filter on dashboard | Not done (good parallel-branch task) |
| User auth / multi-tenant | Not done |
| Attachments / evidence upload | Not done |
| Email / Slack alerts | Not done |

## Agentic tools used (and where)

| Tool | Location / usage |
|------|------------------|
| **CLAUDE.md** (project rules) | `/CLAUDE.md` — commands, scope, verify rules |
| **Skill** | `skills/verify-finding/SKILL.md` — post-change UI verification checklist |
| **Hook** | `.cursor/hooks/pre-commit-checklist.sh` — required files + secret-file guard |
| **Plan → implement → verify** | Documented in `docs/AGENTIC_WORKFLOW.md` |
| **Parallel work** | Documented in `docs/AGENTIC_WORKFLOW.md` (status-filters + ui-polish branches) |
| **MCP / Playwright** | Optional — use for browser UI checks against localhost:5000 |

## Project layout

```
shieldlog-course-project/
├── CLAUDE.md
├── README.md
├── run.py
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── templates/
├── static/
├── docs/
│   ├── DATA_MODEL.md
│   └── AGENTIC_WORKFLOW.md
├── skills/verify-finding/SKILL.md
└── .cursor/hooks/pre-commit-checklist.sh
```

## Screenshots / recording

Add screenshots or a 2–5 minute screen recording here (or upload them separately on the LMS):

- Dashboard with seeded findings
- Create finding form
- Finding detail + status update

## Safety note

This is a **defensive intake tracker** for learning. It does not scan networks, exploit systems, or collect external attack data.
