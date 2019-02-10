from ..Chef import Chef
from .Reaction import Reaction


class LowerMoraleReaction(Reaction):
    def __init__(self, amount: int):
        super(LowerMoraleReaction, self).__init__()
        self.attack = True
        self.amount = amount

    def act(self, chef: Chef):
        if self.attack:
            chef.lower_morale(self.amount)
