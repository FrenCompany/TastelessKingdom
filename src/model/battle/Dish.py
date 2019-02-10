from typing import List
from .Buff.Buff import Buff
from .Attributes import Attributes
from .Chef import Chef


class Dish:
    def __init__(self, chef: Chef, attributes: Attributes, powers: List[Buff] = list()):
        self.attributes = attributes
        self.powers = powers
        self.chef = chef
