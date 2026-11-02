class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight}kg)"


class Weapon(Item):
    def __init__(self, name, weight, damage):
        super().__init__(name, weight)
        self.damage = damage

    def attack(self):
        return f"You strike for {self.damage} damage!"


class Armor(Item):
    def __init__(self, name, weight, protection):
        super().__init__(name, weight)
        self.protection = protection

    def defend(self):
        return f"You take {self.protection} less damage!"


class Potion(Item):
    def __init__(self, name, weight, heal_amount):
        super().__init__(name, weight)
        self.heal_amount = heal_amount

    def consume(self):
        return f"Healed for {self.heal_amount} HP!"
