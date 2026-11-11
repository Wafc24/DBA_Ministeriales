import json
import re

path = r"D:\WILMER_FERRER\JSON\JSON INDIVIDUALES Y COMPLETOS\Sociales.json"
with open(path, "r", encoding="utf-8") as f:
    d = json.load(f)

for g in d.get("grados", []):
    grado = g.get("grado")
    for dba in g.get("dbas", []):
        num = dba.get("numero")
        enun = dba.get("enunciado", "")
        # search for long words
        long_w = [w for w in re.findall(r'[a-zA-ZáéíóúÁÉÍÓÚñÑ]{20,}', enun)]
        if long_w:
            print(f"Grado {grado} DBA {num} Enunciado long words:", long_w)
        for ev in dba.get("evidencias", []):
            long_w_ev = [w for w in re.findall(r'[a-zA-ZáéíóúÁÉÍÓÚñÑ]{20,}', ev)]
            if long_w_ev:
                print(f"Grado {grado} DBA {num} Evidencia long words:", long_w_ev)
