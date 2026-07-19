# Release

## Objectiu

Definir el procés oficial de publicació d'una nova versió del projecte.

---

# Preparació

Verificar que:

- no hi ha errors coneguts crítics
- la documentació està actualitzada
- les funcionalitats previstes estan completades

---

# Revisió

Executar la revisió final.

Corregir qualsevol incidència detectada.

---

# Git

Executar:

```bash
git status
git add .
git commit -m "Release x.x.x"
git push
```

---

# Actualitzar documentació

Modificar:

- CHANGELOG.md
- ROADMAP.md (si cal)
- README.md (si aplica)

---

# Etiquetar la versió

Utilitzar etiquetes coherents.

Exemple:

```
v1.0.0
```

---

# Validació

Comprovar que:

- GitHub està actualitzat
- tots els fitxers s'han publicat
- la documentació coincideix amb la versió publicada

---

# Resultat esperat

Versió publicada, documentada i fàcilment identificable.

---

# Documents relacionats

- github-workflow.md
- revisio-final.md