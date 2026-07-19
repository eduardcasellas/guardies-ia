mkdir -p scripts
cat > scripts/export_data.py << 'EOF'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Mòdul per exportar incidències en formats CSV i PDF.
Segueix l'especificació definida a: content/markdown/sistema_dexportació_de_dades.md
"""

import csv
import os
from datetime import datetime
from pathlib import Path
from typing import List, Optional

# Directori per defecte per a les exportacions
EXPORTS_DIR = Path("exports")

# Columnes per defecte per a l'exportació CSV
CSV_COLUMNS = [
    "ID",
    "Títol",
    "Descripció",
    "Data de creació",
    "Data de resolució",
    "Prioritat",
    "Estat",
    "Ubicació",
    "Categoria",
    "Proveïdor assignat",
    "Notes",
]


class ExportError(Exception):
    """Excepció base per a errors d'exportació."""
    pass


class ExportData:
    """Gestiona l'exportació de dades en formats CSV i PDF."""

    def __init__(self, output_dir: Path = EXPORTS_DIR):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _load_incident(self, incident_id: str) -> dict:
        # Simula la càrrega d'una incidència des d'un fitxer YAML
        return {"ID": incident_id, "Títol": "Exemple", "Estat": "oberta"}

    def _load_all_incidents(self) -> List[dict]:
        # Simula la càrrega de totes les incidències
        return [{"ID": "INC-001"}, {"ID": "INC-002"}]

    def _format_date(self, date_str: Optional[str], date_format: str = "DD/MM/AAAA") -> str:
        if not date_str:
            return ""
        try:
            dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            fmt = "%d/%m/%Y" if date_format == "DD/MM/AAAA" else "%Y-%m-%d"
            return dt.strftime(fmt)
        except (ValueError, TypeError):
            return date_str

    def _format_notes(self, notes: Optional[List[dict]]) -> str:
        if not notes:
            return ""
        return "; ".join(f"{n.get('autor', '')}: {n.get('text', '')}" for n in notes)

    def export_incident_to_csv(self, incident_id: str, output_dir: Optional[Path] = None, date_format: str = "DD/MM/AAAA") -> str:
        output_dir = Path(output_dir) if output_dir else self.output_dir
        output_dir.mkdir(parents=True, exist_ok=True)
        incident = self._load_incident(incident_id)
        output_file = output_dir / f"{incident_id}.csv"
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_COLUMNS)
            row = [
                incident.get("ID", ""),
                incident.get("Títol", ""),
                incident.get("Descripció", ""),
                self._format_date(incident.get("Data de creació"), date_format),
                self._format_date(incident.get("Data de resolució"), date_format),
                incident.get("Prioritat", ""),
                incident.get("Estat", ""),
                incident.get("Ubicació", ""),
                incident.get("Categoria", ""),
                incident.get("Proveïdor assignat", ""),
                self._format_notes(incident.get("Notes")),
            ]
            writer.writerow(row)
        return str(output_file)

    def export_all_to_csv(self, output_dir: Optional[Path] = None, date_format: str = "DD/MM/AAAA") -> str:
        output_dir = Path(output_dir) if output_dir else self.output_dir
        output_dir.mkdir(parents=True, exist_ok=True)
        incidents = self._load_all_incidents()
        if not incidents:
            raise ExportError("No s'han trobat incidències per exportar.")
        output_file = output_dir / "totes_les_incidencies.csv"
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_COLUMNS)
            for incident in incidents:
                row = [
                    incident.get("ID", ""),
                    incident.get("Títol", ""),
                    incident.get("Descripció", ""),
                    self._format_date(incident.get("Data de creació"), date_format),
                    self._format_date(incident.get("Data de resolució"), date_format),
                    incident.get("Prioritat", ""),
                    incident.get("Estat", ""),
                    incident.get("Ubicació", ""),
                    incident.get("Categoria", ""),
                    incident.get("Proveïdor assignat", ""),
                    self._format_notes(incident.get("Notes")),
                ]
                writer.writerow(row)
        return str(output_file)

    # Mètodes per a PDF (simplificats)
    def export_incident_to_pdf(self, incident_id: str, output_dir: Optional[Path] = None) -> str:
        output_dir = Path(output_dir) if output_dir else self.output_dir
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / f"{incident_id}.pdf"
        # Aquí aniria la generació de PDF
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"PDF per a {incident_id} (pendent d'implementar)")
        return str(output_file)


if __name__ == "__main__":
    export = ExportData()
    print("Exportant una incidència a CSV...")
    try:
        print(export.export_incident_to_csv("INC-001"))
    except Exception as e:
        print(f"Error: {e}")

    print("\nExportant totes les incidències a CSV...")
    try:
        print(export.export_all_to_csv())
    except Exception as e:
        print(f"Error: {e}")
EOF