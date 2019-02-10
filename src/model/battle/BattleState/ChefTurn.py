from ..BattleDriver import BattleDriver
from .BattleState import BattleState
from .CitizenTurn import CitizenTurn

class ChefTurn(BattleState):
    def __init__(self, driver: BattleDriver):
        super(ChefTurn, self).__init__(driver)

    def end_turn(self):
        self.driver.set_state(CitizenTurn(self.driver))
