class Player:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def display_inventory(self):
        print("\n=== Inventory ===")
        total_weight = 0
        for item in self.inventory:
            print(f"  {item}")
            total_weight += item.weight
        print(f"\nTotal weight: {total_weight}kg")
