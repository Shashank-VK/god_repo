#!/usr/bin/env bash
# merge.sh — deterministic rebuild of index.jsonl + derived artifacts from worker outputs.
# Order matters: concat -> normalize reasons -> render manuals -> derive index.json -> checksums.
# Run from structerd_output/. Idempotent.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
cd "$ROOT"
echo "[merge] root=$ROOT"
echo "[merge] 1/6 concat results"
cat work-cards/results/W*.jsonl > how-to-use/index.jsonl
lines=$(wc -l < how-to-use/index.jsonl)
echo "[merge] index.jsonl lines=$lines (must be 707)"
[ "$lines" -eq 707 ] || { echo "[merge] FAIL: expected 707 lines"; exit 1; }

echo "[merge] 2/6 normalize not_applicable reasons (enum staging)"
python3 how-to-use/proofs/normalize_reasons.py

echo "[merge] 3/6 stamp reprobe results onto cards"
python3 how-to-use/proofs/annotate_reprobe.py

echo "[merge] 4/6 render manuals"
python3 how-to-use/proofs/render_manuals.py

echo "[merge] 5/6 derive index.json"
python3 - <<'PY'
import json, pathlib
p = pathlib.Path("how-to-use/index.jsonl")
cards = [json.loads(l) for l in p.open() if l.strip()]
cards.sort(key=lambda c: c["source"])
json.dump(cards, open("how-to-use/index.json", "w"), indent=1)
print(f"[merge] index.json derived: {len(cards)}")
PY

echo "[merge] 6/6 checksums"
python3 - <<'PY'
import hashlib, pathlib
h = []
for f in sorted(pathlib.Path("how-to-use").glob("*.md")) + [pathlib.Path("how-to-use/index.jsonl"), pathlib.Path("how-to-use/index.json")]:
    h.append(f"{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.as_posix()}")
pathlib.Path("how-to-use/proofs/CHECKSUMS.sha256").write_text("\n".join(h) + "\n")
print(f"[merge] checksums: {len(h)}")
PY
sha256sum -c how-to-use/proofs/CHECKSUMS.sha256 >/dev/null 2>&1 && echo "[merge] checksums PASS"
echo "[merge] COMPLETE"