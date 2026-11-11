import pymupdf, re, json

doc = pymupdf.open("DBA_C.Sociales-V2.pdf")

soc_grade_pages = {
    "1": (7, 10),
    "2": (11, 15),
    "3": (16, 19),
    "4": (20, 23),
    "5": (24, 27),
    "6": (28, 31),
    "7": (32, 36),
    "8": (37, 40),
    "9": (41, 44),
    "10": (45, 47),
    "11": (48, 50)
}

def clean_text(t):
    lines = [l.strip() for l in t.split('\n') if l.strip()]
    return " ".join(lines)

def get_page_text(page):
    w = page.rect.width
    h = page.rect.height
    # In Sociales, text is in two columns: left (x0 < 310), right (x0 >= 310)
    col1 = page.get_text("text", clip=pymupdf.Rect(0, 50, 310, h - 40))
    col2 = page.get_text("text", clip=pymupdf.Rect(310, 50, w, h - 40))
    return col1 + "\n" + col2

sociales_dbas = {}

for grade, (p_start, p_end) in soc_grade_pages.items():
    sociales_dbas[grade] = {}
    full_grade_text = ""
    for p in range(p_start, p_end + 1):
        full_grade_text += "\n" + get_page_text(doc[p])
        
    # Split by DBA number pattern: \n(\d+)\.\n
    # Look for \n1.\n, \n2.\n ...
    blocks = re.split(r'\n\s*(\d+)\.\s*\n', full_grade_text)
    for i in range(1, len(blocks), 2):
        dba_num = blocks[i].strip()
        content = blocks[i+1]
        
        if "Evidencias de aprendizaje" in content:
            parts = content.split("Evidencias de aprendizaje", 1)
            raw_stmt = parts[0]
            evid_part = parts[1]
            
            # clean stmt (stop before next number or footer)
            stmt = clean_text(raw_stmt)
            
            # split evidences by 'l ' or 'l\t' or 'l\n'
            raw_evids = re.split(r'(?:^|\n)\s*l\s+(?=[A-ZÁÉÍÓÚÑ])', evid_part)
            evidencias = []
            for ev in raw_evids:
                ev_clean = clean_text(ev)
                # filter out navigation noise
                if len(ev_clean) > 8 and not any(k in ev_clean for k in ["Ciencias Sociales", "Derechos Básicos", "Grado"]):
                    evidencias.append(ev_clean)
                    
            # if dba_num not already extracted or has more evidences, keep it
            if dba_num not in sociales_dbas[grade] or len(evidencias) > len(sociales_dbas[grade][dba_num]["evidencias"]):
                sociales_dbas[grade][dba_num] = {
                    "statement": stmt,
                    "evidencias": evidencias
                }

total_dbas = sum(len(v) for v in sociales_dbas.values())
total_evids = sum(sum(len(d["evidencias"]) for d in v.values()) for v in sociales_dbas.values())
print(f"Extracted Sociales V2: {total_dbas} DBAs, {total_evids} evidencias")
for g in sorted(sociales_dbas.keys(), key=lambda x: int(x)):
    print(f"Grado {g}°: {len(sociales_dbas[g])} DBAs -> nums: {sorted(list(sociales_dbas[g].keys()), key=lambda x: int(x))}")

with open("literal_sociales_v2.json", "w", encoding="utf-8") as out:
    json.dump(sociales_dbas, out, indent=2, ensure_ascii=False)
print("Saved to literal_sociales_v2.json!")
