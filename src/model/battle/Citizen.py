from src.model.battle.Dish import Dish
from src.model.battle.Buff.Buff import Buff
from typing import List
from Lib.copy import deepcopy
from src.model.battle.Reaction.Reaction import Reaction
from src.model.battle.Multipliers import Multipliers


class Citizen:
    def __init__(self, max_hp, time, lose_hp_every, multipliers=Multipliers({}), reactions: List[Reaction]=list(), buffs: List[Buff]=list()):
        self.max_hp = max_hp
        self.hp = 0
        self.time = time
        self.lose_hp_every = lose_hp_every
        self.multipliers = multipliers
        self.reactions = reactions
        self.buffs = buffs

    def is_saved(self):
        return self.hp >= self.max_hp

    def eat(self, dish: Dish):
        multipliers_copy = deepcopy(self.multipliers)

        # buff multipliers
        for buff in self.buffs:
            buff.buff_multipliers(multipliers_copy)

        # get happiness
        self.hp += multipliers_copy.eat(dish)

        # get buffs
        for buff in dish.powers:
            self.buffs.append(buff)
            buff.set_parent(self)

        reactions_copy = deepcopy(self.reactions)
        # react
        for buff in self.buffs:
            buff.buff_reaction(reactions_copy)

        for reaction in reactions_copy:
            reaction.act(dish.chef)

    def remove_buff(self, buff: Buff):
        self.buffs.remove(buff)
