import pymupdf, re

def inspect_ing_all():
    doc1 = pymupdf.open("DBA_Ingles_1_5.pdf")
    print("=== INGLES 1-5 ===")
    # Grades: Transición is p8, Grado 1 is p9, Grado 2 is p10, Grado 3 is p11, Grado 4 is p12, Grado 5 is p13
    for p_idx, g_name in [(8, "1"), (9, "2"), (10, "3"), (11, "4"), (12, "5")]:
        txt = doc1[p_idx].get_text()
        print(f"--- GRADO {g_name} (Page {p_idx+1}) ---")
        lines = [l.strip() for l in txt.split('\n') if l.strip()]
        # print non-example text
        for line in lines:
            if any(line.startswith(c) for c in ["1", "2", "3", "4", "5", "6", "7", "8"]):
                print(" ", line)
            elif "Al finalizar" in line or "Comprende" in line or "Responde" in line or "Expresa" in line or "Intercambia" in line or "Identifica" in line or "Asocia" in line or "Organiza" in line or "Menciona" in line or "Compara" in line or "Pregunta" in line or "Produce" in line:
                print("   >", line)

inspect_ing_all()
