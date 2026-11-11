import pymupdf, re, json

doc = pymupdf.open("DBA_Lenguaje-min.pdf")

# Grade page ranges in Lenguaje V2
grade_pages = {
    "1": (7, 10),
    "2": (11, 14),
    "3": (15, 18),
    "4": (19, 22),
    "5": (23, 26),
    "6": (27, 30),
    "7": (31, 34),
    "8": (35, 38),
    "9": (39, 42),
    "10": (43, 46),
    "11": (47, 51)
}

lenguaje_dbas = {}

def clean_text(t):
    # join broken lines
    lines = [l.strip() for l in t.split('\n') if l.strip()]
    return " ".join(lines)

for grade, (p_start, p_end) in grade_pages.items():
    lenguaje_dbas[grade] = {}
    for p in range(p_start, p_end + 1):
        txt = doc[p].get_text()
        
        # split by DBA number patterns: e.g. "\n1.\n", "\n2.\n", etc.
        # or match blocks like: (\d+)\.\n([\s\S]*?)Evidencias de aprendizaje\n([\s\S]*?)(?:Ejemplo|Lenguaje •|\Z)
        # Note: on a page there can be 1 or 2 DBAs
        blocks = re.split(r'(?:^|\n)\s*(\d+)\.\s*\n', txt)
        # blocks[0] is header
        # blocks[1] is dba_num, blocks[2] is content, blocks[3] is dba_num, blocks[4] is content...
        for i in range(1, len(blocks), 2):
            dba_num = blocks[i].strip()
            content = blocks[i+1]
            
            # extract statement and evidencias
            if "Evidencias de aprendizaje" in content:
                parts = content.split("Evidencias de aprendizaje", 1)
                raw_stmt = parts[0]
                evid_part = parts[1]
                
                # stop at Ejemplo or page footer
                evid_part = re.split(r'(?:Ejemplo|Lenguaje\s*•|\d+\.\s*\n)', evid_part)[0]
                
                stmt = clean_text(raw_stmt)
                
                # Evidences start with bullet 'm ' or 'm\t'
                raw_evids = re.split(r'(?:^|\n)\s*m\s+(?=[A-ZÁÉÍÓÚÑ])', evid_part)
                evidencias = []
                for ev in raw_evids:
                    ev_clean = clean_text(ev)
                    if len(ev_clean) > 5 and not ev_clean.startswith("Derechos Básicos"):
                        evidencias.append(ev_clean)
                        
                lenguaje_dbas[grade][dba_num] = {
                    "statement": stmt,
                    "evidencias": evidencias
                }

total_dbas = sum(len(v) for v in lenguaje_dbas.values())
total_evids = sum(sum(len(d["evidencias"]) for d in v.values()) for v in lenguaje_dbas.values())
print(f"Extracted Lenguaje V2: {total_dbas} DBAs, {total_evids} evidencias")
for g in sorted(lenguaje_dbas.keys(), key=lambda x: int(x)):
    print(f"Grado {g}°: {len(lenguaje_dbas[g])} DBAs -> nums: {list(lenguaje_dbas[g].keys())}")

with open("literal_lenguaje_v2.json", "w", encoding="utf-8") as out:
    json.dump(lenguaje_dbas, out, indent=2, ensure_ascii=False)
print("Saved to literal_lenguaje_v2.json!")
