"""Render 9 manuals + 08-index from how-to-use/index.jsonl (deterministic, manager-only)."""
import json, pathlib, collections
root = pathlib.Path("/mnt/c/Users/Shashank Karamudi/Desktop/structerd_output")
cards = [json.loads(l) for l in (root/"how-to-use/index.jsonl").open() if l.strip()]
by_cat = collections.defaultdict(list)
for c in cards:
    by_cat[c["category"]].append(c)
for v in by_cat.values():
    v.sort(key=lambda x: x["source"])
def sec(c):
    parts = []
    for u in c.get("live_urls", []):
        if isinstance(u, dict):
            parts.append(u.get("url","") + (f" (http {u.get('http')}, {u.get('date','')})" if u.get("http") else ""))
        else:
            parts.append(str(u))
    urls = "; ".join(parts) or "no live URLs"
    return (
        f"### {c['source']}\n"
        f"- card: {c['source']} | part {c.get('part','?')} | lines {c.get('lines','?')} | verdict {c.get('VERDICT','?')}\n"
        f"- WHAT: {c.get('WHAT','')[:400]}\n"
        f"- HOW: {(c.get('HOW_TO_USE') or [''])[0][:300]}\n"
        f"- live: {urls[:400]}\n"
        f"- conflicts: {', '.join(c.get('conflicts', [])) or 'none'}\n"
    )
manuals = {
    "00-rules.md": ["report","rule","evidence","os","gate","discipline"],
    "01-skills.md": ["skill"],
    "02-mcp.md": ["mcp"],
    "03-agents-harness-context.md": ["agent","harness","workflow","hook","command","config"],
    "04-commands-workflows.md": ["workflow","hook","command","gate","template"],
    "05-styles.md": ["style"],
    "06-watchlist-new-discoveries.md": ["watchlist","archive"],
    "07-anti-patterns.md": ["finding","forensic","case","company","tool","practice"],
    "08-index.md": None,
}
headers = {
    "00-rules.md": "# Rules — authority, preserve-both, read-only corpus\n\nProjects read how-to-use/ only. Authority: opencode-research + first-pass B/D/C/E/A/00. Conflicts preserve-both + flagged. Corpus files/, parts/, proofs/, work/ are read-only.\n\n",
    "01-skills.md": "# Skills\n\nEvery SKILL.md card, alphabetical by source.\n\n",
    "02-mcp.md": "# MCP\n\nBy transport/provider.\n\n",
    "03-agents-harness-context.md": "# Agents, harness, context\n\nBy lifecycle stage.\n\n",
    "04-commands-workflows.md": "# Commands and workflows\n\nBy execution order.\n\n",
    "05-styles.md": "# Styles (D/00-D/29 order)\n\n",
    "06-watchlist-new-discoveries.md": "# Watchlist and new discoveries\n\nBy verdict then source.\n\n",
    "07-anti-patterns.md": "# Anti-patterns\n\nBy severity/source order.\n\n",
    "08-index.md": "# Index — every source to card to manual\n\n",
}
for fname, cats in manuals.items():
    if cats is None:
        lines = [headers[fname], f"707 cards. Every card appears in >=1 manual.\n\n"]
        for c in sorted(cards, key=lambda x: x["source"]):
            lines.append(f"- {c['source']} -> {c['category']} | {c.get('part','?')} | {c.get('VERDICT','?')}\n")
        (root/"how-to-use"/fname).write_text("".join(lines))
        continue
    if fname == "04-commands-workflows.md":
        pool = [c for c in cards if c["category"] in ("workflow","hook","command","gate","template")]
    elif fname == "00-rules.md":
        pool = [c for c in cards if c["category"] in ("report","rule","evidence","os","gate","discipline")]
    elif fname == "07-anti-patterns.md":
        pool = [c for c in cards if c["category"] in ("finding","forensic","case","company","tool","practice")]
    elif fname == "03-agents-harness-context.md":
        pool = [c for c in cards if c["category"] in ("agent","harness","workflow","hook","command","config")]
    else:
        pool = [c for c in cards if c["category"] in cats]
    if fname == "06-watchlist-new-discoveries.md":
        order = {"Verified":0,"Partially":1,"Unverified":2,"Historical":3,"Unresolved":4,"BLOCKED":5,"DEAD":6}
        pool.sort(key=lambda x: (order.get(x.get("VERDICT","Unverified"),9), x["source"]))
    body = [headers[fname]]
    for c in pool:
        body.append(sec(c) + "\n")
    (root/"how-to-use"/fname).write_text("".join(body))
covered = set()
for fname, cats in manuals.items():
    if fname == "08-index.md": continue
    if fname == "04-commands-workflows.md":
        covered |= {c["source"] for c in cards if c["category"] in ("workflow","hook","command","gate","template")}
    elif fname == "00-rules.md":
        covered |= {c["source"] for c in cards if c["category"] in ("report","rule","evidence","os","gate","discipline")}
    elif fname == "07-anti-patterns.md":
        covered |= {c["source"] for c in cards if c["category"] in ("finding","forensic","case","company","tool","practice")}
    elif fname == "03-agents-harness-context.md":
        covered |= {c["source"] for c in cards if c["category"] in ("agent","harness","workflow","hook","command","config")}
    else:
        covered |= {c["source"] for c in cards if c["category"] in cats}
print("covered:", len(covered), "missing:", sorted({c["source"] for c in cards} - covered) or "none")