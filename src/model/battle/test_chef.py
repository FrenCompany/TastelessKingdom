from unittest import TestCase
from src.model.battle.Chef import Chef


class TestChef(TestCase):
    def test_lower_morale(self):
        chef = Chef(list(), dict(), None, None, None, 5)
        self.assertEqual(5, chef.current_morale)
        chef.lower_morale(2)
        self.assertEqual(3, chef.current_morale)
        chef.lower_morale(3)
        self.assertEqual(0, chef.current_morale)

    def test_is_defeated(self):
        chef = Chef(list(), dict(), None, None, None, 5)
        self.assertFalse(chef.is_defeated())
        chef.lower_morale(2)
        self.assertFalse(chef.is_defeated())
        chef.lower_morale(3)
        self.assertTrue(chef.is_defeated())
