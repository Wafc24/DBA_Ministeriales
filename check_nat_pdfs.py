import os
import pymupdf

nat_dir = r"D:\WILMER_FERRER\JSON\MEN DBA DIVIDIDOS\DBA Nat"
for fname in sorted(os.listdir(nat_dir)):
    if not fname.endswith('.pdf'):
        continue
    fpath = os.path.join(nat_dir, fname)
    doc = pymupdf.open(fpath)
    print(f"=== {fname} ({len(doc)} pages) ===")
    for pno in range(len(doc)):
        text = doc[pno].get_text()
        first_line = text.split('\n')[0] if text else ''
        print(f"  P{pno}: chars={len(text)} | first={repr(first_line[:50])}")
