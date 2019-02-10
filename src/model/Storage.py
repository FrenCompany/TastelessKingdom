from typing import Dict
from src.model.Ingredients import Ingredients


class Storage:

    def __init__(self):
        self.items: Dict[Ingredients, int] = dict()

    def add_item(self, ingredient):
        # agregar llave cuando no existía antes
        if not self.has_item(ingredient):
            self.items[ingredient] = 0

        self.items[ingredient] += 1
        return True

    def substract_item(self, ingredient):
        if self.has_item(ingredient) and self.items[ingredient] > 0:
            self.items[ingredient] -= 1

            return True

        return False

    def has_item(self, ingredient):
        return ingredient in self.items

    def get_item(self, ingredient):
        if self.has_item(ingredient):
            return self.items[ingredient]
        return 0
