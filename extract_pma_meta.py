import json, os, re
import pypdf

base_dir = r"D:\WILMER_FERRER\PRUEBAS PERIODICAS\5. SABER CHECK_2025\P.M.A\Planes por grados"

with open("pma_math_catalog.json", "r", encoding="utf-8") as f:
    cat = json.load(f)

extracted_pma_data = {}

for g in sorted(cat.keys(), key=lambda x: int(x)):
    extracted_pma_data[g] = {}
    for comp_key in ["num_var", "geom_met", "aleatorio"]:
        item = cat[g].get(comp_key)
        if not item:
            continue
        pdf_path = item["path"]
        reader = pypdf.PdfReader(pdf_path)
        num_pages = len(reader.pages)
        
        full_text = ""
        for p in reader.pages:
            full_text += p.extract_text() + "\n"

        # Extract standard
        estandar_match = re.search(r'Est[aá]ndar(?:\s+B[aá]sico\s+de\s+Competencia)?(?:\s*\([^)]*\))?\s*:\s*([^.\n\r]+(?:\.|\n))', full_text, re.IGNORECASE)
        estandar = estandar_match.group(1).strip() if estandar_match else ""
        if len(estandar) < 10:
            estandar_match2 = re.search(r'Est[aá]ndar[^\n\r:]*:\s*([^\n\r]+)', full_text, re.IGNORECASE)
            estandar = estandar_match2.group(1).strip() if estandar_match2 else "Desarrollo de competencias y resolución de problemas matemáticos."

        # Extract DBAs mentioned
        dbas = re.findall(r'(?:DBA[-–\s\d]*[a-zA-Z0-9\.\-]+:\s*[^.\n\r]+|\bDBA\s*#?\s*\d+[^.\n\r]+)', full_text, re.IGNORECASE)
        cleaned_dbas = []
        for d in dbas:
            d_clean = re.sub(r'\s+', ' ', d).strip()
            if len(d_clean) > 8 and d_clean not in cleaned_dbas:
                cleaned_dbas.append(d_clean)

        # Extract activities
        acts = re.findall(r'Actividad\s+\d+\s*:\s*([^.\n\r\(]+)', full_text, re.IGNORECASE)
        cleaned_acts = [re.sub(r'\s+', ' ', a).strip() for a in acts if len(a.strip()) > 3]
        # remove duplicates preserving order
        unique_acts = []
        for a in cleaned_acts:
            if a not in unique_acts:
                unique_acts.append(a)

        # Thought mapping
        comp_display = {
            "num_var": "Pensamiento Numérico - Variacional",
            "geom_met": "Pensamiento Espacial - Métrico",
            "aleatorio": "Pensamiento Aleatorio (Estadística)"
        }[comp_key]

        extracted_pma_data[g][comp_key] = {
            "grade": g,
            "component_key": comp_key,
            "component_title": comp_display,
            "filename": item["filename"],
            "pages": num_pages,
            "standard": estandar[:250],
            "dbas_articulados": cleaned_dbas[:4],
            "actividades": unique_acts[:5]
        }

with open("pma_detailed_content.json", "w", encoding="utf-8") as out:
    json.dump(extracted_pma_data, out, indent=2, ensure_ascii=False)

print("Saved pma_detailed_content.json successfully!")
