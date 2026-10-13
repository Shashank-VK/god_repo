# Everything you need, in three folders. Start at prompt/SYSTEM-PROMPT-UNIVERSAL.md.

## Folder 1 — `superior-os/` (the runnable OS, 128 files)

What it is: a single-developer AI product-engineering operating system. You tag it into
each project; you never copy it.

- `.harness/skills/` — 24 skills (9 process + 15 engineering runbooks), each with a
  `description:` trigger line for progressive disclosure; `index.json` is the registry.
- `.harness/agents/` — 4 subagent specs (coder, explorer, planner, reviewer).
- `.harness/workflows/` — 15 executable workflow state machines.
- `.harness/mcp/` — 4 wired MCP servers + `MCP_SECURITY.md`.
- `.harness/hooks/` — pre-tool security guard, ABAC check, IAL debounce, post-write
  linter.
- `.harness/permissions/` — Cedar ABAC policies + role presets.
- `os/` — the readable contract: gates, rubric, 34 rules, 19 anti-patterns, 6 disciplines,
  16 templates, domain checklists, third-party registries.
- `scripts/` — verification: `verify.sh`, `setup.sh` (download-once), `tag_project.py`,
  `coverage_gate.py`, `claim_check.py`, `secret-scan.sh`, `scope-check.py`, tests.

Key commands (run from `superior-os/`):
```
bash scripts/verify.sh                    # must print ALL GATES PASSED
bash scripts/setup.sh                     # first run only; idempotent thereafter
python3 scripts/tag_project.py <path>     # tag a project to this OS
```

## Folder 2 — `support/` (read-only contract + evidence, 35 files)

- `support/how-to-use/index.jsonl` — 707 cards, one JSON object per line. The behavior
  contract: WHAT / HOW / WHY / NOT-TO-DO / harness wiring / verdict / live URLs / coverage.
- `support/how-to-use/0*.md` — 9 human manuals rendered from those cards.
- `support/how-to-use/proofs/` — banner map, shard map, schemas, coverage ledger (809
  receipts), fetch log (430 rows, every URL with HTTP evidence), reprobe report,
  merge/normalize scripts, quarantine + gap records.
- `support/MANIFEST.sha256` — integrity manifest; Phase 0 of the bring-up prompt checks it.

`support/` is never edited. The OS cites card sources; it never copies the corpus.

## Folder 3 — `prompt/` (paste into any agent)

- `SYSTEM-PROMPT-UNIVERSAL.md` — bring-up: integrity check → download-once setup → prove
  the OS → tag every project. Read this one first.
- `SKILLS-PROMPT-UNIVERSAL.md` — skills playbook: discovery → shortlist → audited
  install → real-session proof → steady-state governance, for the 36 third-party
  entries.

## Plus

- `AUDIT-FINDINGS.md` — full six-axis audit (entities, URLs, card integrity, prohibitions,
  corpus fidelity, execution shape) with honest deviations.

## Verified state (2026-10-13)

707/707 cards · 9 manuals · 24 skills vendored · 15 workflows · 4 agents · 196 live URLs
independently re-probed (191 OK, 5 bot-blocked and queued) · 58 tests green in both
copies · manifest 34/34 · corpus checksums 19/19 + 707/707 unchanged.