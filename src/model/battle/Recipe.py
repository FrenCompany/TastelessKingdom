from typing import List
from src.model.battle.Buff.Buff import Buff


class Recipe:
    def __init__(self, ingredient_list, attributes, powers: List[Buff] = list()):
        self.ingredient_list = ingredient_list
        self.attributes = attributes
        self.powers = powers
