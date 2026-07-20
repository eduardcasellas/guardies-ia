#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Mòdul per enviar notificacions d'incidències per correu electrònic o Telegram.

Segueix l'especificació del projecte IA-Productiva.
Dependències:
    - content/templates/incident-template.md
    - data/incidents/
    - data/providers/
"""

import json
import os
import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from typing import Optional, List
from datetime import datetime


# --- Constants ---

# Directori de configuració
CONFIG_DIR = Path("config")

# Fitxer de configuració de notificacions
NOTIFICATIONS_CONFIG_FILE = CONFIG_DIR / "notifications.json"

# Fitxer de configuració de correu
EMAIL_CONFIG_FILE = CONFIG_DIR / "email.json"

# Fitxer de configuració de Telegram
TELEGRAM_CONFIG_FILE = CONFIG_DIR / "telegram.json"

# Directori de les incidències
INCIDENTS_DIR = Path("data") / "incidents"


class NotificationError(Exception):
    """Excepció base per a errors de notificació."""
    pass


class EmailNotifier:
    """Gestiona l'enviament de notificacions per correu electrònic."""

    def __init__(self, config_file: Path = EMAIL_CONFIG_FILE):
        """
        Inicialitza el notificador de correu.

        Args:
            config_file: Fitxer de configuració del correu.
        """
        self.config = self._load_config(config_file)

    def _load_config(self, config_file: Path) -> dict:
        """
        Carrega la configuració del correu.

        Args:
            config_file: Fitxer de configuració.

        Returns:
            Diccionari amb la configuració.

        Raises:
            NotificationError: Si el fitxer no existeix o no és vàlid.
        """
        if not config_file.exists():
            raise NotificationError(
                f"Fitxer de configuració no trobat: {config_file}. "
                f"Crea'l amb el format: {{'smtp_server': '...', 'smtp_port': 587, 'username': '...', 'password': '...', 'from_address': '...'}}"
            )

        try:
            with open(config_file, "r", encoding="utf-8") as f:
                config = json.load(f)
        except Exception as e:
            raise NotificationError(f"Error en llegir la configuració: {e}")

        required_fields = ["smtp_server", "smtp_port", "username", "password", "from_address"]
        for field in required_fields:
            if field not in config:
                raise NotificationError(f"Camp obligatori faltant a la configuració: {field}")

        return config

    def send_notification(
        self,
        to_address: str,
        subject: str,
        body: str,
        html_body: Optional[str] = None,
    ) -> bool:
        """
        Envia una notificació per correu electrònic.

        Args:
            to_address: Adreça de correu del destinatari.
            subject: Assumpte del correu.
            body: Cos del correu en text pla.
            html_body: Cos del correu en HTML (opcional).

        Returns:
            True si s'ha enviat correctament.

        Raises:
            NotificationError: Si hi ha un error en l'enviament.
        """
        try:
            msg = MIMEMultipart("alternative")
            msg["From"] = self.config["from_address"]
            msg["To"] = to_address
            msg["Subject"] = subject

            # Afegir el cos en text pla
            msg.attach(MIMEText(body, "plain", "utf-8"))

            # Afegir el cos en HTML si es proporciona
            if html_body:
                msg.attach(MIMEText(html_body, "html", "utf-8"))

            # Connectar al servidor SMTP i enviar
            with smtplib.SMTP(self.config["smtp_server"], self.config["smtp_port"]) as server:
                server.starttls()
                server.login(self.config["username"], self.config["password"])
                server.send_message(msg)

            return True

        except Exception as e:
            raise NotificationError(f"Error en enviar el correu: {e}")

    def send_incident_notification(
        self,
        to_address: str,
        incident: dict,
        notification_type: str = "nova",
    ) -> bool:
        """
        Envia una notificació sobre una incidència.

        Args:
            to_address: Adreça de correu del destinatari.
            incident: Diccionari amb les dades de la incidència.
            notification_type: Tipus de notificació (nova, actualitzada, resolta, tancada).

        Returns:
            True si s'ha enviat correctament.
        """
        incident_id = incident.get("ID", "Desconegut")
        titol = incident.get("Títol", "Sense títol")
        prioritat = incident.get("Prioritat", "?")
        estat = incident.get("Estat", "?")
        ubicacio = incident.get("Ubicació", "?")
        descripcio = incident.get("Descripció", "")

        if notification_type == "nova":
            subject = f"[IA-Productiva] Nova incidència: {incident_id} - {titol}"
            body = f"""S'ha creat una nova incidència.

ID: {incident_id}
Títol: {titol}
Prioritat: {prioritat}
Estat: {estat}
Ubicació: {ubicacio}

Descripció:
{descripcio}

--- 
IA-Productiva - Sistema de Notificacions
"""
        elif notification_type == "resolta":
            subject = f"[IA-Productiva] Incidència resolta: {incident_id} - {titol}"
            body = f"""La incidència ha estat resolta.

ID: {incident_id}
Títol: {titol}
Prioritat: {prioritat}
Estat: {estat}
Ubicació: {ubicacio}

--- 
IA-Productiva - Sistema de Notificacions
"""
        else:
            subject = f"[IA-Productiva] Incidència actualitzada: {incident_id} - {titol}"
            body = f"""La incidència ha estat actualitzada.

ID: {incident_id}
Títol: {titol}
Prioritat: {prioritat}
Estat: {estat}
Ubicació: {ubicacio}

--- 
IA-Productiva - Sistema de Notificacions
"""

        return self.send_notification(to_address, subject, body)


