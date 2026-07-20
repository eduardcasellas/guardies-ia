# Sistema d'Estadístiques i Gràfics

## Propòsit
Aquest document defineix com es generen i visualitzen estadístiques i gràfics de les incidències dins del projecte IA-Productiva.

---

# Tipus d'Estadístiques

## Estadístiques globals
- Total d'incidències registrades
- Distribució per estat (oberta, en curs, resolta, tancada)
- Distribució per prioritat (1-5)
- Distribució per categoria
- Distribució per proveïdor
- Temps mitjà de resolució (en hores)
- Incidències creades per dia (sèrie temporal)

## Tendències
- Evolució setmanal d'incidències creades
- Evolució mensual d'incidències resoltes
- Comparativa entre períodes

---

# Gràfics suportats

## Gràfic de barres
Distribució per estat, prioritat, categoria o proveïdor.

## Gràfic de línies
Evolució temporal d'incidències creades o resoltes.

## Gràfic de sectors (circular)
Distribució percentual per estat o categoria.

## Gràfic de dispersió
Relació entre prioritat i temps de resolució.

---

# Interfície d'usuari

## Secció 1: Selector d'estadístiques
| Component | Tipus | Comportament |
|-----------|-------|--------------|
| Tipus d'estadística | `select` | Valors: `globals`, `tendències`, `per categoria`, `per proveïdor` |
| Període | `select` | Valors: `últim mes`, `últim trimestre`, `últim any`, `personalitzat` |
| Data d'inici | `date input` | Visible si període és `personalitzat` |
| Data de fi | `date input` | Visible si període és `personalitzat` |
| Botó "Actualitzar" | `button` | Refresca les dades i els gràfics |

## Secció 2: Resum de mètriques
Targetes amb valors clau:
- Total incidències
- Obertes
- En curs
- Resoltes
- Temps mitjà de resolució
- Incidències crítiques (prioritat 1)

## Secció 3: Gràfics
Es mostren en una quadrícula de 2 columnes:
- Gràfic de barres (distribució per estat)
- Gràfic de sectors (distribució per prioritat)
- Gràfic de línies (evolució temporal)
- Gràfic de barres (distribució per categoria)

---

# Dependències
- `content/templates/incident-template.md`: definició dels camps de la incidència.
- `data/incidents/`: directori on s'emmagatzemen les incidències.
- Llibreria: `Chart.js` (CDN) per a la generació de gràfics.