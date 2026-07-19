

## Resposta de la IA (guardies-ia)

D'acord. He carregat el context complet del projecte.

**Anàlisi de la tasca:**

La primera tasca del MVP és definir una plantilla de registre d'incidències. Seguint les convencions del framework IA-Productiva, he de:

1.  **Crear un document de plantilla** (`content/templates/incident-template.md`) que serveixi com a font de veritat única per a l'estructura de les dades.
2.  **Crear un prompt** (`content/prompts/register-incident.md`) que un usuari o una IA pugui utilitzar per generar un registre d'incidència basat en la plantilla.
3.  **Documentar la decisió** al `docs/decision-log.md`.

La plantilla ha de ser clara, explícita i fàcil de parsejar per una IA, seguint el principi "AI First".

A continuació, el codi Python per crear aquests fitxers:

```python
import os

# --- Configuració de directoris ---
BASE_DIR = "."
CONTENT_DIR = os.path.join(BASE_DIR, "content")
TEMPLATES_DIR = os.path.join(CONTENT_DIR, "templates")
PROMPTS_DIR = os.path.join(CONTENT_DIR, "prompts")
DOCS_DIR = os.path.join(BASE_DIR, "docs")

# Assegurar que els directoris existeixen
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(PROMPTS_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)

# --- 1. Crear la plantilla d'incidència ---
incident_template_content = """# Plantilla d'Incidència

## Propòsit
Aquesta plantilla defineix l'estructura única per al registre d'incidències dins del projecte IA-Productiva. Totes les incidències han de seguir aquest format per garantir la predictibilitat i la reutilització de les dades.

---

# Camps

## Obligatoris

- **ID**: Identificador únic de la incidència. Format: `INC-{YYYYMMDD}-{NNNN}` (ex: `INC-20260716-0001`).
- **Títol**: Resum breu i descriptiu del problema. (Màxim 100 caràcters).
- **Descripció**: Explicació detallada del problema, incloent-hi el comportament esperat i l'observat.
- **Data de creació**: Data i hora en format ISO 8601 (`YYYY-MM-DDTHH:MM:SSZ`).
- **Prioritat**: Valor de l'1 al 5, on 1 és crític i 5 és trivial.
- **Estat**: Valor d'una llista tancada: `oberta`, `en curs`, `resolta`, `tancada`.
- **Ubicació**: Lloc físic o virtual on s'ha detectat la incidència. (ex: "Oficina 3B", "Servidor Producció", "App Mòbil v2.1").

## Opcionals

- **Categoria**: Etiqueta per classificar la incidència. (ex: `hardware`, `software`, `xarxa`, `proveïdor`, `seguretat`).
- **Proveïdor assignat**: Nom del proveïdor o contacte responsable (ha de coincidir amb un contacte de la llista de proveïdors).
- **Data de resolució**: Data i hora en format ISO 8601, només si l'estat és `resolta` o `tancada`.
- **Fotos**: Llista de rutes o URLs a les imatges relacionades.
- **Notes**: Llista de comentaris o observacions addicionals. Cada nota ha d'incloure una data i un autor.

---

# Exemple

```yaml
ID: INC-20260716-0001
Títol: El servidor web no respon
Descripció: El servei HTTP al servidor 192.168.1.10 no respon. Comportament esperat: retornar codi 200. Comportament observat: timeout.
Data de creació: 2026-07-16T10:30:00Z
Prioritat: 1
Estat: oberta
Ubicació: Servidor Producció
Categoria: xarxa
Proveïdor assignat: (pendent)
Data de resolució: (pendent)
Fotos: []
Notes: []
```

---

# Regles de Validació

- L'ID ha de ser únic.
- La prioritat ha de ser un enter entre 1 i 5.
- L'estat ha de ser un dels valors permesos.
- `Data de resolució` no pot existir si `Estat` no és `resolta` o `tancada`.
"""

# Escriure el fitxer de la plantilla
with open(os.path.join(TEMPLATES_DIR, "incident-template.md"), "w", encoding="utf-8") as f:
    f.write(incident_template_content)

print(f"[OK] Creat: {os.path.join(TEMPLATES_DIR, 'incident-template.md')}")

# --- 2. Crear el prompt per registrar una incidència ---
register_incident_prompt_content = """# Prompt: Registrar una incidència

## Objectiu
Aquest prompt guia la creació d'un nou registre d'incidència seguint la plantilla `content/templates/incident-template.md`.

## Instruccions per a la IA

1.  Carrega la plantilla `content/templates/incident-template.md`.
2.  Demana a l'usuari la informació necessària per omplir els camps **obligatoris**.
3.  Genera un identificador únic (`ID`) basat en la data actual.
4.  Pregunta per la informació dels camps **opcionals** si l'usuari no els ha proporcionat.
5.  Valida les dades segons les regles de la plantilla.
6.  Mostra el registre complet en format YAML a l'usuari per a la seva confirmació.
7.  Un cop confirmat, indica el camí on s'hauria d'emmagatzemar el registre (ex: `data/incidents/INC-20260716-0001.yaml`).

## Regles de Comportament

- No inventis informació. Si l'usuari no proporciona un camp opcional, deixa'l com a `(pendent)` o buit segons el tipus.
- Utilitza el català o el castellà segons l'idioma de l'usuari.
- Sigues concís i directe.
"""

with open(os.path.join(PROMPTS_DIR, "register-incident.md"), "w", encoding="utf-8") as f:
    f.write(register_incident_prompt_content)

print(f"[OK] Creat: {os.path.join(PROMPTS_DIR, 'register-incident.md')}")

# --- 3. Actualitzar el registre de decisions ---
decision_log_entry = """
## 2026-07-16

### Títol
Definició de la plantilla de registre d'incidències.

### Context
Es necessita una estructura de dades estàndard per al registre d'incidències que sigui llegible per IA i per humans, i que permeti la generació de formularis i informes de forma consistent.

### Opcions considerades
- **Opció A**: Utilitzar un format lliure (Markdown sense estructura).
- **Opció B**: Definir una plantilla YAML estricta dins d'un fitxer de documentació.
- **Opció C**: Crear una plantilla Markdown amb un bloc YAML incrustat com a exemple, i un prompt associat per guiar-ne l'ús.

### Decisió
S'ha escollit l'Opció C.

### Justificació
- Segueix el principi de "Single Source of Truth" en un sol fitxer de plantilla.
- El format YAML dins de Markdown és fàcil de parsejar per IA i per codi.
- El prompt associat permet reutilitzar la plantilla de forma predictible.
- Compleix amb el principi "AI First" i "Modular Design".

### Conseqüències
- Caldrà crear un sistema d'emmagatzematge (fitxers YAML o base de dades) per a les dades generades.
- S'haurà d'actualitzar el TODO.md per reflectir que aquesta tasca està completa.

### Documents relacionats
- content/templates/incident-template.md
- content/prompts/register-incident.md
"""

with open(os.path.join(DOCS_DIR, "decision-log.md"), "a", encoding="utf-8") as f:
    f.write(decision_log_entry)

print(f"[OK] Actualitzat: {os.path.join(DOCS_DIR, 'decision-log.md')}")

print("\n--- Tasca completada ---")
print("S'han creat/actualitzat 3 fitxers.")
print("Per continuar, caldria actualitzar el TODO.md per marcar la tasca com a feta.")
```

**Explicació de la solució:**

He seguit les convencions del projecte al peu de la lletra:

1.  **Modularitat**: He separat la definició de l'estructura (`templates/incident-template.md`) de la guia d'ús (`prompts/register-incident.md`). Això permet que la plantilla sigui reutilitzable per múltiples processos (formularis, informes, etc.) sense dependre d'un sol prompt.
2.  **Single Source of Truth**: La plantilla és l'única font de veritat per als camps d'una incidència. El prompt només la referència.
3.  **AI First**: La plantilla és explícita, estructurada i conté un exemple en YAML, un format fàcil de parsejar per a una IA. Les regles de validació són clares i deterministes.
4.  **Decision Log**: He documentat la decisió, les opcions considerades i la justificació, assegurant la traçabilitat del projecte.
5.  **Predictibilitat**: En definir una plantilla estricta, qualsevol IA que utilitzi el prompt associat generarà resultats molt similars, reduint la incertesa.

Per a la següent iteració, es podria crear un esborrany del formulari (`content/templates/incident-form.md`) que tradueixi aquests camps a una interfície d'usuari.


## Resposta de la IA (guardies-ia)

D'acord. He carregat el context complet del projecte.

**Anàlisi de la tasca:**

La segona tasca del MVP és crear un formulari per introduir incidències. Seguint les convencions del framework IA-Productiva i la informació de la tasca anterior:

1.  **La plantilla d'incidències ja existeix** (`content/templates/incident-template.md`).
2.  **El prompt per registrar incidències ja existeix** (`content/prompts/register-incident.md`).
3.  **Ara toca crear el formulari** que tradueixi els camps de la plantilla a una interfície d'usuari.

**Decisió de disseny:**

