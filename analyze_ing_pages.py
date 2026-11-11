import pymupdf, re

def check_ing(name, path):
    doc = pymupdf.open(path)
    print(f"=== {name} ({len(doc)} págs) ===")
    for i in range(len(doc)):
        txt = doc[i].get_text()
        dbas = re.findall(r'(?:^|\n)\s*(\d+)\.\s*\n', txt)
        if dbas:
            first_l = txt.split('\n')[0].strip() if txt else ''
            print(f"Pág {i+1}: header='{first_l[:30]}' DBAs: {dbas}")

check_ing("Inglés 1-5", "DBA_Ingles_1_5.pdf")
check_ing("Inglés 6-11", "DBA_Ingles_6_11.pdf")
