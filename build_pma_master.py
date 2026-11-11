import json

with open("pma_drive_catalog.json", "r", encoding="utf-8") as f:
    drive_data = json.load(f)

with open("pma_detailed_content.json", "r", encoding="utf-8") as f:
    detail_data = json.load(f)

GRADE_NAMES = {
    "1": "1° de Primaria", "2": "2° de Primaria", "3": "3° de Primaria",
    "4": "4° de Primaria", "5": "5° de Primaria", "6": "6° de Secundaria",
    "7": "7° de Secundaria", "8": "8° de Secundaria", "9": "9° de Secundaria",
    "10": "10° Media Vocacional", "11": "11° Media Vocacional"
}

COMP_ICONS = {
    "num_var": "🔢",
    "geom_met": "📐",
    "aleatorio": "📊"
}

master_pma = {}

for g in sorted(drive_data.keys(), key=lambda x: int(x)):
    master_pma[g] = []
    for comp_key in ["num_var", "geom_met", "aleatorio"]:
        drv = drive_data[g].get(comp_key, {})
        det = detail_data.get(g, {}).get(comp_key, {})
        
        comp_title = {
            "num_var": "Pensamiento Numérico - Variacional",
            "geom_met": "Pensamiento Espacial - Métrico",
            "aleatorio": "Pensamiento Aleatorio y Sistemas de Datos"
        }[comp_key]

        entry = {
            "grade": g,
            "grade_label": GRADE_NAMES.get(g, f"Grado {g}°"),
            "component_key": comp_key,
            "component_name": comp_title,
            "icon": COMP_ICONS.get(comp_key, "📄"),
            "pdf_title": drv.get("title", det.get("filename", f"Plan de Mejoramiento {g}°")),
            "file_id": drv.get("file_id", ""),
            "drive_view_url": drv.get("drive_view_url", f"https://drive.google.com/drive/folders/1j903O-frGgmELmnRksmOMSR3Yk_dRBUN"),
            "drive_download_url": drv.get("drive_download_url", ""),
            "pages": det.get("pages", 6),
            "standard": det.get("standard", "Competencias y resolución de problemas matemáticos."),
            "dbas_articulados": det.get("dbas_articulados", []),
            "actividades": det.get("actividades", [])
        }
        master_pma[g].append(entry)

with open("pma_master.json", "w", encoding="utf-8") as out:
    json.dump(master_pma, out, indent=2, ensure_ascii=False)

print(f"Generated pma_master.json with {len(master_pma)} grades, total {sum(len(v) for v in master_pma.values())} plans!")
