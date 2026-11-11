import json

# 1. Matemáticas V1 and V2
with open("clean_v1.json", encoding="utf-8") as f:
    mat_v1 = json.load(f)

with open("clean_v2.json", encoding="utf-8") as f:
    mat_v2 = json.load(f)

# 2. Lenguaje V1 and V2
with open("lenguaje_v1.json", encoding="utf-8") as f:
    raw_leng_v1 = json.load(f)

leng_v1 = {}
for item in raw_leng_v1:
    g = str(item["grado"])
    n = str(item["numero"])
    if g not in leng_v1:
        leng_v1[g] = {}
    leng_v1[g][n] = {
        "statement": item["enunciado"],
        "evidencias": item.get("evidencias", [])
    }

with open("literal_lenguaje_v2.json", encoding="utf-8") as f:
    leng_v2 = json.load(f)

# 3. Ciencias Sociales V2
with open("literal_sociales_v2.json", encoding="utf-8") as f:
    soc_v2 = json.load(f)

# 4. Ciencias Naturales V1
with open(r"D:\WILMER_FERRER\JSON\DBA - Ciencias Naturales\DBA_Ciencias_Naturales_v1_Colombia.json", encoding="utf-8") as f:
    nat_raw = json.load(f)
nat_v1 = nat_raw["dbas"]

# 5. Inglés
with open("literal_ingles.json", encoding="utf-8") as f:
    ing_v1 = json.load(f)

# 6. PMA Master (Saber Check)
with open("pma_master.json", encoding="utf-8") as f:
    pma_master = json.load(f)

curriculo_data = {
    "matematicas": {
        "v1": mat_v1,
        "v2": mat_v2
    },
    "lenguaje": {
        "v1": leng_v1,
        "v2": leng_v2
    },
    "sociales": {
        "v2": soc_v2
    },
    "naturales": {
        "v1": nat_v1
    },
    "ingles": {
        "v1": ing_v1
    },
    "pma": pma_master
}

js_content = "/**\n * BANCO MAESTRO DE DATOS CURRICULARES MEN - ASESORÍAS PEDAGÓGICAS S.A.S.\n * Contiene transcripción literal 100% de Matemáticas, Lenguaje, Sociales, Naturales e Inglés,\n * además de los Planes de Mejoramiento Saber Check.\n */\n"
js_content += "var CURRICULO_DATA = " + json.dumps(curriculo_data, ensure_ascii=False, indent=2) + ";\n"
js_content += "if (typeof window !== 'undefined') { window.CURRICULO_DATA = CURRICULO_DATA; }\n"
js_content += "if (typeof globalThis !== 'undefined') { globalThis.CURRICULO_DATA = CURRICULO_DATA; }\n"

with open("dbas_master_data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("dbas_master_data.js generated successfully. Size:", len(js_content))
