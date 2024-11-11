# main.py
from arista_manager.manager import AristaRouterManager

if __name__ == "__main__":
    inventory_file = "config/inventory.json"
    manager = AristaRouterManager(inventory_file)

    # Example: Fetching data
    print("Fetching 'show version' output from MTL-CORE-02:")
    print(manager.fetch_data("MTL-CORE-02", "show ip int brief"))
