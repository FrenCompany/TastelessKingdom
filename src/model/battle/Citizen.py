from .Dish import Dish
from .Buff.Buff import Buff
from typing import List
from Lib.copy import deepcopy


class Citizen:
    def __init__(self, time, loose_hp_every, multipliers, reactions, buffs: List[Buff]=list()):
        self.hp = 0
        self.time = time
        self.loose_hp_every = loose_hp_every
        self.multipliers = multipliers
        self.reactions = reactions
        self.buffs = buffs

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
