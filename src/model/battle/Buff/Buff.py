from abc import ABC, abstractmethod
from ..Citizen import Citizen


class Buff(ABC):
    def __init__(self, cooldown):
        self.cooldown = cooldown
        self.parent: Citizen = None

    def set_parent(self, parent: Citizen):
        self.parent = parent

    def buff_multipliers(self, multipliers):
        return multipliers

    def buff_reaction(self, reaction):
        return reaction

    def tick(self):
        self.cooldown -= 1
        if self.cooldown <= 0:
            self.expire()

    def expire(self):
        self.parent.remove_buff(self)