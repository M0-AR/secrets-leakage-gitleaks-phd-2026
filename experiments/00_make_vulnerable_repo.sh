#!/usr/bin/env bash
# EXP-00: Build a synthetic vulnerable repo from scratch (no cloning of any real repo).
# Reproduces the video premise: a company site + public GitHub repo where a .env
# with an API token was committed, then "deleted" in a later commit (history remains).
set -euo pipefail
ROOT="${1:-/tmp/vuln_repos}"
REPO="$ROOT/definitelysecure-demo"
LEAKED_TOKEN="ds_live_leaked_demo_token_2026_ROTATE_ME"

rm -rf "$REPO"
mkdir -p "$REPO"
cd "$REPO"
git init -q -b main
git config user.email "lab@example.local"
git config user.name "lab"

cat > README.md <<'EOF'
# DefinitelySecure (synthetic lab repo)
Security software for companies running AI workloads. Public mirror for research.
EOF

# Commit 1 (vulnerable): .env WITH the token, like the video's old commit.
cat > .env <<EOF
API_URL=https://api.definitelysecure.example
API_TOKEN=$LEAKED_TOKEN
EOF
git add README.md .env
git commit -qm "feat: initial website + api config"

# Commit 2 (the misconception): developer deletes .env in latest version.
git rm -q --cached .env
rm .env
cat > .env.example <<'EOF'
API_URL=
API_TOKEN=
EOF
git add -A
git commit -qm "chore: remove .env (token still in history!)"

LEAK_COMMIT=$(git log --diff-filter=A --format=%H -- .env | tail -1)
echo "REPO=$REPO"
echo "LEAK_COMMIT=$LEAK_COMMIT"
echo "LEAKED_TOKEN=$LEAKED_TOKEN"
echo "git log --oneline:"
git log --oneline
