import os
import json
import re

target_dir = r"D:\WILMER_FERRER\JSON\JSON INDIVIDUALES Y COMPLETOS"
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

report = {}

for fname in files:
    fpath = os.path.join(target_dir, fname)
    report[fname] = {
        "status": "OK",
        "total_grados": 0,
        "total_dbas": 0,
        "total_evidencias": 0,
        "issues": []
    }
    
    if not os.path.exists(fpath):
        report[fname]["status"] = "FILE_NOT_FOUND"
        continue
        
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        report[fname]["status"] = f"SYNTAX_ERROR: {e}"
        continue
        
    grados_list = data.get("grados", [])
    if isinstance(grados_list, dict):
        grados_items = [{"grado": k, "dbas": v.get("dbas", v) if isinstance(v, dict) else v} for k, v in grados_list.items()]
    elif isinstance(grados_list, list):
        grados_items = grados_list
    else:
        report[fname]["status"] = "INVALID_GRADOS_STRUCTURE"
        continue
        
    report[fname]["total_grados"] = len(grados_items)
    
    for g_entry in grados_items:
        g_name = str(g_entry.get("grado", "?"))
        dbas = g_entry.get("dbas", [])
        if not isinstance(dbas, list):
            report[fname]["issues"].append(f"Grado {g_name}: 'dbas' no es lista.")
            continue
            
        report[fname]["total_dbas"] += len(dbas)
        dba_nums = []
        
        for dba in dbas:
            num = dba.get("numero")
            if num is not None:
                dba_nums.append(num)
            
            stmt = dba.get("enunciado") or dba.get("statement") or ""
            if not stmt or len(stmt.strip()) < 15:
                report[fname]["issues"].append(f"Grado {g_name} DBA #{num}: Enunciado vacío o extremadamente corto.")
                
            # check glued words like "Comprendelaimportancia"
            # 4 lowercase letters followed by lowercase without space in common words, or words > 30 chars
            long_words = [w for w in re.findall(r'[a-zA-ZáéíóúÁÉÍÓÚñÑ]{25,}', stmt)]
            if long_words:
                report[fname]["issues"].append(f"Grado {g_name} DBA #{num}: Palabras pegadas en enunciado: {long_words[:3]}")
                
            # check trailing noise
            if stmt.strip().endswith(("Por ejemplo:", "Por ejemplo :", "así como se muestra en el siguiente ejemplo:")):
                report[fname]["issues"].append(f"Grado {g_name} DBA #{num}: Enunciado termina con frase puente ('Por ejemplo:').")
                
            evids = dba.get("evidencias")
            if evids is None:
                # check if ejemplo_evidencia
                if "ejemplo_evidencia" in dba:
                    # special case for Ingles
                    pass
                else:
                    report[fname]["issues"].append(f"Grado {g_name} DBA #{num}: No tiene campo 'evidencias'.")
            elif isinstance(evids, list):
                report[fname]["total_evidencias"] += len(evids)
                if len(evids) == 0:
                    report[fname]["issues"].append(f"Grado {g_name} DBA #{num}: Lista de evidencias VACÍA (0).")
                for e_idx, ev in enumerate(evids):
                    ev_str = str(ev).strip()
                    if len(ev_str) < 10:
                        report[fname]["issues"].append(f"Grado {g_name} DBA #{num} Evid #{e_idx+1}: Muy corta ({len(ev_str)} chars): '{ev_str}'")
                    if ev_str.endswith((" y", " de", " la", " el", " en", " con", ",")):
                        report[fname]["issues"].append(f"Grado {g_name} DBA #{num} Evid #{e_idx+1}: Truncada al final: '...{ev_str[-25:]}'")
                    long_w_ev = [w for w in re.findall(r'[a-zA-ZáéíóúÁÉÍÓÚñÑ]{25,}', ev_str)]
                    if long_w_ev:
                        report[fname]["issues"].append(f"Grado {g_name} DBA #{num} Evid #{e_idx+1}: Palabras pegadas: {long_w_ev[:2]}")
            else:
                report[fname]["issues"].append(f"Grado {g_name} DBA #{num}: 'evidencias' no es lista.")
                
        # check sequentiality
        if dba_nums and all(isinstance(x, int) for x in dba_nums):
            expected = list(range(1, len(dba_nums) + 1))
            if sorted(dba_nums) != expected:
                report[fname]["issues"].append(f"Grado {g_name}: Numeración discontinua. Presentes: {sorted(dba_nums)}, Esperados: {expected}")

print("\n================== RESUMEN AUDITORIA ==================")
for fname, res in report.items():
    print(f"\n[{fname}]")
    print(f"  Estado: {res['status']}")
    print(f"  Grados: {res['total_grados']} | Total DBAs: {res['total_dbas']} | Total Evidencias: {res['total_evidencias']}")
    print(f"  Total Observaciones/Fallas: {len(res['issues'])}")
    for iss in res['issues'][:6]:
        print(f"    * {iss}")
    if len(res['issues']) > 6:
        print(f"    * ... (+{len(res['issues']) - 6} advertencias más)")

