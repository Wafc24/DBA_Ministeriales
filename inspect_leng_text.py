import pymupdf

doc = pymupdf.open("DBA_Lenguaje-min.pdf")

# Let's inspect page 8 (Grado 1, DBAs 1 & 2) and page 11 (Grado 1, DBAs 7 & 8)
with open("leng_sample.txt", "w", encoding="utf-8") as out:
    for p in [7, 8, 9, 10]:
        out.write(f"=== PAGE {p+1} ===\n")
        out.write(doc[p].get_text() + "\n")
        out.write("="*60 + "\n")
print("Written to leng_sample.txt")
