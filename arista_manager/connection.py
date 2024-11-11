# arista_manager/connection.py

import json
from netmiko import ConnectHandler

class ConnectionManager:
    def __init__(self, inventory_path):
        self.inventory = self._load_inventory(inventory_path)
        self.device_type = self.inventory["device-type"]
        self.username = self.inventory["username"]
        self.password = self.inventory["password"]
        self.core_routers = self.inventory["core-routers"]

    def _load_inventory(self, inventory_path):
        with open(inventory_path, "r") as file:
            return json.load(file)

    def connect(self, hostname):
        ip_address = self.core_routers.get(hostname)
        if not ip_address:
            raise ValueError(f"Router {hostname} not found in inventory.")

        device_params = {
            "device_type": self.device_type,
            "host": ip_address,
            "username": self.username,
            "password": self.password,
            "session_log": "netmiko_session.log"  # Log session for debugging
        }

        # Establish the connection without entering enable mode
        return ConnectHandler(**device_params)

    def disconnect(self, connection):
        connection.disconnect()