Seguint el principi de **Modular Design** i **Single Source of Truth**, no vull duplicar la informació de la plantilla dins del formulari. En lloc d'això, el formulari ha de **referenciar la plantilla** i definir només la capa de presentació.

He considerat dues opcions:

- **Opció A**: Crear un formulari HTML complet amb tots els camps duplicats.
- **Opció B**: Crear un document de formulari (`content/templates/incident-form.md`) que defineixi l'estructura de la interfície d'usuari, referenciant la plantilla per a les regles de validació i els camps.

He escollit l'**Opció B** perquè:
- Manté la plantilla com a única font de veritat per a l'estructura de dades.
- El formulari es converteix en un document independent que pot ser interpretat per una IA per generar la interfície real (HTML, React, etc.).
- Compleix amb el principi "AI First": el formulari és explícit i fàcil de parsejar.

A més, per assegurar la **predictibilitat**, crearé un prompt (`content/prompts/generate-incident-form.md`) que guiï la IA en la generació del formulari real a partir d'aquesta especificació.

A continuació, el codi Python per crear aquests fitxers:

```python
import os

# --- Configuració de directoris ---
BASE_DIR = "."
CONTENT_DIR = os.path.join(BASE_DIR, "content")
TEMPLATES_DIR = os.path.join(CONTENT_DIR, "templates")
PROMPTS_DIR = os.path.join(CONTENT_DIR, "prompts")
DOCS_DIR = os.path.join(BASE_DIR, "docs")

# Assegurar que els directoris existeixen
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(PROMPTS_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)

# --- 1. Crear el formulari (especificació d'interfície) ---
incident_form_content = """# Formulari d'Incidència

## Propòsit
Aquest document defineix la interfície d'usuari per al registre d'incidències.
No duplica la definició dels camps; referencia la plantilla `content/templates/incident-template.md` per a les regles de validació i l'estructura de dades.

---

# Estructura del Formulari

## Secció 1: Informació bàsica

| Camp | Tipus d'input | Comportament |
|------|---------------|--------------|
| Títol | `input text` | Màxim 100 caràcters. Requerit. |
| Descripció | `textarea` | Requerit. |
| Ubicació | `input text` | Requerit. |

## Secció 2: Classificació

| Camp | Tipus d'input | Comportament |
|------|---------------|--------------|
| Prioritat | `select` | Valors: 1 (Crític), 2 (Alt), 3 (Mitjà), 4 (Baix), 5 (Trivial). Per defecte: 3. Requerit. |
| Categoria | `select` | Valors: `hardware`, `software`, `xarxa`, `proveïdor`, `seguretat`, `altre`. Opcional. |
| Estat | `select` | Valors: `oberta`, `en curs`, `resolta`, `tancada`. Per defecte: `oberta`. Requerit. |

## Secció 3: Assignació

| Camp | Tipus d'input | Comportament |
|------|---------------|--------------|
| Proveïdor assignat | `select` | Llista dinàmica de contactes. Opcional. |
| Notes | `textarea` | Opcional. |

## Secció 4: Fitxers

| Camp | Tipus d'input | Comportament |
|------|---------------|--------------|
| Fotos | `file input` | Múltiples fitxers. Formats permesos: jpg, png, gif. Mida màxima: 10 MB per fitxer. Opcional. |

## Secció 5: Accions

| Botó | Acció |
|------|-------|
| Desa | Valida el formulari segons les regles de la plantilla. Genera l'ID automàticament. Desa la incidència. |
| Cancel·la | Torna a la llista d'incidències sense desar. |

---

# Regles de Comportament

- El camp `Data de creació` es genera automàticament en desar.
- El camp `ID` es genera automàticament seguint el format `INC-{YYYYMMDD}-{NNNN}`.
- El camp `Data de resolució` només es mostra si l'estat és `resolta` o `tancada`.
- El selector `Proveïdor assignat` es carrega des de `data/providers/`.
- Totes les validacions han de coincidir amb les definides a `content/templates/incident-template.md`.

---

# Exemple de sortida YAML

```yaml
ID: INC-20260716-0001
Títol: El servidor web no respon
Descripció: El servei HTTP al servidor 192.168.1.10 no respon.
Data de creació: 2026-07-16T10:30:00Z
Prioritat: 1
Estat: oberta
Ubicació: Servidor Producció
Categoria: xarxa
Proveïdor assignat: (pendent)
Data de resolució: (pendent)
Fotos: []
Notes: []
```

---

# Dependències

- `content/templates/incident-template.md`: definició dels camps i regles de validació.
- `data/providers/`: llista de proveïdors per al selector.
"""

# Escriure el fitxer del formulari
with open(os.path.join(TEMPLATES_DIR, "incident-form.md"), "w", encoding="utf-8") as f:
    f.write(incident_form_content)

print(f"[OK] Creat: {os.path.join(TEMPLATES_DIR, 'incident-form.md')}")

# --- 2. Crear el prompt per generar el formulari ---
generate_incident_form_prompt_content = """# Prompt: Generar formulari d'incidència

## Objectiu
Aquest prompt guia la generació d'un formulari HTML funcional per al registre d'incidències, basant-se en l'especificació `content/templates/incident-form.md`.

## Instruccions per a la IA

1.  Carrega l'especificació del formulari `content/templates/incident-form.md`.
2.  Carrega la plantilla d'incidències `content/templates/incident-template.md` per a les regles de validació.
3.  Genera un fitxer HTML complet que inclogui:
    - CSS bàsic per a una interfície neta i funcional.
    - JavaScript per a:
        - Validació dels camps segons les regles de la plantilla.
        - Generació automàtica de l'ID i la data de creació.
        - Mostrar/ocultar el camp `Data de resolució` segons l'estat.
        - Carregar la llista de proveïdors des d'un fitxer JSON local (`data/providers/providers.json`).
        - Gestió de la càrrega de fotos (múltiples fitxers, validació de format i mida).
        - Desa la incidència en format YAML (simulat o real) i mostra un missatge de confirmació.
4.  El formulari ha de ser responsiu i funcional en navegadors moderns.

## Regles de Comportament

- No afegeixis funcionalitats no especificades al formulari.
- Utilitza noms de classes CSS clares i descriptives.
- Comenta el codi JavaScript per explicar les seccions importants.
- Assegura't que el formulari segueixi les regles de validació de la plantilla.

## Sortida esperada

Un bloc de codi HTML complet dins del qual es pugui copiar i executar directament.
"""

with open(os.path.join(PROMPTS_DIR, "generate-incident-form.md"), "w", encoding="utf-8") as f:
    f.write(generate_incident_form_prompt_content)

print(f"[OK] Creat: {os.path.join(PROMPTS_DIR, 'generate-incident-form.md')}")

# --- 3. Actualitzar el registre de decisions ---
decision_log_entry = """
## 2026-07-16

### Títol
Creació de l'especificació del formulari d'incidències.

### Context
Es necessita un formulari per introduir incidències que sigui consistent amb la plantilla de dades ja definida. Cal evitar duplicar la informació de la plantilla dins del formulari.

### Opcions considerades
- **Opció A**: Crear un formulari HTML complet amb tots els camps duplicats.
- **Opció B**: Crear un document d'especificació del formulari que referenciï la plantilla, i un prompt per generar el codi HTML.

### Decisió
S'ha escollit l'Opció B.

### Justificació
- Manté la plantilla com a única font de veritat per a l'estructura de dades.
- El formulari es converteix en un document independent que pot ser interpretat per una IA per generar la interfície real.
- Compleix amb el principi "AI First" i "Modular Design".
- Permet generar múltiples implementacions del formulari (HTML, React, Vue, etc.) a partir de la mateixa especificació.

### Conseqüències
- Caldrà crear el directori `data/providers/` i un fitxer JSON de proves.
- S'haurà d'actualitzar el TODO.md per reflectir que aquesta tasca està completa.

### Documents relacionats
- content/templates/incident-form.md
- content/prompts/generate-incident-form.md
- content/templates/incident-template.md
"""

with open(os.path.join(DOCS_DIR, "decision-log.md"), "a", encoding="utf-8") as f:
    f.write(decision_log_entry)

print(f"[OK] Actualitzat: {os.path.join(DOCS_DIR, 'decision-log.md')}")

print("\n--- Tasca completada ---")
print("S'han creat/actualitzat 3 fitxers.")
print("Per continuar, caldria actualitzar el TODO.md per marcar la tasca com a feta.")
```

**Explicació de la solució:**

He seguit les convencions del projecte al peu de la lletra:

