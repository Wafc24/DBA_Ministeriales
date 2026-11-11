"""
Script de unificación y compilación curricular - Asesorías Pedagógicas S.A.S.
Escanea todos los archivos JSON de 'D:\\WILMER_FERRER\\JSON\\JSON INDIVIDUALES Y COMPLETOS'
y genera el banco de datos centralizado 'dbas_master_data.js'.
"""

import os
import json
import re

SOURCE_DIR = r"D:\WILMER_FERRER\JSON\JSON INDIVIDUALES Y COMPLETOS"
OUTPUT_FILE = r"d:\WILMER_FERRER\JSON\DBA_Antigravity\dbas_master_data.js"

CICLO_MAP = {
    0: "Educación Inicial",
    1: "Ciclo I",
    2: "Ciclo I",
    3: "Ciclo I",
    4: "Ciclo II",
    5: "Ciclo II",
    6: "Ciclo III",
    7: "Ciclo III",
    8: "Ciclo IV",
    9: "Ciclo IV",
    10: "Ciclo V",
    11: "Ciclo V"
}

SUBJECT_PREFIX = {
    "matematicas": "MAT",
    "matematicas_v1": "MAT_V1",
    "lenguaje": "LEN",
    "lenguaje_v1": "LEN_V1",
    "sociales": "SOC",
    "naturales": "NAT",
    "ingles": "ING"
}

def parse_grade(g_val):
    if isinstance(g_val, int):
        return g_val
    g_str = str(g_val).strip().lower()
    if "transici" in g_str:
        return 0
    m = re.search(r'\d+', g_str)
    if m:
        return int(m.group(0))
    return 1

def generate_title(item, subject):
    # Si tiene factor o pensamiento, usarlo
    if item.get("factor"):
        return item["factor"].strip()
    if item.get("pensamiento"):
        return item["pensamiento"].strip()
    if item.get("aclaracion"):
        return item["aclaracion"].strip()
    
    # Generar título conciso a partir del enunciado
    enunciado = item.get("enunciado", "").strip()
    if not enunciado:
        return f"DBA {item.get('numero', 1)}"
    
    # Limpiar verbos introductorios comunes para hacer un título temático
    # Tomar la primera oración o frase clave
    clean = re.sub(r'^(Comprende|Identifica|Reconoce|Utiliza|Explica|Describe|Interpreta|Resuelve|Relaciona|Caracteriza|Analiza|Propone|Produce|Organiza|Clasifica|Compara|Formula|Evalúa|Distingue|Asocia)\s+(que|los|las|el|la|de|en|como)?\s*', '', enunciado, flags=re.IGNORECASE)
    # Cortar en el primer signo de puntuación significativo (paréntesis, punto, punto y coma)
    first_chunk = re.split(r'[\.\;\:\(]', clean)[0].strip()
    if len(first_chunk) > 65:
        first_chunk = first_chunk[:62].rsplit(' ', 1)[0] + '...'
    if first_chunk:
        # Capitalizar primera letra
        return first_chunk[0].upper() + first_chunk[1:]
    return f"DBA {item.get('numero', 1)}"

def process_file(filepath, subject_key, version_label):
    dbas_list = []
    prefix = SUBJECT_PREFIX.get(subject_key, "DBA")
    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)
    
    grados = data.get("grados", [])
    for g in grados:
        g_raw = g.get("grado")
        grade_num = parse_grade(g_raw)
        ciclo = g.get("ciclo") or CICLO_MAP.get(grade_num, "Básica")
        
        dbas = g.get("dbas", [])
        for dba_raw in dbas:
            num = dba_raw.get("numero", 1)
            try:
                num = int(num)
            except:
                num = 1
            
            dba_id = f"{prefix}_G{grade_num}_DBA{num}"
            enunciado = dba_raw.get("enunciado", "").strip()
            
            # Evidencias: lista limpia de strings
            raw_evids = dba_raw.get("evidencias", [])
            evidencias = []
            if isinstance(raw_evids, list):
                for ev in raw_evids:
                    if isinstance(ev, str) and ev.strip():
                        evidencias.append(ev.strip())
                    elif isinstance(ev, dict):
                        ev_text = ev.get("enunciado") or ev.get("texto") or str(ev)
                        if ev_text.strip():
                            evidencias.append(ev_text.strip())
            
            # Ejemplo
            ejemplo = dba_raw.get("ejemplo") or dba_raw.get("ejemplo_evidencia")
            if ejemplo and isinstance(ejemplo, str):
                ejemplo = ejemplo.strip()
            else:
                ejemplo = None
                
            factor = dba_raw.get("factor") or dba_raw.get("pensamiento") or dba_raw.get("aclaracion")
            if factor and isinstance(factor, str):
                factor = factor.strip()
            else:
                factor = None

            habilidades = dba_raw.get("habilidades")

            title = generate_title(dba_raw, subject_key)

            item = {
                "id": dba_id,
                "grade": grade_num,
                "ciclo": ciclo,
                "subject": subject_key.replace("_v1", ""),
                "dba": f"DBA {num}",
                "dba_num": num,
                "title": title,
                "enunciado": enunciado,
                "evidencias": evidencias,
                "ejemplo": ejemplo,
                "factor": factor,
                "version": version_label
            }
            if habilidades:
                item["habilidades"] = habilidades

            dbas_list.append(item)
            
    return dbas_list

