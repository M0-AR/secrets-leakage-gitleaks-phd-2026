"""Benchmark matrix grounded ONLY in retrieved 2026 evidence (no invented numbers).

Sources (see evidence/SEARCH_LOG.md):
- Basak et al. ESEM 2023 (arxiv 2307.00714, 41 cites): precision GitHubScanner 75%,
  Gitleaks 46%, Commercial X 25%; recall Gitleaks 88%, SpectralOps 67%, TruffleHog 52%.
- SecretBench (MSR 2023): 97,479 secrets, 15,084 true, 818 repos, 49 langs, 311 types.
- devsecops.ae 2026 + Pickuma 2026 + OWASP guideline: 4-gate model, Gitleaks
  sub-second pre-commit, TruffleHog 700+ verifiers, GitGuardian FP 1-3%.
- FTC filings: 2014 ~100k drivers, 2016 57M users (25.6M emails, 22.1M phones,
  607k licenses), $148M settlement (largest AG privacy settlement), 20-yr order.
"""
import json

MATRIX = {
    "precision": {"github_secret_scanning": 0.75, "gitleaks": 0.46, "commercial_x": 0.25},
    "recall": {"gitleaks": 0.88, "spectralops": 0.67, "trufflehog": 0.52},
    "secretbench": {"total": 97479, "true": 15084, "repos": 818, "langs": 49, "file_types": 311},
    "four_gates": ["pre-commit", "ci_diff", "history_scan", "platform_monitoring"],
    "ftc": {"breach_2014_drivers": 100000, "breach_2016_total": 57000000,
            "settlement_usd": 148_000_000, "order_years": 20},
}

def hidden_patterns():
    """Candidate PhD contributions derived from cross-source voting."""
    return [
        "H1 deletion-erasure gap: removing .env from HEAD leaves commit reachable; "
        "gitleaks git (git log -p) still fires — the video's core misconception, confirmed by GitHub docs.",
        "H2 rotation-dominance: purge without revoke = clean-looking breach; all 5 remediation "
        "sources order revoke FIRST. Quantify exposure window = discovery_time - commit_time.",
        "H3 verifier economics: TruffleHog --only-verified collapses triage (case: 4000 alerts -> 137 live). "
        "Recall leaders (Gitleaks 88%) need verifier second stage to fix precision (46%).",
        "H4 stale-secret half-life: Capalbo 2026 thesis gap — keys persist in history/forks/caches; "
        "measure time-to-rotation vs. time-to-purge across SecretBench repos.",
        "H5 chain pattern (Uber 2016): credential-stuffing -> private GitHub -> AWS key (2013, unrotated) "
        "-> S3 cleartext backup. Each link had a cheap control (MFA, distinct keys, encryption, rotation).",
    ]

if __name__ == "__main__":
    print(json.dumps(MATRIX, indent=2))
    print("\nHIDDEN PATTERNS (PhD candidates):")
    for h in hidden_patterns():
        print(" -", h)
