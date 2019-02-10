from typing import List
from src.model.battle.Citizen import Citizen
from src.model.battle.Chef import Chef
from src.model.battle.BattleState.ChefTurn import ChefTurn
from src.model.battle.BattleState.BattleEnded import BattleEnded
from src.model.battle.Recipe import Recipe
from src.GUI.BattleGUI import BattleGUI


class BattleDriver:
    def __init__(self, player, citizens: List[Citizen]):
        # TODO: implement player class
        self.chef = Chef(player)
        self.citizens = citizens
        self.state = ChefTurn(self)
        self.gui = BattleGUI(self)

    def set_state(self, state):
        self.state = state

    def recipe_chosen(self, recipe: Recipe):
        if self.chef.can_cook(recipe):
            dish = self.chef.cook(recipe)
            for citizen in self.citizens:
                citizen.eat(dish)
            self.state.end_turn()

    def check_battle_status(self):
        battle_ended = True
        for citizen in self.citizens:
            if not citizen.is_saved() and citizen.is_alive():
                battle_ended = False

        if battle_ended:
            self.set_state(BattleEnded(self))
        # TODO: Notify
        else:
            if self.chef.is_defeated():
                self.set_state(BattleEnded(self))

    def battle_ended(self):
        return self.state.battle_ended()

    def tick_citizens(self):
        for citizen in self.citizens:
            citizen.tick()

    def get_recipe(self, index):
        return self.chef.deck[index]

    def deck_size(self):
        return len(self.chef.deck)

    def action_right(self):
        self.gui.action_right()

    def action_left(self):
        self.gui.action_left()

    def action_up(self):
        self.gui.action_up()

    def action_down(self):
        self.gui.action_down()

    def action_select(self):
        self.gui.action_select()