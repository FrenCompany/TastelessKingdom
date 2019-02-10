from unittest import TestCase
import src.model.battle.BattleDriver as BattleDriver
import src.model.overworld.OverworldPlayer as OverworldPlayer
import src.model.battle.BattleState.SystemTurn as SystemTurn
import src.model.battle.BattleState.CitizenTurn as CitizenTurn
import src.model.battle.Citizen as Citizen
from src.control.Driver import Driver
from src.utils import init_screen


class TestBattleDriver(TestCase):
    def setUp(self):
        self.driver = Driver(init_screen())
        self.player = OverworldPlayer.OverworldPlayer(self.driver)
        citizen = Citizen.Citizen(5, 3, 10)
        self.battle_driver = BattleDriver.BattleDriver(self.player, [citizen])

    def test_set_state(self):
        cit_state = CitizenTurn.CitizenTurn(self.battle_driver)
        self.battle_driver.set_state(cit_state)
        self.assertEqual(self.battle_driver.state, cit_state)
        sys_state = SystemTurn.SystemTurn(self.battle_driver)
        self.battle_driver.set_state(sys_state)
        self.assertEqual(self.battle_driver.state, sys_state)
'''
    def test_recipe_chosen(self):
        self.fail()

    def test_check_battle_status(self):
        self.fail()

    def test_battle_ended(self):
        self.fail()

    def test_tick_citizens(self):
        self.fail()

    def test_get_recipe(self):
        self.fail()
'''