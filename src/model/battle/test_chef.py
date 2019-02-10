from unittest import TestCase
from src.model.battle.Chef import Chef
from src.model.battle.Recipe import Recipe
from src.model.battle.Attributes import Attributes
from src.model.overworld.OverworldPlayer import OverworldPlayer


class TestChef(TestCase):
    def test_lower_morale(self):
        player = OverworldPlayer(None)
        player.set_max_morale(5)
        chef = Chef(player)
        self.assertEqual(5, chef.current_morale)
        chef.lower_morale(2)
        self.assertEqual(3, chef.current_morale)
        chef.lower_morale(3)
        self.assertEqual(0, chef.current_morale)

    def test_is_defeated(self):
        player = OverworldPlayer(None)
        player.set_max_morale(5)
        chef = Chef(player)
        self.assertFalse(chef.is_defeated())
        chef.lower_morale(2)
        self.assertFalse(chef.is_defeated())
        chef.lower_morale(3)
        self.assertTrue(chef.is_defeated())

    def test_cook(self):
        recipe = Recipe({0: 2, 1: 1, 2: 1}, {Attributes.ITALIAN.value: 2}, list())
        player_inventory = {0: 3, 1: 3, 2: 3}
        player = OverworldPlayer(None)
        player.add_recipe(recipe)
        player.set_inventory(player_inventory)
        chef = Chef(player)
        dish = chef.cook(recipe)
        self.assertEqual(1, chef.inventory.get_amount(0))
        self.assertEqual(2, chef.inventory.get_amount(1))
        self.assertEqual(2, chef.inventory.get_amount(2))
        self.assertEqual({Attributes.ITALIAN.value: 2}, dish.attributes)
