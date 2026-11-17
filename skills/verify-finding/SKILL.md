---
name: verify-finding
description: Verify ShieldLog finding create/edit forms and dashboard counts after UI or route changes.
---

# Verify finding workflow

Use this skill after changing finding forms, routes, or dashboard stats.

## Steps
1. Start the app with `python run.py` if it is not running.
2. Open `http://127.0.0.1:5000`.
3. Confirm dashboard counters render (Total / Open / Investigating / Resolved / High-Critical).
4. Create a finding with:
   - title: `Skill check phishing report`
   - category: `phishing`
   - severity: `high`
   - status: `open`
5. Open the detail page and confirm fields match.
6. Edit status to `investigating`, save, confirm badge updates.
7. Delete the test finding if it was only for verification.
8. Report pass/fail with any missing fields or broken links.

## Fail conditions
- Create form accepts empty title
- Severity/status badges missing on dashboard
- Delete does not return to dashboard
- Flash messages never appear after write actions
