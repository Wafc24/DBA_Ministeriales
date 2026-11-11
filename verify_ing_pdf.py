import os
import json
import pymupdf

ing_pdf_dir = r"D:\WILMER_FERRER\JSON\MEN DBA DIVIDIDOS\DBA Ing"
target_dir = r"D:\WILMER_FERRER\JSON\JSON INDIVIDUALES Y COMPLETOS"

def verify_ing():
    with open(os.path.join(target_dir, "Inglés.json"), "r", encoding="utf-8") as f:
        d = json.load(f)
    print("=== VERIFICANDO Inglés.json ===")
    
    doc1 = pymupdf.open(os.path.join(ing_pdf_dir, "1-5 DBA-TRANSICIÓN-Y-PRIMARIA_Inglés-min.pdf"))
    text_1_5 = " ".join([" ".join(p.get_text().split()) for p in doc1])
    
    doc2 = pymupdf.open(os.path.join(ing_pdf_dir, "6-11 dba-ingles-2017 (1).pdf"))
    text_6_11 = " ".join([" ".join(p.get_text().split()) for p in doc2])
    
    for g_item in d.get("grados", []):
        grado_str = g_item.get("grado", "")
        dbas = g_item.get("dbas", [])
        is_primaria = grado_str in ["Transición", "1°", "2°", "3°", "4°", "5°"]
        ref_text = text_1_5 if is_primaria else text_6_11
        
        match_count = 0
        for dba in dbas:
            num = dba.get("numero")
            stmt = dba.get("enunciado", "")
            # take first 30 chars
            snippet = " ".join(stmt[:30].split())
            if snippet in ref_text:
                match_count += 1
            else:
                print(f"  [ALERTA] Grado {grado_str} DBA {num} no coincide: '{snippet}'")
        print(f"Grado {grado_str}: {match_count}/{len(dbas)} DBAs coinciden con PDF oficial.")

verify_ing()
