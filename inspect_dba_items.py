import os, json

folder = r"D:\WILMER_FERRER\JSON\JSON INDIVIDUALES Y COMPLETOS"
files = [f for f in os.listdir(folder) if f.endswith(".json")]

for item in sorted(files):
    p = os.path.join(folder, item)
    print("=" * 60)
    print("FILE:", item)
    with open(p, encoding="utf-8") as f:
        data = json.load(f)
    grados = data.get("grados", [])
    if isinstance(grados, list) and len(grados) > 0:
        first_g = grados[0]
        dbas = first_g.get("dbas", [])
        print(f"  Grade '{first_g.get('grado')}' has {len(dbas)} dbas.")
        if len(dbas) > 0:
            d0 = dbas[0]
            print(f"  DBA 0 keys: {list(d0.keys())}")
            for k in d0.keys():
                val = d0[k]
                if isinstance(val, list):
                    print(f"    {k} (list of {len(val)} items):")
                    for sub in val[:2]:
                        print(f"       - {str(sub)[:120]}")
                else:
                    print(f"    {k}: {str(val)[:120]}")
