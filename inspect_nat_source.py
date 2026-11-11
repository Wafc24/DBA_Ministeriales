import json

path = r"D:\WILMER_FERRER\JSON\DBA - Ciencias Naturales\DBA_Ciencias_Naturales_v1_Colombia.json"
with open(path, "r", encoding="utf-8") as f:
    d = json.load(f)

print("Keys:", list(d.keys()))
dbas = d.get("dbas", {})
for g in sorted(dbas.keys(), key=lambda x: int(x)):
    g_val = dbas[g]
    if isinstance(g_val, dict):
        print(f"Grado {g}: dict con {len(g_val)} keys: {list(g_val.keys())}")
        sample_key = list(g_val.keys())[0]
        print(f"  Item sample ({sample_key}):", json.dumps(g_val[sample_key], indent=2, ensure_ascii=False)[:300])
    elif isinstance(g_val, list):
        print(f"Grado {g}: list con {len(g_val)} items")

