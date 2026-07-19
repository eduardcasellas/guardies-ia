import os

# --- Configuració de directoris ---
BASE_DIR = "."
CONTENT_DIR = os.path.join(BASE_DIR, "content")
TEMPLATES_DIR = os.path.join(CONTENT_DIR, "templates")
PROMPTS_DIR = os.path.join(CONTENT_DIR, "prompts")
RESOURCES_DIR = os.path.join(BASE_DIR, "resources")
SNIPPETS_DIR = os.path.join(RESOURCES_DIR, "snippets")
DOCS_DIR = os.path.join(BASE_DIR, "docs")

# Assegurar que els directoris existeixen
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(PROMPTS_DIR, exist_ok=True)
os.makedirs(SNIPPETS_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)

# --- 1. Crear l'especificació del sistema d'exportació ---
export_system_content = """# Sistema d'Exportació de Dades

## Propòsit
Aquest document defineix com s'exporten les dades d'incidències en formats CSV i PDF dins del projecte IA-Productiva.

---

# Formats d'Exportació

## CSV (Comma Separated Values)

Format de text pla per a fulls de càlcul i eines de BI.

### Columnes per defecte

- ID
- Títol
- Descripció
- Data de creació
- Data de resolució
- Prioritat
- Estat
- Ubicació
- Categoria
- Proveïdor assignat
- Notes (concatenades)

### Exemple