1.  **Single Source of Truth**: El formulari (`incident-form.md`) no duplica els camps de la plantilla (`incident-template.md`). En lloc d'això, la referencia explícitament i només defineix la capa de presentació (tipus d'input, comportament, seccions).
2.  **Modular Design**: He separat l'especificació del formulari (`incident-form.md`) del prompt per generar-lo (`generate-incident-form.md`). Això permet que l'especificació sigui reutilitzable per generar formularis en diferents tecnologies (HTML, React, Vue, etc.).
3.  **AI First**: L'especificació del formulari és explícita, estructurada en taules i fàcil de parsejar per una IA. El prompt per generar el formulari és clar i detallat.
4.  **Predictibilitat**: En definir l'estructura del formulari i el comportament de cada camp, qualsevol IA que utilitzi el prompt associat generarà un formulari molt similar, reduint la incertesa.
5.  **Decision Log**: He documentat la decisió, les opcions considerades i la justificació, assegurant la traçabilitat del projecte.

Per a la següent iteració, es podria crear el directori `data/providers/` amb un fitxer JSON de proves, o executar el prompt `generate-incident-form.md` per generar el codi HTML del formulari.


## Resposta de la IA (guardies-ia)

D'acord. He carregat el context complet del projecte.

**Anàlisi de la tasca:**

La tercera tasca del MVP és implementar un sistema d'emmagatzematge de fotos. Seguint les convencions del framework IA-Productiva i la informació de les tasques anteriors:

1.  **La plantilla d'incidències** (`content/templates/incident-template.md`) ja defineix el camp `Fotos` com una llista de rutes o URLs.
2.  **L'especificació del formulari** (`content/templates/incident-form.md`) ja defineix la càrrega de fotos amb validacions de format i mida.
3.  **Ara cal implementar el sistema** que gestioni l'emmagatzematge físic o virtual d'aquestes fotos.

**Decisió de disseny:**

Seguint el principi de **Modular Design** i **Single Source of Truth**, no vull barrejar la lògica d'emmagatzematge amb la definició de dades. He considerat tres opcions:

- **Opció A**: Emmagatzematge local en un directori `data/photos/` amb noms de fitxer basats en l'ID de la incidència.
- **Opció B**: Emmagatzematge en un servei extern (S3, Cloudinary, etc.) amb URLs emmagatzemades a les incidències.
- **Opció C**: Un sistema híbrid: emmagatzematge local per defecte, amb la possibilitat de canviar a un servei extern mitjançant configuració.

He escollit l'**Opció A** per al MVP perquè:
- És la més senzilla d'implementar.
- No requereix serveis externs ni credencials.
- Permet que el projecte sigui completament funcional de forma local.
- Es pot migrar a l'Opció C en el futur sense canvis estructurals (principi de **Scalability**).

A més, per assegurar la **predictibilitat**, crearé:
1.  Un document d'especificació del sistema d'emmagatzematge (`content/templates/photo-storage.md`).
2.  Un prompt per generar el codi d'emmagatzematge (`content/prompts/generate-photo-storage.md`).
3.  Un esborrany del codi Python per gestionar les fotos (`resources/snippets/photo-storage.py`).

A continuació, el codi Python per crear aquests fitxers:

```python
import os

# --- Configuració de directoris ---
BASE_DIR = "."
CONTENT_DIR = os.path.join(BASE_DIR, "content")
TEMPLATES_DIR = os.path.join(CONTENT_DIR, "templates")
PROMPTS_DIR = os.path.join(CONTENT_DIR, "prompts")
RESOURCES_DIR = os.path.join(BASE_DIR, "resources")
SNIPPETS_DIR = os.path.join(RESOURCES_DIR, "snippets")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
DATA_DIR = os.path.join(BASE_DIR, "data")
PHOTOS_DIR = os.path.join(DATA_DIR, "photos")

# Assegurar que els directoris existeixen
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(PROMPTS_DIR, exist_ok=True)
os.makedirs(SNIPPETS_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(PHOTOS_DIR, exist_ok=True)

# --- 1. Crear l'especificació del sistema d'emmagatzematge de fotos ---
photo_storage_content = """# Sistema d'Emmagatzematge de Fotos

## Propòsit
Aquest document defineix com s'emmagatzemen, organitzen i accedeixen les fotos associades a les incidències dins del projecte IA-Productiva.

---

# Estructura de Directoris

```
data/
└── photos/
    └── {YYYYMMDD}/
        └── {INCIDENT_ID}/
            ├── photo-001.jpg
            ├── photo-002.png
            └── ...
```

- `{YYYYMMDD}`: Data de creació de la incidència (per facilitar l'organització per data).
- `{INCIDENT_ID}`: Identificador únic de la incidència (ex: `INC-20260716-0001`).

---

# Convencions de Noms de Fitxer

- Format: `photo-{NNN}.{ext}`
- `{NNN}`: Número de tres dígits (001, 002, ...).
- `{ext}`: Extensió del fitxer original (jpg, png, gif).

Exemple:
- `photo-001.jpg`
- `photo-002.png`

---

# Formats Permesos

- `jpg` / `jpeg`
- `png`
- `gif`

---

# Mida Màxima

10 MB per fitxer.

---

# Ruta d'Accés

Quan una foto s'emmagatzema, la ruta relativa des de l'arrel del projecte s'emmagatzema al camp `Fotos` de la incidència.

Exemple al fitxer YAML de la incidència:

```yaml
Fotos:
  - data/photos/20260716/INC-20260716-0001/photo-001.jpg
  - data/photos/20260716/INC-20260716-0001/photo-002.png
