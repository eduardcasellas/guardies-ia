#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Mòdul per exportar incidències en formats CSV i PDF.

Segueix l'especificació definida a:
    content/templates/export-system.md

Dependències:
    - content/templates/incident-template.md
    - content/templates/report-generation.md
    - data/incidents/
"""

import csv
import json
import os
from datetime import datetime
from pathlib import Path
from typing import List, Optional

# --- Constants ---

# Directori per defecte per a les exportacions
EXPORTS_DIR = Path("exports")

# Directori de les incidències
INCIDENTS_DIR = Path("data") / "incidents"

# Formats de data permesos
DATE_FORMATS = {
    "DD/MM/AAAA": "%d/%m/%Y",
    "AAAA-MM-DD": "%Y-%m-%d",
}

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
        """
        Inicialitza l'exportador de dades.

        Args:
            output_dir: Directori per a les exportacions. Per defecte: exports/.
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _load_incident(self, incident_id: str) -> dict:
        """
        Carrega una incidència des del fitxer JSON.

        Args:
            incident_id: Identificador de la incidència (ex: INC-20260716-0001).

        Returns:
            Diccionari amb les dades de la incidència.

        Raises:
            ExportError: Si el fitxer no existeix o no es pot llegir.
        """
        # Buscar el fitxer JSON de la incidència
        # Format: data/incidents/INC-20260716-0001.json
        incident_file = INCIDENTS_DIR / f"{incident_id}.json"

        if not incident_file.exists():
            raise ExportError(f"Incidència no trobada: {incident_id}")

        try:
            with open(incident_file, "r", encoding="utf-8") as f:
                incident = json.load(f)
        except Exception as e:
            raise ExportError(f"Error en llegir la incidència {incident_id}: {e}")

        return incident

    def _load_all_incidents(self) -> List[dict]:
        """
        Carrega totes les incidències del directori.

        Returns:
            Llista de diccionaris amb les dades de les incidències.
        """
        incidents = []
        if not INCIDENTS_DIR.exists():
            return incidents

        for filepath in INCIDENTS_DIR.glob("*.json"):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    incident = json.load(f)
                    if incident:
                        incidents.append(incident)
            except Exception:
                continue  # Ignorar fitxers amb errors

        return incidents

    def _format_date(self, date_str: Optional[str], format: str = "DD/MM/AAAA") -> str:
        """
        Formata una data segons el format especificat.

        Args:
            date_str: Data en format ISO 8601 o None.
            format: Format de sortida (DD/MM/AAAA o AAAA-MM-DD).

        Returns:
            Data formatejada o cadena buida si és None.
        """
        if not date_str:
            return ""

        try:
            dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            fmt = DATE_FORMATS.get(format, "%d/%m/%Y")
            return dt.strftime(fmt)
        except (ValueError, TypeError):
            return date_str

    def _format_notes(self, notes: Optional[List[dict]]) -> str:
        """
        Formata les notes per a l'exportació CSV.

        Args:
            notes: Llista de notes o None.

        Returns:
            Notes concatenades separades per "; ".
        """
        if not notes:
            return ""

        formatted = []
        for note in notes:
            autor = note.get("autor", "")
            text = note.get("text", "")
            formatted.append(f"{autor}: {text}")

        return "; ".join(formatted)

    def export_incident_to_csv(
        self,
        incident_id: str,
        output_dir: Optional[Path] = None,
        date_format: str = "DD/MM/AAAA",
    ) -> str:
        """
        Exporta una incidència individual a CSV.

        Args:
            incident_id: Identificador de la incidència.
            output_dir: Directori de sortida (per defecte: exports/).
            date_format: Format de data (DD/MM/AAAA o AAAA-MM-DD).

        Returns:
            Ruta del fitxer CSV generat.
        """
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

    def export_all_to_csv(
        self,
        output_dir: Optional[Path] = None,
        date_format: str = "DD/MM/AAAA",
    ) -> str:
        """
        Exporta totes les incidències a CSV.

        Args:
            output_dir: Directori de sortida (per defecte: exports/).
            date_format: Format de data (DD/MM/AAAA o AAAA-MM-DD).

        Returns:
            Ruta del fitxer CSV generat.
        """
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

    def export_incident_to_pdf(
        self,
        incident_id: str,
        output_dir: Optional[Path] = None,
    ) -> str:
        """
        Exporta una incidència individual a PDF.

        Args:
            incident_id: Identificador de la incidència.
            output_dir: Directori de sortida (per defecte: exports/).

        Returns:
            Ruta del fitxer PDF generat.
        """
        output_dir = Path(output_dir) if output_dir else self.output_dir
        output_dir.mkdir(parents=True, exist_ok=True)

        incident = self._load_incident(incident_id)

        output_file = output_dir / f"{incident_id}.pdf"

        # Generar contingut HTML per al PDF
        html_content = self._generate_incident_html(incident)

        # Intentar utilitzar weasyprint si està disponible
        try:
            from weasyprint import HTML
            HTML(string=html_content).write_pdf(str(output_file))
            return str(output_file)
        except ImportError:
            pass

        # Intentar utilitzar pdfkit si està disponible
        try:
            import pdfkit
            pdfkit.from_string(html_content, str(output_file))
            return str(output_file)
        except ImportError:
            pass

        # Alternativa: guardar com a HTML si no hi ha cap llibreria PDF
        html_output = output_dir / f"{incident_id}.html"
        with open(html_output, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"PDF no disponible. S'ha generat un HTML: {html_output}")
        return str(html_output)

    def _generate_incident_html(self, incident: dict) -> str:
        """
        Genera contingut HTML per a una incidència.

        Args:
            incident: Diccionari amb les dades de la incidència.

        Returns:
            Contingut HTML.
        """
        notes_html = ""
        if incident.get("Notes"):
            notes_html = "<h3>Notes</h3><ul>"
            for note in incident["Notes"]:
                notes_html += f"<li><strong>{note.get('autor', '')}</strong> ({self._format_date(note.get('data', ''))}): {note.get('text', '')}</li>"
            notes_html += "</ul>"

        fotos_html = ""
        if incident.get("Fotos"):
            fotos_html = "<h3>Fotos</h3><ul>"
            for foto in incident["Fotos"]:
                fotos_html += f"<li>{foto}</li>"
            fotos_html += "</ul>"

        html = f"""<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <title>Incidència {incident.get('ID', '')}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h1 {{ color: #1a1a2e; }}
        .field {{ margin-bottom: 10px; }}
        .label {{ font-weight: bold; color: #555; }}
        .value {{ color: #333; }}
    </style>
</head>
<body>
    <h1>Incidència {incident.get('ID', '')}</h1>
    <div class="field"><span class="label">Títol:</span> <span class="value">{incident.get('Títol', '')}</span></div>
    <div class="field"><span class="label">Descripció:</span> <span class="value">{incident.get('Descripció', '')}</span></div>
    <div class="field"><span class="label">Data de creació:</span> <span class="value">{self._format_date(incident.get('Data de creació', ''))}</span></div>
    <div class="field"><span class="label">Data de resolució:</span> <span class="value">{self._format_date(incident.get('Data de resolució', ''))}</span></div>
    <div class="field"><span class="label">Prioritat:</span> <span class="value">{incident.get('Prioritat', '')}</span></div>
    <div class="field"><span class="label">Estat:</span> <span class="value">{incident.get('Estat', '')}</span></div>
    <div class="field"><span class="label">Ubicació:</span> <span class="value">{incident.get('Ubicació', '')}</span></div>
    <div class="field"><span class="label">Categoria:</span> <span class="value">{incident.get('Categoria', '')}</span></div>
    <div class="field"><span class="label">Proveïdor assignat:</span> <span class="value">{incident.get('Proveïdor assignat', '')}</span></div>
    {notes_html}
    {fotos_html}
</body>
</html>"""
        return html


# --- Exemple d'ús ---
if __name__ == "__main__":
    export = ExportData()

    # Exemple: exportar totes les incidències a CSV
    try:
        path = export.export_all_to_csv()
        print(f"Exportació completada: {path}")
    except ExportError as e:
        print(f"Error: {e}")