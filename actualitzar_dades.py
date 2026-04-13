#!/usr/bin/env python3
"""
Actualitza data.json a partir d'un nou fitxer Excel de report setmanal.
Ús: python3 actualitzar_dades.py NOU_REPORT.xlsx
"""
import sys
import json
import pandas as pd

if len(sys.argv) < 2:
    print("Ús: python3 actualitzar_dades.py FITXER.xlsx")
    sys.exit(1)

fitxer = sys.argv[1]
print(f"Llegint {fitxer}...")

df = pd.read_excel(fitxer, sheet_name='BBDD')
df = df.fillna('')

records = []
for _, row in df.iterrows():
    records.append({
        'e':  str(row.get('Nombre Empresa', ''))[:80],
        'fa': str(row.get('Fase', '')),
        'st': str(row.get('Status', '')),
        'fi': str(row.get('Finales', '')),
        'mi': str(row.get('Motivos no interes', '')),
        'pr': str(row.get('Provincia', '')),
        'bb': str(row.get('BBDD', '')),
        'co': str(row.get('Comentario para cliente', ''))[:300],
        'cn': str(row.get('Contacto 1', '')),
        'ca': str(row.get('Cargo 1', '')),
        'ci': str(row.get('Ciudad', '')),
    })

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(records, f, ensure_ascii=False)

print(f"OK: {len(records)} registres escrits a data.json")
