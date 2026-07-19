# GitHub Workflow

## Objectiu

Aquest document defineix el flux oficial de treball amb Git i GitHub dins del projecte IA-Productiva.

L'objectiu és mantenir un historial net, facilitar el seguiment dels canvis i evitar conflictes innecessaris.

---

# Principis

El repositori ha de complir sempre aquests criteris:

- historial llegible
- commits petits
- canvis documentats
- repositori estable
- sincronització freqüent

---

# Flux de treball

## 1. Actualitzar el repositori

Abans de començar una sessió:

```bash
git pull
```

---

## 2. Desenvolupar

Fer els canvis necessaris.

Evitar modificar fitxers que no estiguin relacionats amb la tasca.

---

## 3. Revisar

Comprovar els canvis.

```bash
git status
```

Si és necessari:

```bash
git diff
```

---

## 4. Afegir fitxers

```bash
git add .
```

O afegir únicament els fitxers modificats.

---

## 5. Crear el commit

Cada commit ha de representar una unitat de treball coherent.

Exemple:

```bash
git commit -m "Complete core documentation"
```

---

## 6. Publicar

```bash
git push
```

---

# Missatges dels commits

Han de ser:

- curts
- descriptius
- fàcils d'entendre

Exemples:

```
Complete documentation

Add project templates

Improve prompts

Fix repository structure

Update operating workflow
```

Evitar:

```
Changes

Update

Fix

Final

Test
```

---

# Bones pràctiques

Fer commits:

- després d'un bloc de feina
- abans d'un canvi important
- abans d'una refactorització

No esperar al final del dia per fer un únic commit enorme.

---

# Sincronització

Fer un `push` sempre que es completi una funcionalitat o un conjunt coherent de fitxers.

No acumular molts commits locals.

---

# Historial

L'historial ha de permetre entendre:

- què s'ha fet
- quan
- per què

sense necessitat de llegir el codi.

---

# Branques

Per defecte es treballa sobre:

```
main
```

Quan el projecte creixi es poden crear branques específiques per:

- noves funcionalitats
- experiments
- refactoritzacions

---

# Fitxers especials

Actualitzar quan sigui necessari:

- CHANGELOG.md
- ROADMAP.md
- TODO.md
- SESSION.md

---

# Revisió abans del Push

Verificar:

- no hi ha fitxers temporals
- no hi ha fitxers duplicats
- la documentació està actualitzada
- el projecte continua compilant (si aplica)

---

# Flux resumit

```text
Modificar fitxers

↓

git status

↓

git add .

↓

git commit

↓

git push
```

---

# Objectiu final

Mantenir un repositori ordenat, amb un historial clar i fàcil de seguir tant per persones com per qualsevol IA que participi en el desenvolupament del projecte.
