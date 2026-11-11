import pymupdf, re, json

doc = pymupdf.open("DBA_Lenguaje-min.pdf")
print("Total pages in Lenguaje:", len(doc))

# Let's inspect page texts to understand grade division
# Let's search for "Grado Primero", "Grado Segundo", or "1°", etc.
for i in range(len(doc)):
    txt = doc[i].get_text()
    lines = [l.strip() for l in txt.split('\n') if l.strip()]
    header = lines[0] if lines else ""
    # find any mention of Grado or grade number
    grade_mentions = re.findall(r'(?:Grado\s+([A-Za-z0-9°]+)|\b([1-9]|10|11)°)', txt, re.IGNORECASE)
    dbas = re.findall(r'(?:^|\n)\s*(\d+)\.\s*\n', txt)
    if dbas:
        print(f"Pág {i+1}: header='{header[:30]}' | DBAs: {dbas} | grades: {grade_mentions[:3]}")
