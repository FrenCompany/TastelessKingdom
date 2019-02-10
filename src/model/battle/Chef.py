# Player
from src.model.battle.Recipe import Recipe
from src.model.battle.Inventory import *
from src.model.battle.Dish import Dish


class Chef:
    def __init__(self, player):
        self.deck = player.deck
        self.inventory = Inventory(player.inventory)
        self.specialty = player.specialty
        self.modifier = player.modifier
        self.defense = player.defense
        self.max_morale = player.max_morale
        self.current_morale = player.max_morale

    def cook(self, recipe: Recipe):
        if self.can_cook(recipe):
            for ing in recipe.ingredient_list:
                self.inventory.use_item(ing, recipe.ingredient_list[ing])
            return Dish(self, recipe.attributes, recipe.powers)
        else:
            raise Exception("Not enough ingredients")

    def lower_morale(self, value):
        self.current_morale -= value

    def can_cook(self, recipe: Recipe):
        return self.inventory.can_cook(recipe)

    def tick_buffs(self):
        pass

    def is_defeated(self):
        return self.current_morale <= 0