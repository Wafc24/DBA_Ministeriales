import pymupdf, re

doc = pymupdf.open("DBA_C.Sociales-V2.pdf")
print("Total pages:", len(doc))

for p in range(7, len(doc)):
    txt = doc[p].get_text()
    g_match = re.search(r'Ciencias Sociales\s*•\s*Grado\s*(\d+)º?', txt, re.IGNORECASE)
    grade = g_match.group(1) if g_match else "Unknown"
    # also check DBA numbers on page
    dbas = re.findall(r'(?:^|\n)\s*(\d+)\.\s*\n', txt)
    print(f"Pág {p+1}: Grado {grade} | DBAs: {dbas}")
