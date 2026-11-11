import pymupdf

doc = pymupdf.open("DBA_C.Sociales-V2.pdf")
page = doc[7] # page 8
blocks = page.get_text("blocks")
print(f"Total blocks on page 8: {len(blocks)}")
# sort by x0 then y0, or group by column
# let's see x positions
for b in blocks:
    txt = b[4].strip()
    if len(txt) > 20 and not "330" in txt:
        print(f"[{b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f}, {b[3]:.1f}] -> {txt[:60]}...")
