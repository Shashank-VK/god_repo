# Pilot Report
pilot_pass=true

## Pilot shards run
- W001 (B01, agy gemini-3.8-flash-medium): 2 files, 2 final cards, 2 coverage receipts, exit 0, validate 0 errors
- W016 (B03, opencode muse-spark-1.3-contributor-free): 5 files, 5 cards, 5 receipts, exit 0, validate 0 errors
- W064 (B11, agy gemini-3.8-flash-high): 1 file 01a 3215 lines, 1 card, 7 receipts, exit 0, validate 0 errors
- W089 (B20, opencode nemotron-3-ultra-free after big-pickle kill): 63 files deve template, 63 cards, 63 receipts, exit 0, validate 0 errors
- W092 (B22, agy gemini-3.8-flash-high): 26 files core, 26 cards, 26 receipts, exit 0, validate 0 errors
Total pilot: 97 final cards, 103 coverage receipts.

## Schema validation
- card-schema: 5/5 shards pass validate-cards.py, 0 errors
- coverage-schema: 5/5 pass validate-coverage.py, 0 errors

## Banner-map validation
- 707 rows, 707 unique sources, 0 missing, 0 extra, 0 dups. 32 banner declared vs live +1 noted (live wc -l authoritative).

## Coverage validation
- All pilot ranges sum to live wc -l per source. W064 7 chunks for 3215 lines. No gaps.

## Fetch-log validation
- 0 fetch rows in pilot (corpus-only cards, live_urls [] or corpus refs). No invented URLs. 0 mismatches. Bounded-fetch path exercised in full dispatch with global cap 40 / 2-per-host.

## Split-card merge validation
- Shard-map defines 3 cross-shard splits with single owners: catalog.md 4-way owner W002, B10-mcp 2-way owner W025, 01b-frontend 3-way owner W065. No duplicate owners. Partial/merge rules enforced by validators (results final-only, partials separate). Worker split outputs (W002-W005, W025-W026, W065-W067) pending in full dispatch; merge gate requires all partials + single final per split source.

## Sample manual render
- Grouped 97 pilot cards by category (17 practice, 11 workflow, 9 template, 9 skill, 7 harness, 7 gate, 6 rule, 6 archive, 5 finding, 5 tool, 5 config, 3 hook, 2 os, 2 evidence, 1 mcp, 1 agent, 1 case). Render path index.jsonl -> manuals verified (group-by + source/part cite). Full 9 manuals render after 707 merge.

## Blockers
- Opencode 20-parallel free-model rate limits (42/42 failed, all rate-limit, 0 credits). Fixed: -P 4 + correct routing (ultra-free big, laguna-s small, longcat medium) + 3x backoff. Retry running.
- W089 big-pickle non-free killed per free-only policy, restarted ultra-free, passed.
- 32 banner +1 deltas use live counts for ranges/coverage.

## Models (locked)
- agy: gemini-3.8-flash-medium (small/med), gemini-3.8-flash-high (big)
- opencode free good-context: longcat-2.5-preview-free, nemotron-3-ultra-free, muse-spark-1.3-contributor-free
- openrouter only: nemotron-3-ultra-550b-a55b:free, laguna-s-2.1:free
