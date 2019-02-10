from src.model.battle.BattleState.BattleState import BattleState


class BattleEnded(BattleState):
    def __init__(self, driver):
        super(BattleEnded, self).__init__(driver)

    def end_turn(self):
        pass

    def battle_ended(self):
        return True
