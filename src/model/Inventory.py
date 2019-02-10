from typing import Dict
from src.model.Ingredients import Ingredients


class Inventory:

    def __init__(self, capacity=10):
        self.items: Dict[Ingredients, int] = dict()

        self.used = 0
        self.capacity = capacity

    def has_space(self):
        return self.used < self.capacity

    def add_item(self, item):
        if self.has_space():

            # agregar llave cuando no existía antes
            if not self.has_item(item):
                self.items[item] = 0

            self.items[item] += 1
            self.used += 1
            return True

        return False

    def substract_item(self, item):
        if self.has_item(item):
            self.items[item] -= 1
            self.used -= 1

            # quitar llave cuando no quedan
            if self.items[item] == 0:
                del self.items[item]

            return True

        return False

    def has_item(self, item):
        return item in self.items

    def get_item(self, item):
        if self.has_item(item):
            return self.items[item]
        return 0
