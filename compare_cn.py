import json, pymupdf

with open(r"D:\WILMER_FERRER\JSON\DBA - Ciencias Naturales\DBA_Ciencias_Naturales_v1_Colombia.json", "r", encoding="utf-8") as f:
    cn_json = json.load(f)

doc = pymupdf.open(r"D:\WILMER_FERRER\Mat - Soportes\Ciencias Naturales\DBA_C.Naturales-min.pdf")

# Compare Grado 1 DBA 1 and Grado 4 DBA 1
txt_p8 = doc[7].get_text() # Page 8
print("--- PDF Page 8 ---")
print(txt_p8[:400])
print("--- JSON Grado 1 DBA 1 ---")
json_d1 = cn_json['dbas']['1']
d1_item = json_d1[0] if isinstance(json_d1, list) else list(json_d1.values())[0]
print("Statement:", d1_item['statement'])
print("Evidencias:", d1_item['evidencias'])
