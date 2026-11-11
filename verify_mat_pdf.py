import os
import json
import pymupdf

mat_pdf_dir = r"D:\WILMER_FERRER\JSON\MEN DBA DIVIDIDOS\DBA Mat"
target_dir = r"D:\WILMER_FERRER\JSON\JSON INDIVIDUALES Y COMPLETOS"

def verify_mat(fname):
    with open(os.path.join(target_dir, fname), "r", encoding="utf-8") as f:
        d = json.load(f)
    print(f"=== VERIFICANDO {fname} ===")
    for g_item in d.get("grados", []):
        grado_str = g_item.get("grado", "").replace("°", "").strip()
        dbas = g_item.get("dbas", [])
        
        matching_pdfs = [p for p in os.listdir(mat_pdf_dir) if p.startswith(f"{grado_str}-")]
        if not matching_pdfs:
            print(f"No PDF found for Grado {grado_str}")
            continue
        
        pdf_path = os.path.join(mat_pdf_dir, matching_pdfs[0])
        doc = pymupdf.open(pdf_path)
        full_pdf_text = " ".join([" ".join(page.get_text().split()) for page in doc])
        
        match_count = 0
        for dba in dbas:
            num = dba.get("numero")
            stmt = dba.get("enunciado", "")
            snippet = " ".join(stmt[:35].split())
            if snippet in full_pdf_text:
                match_count += 1
            else:
                print(f"  [ALERTA] Grado {grado_str} DBA {num} no coincide exacto: '{snippet}'")
        print(f"Grado {grado_str}: {match_count}/{len(dbas)} DBAs coinciden con PDF {matching_pdfs[0]}")

verify_mat("Matemáticas_1-5.json")
verify_mat("Matemáticas_6-11.json")
