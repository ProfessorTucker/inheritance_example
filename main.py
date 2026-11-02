from item import *
from player import Player


def main():
    player = Player()
    player.add_item(Weapon("Sword", 3, 25))
    player.add_item(Armor("Plate Mail", 15, 10))
    player.add_item(Potion("Health Potion", 1, 50))

    player.display_inventory()

    print("\n--- Using Specialized Methods ---")
    for item in player.inventory:
        if isinstance(item, Weapon):
            print(item.attack())
        elif isinstance(item, Armor):
            print(item.defend())
        elif isinstance(item, Potion):
            print(item.consume())

main()
