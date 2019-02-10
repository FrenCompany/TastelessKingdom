from src.model.battle.Attributes import Attributes


class Multipliers:

    def __init__(self, mult_dict):
        self.mult = mult_dict

    def eat(self, dish):
        hp = 0
        for name, member in Attributes.__members__.items():
            try:
                if member.value in self.mult:
                    hp += self.mult[member.value] * dish.attributes[member.value]
                else:
                    hp += dish.attributes[member.value]
            except:
                pass
        return hp
