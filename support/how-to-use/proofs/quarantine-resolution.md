# Quarantine resolution

- W071 (04-mcp, 2846 lines): worker first emitted 3 duplicate cards with empty wiring. Quarantined to work-cards/quarantine/W071.*. Reworked with strict one-card prompt via opencode/muse-spark-1.3-contributor-free; final output 1 card, 0 validation errors. Accepted.
- W074 (06b-quality): worker emitted 11 duplicate cards. Quarantined to work-cards/quarantine/W074.* (copies). Reworked to exactly 1 card via opencode/muse-spark-1.3-contributor-free; 0 errors. Accepted.
- W089 (deve 63): first dispatched on non-free big-pickle, killed per free-only policy before completion; restarted on opencode/nemotron-3-ultra-free, then finalized on muse-spark. 63/63 valid. Accepted.
- W066 (01b split non-owner): worker wrongly wrote a final card to results. Moved to work-cards/partials/W066.jsonl as partial_card; results emptied (correct non-owner state). Accepted.
- No unresolved quarantine remains.
