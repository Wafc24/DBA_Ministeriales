import urllib.request, os

files_to_download = {
    "DBA_Lenguaje-min.pdf": "1WAcAPAlwrWLmdn5BKNDJCJjDK_b6lh7c",
    "DBA_C.Sociales-V2.pdf": "1qoTX80kajbteZRZwWrwKhLMxUs5QzPGj",
    "DBA_Ingles_1_5.pdf": "1FRa7Twde5SCwfere2_a2AJQlSgyd-uNW",
    "DBA_Ingles_6_11.pdf": "1xiO-DJyAjXUU1zEfqZJGGr2R8StsumZV"
}

for fname, fid in files_to_download.items():
    if os.path.exists(fname) and os.path.getsize(fname) > 100000:
        print(f"Already exists: {fname} ({os.path.getsize(fname)} bytes)")
        continue
    url = f"https://drive.google.com/uc?export=download&id={fid}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    print(f"Downloading {fname} from ID {fid}...")
    try:
        with urllib.request.urlopen(req) as resp, open(fname, "wb") as out:
            out.write(resp.read())
        print(f"  -> Done! {fname} ({os.path.getsize(fname)} bytes)")
    except Exception as e:
        print(f"  -> Error {fname}: {e}")
