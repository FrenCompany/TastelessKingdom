from typing import List
from src.model.battle.Buff.Buff import Buff


class Dish:
    def __init__(self, chef, attributes, powers: List[Buff] = list()):
        self.attributes = attributes
        self.powers = powers
        self.chef = chef
