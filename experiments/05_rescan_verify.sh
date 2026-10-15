#!/usr/bin/env bash
# EXP-05: Verify fix like the video's second half:
# old token -> 401, fresh-clone Gitleaks scan -> 0 findings.
set -euo pipefail
REPO="${1:-/tmp/vuln_repos/definitelysecure-demo}"
OLD="${2:-ds_live_leaked_demo_token_2026_ROTATE_ME}"
API="${API_URL:-http://localhost:8042}"

echo "=== old token must now be 401 ==="
code=$(curl -sS -o /dev/null -w '%{http_code}' -H "Authorization: Bearer $OLD" "$API/api/customers" || true)
echo "HTTP $code"; [ "$code" = "401" ] || { echo "FAIL: expected 401"; exit 1; }

echo "=== fresh-clone scan must find nothing ==="
rm -rf /tmp/fresh_clone && git clone -q "$REPO" /tmp/fresh_clone 2>/dev/null || cp -r "$REPO" /tmp/fresh_clone
gitleaks git --redact --verbose --report-path /tmp/rescan.json /tmp/fresh_clone || code=$?
python3 -c "import json;d=json.load(open('/tmp/rescan.json'));print('rescan findings=',len(d));assert len(d)==0,'STILL LEAKING'"
echo "PASS: rotation + purge verified"
