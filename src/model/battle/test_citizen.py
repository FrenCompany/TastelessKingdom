from unittest import TestCase
from src.model.battle.Citizen import Citizen
from src.model.battle.Dish import Dish
from src.model.battle.Attributes import Attributes


class TestCitizen(TestCase):
    def setUp(self):
        self.dish1 = Dish(None, {Attributes.ITALIAN.value: 2})
        self.dish2 = Dish(None, {Attributes.SPICY.value: 3})

    def test_simple_eat(self):
        citizen = Citizen(5, 3, 10)
        self.assertEqual(0, citizen.hp)
        citizen.eat(self.dish1)
        self.assertEqual(2, citizen.hp)
        citizen.eat(self.dish1)
        self.assertEqual(4, citizen.hp)

    def test_saved(self):
        citizen = Citizen(5, 2, 10)
        self.assertEqual(0, citizen.hp)
        citizen.eat(self.dish2)
        self.assertEqual(3, citizen.hp)
        self.assertFalse(citizen.is_saved())
        citizen.eat(self.dish2)
        self.assertTrue(citizen.is_saved())

    def test_dead(self):
        citizen = Citizen(10, 2, 10)
        self.assertTrue(citizen.is_alive())
        citizen.tick()
        self.assertTrue(citizen.is_alive())
        citizen.tick()
        self.assertFalse(citizen.is_alive())
