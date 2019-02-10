from typing import Tuple
from abc import ABC, abstractmethod

from settings.GUI import DOOR_COLOR
from src.platforms.Block import Door


class Interactable(ABC):

    @abstractmethod
    def primary_action(self, player):
        pass

    @abstractmethod
    def secondary_action(self, player):
        pass


class Backdoor(Door, Interactable):

    def __init__(self, driver, width, height, x, y, color=DOOR_COLOR,
                 next_level: str = '', entering_pos: Tuple[int, int] = (0, 0)):
        super().__init__(driver, width, height, x, y, color, next_level, entering_pos)

    def primary_action(self, player):
        self.enter_room(player)
        return

    def secondary_action(self, player):
        return

    def collide_left(self, moving_sprite):
        return False

    def collide_right(self, moving_sprite):
        return False

    def collide_bottom(self, moving_sprite):
        return False

    def collide_top(self, moving_sprite):
        return False
