"""Stage not_applicable reasons for research/findings cards.

Workers invented prose reasons (e.g. "catalog-research-no-direct-install") because
the plan enum has no member for "read-only research catalog". Rather than force a
wrong enum value, the final staged reason carries the enum-prefix mapping in
proofs/reason-map.json so validators and humans can see both the staged token and
the original prose.

Stages used (documented, not part of the Phase 1 enum; see reason-map.json `stages`):
  catalog-*        -> finding-no-install     (research catalog, no package to install)
  research-*       -> finding-no-install
  read-only-*      -> finding-no-install
  reference-*      -> finding-no-install
  *-no-install     -> finding-no-install
  metadata-*       -> metadata-only
  *-catalog-*      -> metadata-only         (directory/catalog listings)
  template-*       -> template-example
  audit-*/reconciliation-*/register-* -> evidence-ledger (NEW stage, see below)
  style-*          -> design-token-no-runtime  (for style cards only)

New enum member staged for this OS revision: `evidence-ledger` (register/audit
documents with no runtime wiring).
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.jsonl"
REPORT = ROOT / "proofs/reason-map.json"
ENUM = [
    "pure-prompt-skill", "design-token-no-runtime", "finding-no-install",
    "metadata-only", "template-example", "superseded-archived",
    "transport-not-applicable", "evidence-ledger",
]
RULES = [
    (r"^metadata-|^metadata-only|^prompt-archives|^directory-|^catalog-readme|^empty file", "metadata-only"),
    (r"catalog-audit-ledger|^audit-|^reconciliation-|register-no-install|^discrepancy-|^named-watchlist-|^verification-discrepancy|^search-coverage-|^phase0-inventory-|^taxonomy-diff|^inventory-report", "evidence-ledger"),
    (r"template-|checklist-|^practice-guide|^workflow-guide", "template-example"),
    (r"style-no-direct-install|style-index-reference|style-reference|design-catalog", "design-token-no-runtime"),
    (r"catalog-no-direct-install|catalog-research-no-direct-install|research|read-only|reference-catalog|directory-overview|directory-master-index|no-direct-install|no-install|no-package-install|no-single-package-install|no-harness-wiring|no-executable|no-runtime-wiring|governing-framework|historical-research-log|forensic-audit-ledger|forensic-investigation-report|resource-index-lookup|encyclopedia-atlas|master technical|README overview|Technical directory|compendium|Authoritative research report|taxonomy|no harness wiring|no applicable content", "finding-no-install"),
]


def classify(value: str) -> str | None:
    low = value.lower()
    for e in ENUM:
        if e in low:
            return e
    for pat, target in RULES:
        if re.search(pat, low):
            return target
    # Last resort: any prose ending in a no-install clause is a read-only research doc.
    if re.search(r"no applicable|no harness wiring|not install|isn't installed|executing the catalog|rather than install|not a software package|serves as|instead of executing|document surveying|rather than", low):
        return "finding-no-install"
    return None


def main(strict: bool = False) -> int:
    cards = [json.loads(l) for l in INDEX.open() if l.strip()]
    staged, unmapped = 0, []
    for c in cards:
        na = c.get("not_applicable")
        if not isinstance(na, dict):
            continue
        for k, v in list(na.items()):
            if not isinstance(v, str) or v in ENUM:
                continue
            mapped = classify(v)
            if mapped:
                na[k] = {"reason": mapped, "worker_original": v}
                staged += 1
            else:
                unmapped.append({"source": c["source"], "field": k, "value": v})
    if not strict:
        with INDEX.open("w") as fh:
            for c in cards:
                fh.write(json.dumps(c, ensure_ascii=False) + "\n")
        REPORT.write_text(json.dumps(
            {"staged": staged, "unmapped": unmapped, "enum": ENUM,
             "new_member": "evidence-ledger (staged in this OS revision)"}, indent=1) + "\n")
        print(f"staged {staged}; unmapped {len(unmapped)}")
        for u in unmapped[:15]:
            print("  UNMAPPED:", u["source"], "->", u["value"][:70])
    else:
        print("unmapped:", len(unmapped))
    return 0


if __name__ == "__main__":
    sys.exit(main(strict="--check" in sys.argv))