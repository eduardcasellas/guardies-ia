# Sistema d'Integració amb Calendari

## Propòsit
Aquest document defineix com es gestiona la integració de les incidències amb un calendari (Google Calendar, Outlook, etc.) dins del projecte IA-Productiva.

---

# Esdeveniments de calendari

Cada incidència pot generar un o més esdeveniments de calendari:

- **Data límit de resolució**: Esdeveniment amb la data de resolució prevista.
- **Recordatori de seguiment**: Esdeveniment per fer seguiment de la incidència.
- **Reunió de revisió**: Esdeveniment per revisar l'estat de la incidència.

---

# Estructura de l'esdeveniment

| Camp | Descripció |
|------|------------|
| `títol` | Títol de l'esdeveniment (inclou ID de la incidència). |
| `descripció` | Descripció de la incidència. |
| `data_inici` | Data i hora d'inici de l'esdeveniment. |
| `data_fi` | Data i hora de fi de l'esdeveniment. |
| `ubicació` | Ubicació de la incidència. |
| `recordatoris` | Llista de recordatoris (minuts abans). |

---

# Operacions Suportades

## Crear esdeveniment

1. Carrega la incidència des del fitxer YAML.
2. Genera un esdeveniment de calendari amb les dades de la incidència.
3. Envia l'esdeveniment al calendari configurat.

## Actualitzar esdeveniment

1. Carrega la incidència des del fitxer YAML.
2. Actualitza l'esdeveniment de calendari corresponent.
3. Envia l'actualització al calendari configurat.

## Eliminar esdeveniment

1. Carrega la incidència des del fitxer YAML.
2. Elimina l'esdeveniment de calendari corresponent.
3. Envia l'eliminació al calendari configurat.

---

# Integració amb Google Calendar

Per integrar amb Google Calendar, cal:

1. Crear un projecte a Google Cloud Console.
2. Habilitar l'API de Google Calendar.
3. Crear unes credencials OAuth 2.0.
4. Configurar el fitxer `config/calendar.json` amb les credencials.

---

# Fitxer de configuració
