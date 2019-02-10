from typing import List
from .Citizen import Citizen
from .Chef import Chef
from .BattleState.ChefTurn import ChefTurn
from .Recipe import Recipe


class BattleDriver:
    def __init__(self, player, citizens: List[Citizen]):
        # TODO: implement player class
        self.chef = Chef(player.deck, player.inventory, player.speciality, player.modifier, player.defense,
                         player.max_morale)
        self.citizens = citizens
        self.state = ChefTurn(self)

    def set_state(self, state):
        self.state = state

    def recipe_chosen(self, recipe: Recipe):
        if self.chef.can_cook(recipe):
            dish = self.chef.cook(recipe)
            for citizen in self.citizens:
                citizen.eat(dish)
            self.state.end_turn()

    def get_recipe(self, index):
        return self.chef.deck[index]

    def deck_size(self):
        return len(self.chef.deck)