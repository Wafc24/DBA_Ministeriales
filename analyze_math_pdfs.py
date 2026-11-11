import os, glob
import pypdf

base_dir = r"D:\WILMER_FERRER\PRUEBAS PERIODICAS\5. SABER CHECK_2025\P.M.A\Planes por grados"

pdf_files = []
for root, dirs, files in os.walk(base_dir):
    if "-mat" in root.lower() or "mat" in root.lower():
        for f in files:
            if f.lower().endswith(".pdf"):
                full_path = os.path.join(root, f)
                pdf_files.append(full_path)

print(f"Total Math PDFs found: {len(pdf_files)}")

data = []
for p in pdf_files:
    rel = os.path.relpath(p, base_dir)
    size = os.path.getsize(p)
    try:
        reader = pypdf.PdfReader(p)
        pages = len(reader.pages)
        first_page = reader.pages[0].extract_text() if pages > 0 else ""
        first_lines = [l.strip() for l in first_page.split("\n") if l.strip()][:6]
    except Exception as e:
        pages = 0
        first_lines = [str(e)]
    data.append({
        "path": p,
        "rel": rel,
        "size": size,
        "pages": pages,
        "header": " | ".join(first_lines)
    })

for item in sorted(data, key=lambda x: x["rel"]):
    print(f"[{item['pages']} pgs, {item['size']//1024} KB] {item['rel']}")
    print(f"   Header: {item['header'][:150]}")
