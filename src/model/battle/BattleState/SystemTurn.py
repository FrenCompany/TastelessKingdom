from src.model.battle.BattleState.BattleState import BattleState
from src.model.battle.BattleState.ChefTurn import ChefTurn


class SystemTurn(BattleState):
    def __init__(self, driver):
        super(SystemTurn, self).__init__(driver)
        self.driver.tick_citizens()
        self.driver.check_battle_status()

    def end_turn(self):
        self.driver.set_state(ChefTurn(self.driver))

    def tick_buffs(self):
        for citizen in self.driver.citizens:
            citizen.tick_buffs()
        self.driver.chef.tick_buffs()
