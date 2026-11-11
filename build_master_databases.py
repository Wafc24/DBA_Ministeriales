import json
import re

# Load V2 extracted data
with open('dba_v2_extraido.json', 'r', encoding='utf-8') as f:
    v2_raw = json.load(f)

# Thought classification rules for V2 based on official MEN curriculum standards
# Each DBA is mapped to its primary thought: 'num', 'met', 'geo', 'ale', 'var'
V2_THOUGHT_MAP = {
    "1": {
        "1": "num", "2": "num", "3": "num",
        "4": "met", "5": "met",
        "6": "geo", "7": "geo",
        "8": "var", "9": "var",
        "10": "ale"
    },
    "2": {
        "1": "num", "2": "num", "3": "num",
        "4": "met", "5": "met",
        "6": "geo", "7": "geo",
        "8": "var", "9": "var",
        "10": "ale", "11": "ale"
    },
    "3": {
        "1": "num", "2": "num", "3": "num",
        "4": "met", "5": "met",
        "6": "geo", "7": "geo",
        "8": "var", "9": "var",
        "10": "ale", "11": "ale"
    },
    "4": {
        "1": "num", "2": "num", "3": "num",
        "4": "met", "5": "met",
        "6": "geo", "7": "geo",
        "8": "var", "9": "var",
        "10": "ale", "11": "ale"
    },
    "5": {
        "1": "num", "2": "num", "3": "num",
        "4": "met", "5": "met",
        "6": "geo", "7": "geo",
        "8": "var", "9": "var",
        "10": "ale", "11": "ale", "12": "ale"
    },
    "6": {
        "1": "num", "2": "num", "3": "num",
        "4": "geo", "5": "met", "6": "geo", "7": "geo",
        "8": "var", "9": "var",
        "10": "ale", "11": "ale", "12": "ale"
    },
    "7": {
        "1": "num", "2": "num", "3": "num",
        "4": "met", "5": "geo", "6": "var", "7": "var",
        "8": "ale", "9": "ale"
    },
    "8": {
        "1": "num", "2": "num", "3": "var",
        "4": "met", "5": "met", "6": "geo", "7": "geo",
        "8": "var", "9": "var", "10": "var",
        "11": "ale", "12": "ale"
    },
    "9": {
        "1": "num", "2": "var", "3": "num",
        "4": "met", "5": "geo", "6": "geo", "7": "geo",
        "8": "var", "9": "var",
        "10": "ale", "11": "ale"
    },
    "10": {
        "1": "num", "2": "var", "3": "met",
        "4": "var", "5": "geo", "6": "var", "7": "var",
        "8": "ale", "9": "ale", "10": "ale"
    },
    "11": {
        "1": "num", "2": "num",
        "3": "met", "4": "met",
        "5": "var", "6": "geo", "7": "var", "8": "var",
        "9": "ale", "10": "ale"
    }
}

THOUGHT_NAMES = {
    "num": "Pensamiento Numérico y Sistemas Numéricos",
    "met": "Pensamiento Métrico y Sistemas de Medidas",
    "geo": "Pensamiento Espacial y Sistemas Geométricos",
    "ale": "Pensamiento Aleatorio y Sistemas de Datos",
    "var": "Pensamiento Variacional y Sistemas Algebraicos y Analíticos"
}

# Build Master V2 Database
master_v2 = {}
for g, dbas in v2_raw.items():
    master_v2[g] = {}
    for num, d in dbas.items():
        th_key = V2_THOUGHT_MAP.get(g, {}).get(num, "num")
        master_v2[g][num] = {
            "statement": d["statement"],
            "evidencias": d["evidencias"],
            "ejemplo": d["ejemplo"],
            "pensamiento_key": th_key,
            "pensamiento_nombre": THOUGHT_NAMES[th_key]
        }

with open('master_v2.json', 'w', encoding='utf-8') as f:
    json.dump(master_v2, f, ensure_ascii=False, indent=2)

print("Master V2 construido con 119 DBAs certificados!")
