# arista_manager/manager.py
from .connection import ConnectionManager
from .data_fetcher import DataFetcher

class AristaRouterManager:
    def __init__(self, inventory_file):
        self.connection_manager = ConnectionManager(inventory_file)
        self.data_fetcher = DataFetcher(self.connection_manager)

    def fetch_data(self, hostname, command):
        return self.data_fetcher.fetch_command_output(hostname, command)
