import urllib.request, re, json, time

base_folder_id = "1j903O-frGgmELmnRksmOMSR3Yk_dRBUN"

def fetch_html(fid):
    url = f"https://drive.google.com/drive/folders/{fid}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {fid}: {e}")
        return ""

def get_items(html):
    # returns list of (name, id)
    # pattern: aria-label="([^"]+)"[^>]*?ssk=[\'\"][^:\'\"]*:[^:\'\"]*:([a-zA-Z0-9_\-]+)
    results = []
    matches = re.findall(r'aria-label="([^"]+)"[^>]*?ssk=[\'\"][^:\'\"]*:[^:\'\"]*:([a-zA-Z0-9_\-]+)', html)
    for name, sid in matches:
        if not any(x in name for x in ['Modified', 'Size not available', 'More actions', 'Compartido']):
            clean_id = sid.replace('-0-16', '')
            results.append((name.strip(), clean_id))
    return results

print("Starting scan of Drive folder...")
root_html = fetch_html(base_folder_id)
root_items = get_items(root_html)
print(f"Found {len(root_items)} grade folders in root:")
for name, fid in root_items:
    print(f"  {name} -> {fid}")

# We will store: grade -> component -> {pdf_name, pdf_id, drive_view_url}
drive_catalog = {}

for grade_name, grade_id in root_items:
    g_match = re.search(r'(\d+)', grade_name)
    if not g_match: continue
    g = g_match.group(1)
    drive_catalog[g] = {}
    print(f"\nScanning Grade {g} (ID: {grade_id})...")
    
    g_html = fetch_html(grade_id)
    g_items = get_items(g_html)
    
    # find *-Mat folder
    mat_item = next((it for it in g_items if "mat" in it[0].lower()), None)
    if not mat_item:
        print(f"  No Mat folder found in Grade {g}")
        continue
    
    mat_name, mat_id = mat_item
    print(f"  Found Mat folder: {mat_name} ({mat_id})")
    
    mat_html = fetch_html(mat_id)
    mat_items = get_items(mat_html)
    
    # usually has a subfolder like "1°" or "10°"
    sub_folder = next((it for it in mat_items if "shared folder" in it[0].lower()), None)
    target_items = mat_items
    if sub_folder:
        print(f"    Found deeper grade subfolder: {sub_folder[0]} ({sub_folder[1]})")
        sub_html = fetch_html(sub_folder[1])
        target_items = get_items(sub_html)
    
    # Now in target_items, we have the component folders (1. Numérico - Variacional, etc.)
    for comp_name, comp_id in target_items:
        lower_comp = comp_name.lower()
        if "shared folder" not in lower_comp:
            continue
        
        comp_key = None
        if "num" in lower_comp or "var" in lower_comp:
            comp_key = "num_var"
        elif "geom" in lower_comp or "met" in lower_comp or "espacial" in lower_comp:
            comp_key = "geom_met"
        elif "ale" in lower_comp:
            comp_key = "aleatorio"
            
        if not comp_key:
            continue
            
        print(f"      Component {comp_name} ({comp_key}) -> ID: {comp_id}")
        comp_html = fetch_html(comp_id)
        comp_items = get_items(comp_html)
        
        pdf_item = next((it for it in comp_items if ".pdf" in it[0].lower()), None)
        if pdf_item:
            pdf_title = pdf_item[0].replace("PDF Shared", "").replace("Compartido", "").strip()
            pdf_id = pdf_item[1]
            print(f"        PDF: '{pdf_title}' -> ID: {pdf_id}")
            drive_catalog[g][comp_key] = {
                "title": pdf_title,
                "file_id": pdf_id,
                "drive_view_url": f"https://drive.google.com/file/d/{pdf_id}/view?usp=sharing",
                "drive_download_url": f"https://drive.google.com/uc?export=download&id={pdf_id}"
            }
        else:
            print(f"        No PDF found in {comp_name}")
    
    time.sleep(0.5)

print("\nFinal Drive Catalog:")
with open("pma_drive_catalog.json", "w", encoding="utf-8") as out:
    json.dump(drive_catalog, out, indent=2, ensure_ascii=False)
print("Saved to pma_drive_catalog.json!")
