import json,sys,glob
def check_file(f):
    errs=[]
    for i,line in enumerate(open(f,encoding="utf-8"),1):
        if not line.strip(): continue
        try: c=json.loads(line)
        except Exception as e: return [f"{f}:{i} parse {e}"]
        for k in ["source","worker","range","total_lines","read_sha256_bytes","status","timestamp"]:
            if k not in c: errs.append(f"{f}:{i} missing {k}")
        if len(c.get("read_sha256_bytes",""))!=64: errs.append(f"{f}:{i} bad sha")
    return errs
if __name__=="__main__":
    files=sys.argv[1:] or glob.glob("work-cards/coverage/*.jsonl")
    allerrs=[]
    for f in files: allerrs+=check_file(f)
    print(f"checked {len(files)} files, errors={len(allerrs)}")
    [print(e) for e in allerrs[:50]]
    sys.exit(1 if allerrs else 0)
