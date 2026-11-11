import os, json, re
import pypdf

base_dir = r"D:\WILMER_FERRER\PRUEBAS PERIODICAS\5. SABER CHECK_2025\P.M.A\Planes por grados"

# We want only the 11 grades Math PMA PDFs
grades = [str(g) for g in range(1, 12)]

pma_catalog = {}

for g in grades:
    grade_dir_pattern = f"{g} Grado"
    grade_path = os.path.join(base_dir, grade_dir_pattern)
    if not os.path.exists(grade_path):
        continue
    
    # find math folder inside this grade
    mat_folder = None
    for entry in os.listdir(grade_path):
        lower = entry.lower()
        if "mat" in lower and ("-mat" in lower or "- mat" in lower or lower.startswith("mat")):
            mat_folder = os.path.join(grade_path, entry)
            break
            
    if not mat_folder:
        print(f"No mat folder for Grade {g}!")
        continue
        
    pma_catalog[g] = {}
    
    # Look for subfolders: 1. Numérico - Variacional, 2. Geométrico - Métrico, 3. Aleatorio
    for root, dirs, files in os.walk(mat_folder):
        for f in files:
            if f.lower().endswith(".pdf"):
                full_pdf = os.path.join(root, f)
                lower_path = full_pdf.lower()
                comp_key = None
                comp_name = None
                if "num" in lower_path or "var" in lower_path:
                    comp_key = "num_var"
                    comp_name = "Numérico - Variacional"
                elif "geom" in lower_path or "mtr" in lower_path or "metr" in lower_path or "espacial" in lower_path:
                    comp_key = "geom_met"
                    comp_name = "Geométrico - Métrico"
                elif "ale" in lower_path or "estad" in lower_path:
                    comp_key = "aleatorio"
                    comp_name = "Aleatorio"
                else:
                    comp_key = "general"
                    comp_name = "Matemáticas General"

                try:
                    reader = pypdf.PdfReader(full_pdf)
                    num_pages = len(reader.pages)
                    text_p1 = reader.pages[0].extract_text() if num_pages > 0 else ""
                    # extract title, standard, dba if mentioned
                    dbas_mentioned = re.findall(r'DBA[^\n\r\.\,\;]+', text_p1, re.IGNORECASE)
                except Exception as e:
                    num_pages = 0
                    text_p1 = ""
                    dbas_mentioned = []

                pma_catalog[g][comp_key] = {
                    "grade": g,
                    "component_key": comp_key,
                    "component_name": comp_name,
                    "filename": f,
                    "path": full_pdf,
                    "size_bytes": os.path.getsize(full_pdf),
                    "pages": num_pages,
                    "dbas_mentioned": dbas_mentioned[:5]
                }

print(f"Cataloged {len(pma_catalog)} grades.")
total_pdfs = sum(len(comps) for comps in pma_catalog.values())
print(f"Total Math PMA PDFs: {total_pdfs}")

for g in sorted(pma_catalog.keys(), key=lambda x: int(x)):
    comps = pma_catalog[g]
    print(f"Grado {g}°: {list(comps.keys())}")

with open("pma_math_catalog.json", "w", encoding="utf-8") as out:
    json.dump(pma_catalog, out, indent=2, ensure_ascii=False)
print("Saved to pma_math_catalog.json!")
