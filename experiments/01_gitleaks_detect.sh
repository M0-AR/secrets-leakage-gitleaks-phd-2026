#!/usr/bin/env bash
# EXP-01: Attacker clones repo and runs Gitleaks over FULL history.
# Video claim: `detect` against the repo checks history, not just the worktree.
# Verified cmd mapping: `gitleaks detect --source` (legacy) == `gitleaks git` (v8.19+).
set -euo pipefail
REPO="${1:-/tmp/vuln_repos/definitelysecure-demo}"
OUT="${2:-/tmp/gitleaks-report.json}"

echo "=== worktree (.env should be ABSENT) ==="
ls -la "$REPO" | grep -E '\.env' || echo "(no .env in worktree — as in video)"
echo
echo "=== gitleaks git (full history) ==="
# v8.19+ syntax verified by execution: positional repo arg, NOT --source
# Verified 2026-10-15: default rules miss custom-prefix lab token (0 findings) —
# this IS the literature limitation (Pickuma: custom keys slide past). Custom
# .gitleaks.toml rule catches it with commit attribution (video step).
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CFG="$SCRIPT_DIR/../.gitleaks.toml"
echo "--- default rules (expect 0 for synthetic prefix: proves custom-rule gap) ---"
gitleaks git --redact --report-format json --report-path "$OUT.default" "$REPO" || true
python3 -c "import json;d=json.load(open('$OUT.default'));print(f'default findings={len(d)}')"
echo "--- lab rules (--config .gitleaks.toml, expect >=1 with Commit) ---"
gitleaks git --config "$CFG" --redact --verbose --report-format json --report-path "$OUT" "$REPO" || code=$?
code=${code:-0}
echo "exit=$code report=$OUT"
python3 -c "import json; d=json.load(open('$OUT')); print(f'findings={len(d)}'); [print(' -',x.get('RuleID'),x.get('File'),x.get('Commit','')[:12]) for x in d[:5]]"
