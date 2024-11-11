# arista_manager/data_fetcher.py
class DataFetcher:
    def __init__(self, connection_manager):
        self.connection_manager = connection_manager

    def fetch_command_output(self, hostname, command):
        connection = self.connection_manager.connect(hostname)
        try:
            output = connection.send_command(command)
            return output
        finally:
            self.connection_manager.disconnect(connection)
