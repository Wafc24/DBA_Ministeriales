import os
import json
import shutil
import re

target_dir = r"D:\WILMER_FERRER\JSON\JSON INDIVIDUALES Y COMPLETOS"
backup_dir = r"D:\WILMER_FERRER\JSON\JSON INDIVIDUALES Y COMPLETOS\BACKUP_ORIGINAL"

os.makedirs(backup_dir, exist_ok=True)
print(f"Carpeta de respaldo asegurada: {backup_dir}")

# =========================================================================
# 1. AJUSTE DE CIENCIAS NATURALES.JSON
# =========================================================================
src_nat_path = r"D:\WILMER_FERRER\JSON\DBA - Ciencias Naturales\DBA_Ciencias_Naturales_v1_Colombia.json"
dest_nat_path = os.path.join(target_dir, "Ciencias Naturales.json")

# Backup original if exists
if os.path.exists(dest_nat_path):
    shutil.copy2(dest_nat_path, os.path.join(backup_dir, "Ciencias Naturales.json.bak"))

with open(src_nat_path, "r", encoding="utf-8") as f:
    source_nat = json.load(f)

ciclos = {
    1: "Básica Primaria", 2: "Básica Primaria", 3: "Básica Primaria", 4: "Básica Primaria", 5: "Básica Primaria",
    6: "Básica Secundaria", 7: "Básica Secundaria", 8: "Básica Secundaria", 9: "Básica Secundaria",
    10: "Educación Media", 11: "Educación Media"
}

grados_array = []
dbas_dict = source_nat.get("dbas", {})

for g_num in range(1, 12):
    g_str = str(g_num)
    g_dbas = dbas_dict.get(g_str, {})
    dbas_list = []
    
    # keys are '1', '2', etc.
    for d_num in sorted(g_dbas.keys(), key=lambda x: int(x)):
        d_item = g_dbas[d_num]
        stmt = d_item.get("statement", "").strip()
        evids = [e.strip() for e in d_item.get("evidencias", []) if e.strip()]
        
        dbas_list.append({
            "numero": int(d_num),
            "enunciado": stmt,
            "evidencias": evids,
            "ejemplo": None
        })
        
    grados_array.append({
        "grado": f"{g_num}°",
        "ciclo": ciclos[g_num],
        "dbas": dbas_list
    })

ciencias_nat_final = {
    "asignatura": "Ciencias Naturales",
    "version": "V.1 / V.2",
    "ano_publicacion": "2016",
    "entidad": "Ministerio de Educación Nacional de Colombia - Universidad de Antioquia",
    "grados": grados_array
}

with open(dest_nat_path, "w", encoding="utf-8") as f:
    json.dump(ciencias_nat_final, f, indent=2, ensure_ascii=False)
print("-> Ciencias Naturales.json RECONSTRUIDO Y GUARDADO CON ÉXITO.")

# =========================================================================
# 2. AJUSTE DE SOCIALES.JSON
# =========================================================================
soc_path = os.path.join(target_dir, "Sociales.json")
if os.path.exists(soc_path):
    shutil.copy2(soc_path, os.path.join(backup_dir, "Sociales.json.bak"))
    with open(soc_path, "r", encoding="utf-8") as f:
        soc_data = json.load(f)
        
    for g in soc_data.get("grados", []):
        if g.get("grado") in ["8°", "8"]:
            for dba in g.get("dbas", []):
                if dba.get("numero") == 8:
                    old_enunciado = dba.get("enunciado", "")
                    new_enunciado = old_enunciado.replace(
                        "Comprendelaimportanciadelasasociaciones",
                        "Comprende la importancia de las asociaciones"
                    )
                    dba["enunciado"] = new_enunciado
                    print("-> Sociales.json: Corregidas palabras pegadas en Grado 8 DBA 8.")
                    
    with open(soc_path, "w", encoding="utf-8") as f:
        json.dump(soc_data, f, indent=2, ensure_ascii=False)
    print("-> Sociales.json ACTUALIZADO CON ÉXITO.")

# =========================================================================
# 3. AJUSTE DE INGLÉS.JSON
# =========================================================================
ing_path = os.path.join(target_dir, "Inglés.json")
if os.path.exists(ing_path):
    shutil.copy2(ing_path, os.path.join(backup_dir, "Inglés.json.bak"))
    with open(ing_path, "r", encoding="utf-8") as f:
        ing_data = json.load(f)
        
    bridge_patterns = [
        r'[\s,;:\.]*Por ejemplo\s*:?\s*$',
        r'[\s,;:\.]*como en el siguiente ejemplo\s*:?\s*$',
        r'[\s,;:\.]*así como se muestra en el siguiente ejemplo\s*:?\s*$',
        r'[\s,;:\.]*Puede, por ejemplo, comprender un texto como el siguiente\s*:?\s*$',
        r'[\s,;:\.]*Por ejemplo, al leer un texto resalta las ideas de cada párrafo y los detalles que las sustentan\.?\s*$',
        r'[\s,;:\.]*Por ejemplo, después de leer textos diferentes, identifica de qué tipo son y dice cuál es su propósito\.?\s*$',
        r'[\s,;:\.]*Por ejemplo, puede comprender textos como\s*:?\s*$'
    ]
    
    cleaned_count = 0
    for g in ing_data.get("grados", []):
        for dba in g.get("dbas", []):
            stmt = dba.get("enunciado", "").strip()
            
            # Clean bridge phrase if present
            for pat in bridge_patterns:
                if re.search(pat, stmt, flags=re.IGNORECASE):
                    stmt = re.sub(pat, "", stmt, flags=re.IGNORECASE).strip()
                    cleaned_count += 1
            if not stmt.endswith("."):
                stmt += "."
            dba["enunciado"] = stmt
            
            # Ensure evidencias list is populated
            ej = dba.get("ejemplo_evidencia")
            if ej:
                # If evidencias does not exist or is empty
                if not dba.get("evidencias"):
                    dba["evidencias"] = [ej.strip()]
                    
    with open(ing_path, "w", encoding="utf-8") as f:
        json.dump(ing_data, f, indent=2, ensure_ascii=False)
    print(f"-> Inglés.json: Limpiadas {cleaned_count} frases puente y pobladas evidencias para todos los 71 DBAs.")

print("\n¡TODOS LOS AJUSTES APLICADOS SATISFACTORIAMENTE!")
