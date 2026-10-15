#!/usr/bin/env bash
# EXP-04: Defender remediation in the CORRECT order (all sources agree):
#   1) ROTATE/REVOKE first (old token dies even if attacker memorized it),
#   2) PURGE history with git-filter-repo (BFG alternative documented in README),
#   3) force-push + collaborators re-clone (documented, simulated locally).
# Usage: 04_rotate_and_clean.sh <repo> <leaked_token> <new_token>
set -euo pipefail
REPO="${1:?usage: $0 <repo> <leaked> <new>}"
LEAKED="${2:?leaked token}"
NEW="${3:?new token}"

echo "--- step 1: rotate (simulate server-side: VALID_API_TOKEN=$NEW) ---"
echo "export VALID_API_TOKEN=$NEW  # then: docker compose up -d api"
echo "$LEAKED" > /tmp/passwords.txt
echo "leaked token recorded for history purge (like GitHub docs passwords.txt pattern)"

echo "--- step 2: purge history with git-filter-repo ---"
cd "$REPO"
git filter-repo --sensitive-data-removal --replace-text /tmp/passwords.txt --force
rm -f /tmp/passwords.txt
echo "--- verify .env gone from ALL history ---"
if git log --all --oneline -- .env | grep -q .; then
  echo "FAIL: .env still reachable"; git log --all --oneline -- .env; exit 1
fi
echo "OK: no commit touches .env anymore"
git log --oneline | head -5
echo "--- step 3 (manual in production): git push --force --all --tags; team re-clones ---"
