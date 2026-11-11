import json, pypdf, re

def inspect_lenguaje():
    print("=== EXTRACTING LENGUAJE V2 FROM PDF ===")
    reader = pypdf.PdfReader("DBA_Lenguaje-min.pdf")
    # let's see how each page is structured
    # usually pages 8-11 are grado 1, etc.
    # let's print page headers from page 7 to 20
    for p_num in range(7, 22):
        txt = reader.pages[p_num].extract_text()
        first_line = txt.split('\n')[0] if txt else ''
        # check if DBA number appears
        dbas = re.findall(r'(?:^|\n)\s*(\d+)\.\s*\n([^\n]+)', txt)
        print(f"Pág {p_num+1}: first_line='{first_line[:40]}' DBAs found: {dbas}")

inspect_lenguaje()
