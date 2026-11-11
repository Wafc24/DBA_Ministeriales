import json

with open(r"D:\WILMER_FERRER\JSON\JSON INDIVIDUALES Y COMPLETOS\Sociales.json", 'r', encoding='utf-8') as f:
    d = json.load(f)

for g in d['grados']:
    grado_num = g.get('grado')
    for dba in g.get('dbas', []):
        num = dba.get('numero')
        evs = dba.get('evidencias', [])
        # print if any evidence is short, weird, or if grade is 8
        if grado_num in ['8°', '8'] and num in [7, 8]:
            print(f"Grado {grado_num} DBA {num}:")
            print(f"  Enunciado: {dba.get('enunciado')}")
            print(f"  Evidencias ({len(evs)}):")
            for e in evs:
                print(f"    - {e}")
