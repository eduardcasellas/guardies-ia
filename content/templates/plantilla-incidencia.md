# Plantilla d'Incidència

## Camps obligatoris

- **ID**: [generat automàticament]
- **Data i hora**: [YYYY-MM-DD HH:MM]
- **Tipus d'incidència**: [maquinari / programari / xarxa / usuari / proveïdor / altre]
- **Proveïdor afectat**: [nom del proveïdor]
- **Telèfon de contacte**: [número de telèfon]
- **Descripció breu**: [resum de l'incidència]

## Camps opcionals

- **Nivell de gravetat**: [baix / mitjà / alt / crític]
- **Imatges**: [URL o ruta de les fotos]
- **Explicació detallada**: [text lliure]
- **Accions realitzades**: [passos fets per resoldre]
- **Estat**: [obert / en progrés / resolt / tancat]
- **Temps de resolució**: [minuts o hores]
- **Comentaris**: [notes addicionals]

## Exemple d'ús

```yaml
ID: INC-001
Data i hora: 2026-07-19 14:30
Tipus d'incidència: xarxa
Proveïdor afectat: FibraTel
Telèfon de contacte: 900 123 456
Descripció breu: Caiguda de la connexió a internet
Nivell de gravetat: alt
Imatges: /assets/incidents/inc-001_01.jpg
Explicació detallada: El router principal ha deixat de funcionar després d'un tall de llum.
Accions realitzades: Reinici del router, verificació de cables.
Estat: en progrés
Temps de resolució: 45 min
Comentaris: Contactar amb el proveïdor si no es resol en 1 hora.