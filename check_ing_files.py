import urllib.request, re

url = "https://drive.google.com/drive/folders/1g4Bt3MlYV74Z8IB-wcklQlzYEJzTTaGN"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

matches = re.findall(r'aria-label="([^"]+)"[^>]*?ssk=[\'\"][^:\'\"]*:[^:\'\"]*:([a-zA-Z0-9_\-]+)', html)
print("=== DBA Ing items ===")
for name, sid in matches:
    if not any(x in name for x in ['Modified', 'Size not available', 'More actions', 'Compartido', 'desktop.ini']):
        print(f"  * {name} -> {sid.replace('-0-16', '')}")
