#!/usr/bin/env bash
# EXP-02: Recover the secret from history WITHOUT checking out the old commit.
# Video cmd: git show <commit>:.env — proves deletion != erasure.
set -euo pipefail
REPO="${1:-/tmp/vuln_repos/definitelysecure-demo}"
COMMIT="${2:-}"
if [ -z "$COMMIT" ]; then
  COMMIT=$(git -C "$REPO" log --diff-filter=A --format=%H -- .env | tail -1)
fi
echo "COMMIT=$COMMIT"
git -C "$REPO" show "$COMMIT:.env"
