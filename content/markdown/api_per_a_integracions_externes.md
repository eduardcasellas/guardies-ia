# API per a Integracions Externes

## Propòsit
Aquest document defineix una API REST per permetre la integració de sistemes externs amb el projecte IA-Productiva, facilitant la gestió d'incidències, proveïdors, fotos i notes de forma programàtica.

---

# Consideracions generals

- **Base URL**: `http://localhost:8000/api/v1`
- **Format de les respostes**: JSON
- **Autenticació**: Token Bearer (configurable a `config/api.json`)
- **Codificació**: UTF-8
- **Errors**: Respostes amb codis HTTP estàndard i missatges descriptius

---

# Autenticació

Totes les peticions han d'incloure la capçalera:
