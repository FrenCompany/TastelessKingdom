from typing import List
from .Citizen import Citizen
from .Chef import Chef
from .BattleState.ChefTurn import ChefTurn


class BattleDriver:
    def __init__(self, player, citizens: List[Citizen]):
        # TODO: implement player class
        self.chef = Chef(player.deck, player.inventory, player.speciality, player.modifier, player.defense,
                         player.max_morale)
        self.citizens = citizens
        self.state = ChefTurn(self)

    def set_state(self, state):
        self.state = state

    def recipe_chosen(self, recipe):
        dish = self.chef.cook(recipe)
        for citizen in self.citizens:
            citizen.eat(dish)
