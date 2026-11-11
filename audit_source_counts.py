import os, json

folder = r"D:\WILMER_FERRER\JSON\JSON INDIVIDUALES Y COMPLETOS"
files = [
    "Ciencias Naturales.json",
    "Inglés.json",
    "Lenguaje_1-5.json",
    "Lenguaje_6-11.json",
    "Lenguaje_V1.json",
    "Matemáticas_1-5.json",
    "Matemáticas_6-11.json",
    "Matemáticas_V1.json",
    "Sociales.json"
]

for fname in files:
    fpath = os.path.join(folder, fname)
    with open(fpath, encoding="utf-8") as f:
        d = json.load(f)
    print("=" * 70)
    print("FILE:", fname)
    print("Top keys:", [k for k in d.keys() if k != "grados"])
    grados = d.get("grados", [])
    print(f"Grades count: {len(grados)}")
    for g in grados:
        g_name = g.get("grado")
        dbas = g.get("dbas", [])
        total_evids = sum(len(x.get("evidencias", [])) for x in dbas)
        print(f"  Grade: {g_name} -> {len(dbas)} DBAs, {total_evids} evidencias")