class TelegramNotifier:
    """Gestiona l'enviament de notificacions per Telegram."""

    def __init__(self, config_file: Path = TELEGRAM_CONFIG_FILE):
        """
        Inicialitza el notificador de Telegram.

        Args:
            config_file: Fitxer de configuració de Telegram.
        """
        self.config = self._load_config(config_file)

    def _load_config(self, config_file: Path) -> dict:
        """
        Carrega la configuració de Telegram.

        Args:
            config_file: Fitxer de configuració.

        Returns:
            Diccionari amb la configuració.

        Raises:
            NotificationError: Si el fitxer no existeix o no és vàlid.
        """
        if not config_file.exists():
            raise NotificationError(
                f"Fitxer de configuració no trobat: {config_file}. "
                f"Crea'l amb el format: {{'bot_token': '...', 'chat_id': '...'}}"
            )

        try:
            with open(config_file, "r", encoding="utf-8") as f:
                config = json.load(f)
        except Exception as e:
            raise NotificationError(f"Error en llegir la configuració: {e}")

        required_fields = ["bot_token", "chat_id"]
        for field in required_fields:
            if field not in config:
                raise NotificationError(f"Camp obligatori faltant a la configuració: {field}")

        return config

    def send_notification(self, message: str) -> bool:
        """
        Envia una notificació per Telegram.

        Args:
            message: Missatge a enviar.

        Returns:
            True si s'ha enviat correctament.

        Raises:
            NotificationError: Si hi ha un error en l'enviament.
        """
        try:
            url = f"https://api.telegram.org/bot{self.config['bot_token']}/sendMessage"
            payload = {
                "chat_id": self.config["chat_id"],
                "text": message,
                "parse_mode": "HTML",
            }
            response = requests.post(url, json=payload, timeout=10)

            if response.status_code != 200:
                raise NotificationError(
                    f"Error en enviar el missatge: {response.status_code} - {response.text}"
                )

            return True

        except requests.exceptions.RequestException as e:
            raise NotificationError(f"Error de connexió amb Telegram: {e}")

    def send_incident_notification(
        self,
        incident: dict,
        notification_type: str = "nova",
    ) -> bool:
        """
        Envia una notificació sobre una incidència per Telegram.

        Args:
            incident: Diccionari amb les dades de la incidència.
            notification_type: Tipus de notificació (nova, actualitzada, resolta, tancada).

        Returns:
            True si s'ha enviat correctament.
        """
        incident_id = incident.get("ID", "Desconegut")
        titol = incident.get("Títol", "Sense títol")
        prioritat = incident.get("Prioritat", "?")
        estat = incident.get("Estat", "?")
        ubicacio = incident.get("Ubicació", "?")
        descripcio = incident.get("Descripció", "")

        # Truncar la descripció si és massa llarga
        if len(descripcio) > 200:
            descripcio = descripcio[:200] + "..."

        emoji_prioritat = {1: "🔴", 2: "🟠", 3: "🟡", 4: "🔵", 5: "🟢"}
        emoji_estat = {"oberta": "🆕", "en curs": "🔄", "resolta": "✅", "tancada": "🔒"}
        emoji_tipus = {"nova": "🆕", "actualitzada": "🔄", "resolta": "✅", "tancada": "🔒"}

        prioritat_emoji = emoji_prioritat.get(prioritat, "⚪")
        estat_emoji = emoji_estat.get(estat, "❓")
        tipus_emoji = emoji_tipus.get(notification_type, "📝")

        message = f"""{tipus_emoji} <b>Incidència {notification_type.upper()}</b>

<b>ID:</b> {incident_id}
<b>Títol:</b> {titol}
<b>Prioritat:</b> {prioritat_emoji} {prioritat}
<b>Estat:</b> {estat_emoji} {estat}
<b>Ubicació:</b> {ubicacio}

<b>Descripció:</b>
{descripcio}

---
IA-Productiva · Sistema de Notificacions"""

        return self.send_notification(message)


