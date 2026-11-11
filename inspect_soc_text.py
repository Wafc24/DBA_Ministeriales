import pymupdf

doc = pymupdf.open("DBA_C.Sociales-V2.pdf")

with open("soc_sample.txt", "w", encoding="utf-8") as out:
    for p in [7, 8, 9, 10]:
        out.write(f"=== PAGE {p+1} ===\n")
        out.write(doc[p].get_text() + "\n")
        out.write("="*60 + "\n")
print("Written to soc_sample.txt")
