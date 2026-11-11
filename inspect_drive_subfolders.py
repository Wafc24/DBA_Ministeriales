import urllib.request, re

folders = {
    "Inglés": "1g4Bt3MlYV74Z8IB-wcklQlzYEJzTTaGN",
    "Lenguaje": "1z6xQaKkwkeh0uiwMuhMdmwaJ0rUgUbhs",
    "Matemáticas": "1LkRwJTCRn9tzLbPPSFntTBIZxAZwxJpR",
    "Naturales": "1MHyEkkix47__Ej39KEDt8M7oJklvvwYx",
    "Sociales": "11k6vO0E3toqeVqaF3GGTADEq10W33q2J"
}

for name, fid in folders.items():
    url = f"https://drive.google.com/drive/folders/{fid}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            items_ssk = re.findall(r'aria-label="([^"]+)"[^>]*?ssk=[\'\"][^:\'\"]*:[^:\'\"]*:([a-zA-Z0-9_\-]+)', html)
            print(f"=== {name} (Folder ID: {fid}) ===")
            for iname, sid in items_ssk:
                if not any(x in iname for x in ['Modified', 'Size not available', 'More actions', 'Compartido', 'desktop.ini']):
                    print(f"   * {iname} -> {sid.replace('-0-16', '')}")
    except Exception as e:
        print(f"Error {name}: {e}")
