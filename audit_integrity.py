import json
import os

def audit_json(filename):
    if not os.path.exists(filename):
        print(f"Archivo no encontrado: {filename}")
        return
    print(f"==================================================")
    print(f" AUDITORIA: {filename}")
    print(f"==================================================")
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    issues = []
    total_dbas = 0
    total_evidencias = 0
    
    # Check if dict of grades or list
    if isinstance(data, dict):
        for grade, dbas in data.items():
            if not isinstance(dbas, dict): 
                continue
            for dba_num, info in dbas.items():
                total_dbas += 1
                stmt = info.get('statement') or info.get('enunciado') or ''
                evids = info.get('evidencias') or []
                total_evidencias += len(evids)
                
                # Check statement
                if len(stmt.strip()) < 20:
                    issues.append(f"G{grade} DBA {dba_num}: Enunciado muy corto ({len(stmt)} chars): '{stmt}'")
                if any(junk in stmt for junk in ['Derechos Básicos', 'Ministerio', 'Grado ']):
                    issues.append(f"G{grade} DBA {dba_num}: Posible ruido en Enunciado: '{stmt[:60]}...'")
                
                # Check evidencias
                if len(evids) == 0:
                    issues.append(f"G{grade} DBA {dba_num}: ¡0 EVIDENCIAS!")
                for idx, ev in enumerate(evids):
                    ev_clean = ev.strip()
                    if len(ev_clean) < 15:
                        issues.append(f"G{grade} DBA {dba_num} Evid {idx+1}: Muy corta ({len(ev_clean)} chars): '{ev_clean}'")
                    if any(junk in ev_clean for junk in ['Derechos Básicos', 'Ministerio de Educación', 'Grado ']):
                        issues.append(f"G{grade} DBA {dba_num} Evid {idx+1}: Contiene encabezado/pie de página: '{ev_clean[:50]}...'")
                    if ev_clean.endswith((' y', ' o', ' de', ' la', ' el', ' en', ' con', ',')):
                        issues.append(f"G{grade} DBA {dba_num} Evid {idx+1}: Truncada al final: '...{ev_clean[-30:]}'")
    elif isinstance(data, list):
        total_dbas = len(data)
        for idx, item in enumerate(data):
            stmt = item.get('statement') or item.get('enunciado') or ''
            evids = item.get('evidencias') or []
            total_evidencias += len(evids)
            g = item.get('grado', '?')
            num = item.get('numero', idx+1)
            if len(stmt.strip()) < 20:
                issues.append(f"G{g} DBA {num}: Enunciado muy corto: '{stmt}'")
            if len(evids) == 0:
                issues.append(f"G{g} DBA {num}: ¡0 EVIDENCIAS!")
    
    print(f"Total DBAs: {total_dbas} | Total Evidencias: {total_evidencias}")
    print(f"Anomalías detectadas: {len(issues)}")
    for iss in issues[:12]:
        print(" [!]", iss)
    if len(issues) > 12:
        print(f" ... y {len(issues)-12} advertencias adicionales.")
    print()

for f in ['literal_lenguaje_v2.json', 'literal_sociales_v2.json', 'master_v2.json', 'literal_ingles.json', 'master_v1.json']:
    audit_json(f)
