import json

files = {
    'Lenguaje': r'D:\WILMER_FERRER\JSON\DBA - Lenguaje\dba_lenguaje_v2_men_2016.json',
    'Ciencias Naturales': r'D:\WILMER_FERRER\JSON\DBA - Ciencias Naturales\DBA_Ciencias_Naturales_v1_Colombia.json',
    'Sociales y Ciudadana': r'D:\WILMER_FERRER\JSON\DBA - Sociales y Ciudadana\dba_ciencias_sociales_men.json',
    'Inglés': r'D:\WILMER_FERRER\JSON\DBA - Ingles\dba_ingles_men_colombia.json'
}

for name, path in files.items():
    print(f"=== {name} ===")
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if name == 'Ciencias Naturales':
        dbas = data['dbas']
        g1 = dbas['1']
        item = g1[0] if isinstance(g1, list) else list(g1.values())[0]
        print("Grado 1 DBA 1:")
        print("  Statement:", item.get('statement'))
        print("  Evidencias count:", len(item.get('evidencias', [])))
        for ev in item.get('evidencias', [])[:3]:
            print("    -", ev)
    else:
        # list of items
        item = data[0]
        print("Item 1 (Grado " + str(item.get('grado')) + " DBA #" + str(item.get('numero')) + "):")
        print("  Enunciado:", item.get('enunciado') or item.get('statement'))
        print("  Factor / Eje:", item.get('factor') or item.get('eje'))
        print("  Evidencias count:", len(item.get('evidencias', [])))
        for ev in item.get('evidencias', [])[:3]:
            print("    -", ev)
