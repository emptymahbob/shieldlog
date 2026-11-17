#!/usr/bin/env bash
# Lightweight pre-commit checklist hook for ShieldLog (course demo).
# Intended as an agent/hook example — wire into your local git hooks if desired.

set -euo pipefail

echo "[shieldlog hook] Running pre-commit checklist..."

if [[ ! -f "CLAUDE.md" ]]; then
  echo "Missing CLAUDE.md"
  exit 1
fi

if [[ ! -f "docs/DATA_MODEL.md" ]]; then
  echo "Missing docs/DATA_MODEL.md"
  exit 1
fi

if [[ ! -f "requirements.txt" ]]; then
  echo "Missing requirements.txt"
  exit 1
fi

# Fail if obvious secret files are staged
if git diff --cached --name-only | grep -E '(\.env$|credentials\.json|id_rsa)' >/dev/null 2>&1; then
  echo "Refusing commit: secret-like file staged"
  exit 1
fi

echo "[shieldlog hook] Checklist passed."
