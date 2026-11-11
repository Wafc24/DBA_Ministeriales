import os
import json

target_dir = r"D:\WILMER_FERRER\JSON\JSON INDIVIDUALES Y COMPLETOS"
for fname in sorted(os.listdir(target_dir)):
    if not fname.endswith('.json'):
        continue
    fpath = os.path.join(target_dir, fname)
    print(f"==================================================")
    print(f" ARCHIVO: {fname}")
    print(f"==================================================")
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            grados = data.get('grados')
            if isinstance(grados, dict):
                print(f"Grados ({len(grados)}): {list(grados.keys())}")
                total_dbas = 0
                total_evids = 0
                for g, gdata in grados.items():
                    if isinstance(gdata, dict):
                        dbas = gdata.get('dbas', [])
                    elif isinstance(gdata, list):
                        dbas = gdata
                    else:
                        dbas = []
                    total_dbas += len(dbas)
                    ev_count = sum(len(x.get('evidencias', [])) for x in dbas)
                    total_evids += ev_count
                    nums = [x.get('numero') for x in dbas]
                    print(f"  Grado {g}: {len(dbas)} DBAs (Evidencias: {ev_count}) -> Nums: {nums}")
                print(f"TOTAL: {total_dbas} DBAs, {total_evids} evidencias")
            elif isinstance(grados, list):
                print(f"Grados lista ({len(grados)})")
                total_dbas = 0
                total_evids = 0
                for gdata in grados:
                    g = gdata.get('grado')
                    dbas = gdata.get('dbas', [])
                    total_dbas += len(dbas)
                    ev_count = sum(len(x.get('evidencias', [])) for x in dbas)
                    total_evids += ev_count
                    nums = [x.get('numero') for x in dbas]
                    print(f"  Grado {g}: {len(dbas)} DBAs (Evidencias: {ev_count}) -> Nums: {nums}")
                print(f"TOTAL: {total_dbas} DBAs, {total_evids} evidencias")
            else:
                print(f"Formato no reconocido o sin clave 'grados': {list(data.keys())[:10]}")
    except Exception as e:
        print(f"ERROR: {e}")
    print()
