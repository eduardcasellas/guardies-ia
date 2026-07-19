import os

# --- Configuració de directoris ---
BASE_DIR = "."
CONTENT_DIR = os.path.join(BASE_DIR, "content")
TEMPLATES_DIR = os.path.join(CONTENT_DIR, "templates")
PROMPTS_DIR = os.path.join(CONTENT_DIR, "prompts")
HTML_DIR = os.path.join(CONTENT_DIR, "html")
DOCS_DIR = os.path.join(BASE_DIR, "docs")

# Assegurar que els directoris existeixen
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(PROMPTS_DIR, exist_ok=True)
os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)

# --- 1. Crear l'especificació del sistema de notes ---
notes_system_content = ""# Sistema de Comentaris i Notes

## Propòsit
"""Aquest document defineix com es gestionen els comentaris i notes associades a les incidències dins del projecte IA-Productiva."""

"""
--

# Estructura de Dades

Cada nota és un objecte amb els camps següents:

| Camp | Tipus | Descripció |
|------|-------|------------|
| data | string (ISO 8601) | "Data i hora de la nota. Ex: `2026-7-16T10:30:00Z`" |
| autor | string | Nom de la persona o sistema que afegeix la nota. |
| text | string | Contingut de la nota. Màxim 1000 caràcters. |

--
"""

# Emmagatzematge

"""Les notes s'emmagatzemen dins del fitxer YAML de la incidència corresponent, dins del camp `Notes`.
Exemple:"""