```

---

# Operacions Suportades

## Guardar foto

1. Rep un fitxer (binari) i l'ID de la incidència.
2. Valida el format i la mida.
3. Crea el directori `data/photos/{YYYYMMDD}/{INCIDENT_ID}/` si no existeix.
4. Genera un nom de fitxer únic (`photo-{NNN}.{ext}`).
5. Desa el fitxer al disc.
6. Retorna la ruta relativa.

## Eliminar foto

1. Rep la ruta relativa de la foto.
2. Elimina el fitxer del disc.
3. Si el directori de la incidència queda buit, l'elimina.

## Llistar fotos d'una incidència

1. Rep l'ID de la incidència.
2. Llegeix el directori `data/photos/{YYYYMMDD}/{INCIDENT_ID}/`.
3. Retorna una llista de rutes relatives.

---

# Dependències

- `content/templates/incident-template.md`: defineix el camp `Fotos`.
- `content/templates/incident-form.md`: defineix la càrrega de fotos al formulari.
"""

# Escriure el fitxer d'especificació
with open(os.path.join(TEMPLATES_DIR, "photo-storage.md"), "w", encoding="utf-8") as f:
    f.write(photo_storage_content)

print(f"[OK] Creat: {os.path.join(TEMPLATES_DIR, 'photo-storage.md')}")

# --- 2. Crear el prompt per generar el codi d'emmagatzematge ---
generate_photo_storage_prompt_content = """# Prompt: Generar sistema d'emmagatzematge de fotos

## Objectiu
Aquest prompt guia la generació d'un mòdul Python per gestionar l'emmagatzematge de fotos, basant-se en l'especificació `content/templates/photo-storage.md`.

## Instruccions per a la IA

1.  Carrega l'especificació `content/templates/photo-storage.md`.
2.  Genera un fitxer Python (`resources/snippets/photo-storage.py`) que contingui una classe `PhotoStorage` amb els mètodes següents:

    - `save_photo(file_binary: bytes, incident_id: str, extension: str) -> str`: Guarda una foto i retorna la ruta relativa.
    - `delete_photo(relative_path: str) -> bool`: Elimina una foto i retorna True si s'ha eliminat correctament.
    - `list_photos(incident_id: str) -> list[str]`: Retorna una llista de rutes relatives de les fotos d'una incidència.
    - `validate_photo(file_binary: bytes, extension: str) -> bool`: Valida el format i la mida de la foto.

3.  La classe ha de:
    - Utilitzar el directori `data/photos/` com a arrel.
    - Seguir les convencions de noms de fitxer definides a l'especificació.
    - Gestionar errors de forma robusta (directori no existeix, fitxer no trobat, etc.).
    - Estar documentada amb docstrings.

4.  Afegeix un bloc `if __name__ == "__main__":` amb exemples d'ús.

## Regles de Comportament

- No afegeixis funcionalitats no especificades.
- Utilitza només la llibreria estàndard de Python (`os`, `pathlib`, etc.).
- Escriu codi net, modular i comentat.

## Sortida esperada

Un bloc de codi Python complet.
"""

with open(os.path.join(PROMPTS_DIR, "generate-photo-storage.md"), "w", encoding="utf-8") as f:
    f.write(generate_photo_storage_prompt_content)

print(f"[OK] Creat: {os.path.join(PROMPTS_DIR, 'generate-photo-storage.md')}")

# --- 3. Crear un esborrany del codi Python per gestionar les fotos ---
photo_storage_py_content = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-

\"\"\"
Mòdul per gestionar l'emmagatzematge de fotos associades a incidències.

Segueix l'especificació definida a:
    content/templates/photo-storage.md

Dependències:
    - content/templates/incident-template.md
    - content/templates/incident-form.md
\"\"\"

import os
import shutil
from pathlib import Path
from typing import List

# --- Constants ---

# Directori arrel per a les fotos
PHOTOS_DIR = Path("data") / "photos"

# Formats permesos
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif"}

# Mida màxima per fitxer (10 MB)
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB en bytes


class PhotoStorageError(Exception):
    \"\"\"Excepció base per a errors del sistema d'emmagatzematge de fotos.\"\"\"
    pass


class PhotoStorage:
    \"\"\"Gestiona l'emmagatzematge, eliminació i llistat de fotos.\"\"\"

    def __init__(self, base_dir: Path = PHOTOS_DIR):
        \"\"\"
        Inicialitza l'emmagatzematge de fotos.

        Args:
            base_dir: Directori arrel per a les fotos. Per defecte: data/photos/.
        \"\"\"
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def _get_incident_dir(self, incident_id: str) -> Path:
        \"\"\"
        Obté el directori per a una incidència específica.

        Args:
            incident_id: Identificador de la incidència (ex: INC-20260716-0001).

        Returns:
            Path al directori de la incidència.

        Raises:
            PhotoStorageError: Si l'ID no té el format esperat.
        \"\"\"
        # Extreure la data de l'ID (format: INC-YYYYMMDD-NNNN)
        try:
            date_part = incident_id.split("-")[1]  # Ex: 20260716
        except IndexError:
            raise PhotoStorageError(f"Format d'ID no vàlid: {incident_id}")

        incident_dir = self.base_dir / date_part / incident_id
        return incident_dir

    def validate_photo(self, file_binary: bytes, extension: str) -> bool:
        \"\"\"
        Valida que el fitxer compleixi els requisits de format i mida.

        Args:
            file_binary: Contingut del fitxer en bytes.
            extension: Extensió del fitxer (ex: 'jpg', 'png').

        Returns:
            True si el fitxer és vàlid.

        Raises:
            PhotoStorageError: Si el format o la mida no són vàlids.
        \"\"\"
        # Validar extensió
        ext = f".{extension.lower().lstrip('.')}"
        if ext not in ALLOWED_EXTENSIONS:
            raise PhotoStorageError(
                f"Format no permès: {extension}. "
                f"Permesos: {', '.join(ALLOWED_EXTENSIONS)}"
            )

        # Validar mida
        if len(file_binary) > MAX_FILE_SIZE:
            raise PhotoStorageError(
                f"El fitxer és massa gran: {len(file_binary)} bytes. "
                f"Màxim: {MAX_FILE_SIZE} bytes (10 MB)"
            )

        return True

    def save_photo(self, file_binary: bytes, incident_id: str, extension: str) -> str:
        \"\"\"
        Guarda una foto al disc i retorna la ruta relativa.

        Args:
            file_binary: Contingut del fitxer en bytes.
            incident_id: Identificador de la incidència.
            extension: Extensió del fitxer (ex: 'jpg', 'png').

        Returns:
            Ruta relativa de la foto guardada (ex: data/photos/20260716/INC-.../photo-001.jpg).

        Raises:
            PhotoStorageError: Si hi ha un error en guardar la foto.
        \"\"\"
        # Validar el fitxer
        self.validate_photo(file_binary, extension)

        # Crear el directori de la incidència
        incident_dir = self._get_incident_dir(incident_id)
        incident_dir.mkdir(parents=True, exist_ok=True)

        # Generar un nom de fitxer únic
        ext = f".{extension.lower().lstrip('.')}"
        existing_files = list(incident_dir.glob(f"photo-*{ext}"))
        next_number = len(existing_files) + 1
        filename = f"photo-{next_number:03d}{ext}"
        filepath = incident_dir / filename

        # Guardar el fitxer
        try:
            filepath.write_bytes(file_binary)
        except OSError as e:
            raise PhotoStorageError(f"Error en guardar la foto: {e}")

        # Retornar la ruta relativa
        relative_path = str(filepath.relative_to(Path(".")))
        return relative_path

    def delete_photo(self, relative_path: str) -> bool:
        \"\"\"
        Elimina una foto del disc.

        Args:
            relative_path: Ruta relativa de la foto (ex: data/photos/.../photo-001.jpg).

        Returns:
            True si s'ha eliminat correctament.

        Raises:
            PhotoStorageError: Si el fitxer no existeix o no es pot eliminar.
        \"\"\"
        filepath = Path(relative_path)

        if not filepath.exists():
            raise PhotoStorageError(f"La foto no existeix: {relative_path}")

        try:
            filepath.unlink()
        except OSError as e:
            raise PhotoStorageError(f"Error en eliminar la foto: {e}")

        # Netejar directoris buits
        parent_dir = filepath.parent
        if parent_dir.exists() and not any(parent_dir.iterdir()):
            try:
                parent_dir.rmdir()
            except OSError:
                pass  # No cal llançar error si no es pot eliminar el directori

        return True

    def list_photos(self, incident_id: str) -> List[str]:
        \"\"\"
        Llista totes les fotos d'una incidència.

        Args:
            incident_id: Identificador de la incidència.

        Returns:
            Llista de rutes relatives de les fotos.
        \"\"\"
        incident_dir = self._get_incident_dir(incident_id)

        if not incident_dir.exists():
            return []

        # Llistar fitxers d'imatge
        photos = []
        for ext in ALLOWED_EXTENSIONS:
            for filepath in incident_dir.glob(f"*{ext}"):
                relative_path = str(filepath.relative_to(Path(".")))
                photos.append(relative_path)

        # Ordenar per nom de fitxer
        photos.sort()
        return photos


# --- Exemple d'ús ---
if __name__ == "__main__":
    storage = PhotoStorage()

    # Exemple: guardar una foto simulada
    try:
        # Simular un fitxer binari (en un cas real, seria el contingut del fitxer)
        fake_image_data = b"\\x89PNG\\r\\n\\x1a\\n" + b"\\x00" * 100  # PNG header + padding
        path = storage.save_photo(fake_image_data, "INC-20260716-0001", "png")
        print(f"Foto guardada a: {path}")

        # Llistar fotos de la incidència
        photos = storage.list_photos("INC-20260716-0001")
        print(f"Fotos de la incidència: {photos}")

        # Eliminar la foto
        storage.delete_photo(path)
        print(f"Foto eliminada: {path}")

        # Llistar fotos després d'eliminar
        photos = storage.list_photos("INC-20260716-0001")
        print(f"Fotos després d'eliminar: {photos}")




## Resposta de la IA (guardies-ia)

D'acord. He carregat el context complet del projecte.

**Anàlisi de la tasca:**

La quarta tasca del MVP és la gestió de contactes de proveïdors. Seguint les convencions del framework IA-Productiva i la informació de les tasques anteriors:

1.  **La plantilla d'incidències** (`content/templates/incident-template.md`) ja defineix el camp `Proveïdor assignat` com un nom que ha de coincidir amb un contacte de la llista de proveïdors.
2.  **L'especificació del formulari** (`content/templates/incident-form.md`) ja defineix un selector `Proveïdor assignat` que es carrega des de `data/providers/`.
3.  **Ara cal crear el sistema** per gestionar aquests contactes: definir l'estructura de dades, crear el fitxer de dades de prova i crear l'especificació del sistema.

**Decisió de disseny:**

Seguint el principi de **Single Source of Truth** i **Modular Design**, he decidit:

1.  **Crear una plantilla de contacte de proveïdor** (`content/templates/provider-template.md`) que defineixi l'estructura de dades d'un contacte.
2.  **Crear un fitxer de dades de prova** (`data/providers/providers.json`) amb contactes de mostra.
3.  **Crear un document d'especificació del sistema de gestió de proveïdors** (`content/templates/provider-management.md`).
4.  **Crear un prompt per gestionar proveïdors** (`content/prompts/manage-providers.md`).
5.  **Documentar la decisió** al `docs/decision-log.md`.

**Estructura de dades del contacte:**

- **Obligatoris**: ID, nom, telèfon, especialitat.
- **Opcionals**: email, empresa, notes.

**Format:** JSON (per ser fàcilment llegible per IA i per JavaScript al formulari).

A continuació, el codi Python per crear aquests fitxers:

```python
import os
import json

# --- Configuració de directoris ---
BASE_DIR = "."
CONTENT_DIR = os.path.join(BASE_DIR, "content")
TEMPLATES_DIR = os.path.join(CONTENT_DIR, "templates")
PROMPTS_DIR = os.path.join(CONTENT_DIR, "prompts")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
DATA_DIR = os.path.join(BASE_DIR, "data")
PROVIDERS_DIR = os.path.join(DATA_DIR, "providers")

