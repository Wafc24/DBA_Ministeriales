import pymupdf, re

doc = pymupdf.open("DBA_Ingles_6_11.pdf")
print("=== INGLES 6-11 ===")
for p in range(14, len(doc)):
    txt = doc[p].get_text()
    g_match = re.search(r'Grado\s+(\d+)', txt, re.IGNORECASE)
    if g_match:
        g = g_match.group(1)
        # find DBAs on page
        # DBA numbers appear as standalone digits or with statement
        dbas = re.findall(r'(?:^|\n)\s*(\d+)\s*\n([A-ZÁÉÍÓÚ][^\n]+)', txt)
        print(f"Page {p+1}: Grado {g} -> DBAs: {dbas}")
