from .Attributes import *


class Multipliers:

    def __init__(self, mult_dict):
        self.mult = mult_dict

    def eat(self, dish):
        hp = 0
        for name, member in Attributes.__members__.items():
            try:
                hp += self.mult[name] * getattr(dish, name)
            except:
                pass
        return hp
