

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
