# Sistema de Comentaris i Notes

## Propòsit
Aquest document defineix com es gestionen els comentaris i notes associades a les incidències dins del projecte IA-Productiva.

---

# Estructura de Dades

Cada nota és un objecte amb els camps següents:

| Camp | Tipus | Descripció |
|------|-------|------------|
| `data` | string (ISO 8601) | Data i hora de la nota. Ex: `2026-07-16T10:30:00Z` |
| `autor` | string | Nom de la persona o sistema que afegeix la nota. |
| `text` | string | Contingut de la nota. Màxim 1000 caràcters. |

---

# Emmagatzematge

Les notes s'emmagatzemen dins del fitxer YAML de la incidència corresponent, dins del camp `Notes`, tal com es defineix a la plantilla `content/templates/incident-template.md`.

Exemple dins d'una incidència:
