# Decision Log

## Objectiu

Aquest document registra les decisions importants preses durant l'evolució del projecte.

El seu propòsit és evitar que es tornin a discutir decisions ja resoltes i facilitar la comprensió del perquè de l'arquitectura actual.

---

# Quan registrar una decisió

Registrar només decisions que afectin el projecte de forma significativa.

Per exemple:

- arquitectura
- estructura del repositori
- convencions
- metodologia
- eines principals
- processos
- automatitzacions

No registrar tasques quotidianes.

---

# Format

Cada entrada ha de seguir aquesta estructura.

---

## Data

AAAA-MM-DD

### Títol

Nom curt de la decisió.

### Context

Quin problema existia.

### Opcions considerades

- Opció A
- Opció B
- Opció C

### Decisió

Quina opció s'ha escollit.

### Justificació

Per què s'ha pres aquesta decisió.

### Conseqüències

Quin impacte tindrà.

### Documents relacionats

Llista de documents afectats.

---

# Exemple

## Data

2026-07-16

### Títol

Separació entre prompts i documentació.

### Context

Els prompts començaven a contenir informació estructural del projecte.

### Opcions considerades

- Mantenir-ho tot dins dels prompts.
- Separar documentació i prompts.

### Decisió

Crear una documentació centralitzada i deixar els prompts com a consumidors d'aquesta informació.

### Justificació

Evita duplicats i facilita el manteniment.

### Conseqüències

Els prompts es tornen més petits i reutilitzables.

### Documents relacionats

- architecture.md
- context-loading.md
- conventions.md

---

# Bones pràctiques

Cada decisió ha de ser:

- clara
- justificable
- verificable
- reutilitzable

---

# Què NO registrar

No registrar:

- errors temporals
- proves
- idees
- hipòtesis
- tasques pendents

Aquest tipus d'informació pertany a:

- TODO.md
- SESSION.md

---

# Revisió

Les decisions antigues poden quedar obsoletes.

En aquest cas:

- no eliminar-les
- marcar-les com a substituïdes
- referenciar la nova decisió

---

# Objectiu final

Mantenir un historial clar de les decisions importants perquè qualsevol persona o IA pugui entendre l'evolució del projecte sense haver de deduir-la.