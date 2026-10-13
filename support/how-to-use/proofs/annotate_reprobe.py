"""Stamp reprobe results onto cards: blocked URLs become {url,http,date,note}.

Runs as part of merge.sh after concat+normalize, so per-card edits survive rebuilds.
Idempotent: a URL already annotated with http!=None is left alone.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path("/mnt/c/Users/Shashank Karamudi/Desktop/structerd_output")
REPORT = ROOT / "how-to-use/proofs/reprobe.json"
INDEX = ROOT / "how-to-use/index.jsonl"


def main() -> int:
    if not REPORT.exists():
        print("[annotate] no reprobe.json; nothing to stamp")
        return 0
    blocked = {i["url"]: i for i in json.loads(REPORT.read_text())["non_200"]}
    cards = [json.loads(l) for l in INDEX.open() if l.strip()]
    n = 0
    for c in cards:
        out = []
        for u in c.get("live_urls", []):
            url = u if isinstance(u, str) else u.get("url", "")
            if url in blocked and isinstance(u, str):
                it = blocked[url]
                out.append({"url": url, "http": it["http"], "date": "2026-10-13",
                            "note": "reprobe bot-blocked; original worker evidence retained"})
                n += 1
            else:
                out.append(u)
        c["live_urls"] = out
    with INDEX.open("w") as fh:
        for c in cards:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(f"[annotate] stamped {n} blocked URLs")
    return 0


if __name__ == "__main__":
    sys.exit(main())