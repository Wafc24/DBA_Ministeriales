import pypdf

def check_pdf(name, path):
    try:
        reader = pypdf.PdfReader(path)
        print(f"[{name}] -> {len(reader.pages)} páginas")
    except Exception as e:
        print(f"[{name}] -> Error: {e}")

check_pdf("Lenguaje V2", "DBA_Lenguaje-min.pdf")
check_pdf("Sociales V2", "DBA_C.Sociales-V2.pdf")
check_pdf("Inglés 1-5", "DBA_Ingles_1_5.pdf")
check_pdf("Inglés 6-11", "DBA_Ingles_6_11.pdf")
check_pdf("Naturales V1", r"D:\WILMER_FERRER\Mat - Soportes\Ciencias Naturales\DBA_C.Naturales-min.pdf")
check_pdf("Matemáticas V2", r"D:\WILMER_FERRER\DOCUMENTOS PARA MATEMÁTICAS\DBA_Matematicas-min.pdf")
