import urllib.request, re

url = "https://drive.google.com/drive/folders/15IlZiGNfjqd0ZxxxvE_SbeffbJYF1TLM"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'aria-label="([^"]+?)"', html)
        print("Total aria-labels found:", len(matches))
        for m in matches:
            if any(k in m.lower() for k in ['shared folder', 'pdf', 'json', 'mat', 'len', 'soc', 'nat', 'ing', 'dba', 'cienc']):
                print("  Item:", m)
        
        # also check items with ssk
        items_ssk = re.findall(r'aria-label="([^"]+)"[^>]*?ssk=[\'\"][^:\'\"]*:[^:\'\"]*:([a-zA-Z0-9_\-]+)', html)
        print("Items with ssk:", len(items_ssk))
        for name, sid in items_ssk:
            if not any(x in name for x in ['Modified', 'Size not available', 'More actions']):
                print(f"   * {name} -> {sid}")
except Exception as e:
    print("Error:", e)
