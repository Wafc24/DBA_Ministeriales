import json

path = r"D:\WILMER_FERRER\JSON\JSON INDIVIDUALES Y COMPLETOS\Inglés.json"
with open(path, "r", encoding="utf-8") as f:
    d = json.load(f)

for g in d.get("grados", []):
    grado = g.get("grado")
    for dba in g.get("dbas", []):
        num = dba.get("numero")
        enun = dba.get("enunciado", "")
        ej = dba.get("ejemplo_evidencia", "")
        # print first dba of each grade
        if num == 1:
            print(f"Grado {grado} DBA 1:")
            print(f"  Enunciado: {enun}")
            print(f"  Ejemplo: {ej}")