def main():
    print("Iniciando compilación del banco curricular unificado...")
    
    # 1. Matemáticas V2 (1-5 y 6-11)
    mat_v2_p1 = process_file(os.path.join(SOURCE_DIR, "Matemáticas_1-5.json"), "matematicas", "V.2")
    mat_v2_p2 = process_file(os.path.join(SOURCE_DIR, "Matemáticas_6-11.json"), "matematicas", "V.2")
    matematicas = mat_v2_p1 + mat_v2_p2
    
    # 2. Matemáticas V1
    matematicas_v1 = process_file(os.path.join(SOURCE_DIR, "Matemáticas_V1.json"), "matematicas_v1", "V.1")
    
    # 3. Lenguaje V2 (1-5 y 6-11)
    len_v2_p1 = process_file(os.path.join(SOURCE_DIR, "Lenguaje_1-5.json"), "lenguaje", "V.2")
    len_v2_p2 = process_file(os.path.join(SOURCE_DIR, "Lenguaje_6-11.json"), "lenguaje", "V.2")
    lenguaje = len_v2_p1 + len_v2_p2
    
    # 4. Lenguaje V1
    lenguaje_v1 = process_file(os.path.join(SOURCE_DIR, "Lenguaje_V1.json"), "lenguaje_v1", "V.1")
    
    # 5. Sociales
    sociales = process_file(os.path.join(SOURCE_DIR, "Sociales.json"), "sociales", "V.2")
    
    # 6. Naturales
    naturales = process_file(os.path.join(SOURCE_DIR, "Ciencias Naturales.json"), "naturales", "V.2")
    
    # 7. Inglés
    ingles = process_file(os.path.join(SOURCE_DIR, "Inglés.json"), "ingles", "V.1")

    # Estadísticas
    print("\n--- RESUMEN DE COMPILACIÓN ---")
    print(f"Matemáticas (V.2): {len(matematicas)} DBAs (Grados 1 a 11)")
    print(f"Matemáticas (V.1): {len(matematicas_v1)} DBAs (Grados 1 a 11)")
    print(f"Lenguaje (V.2): {len(lenguaje)} DBAs (Grados 1 a 11)")
    print(f"Lenguaje (V.1): {len(lenguaje_v1)} DBAs (Grados 1 a 11)")
    print(f"Ciencias Sociales: {len(sociales)} DBAs (Grados 1 a 11)")
    print(f"Ciencias Naturales: {len(naturales)} DBAs (Grados 1 a 11)")
    print(f"Inglés: {len(ingles)} DBAs (Transición y 1 a 11)")

    master_database = {
        "matematicas": matematicas,
        "matematicas_v1": matematicas_v1,
        "lenguaje": lenguaje,
        "lenguaje_v1": lenguaje_v1,
        "sociales": sociales,
        "naturales": naturales,
        "ingles": ingles
    }

    # Serializar en dbas_master_data.js
    header = """/**
 * PLATAFORMA CURRICULAR UNIFICADA MEN - ASESORÍAS PEDAGÓGICAS S.A.S.
 * Banco Maestro Centralizado de Derechos Básicos de Aprendizaje (DBA)
 * 100% Literal Oficial MEN Colombia • Todas las áreas y grados
 * Generado automáticamente por build_curriculo.py
 */
"""
    json_str = json.dumps(master_database, ensure_ascii=False, indent=2)
    js_content = f"{header}\nvar MASTER_DBA_DATABASE = {json_str};\nif (typeof window !== 'undefined') {{ window.MASTER_DBA_DATABASE = MASTER_DBA_DATABASE; }}\nif (typeof globalThis !== 'undefined') {{ globalThis.MASTER_DBA_DATABASE = MASTER_DBA_DATABASE; }}\n"
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"\n[OK] Archivo centralizado '{OUTPUT_FILE}' generado con exito. Tamano: {len(js_content):,} bytes.")

if __name__ == "__main__":
    main()
