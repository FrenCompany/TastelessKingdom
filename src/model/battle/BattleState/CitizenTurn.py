from src.model.battle.BattleState.BattleState import BattleState
from src.model.battle.BattleDriver import BattleDriver

class CitizenTurn(BattleState):
    def __init__(self, driver: BattleDriver):
        super(CitizenTurn, self).__init__(driver)

    def end_turn(self):
        self.driver.set_state(CitizenTurn(self.driver))
