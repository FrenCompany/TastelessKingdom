from src.model.battle.BattleState.BattleState import BattleState
from src.model.battle.BattleDriver import BattleDriver
from src.model.battle.BattleState.SystemTurn import SystemTurn


class CitizenTurn(BattleState):
    def __init__(self, driver: BattleDriver):
        super(CitizenTurn, self).__init__(driver)
        self.react()

    def end_turn(self):
        self.driver.set_state(SystemTurn(self.driver))

    def react(self):
        for citizen in self.driver.citizens:
            citizen.react(self.driver.chef)
        self.end_turn()
