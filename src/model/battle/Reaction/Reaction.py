from abc import ABC


class Reaction(ABC):
    def __init__(self):
        self.attack = False

    def act(self, chef):
        pass

    def cancelAttack(self):
        self.attack = False
