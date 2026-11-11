import os
import json
import pymupdf

leng_pdf_dir = r"D:\WILMER_FERRER\JSON\MEN DBA DIVIDIDOS\DBA Leng"
target_dir = r"D:\WILMER_FERRER\JSON\JSON INDIVIDUALES Y COMPLETOS"

def verify_leng(fname):
    with open(os.path.join(target_dir, fname), "r", encoding="utf-8") as f:
        d = json.load(f)
    print(f"=== VERIFICANDO {fname} ===")
    for g_item in d.get("grados", []):
        grado_str = g_item.get("grado", "").replace("°", "").strip()
        dbas = g_item.get("dbas", [])
        
        # find matching pdf
        matching_pdfs = [p for p in os.listdir(leng_pdf_dir) if p.startswith(f"{grado_str} ") or p.startswith(f"{grado_str}-")]
        if not matching_pdfs:
            # fallback to full PDF
            matching_pdfs = ["DBA_Lenguaje-min.pdf"]
        
        pdf_path = os.path.join(leng_pdf_dir, matching_pdfs[0])
        doc = pymupdf.open(pdf_path)
        full_pdf_text = " ".join([" ".join(page.get_text().split()) for page in doc])
        
        match_count = 0
        for dba in dbas:
            num = dba.get("numero")
            stmt = dba.get("enunciado", "")
            snippet = " ".join(stmt[:40].split())
            if snippet in full_pdf_text:
                match_count += 1
            else:
                print(f"  [ALERTA] Grado {grado_str} DBA {num} no coincide exacto: '{snippet}'")
        print(f"Grado {grado_str}: {match_count}/{len(dbas)} DBAs coinciden con PDF {matching_pdfs[0]}")

verify_leng("Lenguaje_1-5.json")
verify_leng("Lenguaje_6-11.json")
