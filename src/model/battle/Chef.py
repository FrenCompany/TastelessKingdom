# Player
from .Inventory import *


class Chef:
    def __init__(self, player_deck, player_inventory, player_specialty, player_modifier, player_defense,
                 cooldown,
                 max_morale):
        self.deck = player_deck
        self.inventory = Inventory(player_inventory)
        self.specialty = player_specialty
        self.modifier = player_modifier
        self.defense = player_defense
        self.cooldown = cooldown
        self.max_morale = max_morale
        self.current_morale = max_morale

    def cook(self, recipe):
        for ing in recipe.ingredient_list:
            self.inventory.use_item(ing)

    def lower_morale(self, value):
        self.current_morale -= value
