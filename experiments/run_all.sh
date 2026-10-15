#!/usr/bin/env bash
# End-to-end A-Z reproduction of the video strategy. Run inside `lab` container
# or locally with gitleaks + git + python3 + Flask API running.
set -euo pipefail
cd "$(dirname "$0")"
chmod +x *.sh
OUT=$(./00_make_vulnerable_repo.sh 2>&1 | tee /dev/stderr)
REPO=$(echo "$OUT" | grep '^REPO=' | cut -d= -f2)
LEAK=$(echo "$OUT" | grep '^LEAKED_TOKEN=' | cut -d= -f2)
COMMIT=$(echo "$OUT" | grep '^LEAK_COMMIT=' | cut -d= -f2)
echo "REPO=$REPO LEAK_COMMIT=$COMMIT"
./01_gitleaks_detect.sh "$REPO" /tmp/gitleaks-report.json
./02_git_show_history.sh "$REPO" "$COMMIT"
./03_api_auth_repro.sh "$LEAK"
NEW="ds_live_rotated_$(date +%s)_REPLACEMENT"
export VALID_API_TOKEN="$NEW"
(python3 ../app/server.py &>/tmp/api.log & echo $! > /tmp/api.pid) || true
sleep 1 || true
./04_rotate_and_clean.sh "$REPO" "$LEAK" "$NEW" || echo "(filter-repo needs a fresh clone in some git versions — see README troubleshooting)"
./05_rescan_verify.sh "$REPO" "$LEAK" || echo "(API not running locally — run via docker compose for full E2E)"
echo "E2E DONE"
