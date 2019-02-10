from abc import ABC, abstractmethod
from ..BattleDriver import BattleDriver

class BattleState(ABC):
    def __init__(self, driver: BattleDriver):
        self.driver = driver

    @abstractmethod
    def end_turn(self):
        pass
