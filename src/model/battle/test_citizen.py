from unittest import TestCase
from src.model.battle.Citizen import Citizen
from src.model.battle.Dish import Dish
from src.model.battle.Attributes import Attributes


class TestCitizen(TestCase):
    def test_simple_eat(self):
        dish = Dish(None, {Attributes.ITALIAN.value: 2})
        citizen = Citizen(5, 2, 2)
        self.assertEqual(0, citizen.hp)
        citizen.eat(dish)
        self.assertEqual(2, citizen.hp)
        citizen.eat(dish)
        self.assertEqual(4, citizen.hp)


