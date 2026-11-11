import os, json

folder = r"D:\WILMER_FERRER\JSON\JSON INDIVIDUALES Y COMPLETOS"
files = [f for f in os.listdir(folder) if f.endswith(".json")]

for item in sorted(files):
    p = os.path.join(folder, item)
    print("=" * 60)
    print("FILE:", item, "| Size:", os.path.getsize(p))
    try:
        with open(p, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            print(f"  Type: LIST, Length: {len(data)}")
            if len(data) > 0:
                first = data[0]
                if isinstance(first, dict):
                    print("  Keys in item 0:", list(first.keys()))
                    print("  Sample item 0:", json.dumps(first, ensure_ascii=False)[:300])
        elif isinstance(data, dict):
            print(f"  Type: DICT, Top-level keys: {list(data.keys())[:12]}")
            first_k = list(data.keys())[0]
            val = data[first_k]
            print(f"  Sample key '{first_k}' (type: {type(val).__name__})")
            if isinstance(val, dict):
                subkeys = list(val.keys())
                print(f"    Subkeys ({len(subkeys)}): {subkeys[:8]}")
                sample_inner = val[subkeys[0]]
                if isinstance(sample_inner, dict):
                    print("    Inner dict keys:", list(sample_inner.keys()))
                    print("    Inner sample:", json.dumps(sample_inner, ensure_ascii=False)[:300])
            elif isinstance(val, list):
                print(f"    List length: {len(val)}")
                if len(val) > 0 and isinstance(val[0], dict):
                    print("    List item keys:", list(val[0].keys()))
                    print("    List item sample:", json.dumps(val[0], ensure_ascii=False)[:300])
    except Exception as e:
        print("  ERROR reading:", e)
