#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Mòdul per exportar incidències en formats CSV i PDF.
"""

import csv
import os
from datetime import datetime
from pathlib import Path

EXPORTS_DIR = Path("exports")
INCIDENTS_DIR = Path("data/incidents")

def load_incident(incident_id):
    """Carrega una incidència des d'un fitxer (simulat)."""
    # Simula la càrrega d'una incidència
    return {
        "id": incident_id,
        "titol": "Exemple d'incidència",
        "descripcio": "Descripció de prova",
        "data_creacio": datetime.now().isoformat(),
        "prioritat": 3,
        "estat": "oberta"
    }

def export_to_csv(incident_id, output_dir=EXPORTS_DIR):
    """Exporta una incidència a CSV."""
    output_dir.mkdir(parents=True, exist_ok=True)
    incident = load_incident(incident_id)
    output_file = output_dir / f"{incident_id}.csv"
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Títol", "Descripció", "Data", "Prioritat", "Estat"])
        writer.writerow([
            incident["id"],
            incident["titol"],
            incident["descripcio"],
            incident["data_creacio"],
            incident["prioritat"],
            incident["estat"]
        ])
    print(f"✅ Exportat: {output_file}")
    return str(output_file)

if __name__ == "__main__":
    # Prova ràpida
    export_to_csv("INC-001")