class NotificationManager:
    """Gestiona l'enviament de notificacions per múltiples canals."""

    def __init__(self, config_file: Path = NOTIFICATIONS_CONFIG_FILE):
        """
        Inicialitza el gestor de notificacions.

        Args:
            config_file: Fitxer de configuració de notificacions.
        """
        self.config = self._load_config(config_file)
        self.email_notifier = None
        self.telegram_notifier = None

        # Inicialitzar els notificadors segons la configuració
        if self.config.get("email", {}).get("enabled", False):
            try:
                self.email_notifier = EmailNotifier()
            except NotificationError as e:
                print(f"Avís: No es pot inicialitzar el notificador de correu: {e}")

        if self.config.get("telegram", {}).get("enabled", False):
            try:
                self.telegram_notifier = TelegramNotifier()
            except NotificationError as e:
                print(f"Avís: No es pot inicialitzar el notificador de Telegram: {e}")

    def _load_config(self, config_file: Path) -> dict:
        """
        Carrega la configuració de notificacions.

        Args:
            config_file: Fitxer de configuració.

        Returns:
            Diccionari amb la configuració.
        """
        default_config = {
            "email": {
                "enabled": False,
                "recipients": []
            },
            "telegram": {
                "enabled": False
            },
            "notify_on": {
                "nova": True,
                "actualitzada": True,
                "resolta": True,
                "tancada": False
            }
        }

        if not config_file.exists():
            # Crear el fitxer de configuració per defecte
            config_file.parent.mkdir(parents=True, exist_ok=True)
            with open(config_file, "w", encoding="utf-8") as f:
                json.dump(default_config, f, indent=2, ensure_ascii=False)
            return default_config

        try:
            with open(config_file, "r", encoding="utf-8") as f:
                config = json.load(f)
            # Fusionar amb la configuració per defecte
            for key in default_config:
                if key not in config:
                    config[key] = default_config[key]
            return config
        except Exception:
            return default_config

    def _load_incident(self, incident_id: str) -> dict:
        """
        Carrega una incidència des del fitxer JSON.

        Args:
            incident_id: Identificador de la incidència.

        Returns:
            Diccionari amb les dades de la incidència.

        Raises:
            NotificationError: Si el fitxer no existeix.
        """
        incident_file = INCIDENTS_DIR / f"{incident_id}.json"

        if not incident_file.exists():
            # Provar amb extensió .yaml
            incident_file = INCIDENTS_DIR / f"{incident_id}.yaml"
            if not incident_file.exists():
                raise NotificationError(f"Incidència no trobada: {incident_id}")

        try:
            with open(incident_file, "r", encoding="utf-8") as f:
                if incident_file.suffix == ".json":
                    return json.load(f)
                else:
                    import yaml
                    return yaml.safe_load(f)
        except Exception as e:
            raise NotificationError(f"Error en llegir la incidència: {e}")

    def notify(
        self,
        incident_id: str,
        notification_type: str = "nova",
    ) -> dict:
        """
        Envia notificacions per tots els canals configurats.

        Args:
            incident_id: Identificador de la incidència.
            notification_type: Tipus de notificació (nova, actualitzada, resolta, tancada).

        Returns:
            Diccionari amb els resultats de l'enviament.
        """
        results = {"email": False, "telegram": False}

        # Comprovar si s'ha de notificar per a aquest tipus
        if not self.config.get("notify_on", {}).get(notification_type, True):
            return results

        try:
            incident = self._load_incident(incident_id)
        except NotificationError as e:
            print(f"Error: {e}")
            return results

        # Enviar per correu
        if self.email_notifier and self.config.get("email", {}).get("recipients"):
            for recipient in self.config["email"]["recipients"]:
                try:
                    self.email_notifier.send_incident_notification(
                        recipient, incident, notification_type
                    )
                    results["email"] = True
                except NotificationError as e:
                    print(f"Error en enviar correu a {recipient}: {e}")

        # Enviar per Telegram
        if self.telegram_notifier:
            try:
                self.telegram_notifier.send_incident_notification(
                    incident, notification_type
                )
                results["telegram"] = True
            except NotificationError as e:
                print(f"Error en enviar Telegram: {e}")

        return results


# --- Exemple d'ús ---
if __name__ == "__main__":
    # Exemple: enviar notificació per a una incidència
    manager = NotificationManager()

    # Provar d'enviar una notificació
    try:
        result = manager.notify("INC-20260716-0001", "nova")
        print(f"Resultat de la notificació: {result}")
    except Exception as e:
        print(f"Error: {e}")