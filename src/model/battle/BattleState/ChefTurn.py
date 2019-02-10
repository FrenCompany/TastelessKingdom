from src.model.battle.BattleDriver import BattleDriver
from src.model.battle.BattleState.BattleState import BattleState
from src.model.battle.BattleState.CitizenTurn import CitizenTurn


class ChefTurn(BattleState):
    def __init__(self, driver: BattleDriver):
        super(ChefTurn, self).__init__(driver)
        self.recipe_index = 0

    def get_recipe(self, index):
        return self.driver.get_recipe(index)

    def next_recipe(self):
        self.recipe_index = (self.recipe_index + 1) % self.driver.deck_size()

    def prev_recipe(self):
        self.recipe_index = (self.recipe_index - 1) % self.driver.deck_size()

    def select(self):
        self.driver.recipe_chosen(self.get_recipe(self.recipe_index))

    def end_turn(self):
        self.driver.set_state(CitizenTurn(self.driver))
