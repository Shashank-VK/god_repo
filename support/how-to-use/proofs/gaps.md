# Gaps (carried, nothing silently dropped)

## Input work gaps (pre-existing evidence, carried from work/)
- work/results/R17.jsonl empty (0 lines).
- work/micro-results/Q71/Q72/Q73.jsonl invalid WIP placeholders (1 line each, non-JSON).
- work/micro-results/Q96-Q100.jsonl short (37 lines vs 38).
- work/missing.json 1,672 entries; work/recheck.json 2,123 entries with prior_verdict/prior_note.
- work/inventory_urls.json 6,124 entries; entry [0] "https://" artifact.

## Corpus nuances
- 32 banner declared vs live wc -l +1 deltas (live authoritative, ranges use live counts).
- Duplicate-content pairs kept as separate cards with duplicate_content:true (C==23-watchlist, E==22-archives).
- resource-index.json single-line file (wc -l 1).

## Fetch gaps (Phase 1 — resolved 2026-10-12)
- 101 live_urls lacked fetch-log evidence at merge; bulk-verified via HEAD/GET (100x200, appended to fetch-log.jsonl by merge-verify).
- Malformed Antigravity URL RESOLVED: pinned to https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/ (page title verified via fetch, HTTP 200); card live_urls updated, recheck-queue.json cleared to [].
- fetch-log rows by workers lack evidence_type (null); merge-verify rows carry github/official_docs.

## Execution notes
- Agy individual quota exhausted twice (first 19 shards, then final 4); all covered by opencode free models. No source left uncovered: 707/707.
- Opencode free-model rate limits forced sequential/low-parallel execution; longcat 0/37 at concurrency, muse-spark delivered small/med + final big singles.
