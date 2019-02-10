# Player
from src.model.battle.Recipe import Recipe
from src.model.battle.Inventory import *
from src.model.battle.Dish import Dish


class Chef:
    def __init__(self, player_deck, player_inventory, player_specialty, player_modifier, player_defense,
                 max_morale):
        self.deck = player_deck
        self.inventory = Inventory(player_inventory)
        self.specialty = player_specialty
        self.modifier = player_modifier
        self.defense = player_defense
        self.max_morale = max_morale
        self.current_morale = max_morale

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