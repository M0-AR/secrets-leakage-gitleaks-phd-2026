# Evidence log — every claim below was retrieved 2026-10-15 via sequential search
# (one-at-a-time, no parallel websearch to avoid 429). Voting = independent convergence.

## 1. websearch (Exa-equivalent, first per instruction)
- Q "Uber 2014 2016 GitHub API key breach timeline" -> FTC revised analysis PDF:
  2014 public GitHub key, full-admin single AWS key, 100k+ licenses; 2016 private-repo key
  via credential stuffing, 25.6M emails / 22.1M phones / 607k licenses, $100k bug-bounty
  cover-up, disclosure 2017-11-21. Corroborated by breaches.cloud timeline + Ars 2015 + AP 2017.
- Q "Gitleaks detect git history best practice 2026 2027" -> gitleaks README (git log -p,
  log-opts, redact, baseline), trustedoss (delete != erase, force-push insufficient),
  h2security 2026 (scan commits not files, --redact, rotate-then-rewrite), Pickuma 2026
  (100+ rules, entropy, protect --staged <1s, MIT binary vs licensed action).
- Q "rotate revoke clean filter-repo BFG remediation" -> GitHub remediation tutorial
  (revoke FIRST, 7 steps), GitHub sensitive-data removal (filter-repo >=2.47, support ticket
  for PR refs/GC, re-clone not pull), GitGuardian (revoke-only usually sufficient; rewrite
  optional/disruptive), Checkmarx + Harness + BattleTest (same order).
- Q "prevent Vault env push protection SOC2 GRC 2026" -> OWASP DevSecOps guideline
  (5 layers: pre-commit/CI/push-protection/history/public-monitoring; OIDC > static keys;
  maturity Starting->Advanced), HashiCorp Vault Radar (cloud/agent/CLI), KloudVin 2026
  (pre-commit≠enforcement, CI≠prevention, push-protection=only unbypassable gate;
  4000->137 via validity checks; OIDC deleted 300+ keys), Clutch 2026 (identity not string).

## 2. duckduckgo_search + fetch
- Q "trufflehog vs gitleaks benchmark 2026" -> 8 results; fetched devsecops.ae 2026-04-22:
  7-scanner benchmark, 4-gate model, stack = Gitleaks (pre-commit+CI) + TruffleHog
  (verified history, 700+ types) + GitHub scanning (+GitGuardian for regulated).

## 3. openresearch (9 sub-tools, distinct keywords)
- web_search "DefinitelySecure Gitleaks curl bearer 2026" -> tech-insider 2026 tutorial pattern.
- search_openalex "hardcoded secrets empirical" -> Soltaniani 2026 (CodeBERT+MCC),
  Capalbo 2026 thesis (stale-history sanitization gap = PhD opening), Krause 2025 (human factors).
- hacker_news "Gitleaks secrets" -> none (negative evidence logged).
- stackoverflow "gitleaks pre-commit filter-repo" -> none (negative evidence logged).
- search_news "secrets leaked GitHub breach API key" -> 2026-09-22 hundreds leaked GitHub App
  keys still authenticate (proves revoke-first thesis on LIVE data).
- search_sec_filings "Uber breach GitHub key" -> 193 hits (disclosure regime context).
- search_europepmc "data breach disclosure health" -> 3121 papers (adjacent domain).
- get_current_date -> 2026-10-15 UTC anchor. get_company_financials UBER -> revenue/net/assets table.

## 4. paper-search (unified + arxiv + semantic)
- search_papers "secrets detection gitleaks trufflehog benchmark" -> Basak et al. ESEM 2023
  (precision GitHub 75/Gitleaks 46; recall Gitleaks 88/Spectral 67/TruffleHog 52) + SecretBench
  (97,479 secrets, 15,084 true, 818 repos, 49 langs) + Neural-Sentinel 2026 (F1 98.5% claim).
- search_arxiv "secret sprawl GitHub 2024-2026" -> no direct hit (gap logged).
- search_semantic "SecretBench precision recall" -> Basak 41 cites + Baby et al. 2026
  (3-class placeholder-aware, MCC 0.86, F1 0.90, -33% high-severity alerts).

## 5. agent-reach / gitmcp / kaggle / wiki / gsd / superpowers
- agent-reach_search web "Uber breach cost FTC settlement" -> Reuters $148M largest AG privacy
  settlement; Senate 2018 hearing; DOJ non-prosecution 2022.
- agent-reach_search github "gitleaks pre-commit" -> gh CLI flag error (tooling negative evidence).
- agent-reach_stock_quote UBER -> $69.69, mcap $142.35B, PE 15.73 (live-market anchor).
- gitmcp documentation + code (gitleaks/gitleaks) -> full README + pre-commit/Docker/MIT verified.
- kaggle search_everything + discussions_search "API keys leakage" -> no security dataset
  (gap: publish SecretBench-derived lab dataset as contribution).
- wiki_search "Uber breach 2016" -> Uber / Controversies / Credential-stuffing pages confirm chain.
- gsd_websearch "Gitleaks TruffleHog FP benchmark" -> empty (negative evidence).
- superpowers_semantic_search "reproducibility docker benchmark" -> systematic-debugging signals.

## Voting result (convergent, publishable)
1. Deletion != erasure (unanimous: video, GitHub, GitGuardian, OWASP, FTC history).
2. Revoke-first ordering (unanimous across 5 remediation guides).
3. Gitleaks=gate speed, TruffleHog=verifier, platform=backstop (3 benchmarks agree).
4. Chain-of-cheap-controls (Uber: MFA + distinct keys + encryption + rotation all missing).
5. Live keys still authenticate in 2026 press (revocation gap is current, not historical).
