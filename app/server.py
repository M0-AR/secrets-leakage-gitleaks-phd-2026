"""Fake DefinitelySecure-like customer API (lab only, no real data).

Reproduces the video's attacker step: curl with
`Authorization: Bearer <token>` against an internal customer endpoint.
The valid token is read from VALID_API_TOKEN env so rotation can be
demonstrated without code changes — exactly the remediation order the
GitHub + GitGuardian + OWASP sources mandate: revoke/rotate FIRST,
history purge SECOND.
"""
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

CUSTOMERS = [
    {"customer_id": "C-1001", "company": "Acme Robotics", "employees": 240, "plan": "enterprise"},
    {"customer_id": "C-1002", "company": "Northwind AI", "employees": 85, "plan": "team"},
    {"customer_id": "C-1003", "company": "Contoso Labs", "employees": 1320, "plan": "enterprise"},
]


def current_valid_token() -> str:
    return os.environ.get("VALID_API_TOKEN", "ds_live_leaked_demo_token_2026_ROTATE_ME")


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/api/customers")
def customers():
    auth = request.headers.get("Authorization", "")
    expected = f"Bearer {current_valid_token()}"
    if auth != expected:
        return jsonify(error="unauthorized", hint="valid bearer token required"), 401
    return jsonify(api="internal-customer-api", count=len(CUSTOMERS), customers=CUSTOMERS)


if __name__ == "__main__":
    port = int(os.environ.get("API_PORT", "8042"))
    app.run(host="0.0.0.0", port=port)
