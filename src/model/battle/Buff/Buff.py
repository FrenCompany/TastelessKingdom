from abc import ABC, abstractmethod

class Buff(ABC):
    def __init__(self, cooldown):
        self.cooldown = cooldown

    def buff_multipliers(self, multipliers):
        return multipliers

    def buff_reaction(self, reaction):
        return reaction

    def tick(self):
        self.cooldown -= 1
