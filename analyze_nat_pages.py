import pymupdf, re

doc = pymupdf.open(r"D:\WILMER_FERRER\Mat - Soportes\Ciencias Naturales\DBA_C.Naturales-min.pdf")
print("Total pages in Naturales:", len(doc))

for i in range(len(doc)):
    txt = doc[i].get_text()
    lines = [l.strip() for l in txt.split('\n') if l.strip()]
    header = lines[0] if lines else ""
    grade_mentions = re.findall(r'(?:Grado\s+([A-Za-z0-9°]+)|\b([1-9]|10|11)°)', txt, re.IGNORECASE)
    dbas = re.findall(r'(?:^|\n)\s*(\d+)\.\s*\n', txt)
    if dbas:
        print(f"Pág {i+1}: header='{header[:30]}' | DBAs: {dbas} | grades: {grade_mentions[:3]}")
