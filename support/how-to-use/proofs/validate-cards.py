import json,sys,glob,pathlib
allowed_cat={"skill","mcp","agent","harness","workflow","hook","command","gate","style","watchlist","archive","report","finding","company","tool","practice","forensic","case","evidence","rule","template","discipline","os","config"}
allowed_ver={"Verified","Partially","Unverified","Historical","Unresolved","BLOCKED","DEAD"}
req=["source","part","lines","category","WHAT","WHERE_USED","HOW_TO_USE","WHY","WHAT_NOT_TO_DO","HARNESS_WIRING","NEW_DISCOVERY","VERDICT","live_urls","conflicts","coverage","not_applicable"]
def check_file(f):
    errs=[]
    for i,line in enumerate(open(f,encoding="utf-8"),1):
        if not line.strip(): continue
        try: c=json.loads(line)
        except Exception as e: errs.append(f"{f}:{i} JSON parse {e}"); continue
        for k in req:
            if k not in c: errs.append(f"{f}:{i} missing {k}")
        if c.get("category") not in allowed_cat: errs.append(f"{f}:{i} bad category {c.get('category')}")
        if c.get("VERDICT") not in allowed_ver: errs.append(f"{f}:{i} bad verdict {c.get('VERDICT')}")
        if c.get("type","final_card")=="partial_card": errs.append(f"{f}:{i} partial_card in results")
        hw=c.get("HARNESS_WIRING",{})
        na=c.get("not_applicable",{})
        if not hw and not na: errs.append(f"{f}:{i} empty wiring without reason")
    return errs
if __name__=="__main__":
    files=sys.argv[1:] or glob.glob("work-cards/results/*.jsonl")
    allerrs=[]
    for f in files: allerrs+=check_file(f)
    print(f"checked {len(files)} files, errors={len(allerrs)}")
    [print(e) for e in allerrs[:50]]
    sys.exit(1 if allerrs else 0)
