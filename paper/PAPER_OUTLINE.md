# Paper artifacts — from lab to publishable contribution

## Proposed title
*Stale Secrets: Measuring the Deletion–Erasure Gap in Git History and the Economics of Verify-Then-Rotate Remediation*

## Research questions
1. RQ1 (prevalence): what fraction of removed `.env`/key files remain reachable in history across public repos?
2. RQ2 (exposure): for leaked tokens, what is commit→discovery→rotation latency, and does purge precede revoke (anti-pattern)?
3. RQ3 (tooling): on SecretBench + synthetic lab repos, what is precision/recall/latency of Gitleaks (gate) vs TruffleHog `--only-verified` (triage) vs stacked pipeline?
4. RQ4 (economics): what is $/record and audit-year cost of revoke-first vs purge-first (Uber $148M + 20-yr order as upper anchor)?

## Method (reproducible via this repo)
- Lab: docker compose up -> experiments/run_all.sh (A-Z video reproduction with assertions).
- Corpus: SecretBench (97,479 / 15,084 true) + fresh 2026 GitHub sample via push-protection-era APIs.
- Metrics: precision, recall, F1, MCC, MTTR (rotation), scanner latency, FP/1k commits.
- Live anchor: UBER price/mcap snapshot + SEC financials + 2026 press (leaked App keys still valid).

## Hidden patterns (novelty claims)
- See benchmarks/benchmark_matrix.py `hidden_patterns()` H1–H5. Strongest: verifier-economics
  collapse (4000→137) and chain-of-cheap-controls formalization.

## Venue targets
- MSR / ESEM (empirical), USENIX Security / CCS (measurement), SOUPS (human factors: why `.env` deleted not rotated).
