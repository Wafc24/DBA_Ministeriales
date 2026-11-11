import pymupdf, re, json

doc = pymupdf.open("DBA_C.Sociales-V2.pdf")

def get_page_text_columns(page):
    w = page.rect.width
    h = page.rect.height
    col1 = page.get_text("text", clip=pymupdf.Rect(0, 0, 310, h))
    col2 = page.get_text("text", clip=pymupdf.Rect(310, 0, w, h))
    return col1 + "\n" + col2

t8 = get_page_text_columns(doc[7])
print("Sample text page 8 with column clips:")
with open("test_soc_col.txt", "w", encoding="utf-8") as out:
    out.write(t8)
print("Saved to test_soc_col.txt")
