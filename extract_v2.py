import fitz
import json
import re

def clean_text(text):
    if not text:
        return ""
    # Fix broken hyphenated words at line breaks
    text = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', text)
    # Normalize whitespace
    text = re.sub(r'[ \t]+', ' ', text)
    # Remove leading/trailing whitespace
    lines = [l.strip() for l in text.split('\n')]
    # Filter empty lines
    text = '\n'.join([l for l in lines if l])
    return text.strip()

def extract_v2():
    doc = fitz.open(r'D:\WILMER_FERRER\DOCUMENTOS PARA MATEMÁTICAS\DBA_V1_MAT\DBA_V2. Matemáticas.pdf')
    
    grade_ranges = {
        1: (7, 14),
        2: (14, 21),
        3: (21, 29),
        4: (29, 36),
        5: (36, 44),
        6: (44, 52),
        7: (52, 58),
        8: (58, 65),
        9: (65, 73),
        10: (73, 80),
        11: (80, 86)
    }

    result = {}

    for g, (start_p, end_p) in grade_ranges.items():
        grade_blocks = []
        for pno in range(start_p, end_p):
            blocks = doc[pno].get_text('blocks')
            page_blocks = []
            for b in blocks:
                x0, y0, x1, y1, text, bno, btype = b
                if btype != 0:
                    continue
                t = text.strip()
                if not t:
                    continue
                # Skip header and footer
                if y0 < 100 and ('Derechos Básicos' in t or 'Matemáticas' in t):
                    continue
                if y0 > 750 and re.match(r'^\d{1,3}$', t):
                    continue
                if y1 < 60:
                    continue
                col = 0 if x0 < 305 else 1
                page_blocks.append((col, y0, t, pno + 1))
            # Sort by column (left first, then right), then by vertical position
            page_blocks.sort(key=lambda x: (x[0], x[1]))
            grade_blocks.extend(page_blocks)

        # Parse into DBAs
        dbas = {}
        current_dba = None
        current_section = None # 'statement', 'evidencias', 'ejemplo'

        i = 0
        while i < len(grade_blocks):
            col, y0, text, pno = grade_blocks[i]

            # Detect start of DBA: e.g. "1.\nIdentifica..." or "1." followed by text
            m = re.match(r'^(\d{1,2})\.\s*\n([A-ZÁÉÍÓÚ].*)', text, re.DOTALL)
            dba_num = None
            statement_init = ""

            if m:
                dba_num = int(m.group(1))
                statement_init = m.group(2).strip()
            else:
                m_num = re.match(r'^(\d{1,2})\.$', text)
                if m_num and i + 1 < len(grade_blocks):
                    next_text = grade_blocks[i+1][2]
                    if re.match(r'^[A-ZÁÉÍÓÚ]', next_text):
                        num_cand = int(m_num.group(1))
                        if 1 <= num_cand <= 20:
                            dba_num = num_cand
                            statement_init = next_text.strip()
                            i += 1 # advance extra block

            if dba_num is not None:
                current_dba = dba_num
                dbas[current_dba] = {
                    "dba_num": current_dba,
                    "statement": statement_init,
                    "evidencias_raw": [],
                    "ejemplo_raw": []
                }
                current_section = "statement"
                i += 1
                continue

            if current_dba is not None:
                # Check for Evidencias header
                if 'Evidencias de aprendizaje' in text:
                    current_section = 'evidencias'
                    rem = text.replace('Evidencias de aprendizaje', '').strip()
                    if rem:
                        dbas[current_dba]['evidencias_raw'].append(rem)
                # Check for Ejemplo header (standalone, with footnotes [1], 2, or inline)
                elif re.search(r'(?:^|\n)\s*Ejemplo(?:\[\d+\]|\d+)?\s*(?:\n|$)', text):
                    current_section = 'ejemplo'
                    # Split before and after Ejemplo
                    parts = re.split(r'(?:^|\n)\s*Ejemplo(?:\[\d+\]|\d+)?\s*(?:\n|$)', text, maxsplit=1)
                    before_ej = parts[0].strip()
                    after_ej = parts[1].strip() if len(parts) > 1 else ""
                    if before_ej:
                        # Belongs to previous section (e.g. evidencias)
                        dbas[current_dba]['evidencias_raw'].append(before_ej)
                    if after_ej:
                        dbas[current_dba]['ejemplo_raw'].append(after_ej)
                else:
                    if current_section == 'statement':
                        if not any(k in text for k in ['Evidencias de aprendizaje', 'Ejemplo', 'm\t']):
                            dbas[current_dba]['statement'] += ' ' + text
                    elif current_section == 'evidencias':
                        dbas[current_dba]['evidencias_raw'].append(text)
                    elif current_section == 'ejemplo':
                        dbas[current_dba]['ejemplo_raw'].append(text)

            i += 1

        # Process and clean fields for this grade
        grade_clean = {}
        for num, d in sorted(dbas.items()):
            stmt = clean_text(d['statement'])
            
            # Process evidencias
            ev_full = ' '.join(d['evidencias_raw'])
            # Bullet markers: 'm\t', 'm ', or 'm' immediately followed by an uppercase letter
            ev_parts = re.split(r'(?:^|\n|\s+)m[\t\s]*(?=[A-ZÁÉÍÓÚ])|(?:\n|\s+)m\s+', ev_full)
            evidencias_list = []
            for ep in ev_parts:
                ep_clean = clean_text(ep)
                if len(ep_clean) > 8 and not ep_clean.startswith('Evidencias'):
                    evidencias_list.append(ep_clean)

            # Process ejemplo
            ej_full = '\n\n'.join([clean_text(block) for block in d['ejemplo_raw'] if clean_text(block)])
            # Clean up example formatting
            ej_clean = clean_text(ej_full)

            grade_clean[str(num)] = {
                "statement": stmt,
                "evidencias": evidencias_list,
                "ejemplo": ej_clean
            }

        result[str(g)] = grade_clean
        print(f"Grado {g}: Procesados {len(grade_clean)} DBAs.")

    with open('dba_v2_extraido.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print("Guardado dba_v2_extraido.json exitosamente!")

if __name__ == '__main__':
    extract_v2()
