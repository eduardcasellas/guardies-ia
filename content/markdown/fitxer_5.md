# Prompt: Generar codi d'exportació de dades

## Objectiu
Aquest prompt guia la generació d'un mòdul Python per exportar incidències en formats CSV i PDF, basant-se en l'especificació `content/templates/export-system.md`.

## Instruccions per a la IA

1. Carrega l'especificació `content/templates/export-system.md`.
2. Carrega la plantilla d'incidències `content/templates/incident-template.md` per a les regles de validació.
3. Carrega el sistema d'informes `content/templates/report-generation.md` per a les mètriques.
4. Genera un fitxer Python (`resources/snippets/export-data.py`) que contingui:

   ### Classe `ExportData`

   Mètodes:

   - `export_incident_to_csv(incident_id: str, output_dir: str = "exports/") -> str`: Exporta una incidència individual a CSV.
   - `export_incidents_to_csv(incident_ids: list[str], output_dir: str = "exports/") -> str`: Exporta múltiples incidències a CSV.
   - `export_all_to_csv(output_dir: str = "exports/") -> str`: Exporta totes les incidències a CSV.
   - `export_incident_to_pdf(incident_id: str, output_dir: str = "exports/") -> str`: Exporta una incidència individual a PDF.
   - `export_report_to_pdf(report_type: str, period: str, output_dir: str = "exports/") -> str`: Exporta un informe a PDF.

   ### Funcions auxiliars

   - `_load_incident(incident_id: str) -> dict`: Carrega una incidència des del fitxer YAML.
   - `_load_all_incidents() -> list[dict]`: Carrega totes les incidències.
   - `_format_date(date_str: str, format: str = "DD/MM/AAAA") -> str`: Formata una data.
   - `_generate_pdf(content: str, output_path: str) -> str`: Genera un fitxer PDF.

5. La classe ha de:
   - Utilitzar el directori `exports/` per defecte.
   - Gestionar errors de forma robusta (directori no existeix, fitxer no trobat, etc.).
   - Estar documentada amb docstrings.
   - Utilitzar només llibreries estàndard per al CSV (`csv`).
   - Per al PDF, utilitzar `reportlab` si està disponible, o generar HTML com a alternativa.

6. Afegeix un bloc `if __name__ == "__main__":` amb exemples d'ús.

## Regles de Comportament

- No afegeixis funcionalitats no especificades.
- Escriu codi net, modular i comentat.
- Gestiona correctament els errors i les excepcions.

## Sortida esperada

Un bloc de codi Python complet.