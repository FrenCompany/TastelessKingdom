from src.model.battle.Chef import Chef
from src.model.battle.Reaction.Reaction import Reaction


class LowerMoraleReaction(Reaction):
    def __init__(self, amount: int):
        super(LowerMoraleReaction, self).__init__()
        self.attack = True
        self.amount = amount

    def act(self, chef: Chef):
        if self.attack:
            chef.lower_morale(self.amount)
