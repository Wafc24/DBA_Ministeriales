import fitz
import json
import re

def clean_text(text):
    if not text:
        return ""
    # Fix hyphenation
    text = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', text)
    # Normalize spaces
    text = re.sub(r'[ \t]+', ' ', text)
    lines = [l.strip() for l in text.split('\n')]
    text = '\n'.join([l for l in lines if l])
    return text.strip()

def extract_v1():
    grade_counts = {
        1: 10,
        2: 14,
        3: 15,
        4: 17,
        5: 17,
        6: 18,
        7: 15,
        8: 18,
        9: 18,
        10: 17,
        11: 17
    }

    result = {}

    for g, max_dba in grade_counts.items():
        path = rf'D:\WILMER_FERRER\DOCUMENTOS PARA MATEMÁTICAS\DBA_V1_MAT\GRADO {g}°.pdf'
        doc = fitz.open(path)
        
        # We need to collect DBAs 1 to max_dba
        grade_dbas = {}

        # Scan each page before the blank notes page
        for pno in range(len(doc)):
            page = doc[pno]
            
            # Find all white circle numbers
            circles = []
            for b in page.get_text('dict')['blocks']:
                if 'lines' in b:
                    for l in b['lines']:
                        for s in l['spans']:
                            t = s['text'].strip()
                            if s['color'] == 16777215 and (re.match(r'^[1-9]\d?$', t) or t in ['1O','2O']):
                                num = int(t.replace('O','0'))
                                if 1 <= num <= max_dba:
                                    circles.append((num, s['bbox'][0], s['bbox'][1], s['bbox'][2], s['bbox'][3]))
            
            # Deduplicate circles by num on this page (keeping leftmost/topmost)
            page_circles = {}
            for c in circles:
                num = c[0]
                if num not in page_circles:
                    page_circles[num] = c
            
            if not page_circles:
                continue

            # Get all text blocks on this page
            blocks = page.get_text('blocks')
            valid_blocks = []
            for b in blocks:
                if b[6] != 0: continue
                x0, y0, x1, y1, text, bno, btype = b
                t = text.strip()
                if not t: continue
                # Skip header / footer
                if y0 < 100 and ('DERECHOS BÁSICOS' in t or 'MATEMÁTICAS' in t): continue
                if y0 > 750 and ('V1' in t or 'Página' in t or 'MINEDUCACIÓN' in t): continue
                if t in ['V1', 'Libertad y Orden']: continue
                valid_blocks.append((x0, y0, x1, y1, t))

            # Assign each block to the closest/most appropriate circle
            # For each circle on the page, find which blocks belong to it
            # Sort circles by position (column-wise or y-wise)
            circle_list = sorted(page_circles.values(), key=lambda c: (0 if c[1] < 300 else 1, c[2]))
            
            for b in valid_blocks:
                bx0, by0, bx1, by1, bt = b
                # Determine which circle owns this block
                # A block belongs to circle C if it is in the same column/region and below/aligned with C
                best_c = None
                best_dist = float('inf')
                
                b_col = 0 if bx0 < 305 else 1
                for c in circle_list:
                    c_num, cx0, cy0, cx1, cy1 = c
                    c_col = 0 if cx0 < 305 else 1
                    
                    # If columns match
                    if b_col == c_col:
                        # block should ideally be at or below circle y (with 15pt margin)
                        if by0 >= cy0 - 25:
                            dy = by0 - cy0
                            if dy < best_dist:
                                best_dist = dy
                                best_c = c_num
                    else:
                        # If cross-column assignment is needed when only 1 column exists
                        pass
                
                # If no matching column found, assign to closest circle overall
                if best_c is None:
                    for c in circle_list:
                        c_num, cx0, cy0, cx1, cy1 = c
                        dist = ((bx0 - cx0)**2 + (by0 - cy0)**2)**0.5
                        if dist < best_dist:
                            best_dist = dist
                            best_c = c_num

                if best_c is not None:
                    if best_c not in grade_dbas:
                        grade_dbas[best_c] = []
                    grade_dbas[best_c].append((by0, bx0, bt))

        # Now for each DBA, combine its blocks and split into Statement & Ejemplo
        grade_clean = {}
        for num in range(1, max_dba + 1):
            blocks_for_num = grade_dbas.get(num, [])
            blocks_for_num.sort(key=lambda x: x[0]) # sort by y
            full_text = '\n\n'.join([b[2] for b in blocks_for_num])
            full_text = clean_text(full_text)
            
            # Split statement and ejemplo
            # Look for "Por ejemplo:" or "Por ejemplo,"
            parts = re.split(r'(?:^|\n|\s+)(Por ejemplo:?|Por ejemplo,|Ejemplo:)', full_text, maxsplit=1, flags=re.IGNORECASE)
            if len(parts) >= 3:
                stmt = clean_text(parts[0])
                ej_prefix = parts[1]
                ej = clean_text(parts[2])
                ejemplo_final = f"{ej_prefix} {ej}" if ej else ej_prefix
            else:
                stmt = full_text
                ejemplo_final = ""

            grade_clean[str(num)] = {
                "statement": stmt,
                "ejemplo": ejemplo_final,
                "full_text": full_text
            }

        result[str(g)] = grade_clean
        print(f"Grado {g} V1: Procesados {len(grade_clean)} DBAs.")

    with open('dba_v1_extraido.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print("Guardado dba_v1_extraido.json exitosamente!")

if __name__ == '__main__':
    extract_v1()