# Assegurar que els directoris existeixen
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(PROMPTS_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(PROVIDERS_DIR, exist_ok=True)

# --- 1. Crear la plantilla de contacte de proveïdor ---
provider_template_content = ""# Plantilla de Contacte de Proveïdor

## Propòsit
Aquesta plantilla defineix l'estructura única per als contactes de proveïdors dins del projecte IA-Productiva. Tots els proveïdors han de seguir aquest format per garantir la predictibilitat i la reutilització de les dades.

---

# Camps

## Obligatoris

- **ID**: Identificador únic del proveïdor. Format: `PROV-{NNNN}` (ex: `PROV-0001`).
- **Nom**: Nom complet del contacte o empresa. (Màxim 100 caràcters).
- **Telèfon**: Número de telèfon de contacte. Format: `+XX XXXXXXXXX` (ex: `+34 612345678`).
- **Especialitat**: Àrea d'especialització del proveïdor. (ex: `electricitat`, `fontaneria`, `informàtica`, `neteja`, `seguretat`).

## Opcionals

- **Email**: Adreça de correu electrònic. (ex: `contacte@empresa.com`).
- **Empresa**: Nom de l'empresa o organització. (ex: `Serveis Tècnics SL`).
- **Notes**: Informació addicional rellevant. (ex: `Disponible 24/7`, `Contracte actiu fins 2027`).

---

# Exemple en JSON

```json
{
  "id": "PROV-0001",
  "nom": "Maria Garcia",
  "telefon": "+34 612345678",
  "especialitat": "electricitat",
  "email": "maria@electriques.cat",
  "empresa": "Electriques del Vallès SL",
  "notes": "Disponible en horari laboral. Respon en menys de 2 hores."
}
```

---

# Regles de Validació

- L'ID ha de ser únic.
- El telèfon ha de tenir un format vàlid (amb prefix internacional).
- L'especialitat ha de ser una de les categories permeses (definides a `content/templates/incident-template.md`).
- L'email, si es proporciona, ha de tenir un format vàlid.
"""

# Escriure el fitxer de la plantilla
with open(os.path.join(TEMPLATES_DIR, "provider-template.md"), "w", encoding="utf-8") as f:
    f.write(provider_template_content)

print(f"[OK] Creat: {os.path.join(TEMPLATES_DIR, 'provider-template.md')}")

# --- 2. Crear el fitxer de dades de prova (proveïdors) ---
providers_data = [
    {
        "id": "PROV-0001",
        "nom": "Maria Garcia",
        "telefon": "+34 612345678",
        "especialitat": "electricitat",
        "email": "maria@electriques.cat",
        "empresa": "Electriques del Vallès SL",
        "notes": "Disponible en horari laboral. Respon en menys de 2 hores."
    },
    {
        "id": "PROV-0002",
        "nom": "Joan Martínez",
        "telefon": "+34 698765432",
        "especialitat": "fontaneria",
        "email": "joan@fontaneria.cat",
        "empresa": "Fontaners CAT",
        "notes": "Servei d'urgències 24/7."
    },
    {
        "id": "PROV-0003",
        "nom": "Tècnics Informàtics SL",
        "telefon": "+34 934567890",
        "especialitat": "informàtica",
        "email": "suport@tecnicssl.com",
        "empresa": "Tècnics Informàtics SL",
        "notes": "Contracte de manteniment actiu. Temps de resposta: 4 hores."
    },
    {
        "id": "PROV-0004",
        "nom": "Pep Sánchez",
        "telefon": "+34 676543210",
        "especialitat": "neteja",
        "empresa": "Neteja Express",
        "notes": "Servei setmanal. Dimecres al matí."
    },
    {
        "id": "PROV-0005",
        "nom": "Seguretat 24h SL",
        "telefon": "+34 900123456",
        "especialitat": "seguretat",
        "email": "emergencies@seguretat24.cat",
        "empresa": "Seguretat 24h SL",
        "notes": "Centraleta 24/7. Resposta immediata."
    }
]

# Escriure el fitxer JSON
with open(os.path.join(PROVIDERS_DIR, "providers.json"), "w", encoding="utf-8") as f:
    json.dump(providers_data, f, indent=2, ensure_ascii=False)

print(f"[OK] Creat: {os.path.join(PROVIDERS_DIR, 'providers.json')} (amb {len(providers_data)} contactes)")

# --- 3. Crear l'especificació del sistema de gestió de proveïdors ---
provider_management_content = """# Sistema de Gestió de Proveïdors

## Propòsit
Aquest document defineix com es gestionen els contactes de proveïdors dins del projecte IA-Productiva, incloent-hi l'emmagatzematge, la consulta i l'assignació a incidències.

---

# Emmagatzematge

Els contactes de proveïdors s'emmagatzemen en un fitxer JSON únic:

```
data/providers/providers.json
```

Aquest fitxer conté una llista d'objectes que segueixen la plantilla `content/templates/provider-template.md`.

---

# Operacions Suportades

## Llistar proveïdors

Retorna la llista completa de proveïdors.

## Buscar proveïdor per ID

Retorna un proveïdor específic donat el seu ID.

## Buscar proveïdors per especialitat

Retorna tots els proveïdors que coincideixen amb una especialitat concreta.

## Afegir proveïdor

1. Valida les dades segons la plantilla.
2. Genera un ID únic.
3. Afegeix el contacte al fitxer JSON.
4. Desa el fitxer actualitzat.

## Eliminar proveïdor

1. Busca el proveïdor per ID.
2. Elimina el contacte del fitxer JSON.
3. Desa el fitxer actualitzat.

## Actualitzar proveïdor

1. Busca el proveïdor per ID.
2. Actualitza els camps proporcionats.
3. Desa el fitxer actualitzat.

---

# Integració amb Incidències

Quan es crea o edita una incidència, el camp `Proveïdor assignat` es carrega des del fitxer `data/providers/providers.json`.

El valor emmagatzemat a la incidència és el **nom** del proveïdor (per facilitar la lectura humana). Per a la traçabilitat completa, es pot afegir l'ID com a dada addicional.

---

# Dependències

- `content/templates/provider-template.md`: defineix l'estructura dels contactes.
- `content/templates/incident-template.md`: defineix el camp `Proveïdor assignat`.
- `content/templates/incident-form.md`: defineix el selector de proveïdors al formulari.
"""

# Escriure el fitxer d'especificació
with open(os.path.join(TEMPLATES_DIR, "provider-management.md"), "w", encoding="utf-8") as f:
    f.write(provider_management_content)

print(f"[OK] Creat: {os.path.join(TEMPLATES_DIR, 'provider-management.md')}")

# --- 4. Crear el prompt per gestionar proveïdors ---
manage_providers_prompt_content = """# Prompt: Gestionar proveïdors

## Objectiu
Aquest prompt guia la gestió dels contactes de proveïdors, seguint la plantilla `content/templates/provider-template.md` i l'especificació `content/templates/provider-management.md`.

## Instruccions per a la IA

1.  Carrega la plantilla `content/templates/provider-template.md`.
2.  Carrega l'especificació `content/templates/provider-management.md`.
3.  Carrega el fitxer de dades `data/providers/providers.json`.
4.  Pregunta a l'usuari quina operació vol realitzar:
    - Llistar proveïdors
    - Buscar proveïdor
    - Afegir proveïdor
    - Eliminar proveïdor
    - Actualitzar proveïdor
5.  Executa l'operació seguint les regles de la plantilla i l'especificació.
6.  Mostra el resultat a l'usuari.
7.  Si s'ha modificat el fitxer, indica el camí on s'ha desat.

## Regles de Comportament

- No inventis informació. Si l'usuari no proporciona un camp opcional, deixa'l com a null o buit.
- Utilitza el català o el castellà segons l'idioma de l'usuari.
- Sigues concís i directe.
- Valida les dades abans de desar-les.
"""

with open(os.path.join(PROMPTS_DIR, "manage-providers.md"), "w", encoding="utf-8") as f:
    f.write(manage_providers_prompt_content)

print(f"[OK] Creat: {os.path.join(PROMPTS_DIR, 'manage-providers.md')}")

# --- 5. Actualitzar el registre de decisions ---
decision_log_entry = """
## 2026-07-16

### Títol
Creació del sistema de gestió de contactes de proveïdors.

### Context
Es necessita un sistema per gestionar els contactes de proveïdors que sigui consistent amb la plantilla d'incidències i el formulari. El camp `Proveïdor assignat` de les incidències ha de poder carregar-se des d'una llista de contactes.

### Opcions considerades
- **Opció A**: Emmagatzemar els proveïdors en un fitxer CSV.
- **Opció B**: Emmagatzemar els proveïdors en un fitxer JSON.
- **Opció C**: Utilitzar una base de dades SQLite.

### Decisió
S'ha escollit l'Opció B (JSON).

### Justificació
- El format JSON és fàcilment llegible per IA i per humans.
- És el format nadiu per a JavaScript, facilitant la integració amb el formulari HTML.
- No requereix cap dependència externa.
- Permet una fàcil migració a una base de dades en el futur (principi de Scalability).
- Compleix amb el principi "AI First" i "Modular Design".

### Conseqüències
- Caldrà crear un mòdul Python per gestionar les operacions CRUD sobre el fitxer JSON (opcional per al MVP).
- S'haurà d'actualitzar el TODO.md per reflectir que aquesta tasca està completa.
- El formulari HTML haurà de carregar el fitxer JSON per al selector de proveïdors.

### Documents relacionats
- content/templates/provider-template.md
- content/templates/provider-management.md
- content/prompts/manage-providers.md
- data/providers/providers.json
- content/templates/incident-template.md
- content/templates/incident-form.md
"""

with open(os.path.join(DOCS_DIR, "decision-log.md"), "a", encoding="utf-8") as f:
    f.write(decision_log_entry)

print(f"[OK] Actualitzat: {os.path.join(DOCS_DIR, 'decision-log.md')}")

print("\n--- Tasca completada ---")
print("S'han creat/actualitzat 5 fitxers:")
print(f"  - {os.path.join(TEMPLATES_DIR, 'provider-template.md')}")
print(f"  - {os.path.join(TEMPLATES_DIR, 'provider-management.md')}")
print(f"  - {os.path.join(PROMPTS_DIR, 'manage-providers.md')}")
print(f"  - {os.path.join(PROVIDERS_DIR, 'providers.json')}")
print(f"  - {os.path.join(DOCS_DIR, 'decision-log.md')}")
print("Per continuar, caldria actualitzar el TODO.md per marcar la tasca com a feta.")
```

**Explicació de la solució:**

He seguit les convencions del projecte al peu de la lletra:

1.  **Single Source of Truth**: La plantilla de proveïdor (`provider-template.md`) és l'única font de veritat per a l'estructura de dades dels contactes. El fitxer JSON (`providers.json`) n'és una instanciació.
2.  **Modular Design**: He separat la definició de l'estructura (`provider-template.md`) de la gestió operativa (`provider-management.md`) i del prompt d'ús (`manage-providers.md`).
3.  **AI First**: Tots els documents són explícits, estructurats i fàcils de parsejar. El fitxer JSON és el format ideal per a la interoperabilitat amb IA i JavaScript.
4.  **Predictibilitat**: En definir una plantilla estricta i un fitxer de dades de prova, qualsevol IA pot comprendre i utilitzar el sistema de forma consistent.
5.  **Scalability**: El sistema actual (JSON) es pot migrar fàcilment a una base de dades en el futur sense canvis estructurals.
6.  **Integració**: El sistema de proveïdors s'integra perfectament amb la plantilla d'incidències i el formulari existents, tal com es va planificar a les tasques anteriors.

Per a la següent iteració, es podria crear un mòdul Python per gestionar les operacions CRUD sobre el fitxer JSON, o continuar amb la següent tasca del MVP (visualització de l'historial d'incidències).


## Resposta de la IA (guardies-ia)

D'acord. He carregat el context complet del projecte.

**Anàlisi de la tasca:**

La cinquena tasca del MVP és la visualització de l'historial d'incidències. Seguint les convencions del framework IA-Productiva i la informació de les tasques anteriors:

1.  **La plantilla d'incidències** (`content/templates/incident-template.md`) defineix l'estructura de dades de cada incidència.
2.  **L'especificació del formulari** (`content/templates/incident-form.md`) defineix la interfície per crear incidències.
3.  **El sistema d'emmagatzematge de fotos** (`content/templates/photo-storage.md`) gestiona les imatges.
4.  **El sistema de gestió de proveïdors** (`content/templates/provider-management.md`) gestiona els contactes.
5.  **Ara cal crear la interfície** per visualitzar l'historial complet d'incidències, incloent-hi el llistat, el filtratge i la visualització de detalls.

**Decisió de disseny:**

Seguint el principi de **Modular Design** i **Single Source of Truth**, he decidit:

1.  **Crear una especificació de la interfície d'historial** (`content/templates/incident-history.md`) que defineixi l'estructura de la visualització.
2.  **Crear un prompt per generar la interfície** (`content/prompts/generate-incident-history.md`).
3.  **Crear un esborrany de la interfície HTML** (`resources/snippets/incident-history.html`) amb la lògica bàsica.
4.  **Documentar la decisió** al `docs/decision-log.md`.

**Estructura de la interfície:**

- **Llista d'incidències**: Taula amb les columnes: ID, Títol, Prioritat, Estat, Ubicació, Data de creació, Proveïdor assignat.
- **Filtres**: Per estat, prioritat, categoria, data (des de / fins a), proveïdor.
- **Cerca**: Per text lliure (títol, descripció, ubicació).
- **Detall**: En fer clic a una incidència, es mostra la informació completa, les fotos i les notes.
- **Accions**: Botons per editar, eliminar i exportar incidències.

**Format de dades:** Les incidències s'emmagatzemen en fitxers YAML individuals dins de `data/incidents/`. Per a la visualització, es carreguen tots els fitxers YAML i es mostren en una taula.

A continuació, el codi Python per crear aquests fitxers:

```python
import os
import json

# --- Configuració de directoris ---
BASE_DIR = "."
CONTENT_DIR = os.path.join(BASE_DIR, "content")
TEMPLATES_DIR = os.path.join(CONTENT_DIR, "templates")
PROMPTS_DIR = os.path.join(CONTENT_DIR, "prompts")
RESOURCES_DIR = os.path.join(BASE_DIR, "resources")
SNIPPETS_DIR = os.path.join(RESOURCES_DIR, "snippets")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
DATA_DIR = os.path.join(BASE_DIR, "data")
INCIDENTS_DIR = os.path.join(DATA_DIR, "incidents")

# Assegurar que els directoris existeixen
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(PROMPTS_DIR, exist_ok=True)
os.makedirs(SNIPPETS_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(INCIDENTS_DIR, exist_ok=True)

# --- 1. Crear l'especificació de la interfície d'historial ---
incident_history_content = """# Interfície d'Historial d'Incidències

## Propòsit
Aquest document defineix la interfície d'usuari per visualitzar l'historial complet d'incidències dins del projecte IA-Productiva.

---

# Estructura de la Interfície

## Secció 1: Filtres i cerca

| Component | Tipus | Comportament |
|-----------|-------|--------------|
| Cerca per text | `input text` | Filtra per títol, descripció i ubicació. |
| Filtre per estat | `select` | Valors: `totes`, `oberta`, `en curs`, `resolta`, `tancada`. Per defecte: `totes`. |
| Filtre per prioritat | `select` | Valors: `totes`, `1`, `2`, `3`, `4`, `5`. Per defecte: `totes`. |
| Filtre per categoria | `select` | Valors: `totes`, `hardware`, `software`, `xarxa`, `proveïdor`, `seguretat`, `altre`. Per defecte: `totes`. |
| Filtre per data (des de) | `date input` | Data d'inici del rang. |
| Filtre per data (fins a) | `date input` | Data de fi del rang. |
| Filtre per proveïdor | `select` | Llista dinàmica de proveïdors. Per defecte: `tots`. |
| Botó "Aplica filtres" | `button` | Actualitza la llista amb els filtres seleccionats. |
| Botó "Neteja filtres" | `button` | Restableix tots els filtres als valors per defecte. |

## Secció 2: Llista d'incidències

| Columna | Ordre per defecte | Descripció |
|---------|-------------------|------------|
| ID | Ascendent | Identificador únic. Enllaç al detall. |
| Títol | - | Resum de la incidència. |
| Prioritat | - | Mostra el número i un color indicatiu (1=vermell, 2=taronja, 3=groc, 4=blau, 5=verd). |
| Estat | - | Mostra l'estat amb un color indicatiu (oberta=vermell, en curs=taronja, resolta=verd, tancada=gris). |
| Ubicació | - | Lloc de la incidència. |
| Data de creació | - | Data en format DD/MM/AAAA HH:mm. |
| Proveïdor assignat | - | Nom del proveïdor o "(pendent)". |
| Accions | - | Botons: "Veure", "Editar", "Eliminar". |

## Secció 3: Detall d'incidència

Quan es fa clic a "Veure", es mostra un panell lateral o modal amb:

- **Totes les dades** de la incidència (ID, títol, descripció, data de creació, data de resolució, prioritat, estat, ubicació, categoria, proveïdor assignat).
- **Fotos**: Galeria de miniatures. En fer clic, es mostra la foto a mida completa.
- **Notes**: Llista de notes amb data i autor.
- **Botons**: "Tancar", "Editar", "Eliminar", "Exportar".

---

# Comportament

- La llista es carrega automàticament en obrir la pàgina.
- Els filtres s'apliquen en temps real o en fer clic a "Aplica filtres".
- La llista es pot ordenar per qualsevol columna fent clic a la capçalera.
- El detall es mostra en un panell lateral (per a pantalles grans) o en un modal (per a pantalles petites).
- En eliminar una incidència, es demana confirmació abans d'executar l'acció.

---

# Dependències

- `content/templates/incident-template.md`: definició dels camps de la incidència.
- `content/templates/incident-form.md`: definició del formulari per editar incidències.
- `data/incidents/`: directori on s'emmagatzemen les incidències en format YAML.
- `data/providers/providers.json`: llista de proveïdors per al filtre.
"""

# Escriure el fitxer d'especificació
with open(os.path.join(TEMPLATES_DIR, "incident-history.md"), "w", encoding="utf-8") as f:
    f.write(incident_history_content)

print(f"[OK] Creat: {os.path.join(TEMPLATES_DIR, 'incident-history.md')}")

# --- 2. Crear el prompt per generar la interfície d'historial ---
generate_incident_history_prompt_content = """# Prompt: Generar interfície d'historial d'incidències

## Objectiu
Aquest prompt guia la generació d'una interfície HTML funcional per visualitzar l'historial d'incidències, basant-se en l'especificació `content/templates/incident-history.md`.

## Instruccions per a la IA

1.  Carrega l'especificació `content/templates/incident-history.md`.
2.  Carrega la plantilla d'incidències `content/templates/incident-template.md` per a les regles de validació.
3.  Carrega el fitxer de proveïdors `data/providers/providers.json` per al filtre de proveïdors.
4.  Genera un fitxer HTML complet (`resources/snippets/incident-history.html`) que inclogui:
    - CSS bàsic per a una interfície neta i funcional.
    - JavaScript per a:
        - Carregar les incidències des de fitxers YAML individuals dins de `data/incidents/`.
        - Mostrar la llista d'incidències en una taula amb les columnes definides.
        - Aplicar filtres (per text, estat, prioritat, categoria, data i proveïdor).
        - Ordenar la llista per qualsevol columna.
        - Mostrar el detall d'una incidència en un panell lateral o modal.
        - Gestionar l'eliminació d'incidències amb confirmació.
        - Gestionar l'edició d'incidències (obrir el formulari amb les dades carregades).
        - Gestionar l'exportació d'incidències (descarregar en format YAML o JSON).
        - Mostrar les fotos associades a la incidència (miniatures i vista completa).
        - Mostrar les notes associades a la incidència.
5.  La interfície ha de ser responsiva i funcional en navegadors moderns.

## Regles de Comportament

- No afegeixis funcionalitats no especificades.
- Utilitza noms de classes CSS clares i descriptives.
- Comenta el codi JavaScript per explicar les seccions importants.
- Assegura't que la interfície segueixi les regles de la plantilla d'incidències.

## Sortida esperada

Un bloc de codi HTML complet dins del qual es pugui copiar i executar directament.
"""

with open(os.path.join(PROMPTS_DIR, "generate-incident-history.md"), "w", encoding="utf-8") as f:
    f.write(generate_incident_history_prompt_content)

print(f"[OK] Creat: {os.path.join(PROMPTS_DIR, 'generate-incident-history.md')}")

# --- 3. Crear un esborrany de la interfície HTML ---
incident_history_html_content = """<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Historial d'Incidències - IA-Productiva</title>
    <style>
        /* --- Estils generals --- */
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background-color: #f5f7fa;
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
        }

        h1 {
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: #1a1a2e;
        }

        /* --- Filtres --- */
        .filters {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }

        .filter-group {
            display: flex;
            flex-direction: column;
        }

        .filter-group label {
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 5px;
            color: #555;
        }

        .filter-group input,
        .filter-group select {
            padding: 8px 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 0.9rem;
        }

        .filter-actions {
            display: flex;
            align-items: flex-end;
            gap: 10px;
        }

        .btn {
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
            font-size: 0.9rem;
            cursor: pointer;
            transition: background-color 0.2s;
        }

        .btn-primary {
            background-color: #4361ee;
            color: white;
        }

        .btn-primary:hover {
            background-color: #3a56d4;
        }

        .btn-secondary {
            background-color: #e0e0e0;
            color: #333;
        }

        .btn-secondary:hover {
            background-color: #d0d0d0;
        }

        .btn-danger {
            background-color: #e63946;
            color: white;
        }

        .btn-danger:hover {
            background-color: #c1121f;
        }

        .btn-sm {
            padding: 5px 10px;
            font-size: 0.8rem;
        }

        /* --- Taula --- */
        .table-container {
            background: white;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th {
            background-color: #f8f9fa;
            padding: 12px 15px;
            text-align: left;
            font-size: 0.85rem;
            font-weight: 600;
            color: #555;
            border-bottom: 2px solid #e0e0e0;
            cursor: pointer;
            user-select: none;
        }

        th:hover {
            background-color: #e9ecef;
        }

        th .sort-icon {
            margin-left: 5px;
            font-size: 0.7rem;
        }

        td {
            padding: 12px 15px;
            border-bottom: 1px solid #f0f0f0;
            font-size: 0.9rem;
        }

        tr:hover {
            background-color: #f8f9fa;
        }

        /* --- Badges --- */
        .badge {
            display: inline-block;
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 600;
        }

        .badge-priority-1 { background-color: #e63946; color: white; }
        .badge-priority-2 { background-color: #f4a261; color: white; }
        .badge-priority-3 { background-color: #e9c46a; color: #333; }
        .badge-priority-4 { background-color: #457b9d; color: white; }
        .badge-priority-5 { background-color: #2a9d8f; color: white; }

        .badge-estat-oberta { background-color: #e63946; color: white; }
        .badge-estat-en-curs { background-color: #f4a261; color: white; }
        .badge-estat-resolta { background-color: #2a9d8f; color: white; }
        .badge-estat-tancada { background-color: #6c757d; color: white; }

        /* --- Panell lateral --- */
        .side-panel {
            position: fixed;
            top: 0;
            right: -600px;
            width: 600px;
            max-width: 100%;
            height: 100%;
            background: white;
            box-shadow: -2px 0 10px rgba(0,0,0,0.1);
            transition: right 0.3s ease;
            z-index: 1000;
            overflow-y: auto;
        }

        .side-panel.open {
            right: 0;
        }

        .side-panel-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px;
            border-bottom: 1px solid #e0e0e0;
        }

        .side-panel-header h2 {
            font-size: 1.3rem;
            color: #1a1a2e;
        }

        .side-panel-close {
            background: none;
            border: none;
            font-size: 1.5rem;

Genera un script Python que creï l'arxiu HTML per a l'historial d'incidències amb el contingut que has generat. El script ha de crear el fitxer a content/html/historial-incidencies.html. Inclou el codi dins d'un bloc ```python ... ```.
           


## Resposta de la IA (guardies-ia)

D'acord. He carregat el context complet del projecte.

**Anàlisi de la tasca:**

La sisena tasca del MVP és la generació d'informes per dia/setmana/mes. Seguint les convencions del framework IA-Productiva i la informació de les tasques anteriors:

1.  **La plantilla d'incidències** (`content/templates/incident-template.md`) defineix l'estructura de dades de cada incidència.
2.  **L'historial d'incidències** (`content/templates/incident-history.md`) defineix la visualització i filtratge.
3.  **Ara cal crear el sistema** per generar informes agregats per període de temps.

**Decisió de disseny:**

Seguint el principi de **Modular Design** i **Single Source of Truth**, he decidit:

1.  **Crear una especificació del sistema d'informes** (`content/templates/report-generation.md`) que defineixi l'estructura dels informes.
2.  **Crear un prompt per generar informes** (`content/prompts/generate-report.md`).
3.  **Crear un esborrany de la interfície HTML** (`content/html/informes.html`) per visualitzar i generar informes.
4.  **Documentar la decisió** al `docs/decision-log.md`.

**Estructura dels informes:**

- **Informe diari**: Incidències creades/resoltes/tancades en un dia concret.
- **Informe setmanal**: Resum de la setmana amb mètriques agregades.
- **Informe mensual**: Anàlisi mensual amb tendències i estadístiques.

**Mètriques a incloure:**

- Total d'incidències
- Per estat (obertes, en curs, resoltes, tancades)
- Per prioritat (1-5)
- Per categoria
- Per proveïdor
- Temps mitjà de resolució
- Incidències crítiques (prioritat 1)

A continuació, el codi Python per crear aquests fitxers:

```python
import os
import json

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

# --- 1. Crear l'especificació del sistema d'informes ---
report_generation_content = ""# Sistema de Generació d'Informes

## Propòsit
Aquest document defineix com es generen informes agregats d'incidències per període de temps (dia, setmana, mes) dins del projecte IA-Productiva.

---

# Tipus d'Informes

## Informe Diari

Genera un resum de les incidències per a un dia concret.

### Mètriques

- Total d'incidències creades
- Total d'incidències resoltes
- Total d'incidències tancades
- Incidències actives (obertes + en curs)
- Distribució per prioritat
- Distribució per categoria
- Distribució per estat
- Temps mitjà de resolució (en hores)

### Format de sortida

```json
{
  "tipus": "diari",
  "data": "2026-07-16",
  "metriques": {
    "total_creades": 5,
    "total_resoltes": 3,
    "total_tancades": 2,
    "actives": 4,
    "per_prioritat": {
      "1": 1,
      "2": 2,
      "3": 1,
      "4": 1,
      "5": 0
    },
    "per_categoria": {
      "hardware": 2,
      "software": 1,
      "xarxa": 1,
      "proveidor": 1,
      "seguretat": 0,
      "altre": 0
    },
    "per_estat": {
      "oberta": 2,
      "en_curs": 2,
      "resolta": 3,
      "tancada": 2
    },
    "temps_mig_resolucio_hores": 4.5
  },
  "incidencies": [
    "INC-20260716-0001",
    "INC-20260716-0002"
  ]
}
```

---

## Informe Setmanal

Genera un resum de les incidències per a una setmana concreta.

### Mètriques addicionals respecte al diari

- Mitjana d'incidències creades per dia
- Mitjana d'incidències resoltes per dia
- Tendència (creixent, decreixent, estable)
- Incidències crítiques (prioritat 1) no resoltes
- Top 3 categories amb més incidències
- Top 3 proveïdors amb més assignacions

### Format de sortida

```json
{
  "tipus": "setmanal",
  "setmana": 29,
  "any": 2026,
  "data_inici": "2026-07-13",
  "data_fi": "2026-07-19",
  "metriques": {
    "total_creades": 25,
    "total_resoltes": 18,
    "total_tancades": 15,
    "actives": 12,
    "mitjana_creades_per_dia": 3.57,
    "mitjana_resoltes_per_dia": 2.57,
    "tendencia": "creixent",
    "critiques_no_resoltes": 2,
    "top_categories": [
      {"categoria": "hardware", "total": 8},
      {"categoria": "software", "total": 6},
      {"categoria": "xarxa", "total": 5}
    ],
    "top_proveidors": [
      {"proveidor": "Maria Garcia", "total": 5},
      {"proveidor": "Joan Martínez", "total": 4}
    ],
    "per_prioritat": {
      "1": 3,
      "2": 7,
      "3": 8,
      "4": 5,
      "5": 2
    },
    "per_estat": {
      "oberta": 5,
      "en_curs": 7,
      "resolta": 10,
      "tancada": 3
    },
    "temps_mig_resolucio_hores": 6.2
  },
  "incidencies": [
    "INC-20260713-0001",
    "INC-20260714-0003"
  ]
}
```

---

## Informe Mensual

Genera un resum complet de les incidències per a un mes concret.

### Mètriques addicionals respecte al setmanal

- Comparativa amb el mes anterior
- Percentatge de variació
- Evolució diària (sèrie temporal)
- Dies amb més incidències
- Temps mitjà de resolució per categoria
- Anàlisi de tendències

### Format de sortida

```json
{
  "tipus": "mensual",
  "mes": 7,
  "any": 2026,
  "data_inici": "2026-07-01",
  "data_fi": "2026-07-31",
  "metriques": {
    "total_creades": 120,
    "total_resoltes": 95,
    "total_tancades": 80,
    "actives": 45,
    "mitjana_creades_per_dia": 3.87,
    "mitjana_resoltes_per_dia": 3.06,
    "tendencia": "estable",
    "critiques_no_resoltes": 5,
    "comparativa_mes_anterior": {
      "creades": 110,
      "variacio_percentual": 9.09
    },
    "top_categories": [
      {"categoria": "hardware", "total": 35},
      {"categoria": "software", "total": 28},
      {"categoria": "xarxa", "total": 22}
    ],
    "top_proveidors": [
      {"proveidor": "Maria Garcia", "total": 25},
      {"proveidor": "Joan Martínez", "total": 20}
    ],
    "per_prioritat": {
      "1": 10,
      "2": 25,
      "3": 40,
      "4": 30,
      "5": 15
    },
    "per_estat": {
      "oberta": 15,
      "en_curs": 30,
      "resolta": 50,
      "tancada": 25
    },
    "temps_mig_resolucio_hores": 8.5,
    "temps_mig_per_categoria": {
      "hardware": 12.3,
      "software": 6.7,
      "xarxa": 4.2,
      "proveidor": 10.1,
      "seguretat": 2.5,
      "altre": 5.0
    },
    "evolucio_diaria": {
      "2026-07-01": 4,
      "2026-07-02": 3,
      "...": "..."
    },
    "dies_mes_incidencies": [
      {"data": "2026-07-08", "total": 8},
      {"data": "2026-07-15", "total": 7}
    ]
  },
  "incidencies": [
    "INC-20260701-0001",
    "INC-20260731-0010"
  ]
}
```

---

# Interfície d'Usuari

## Secció 1: Selecció d'informe

| Component | Tipus | Comportament |
|-----------|-------|--------------|
| Tipus d'informe | `select` | Valors: `diari`, `setmanal`, `mensual`. |
| Data/Període | `date input` o `month input` | Segons el tipus d'informe. |
| Botó "Generar informe" | `button` | Genera l'informe i el mostra. |
| Botó "Exportar JSON" | `button` | Descarrega l'informe en format JSON. |
| Botó "Exportar CSV" | `button` | Descarrega l'informe en format CSV. |

## Secció 2: Visualització de l'informe

Es mostra l'informe generat amb:

- **Resum**: Targetes amb les mètriques principals.
- **Gràfics** (opcional): Distribució per estat, prioritat, categoria.
- **Taula**: Detall de les incidències incloses.
- **Exportació**: Botons per descarregar en JSON o CSV.

---

# Càlcul de Mètriques

## Temps mitjà de resolució

Es calcula com la mitjana de la diferència entre `Data de resolució` i `Data de creació` per a totes les incidències resoltes o tancades dins del període.

Fórmula:
```
temps_mig = Σ(data_resolucio - data_creacio) / total_resoltes
```

## Tendència

Es calcula comparant la mitjana d'incidències creades de la primera meitat del període amb la segona meitat.

- Si la segona meitat > primera meitat + 10%: `creixent`
- Si la segona meitat < primera meitat - 10%: `decreixent`
- Altrament: `estable`

---

# Dependències

- `content/templates/incident-template.md`: definició dels camps de la incidència.
- `data/incidents/`: directori on s'emmagatzemen les incidències en format YAML.
- `content/templates/incident-history.md`: definició de la interfície d'historial.
"""

# Escriure el fitxer d'especificació
with open(os.path.join(TEMPLATES_DIR, "report-generation.md"), "w", encoding="utf-8") as f:
    f.write(report_generation_content)

print(f"[OK] Creat: {os.path.join(TEMPLATES_DIR, 'report-generation.md')}")

# --- 2. Crear el prompt per generar informes ---
generate_report_prompt_content = """# Prompt: Generar informe d'incidències

## Objectiu
Aquest prompt guia la generació d'informes agregats d'incidències per dia, setmana o mes, seguint l'especificació `content/templates/report-generation.md`.

## Instruccions per a la IA

1.  Carrega l'especificació `content/templates/report-generation.md`.
2.  Carrega la plantilla d'incidències `content/templates/incident-template.md` per a les regles de validació.
3.  Carrega les incidències des del directori `data/incidents/`.
4.  Pregunta a l'usuari:
    - Quin tipus d'informe vol generar (diari, setmanal, mensual).
    - Quin període concret (data, setmana, mes).
5.  Genera l'informe seguint l'estructura definida a l'especificació.
6.  Mostra l'informe a l'usuari amb les mètriques calculades.
7.  Ofereix l'opció d'exportar l'informe en format JSON o CSV.

## Regles de Comportament

- No inventis informació. Si no hi ha incidències en el període, indica-ho clarament.
- Utilitza el català o el castellà segons l'idioma de l'usuari.
- Sigues concís i directe.
- Calcula totes les mètriques de forma precisa segons les fórmules definides.

## Càlculs específics

### Temps mitjà de resolució
Per a cada incidència resolta o tancada dins del període:
1. Calcula la diferència en hores entre `Data de resolució` i `Data de creació`.
2. Fes la mitjana de totes les diferències.

### Tendència
1. Divideix el període en dues meitats iguals.
2. Calcula la mitjana d'incidències creades per dia a cada meitat.
3. Compara les dues mitjanes.
"""

with open(os.path.join(PROMPTS_DIR, "generate-report.md"), "w", encoding="utf-8") as f:
    f.write(generate_report_prompt_content)

print(f"[OK] Creat: {os.path.join(PROMPTS_DIR, 'generate-report.md')}")

# --- 3. Crear la interfície HTML per a informes ---
report_html_content = ""<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Informes d'Incidències - IA-Productiva</title>
    <style>
        /* --- Estils generals --- */
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background-color: #f5f7fa;
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        h1 {
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: #1a1a2e;
        }

        /* --- Selector d'informe --- */
        .report-selector {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            align-items: flex-end;
        }

        .report-group {
            display: flex;
            flex-direction: column;
        }

        .report-group label {
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 5px;
            color: #555;
        }

        .report-group input,
        .report-group select {
            padding: 8px 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 0.9rem;
        }

        .btn {
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
            font-size: 0.9rem;
            cursor: pointer;
            transition: background-color 0.2s;
        }

        .btn-primary {
            background-color: #4361ee;
            color: white;
        }

        .btn-primary:hover {
            background-color: #3a56d4;
        }

        .btn-secondary {
            background-color: #e0e0e0;
            color: #333;
        }

        .btn-secondary:hover {
            background-color: #d0d0d0;
        }

        .btn-success {
            background-color: #2a9d8f;
            color: white;
        }

        .btn-success:hover {
            background-color: #21867a;
        }

        /* --- Resum de
