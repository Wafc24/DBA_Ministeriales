import os, json

folder = r"D:\WILMER_FERRER\JSON\JSON INDIVIDUALES Y COMPLETOS"
files = [f for f in os.listdir(folder) if f.endswith(".json")]

for item in sorted(files):
    p = os.path.join(folder, item)
    print("=" * 60)
    print("FILE:", item)
    with open(p, encoding="utf-8") as f:
        data = json.load(f)
    grados = data.get("grados", {})
    print(f"  Metadata: asignatura={data.get('asignatura')}, version={data.get('version')}, seccion={data.get('seccion')}")
    print(f"  grados type: {type(grados).__name__}")
    if isinstance(grados, dict):
        print(f"  grados keys: {list(grados.keys())}")
        for gk in list(grados.keys())[:2]:
            g_val = grados[gk]
            print(f"    Grade '{gk}' type: {type(g_val).__name__}")
            if isinstance(g_val, dict):
                print(f"      Keys in '{gk}': {list(g_val.keys())[:8]}")
                # check if dbas or list inside
                first_sub = list(g_val.keys())[0]
                print(f"      Subkey '{first_sub}' sample: {str(g_val[first_sub])[:150]}")
            elif isinstance(g_val, list):
                print(f"      List items in '{gk}': {len(g_val)}")
                if len(g_val) > 0:
                    print(f"      First item in list: {list(g_val[0].keys()) if isinstance(g_val[0], dict) else type(g_val[0])}")
                    print(f"      Sample: {json.dumps(g_val[0], ensure_ascii=False)[:200]}")
    elif isinstance(grados, list):
        print(f"  grados is list with len: {len(grados)}")
        if len(grados) > 0:
            print(f"  First grade item keys: {list(grados[0].keys())}")
            print(f"  Sample: {json.dumps(grados[0], ensure_ascii=False)[:200]}")
