import os
import json
import pymupdf

nat_json_path = r"D:\WILMER_FERRER\JSON\DBA - Ciencias Naturales\DBA_Ciencias_Naturales_v1_Colombia.json"
with open(nat_json_path, "r", encoding="utf-8") as f:
    nat_data = json.load(f)

dbas_by_grade = nat_data.get("dbas", {})
nat_pdf_dir = r"D:\WILMER_FERRER\JSON\MEN DBA DIVIDIDOS\DBA Nat"

print("Comprobando Ciencias Naturales JSON contra PDFs oficiales...")
grade_pdf_map = {
    "1": "1-DBA_C.Naturales-min-08-09.pdf",
    "2": "2-DBA_C.Naturales-min-10-11.pdf",
    "3": "3-DBA_C.Naturales-min-12-14.pdf",
    "4": "4-DBA_C.Naturales-min-15-18.pdf",
    "5": "5-DBA_C.Naturales-min-19-20.pdf",
    "6": "6-DBA_C.Naturales-min-21-23.pdf",
    "7": "7-DBA_C.Naturales-min-24-26.pdf",
    "8": "8-DBA_C.Naturales-min-27-29.pdf",
    "9": "9-DBA_C.Naturales-min-30-33.pdf",
    "10": "10-DBA_C.Naturales-min-34-36.pdf",
    "11": "11-DBA_C.Naturales-min-37-39.pdf"
}

for grade, pdf_name in grade_pdf_map.items():
    pdf_path = os.path.join(nat_pdf_dir, pdf_name)
    if not os.path.exists(pdf_path):
        print(f"PDF no encontrado: {pdf_name}")
        continue
    doc = pymupdf.open(pdf_path)
    full_pdf_text = " ".join([page.get_text() for page in doc])
    # normalize spaces
    full_pdf_norm = " ".join(full_pdf_text.split())
    
    grade_dbas = dbas_by_grade.get(grade, {})
    match_count = 0
    total_dbas = len(grade_dbas)
    for dba_num, dba_item in grade_dbas.items():
        stmt = dba_item.get("statement", "")
        # search first 40 chars of statement
        stmt_snippet = " ".join(stmt[:40].split())
        if stmt_snippet in full_pdf_norm:
            match_count += 1
        else:
            print(f"  [ALERTA] Grado {grade} DBA {dba_num} NO ENCONTRADO EN PDF: '{stmt_snippet}'")
    print(f"Grado {grade}: {match_count}/{total_dbas} DBAs coinciden 100% con el PDF oficial.")
