from abc import ABC, abstractmethod


class BattleState(ABC):
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def end_turn(self):
        pass

    def battle_ended(self):
        return False