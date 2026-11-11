import urllib.request, re, pypdf

# get list of items in DBA Lenguaje
url = "https://drive.google.com/drive/folders/1z6xQaKkwkeh0uiwMuhMdmwaJ0rUgUbhs"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

matches = re.findall(r'aria-label="([^"]+)"[^>]*?ssk=[\'\"][^:\'\"]*:[^:\'\"]*:([a-zA-Z0-9_\-]+)', html)
file_id = None
for name, sid in matches:
    if "1 dba_lenguaje" in name.lower():
        file_id = sid.replace('-0-16', '')
        print("Found:", name, file_id)
        break

if file_id:
    dl_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    req_dl = urllib.request.Request(dl_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req_dl) as resp, open("sample_leng_1.pdf", "wb") as out:
        out.write(resp.read())
    print("Downloaded sample_leng_1.pdf!")
    reader = pypdf.PdfReader("sample_leng_1.pdf")
    print("Num pages:", len(reader.pages))
    for i, page in enumerate(reader.pages):
        print(f"--- PAGE {i+1} ---")
        print(page.extract_text()[:400])
