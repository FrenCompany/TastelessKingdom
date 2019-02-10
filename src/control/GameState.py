from pygame.locals import *

from settings.GUI import TITLE_COLOR, SUBTITLE_COLOR, MENU_BACKGROUND
from src.control.Player import Player
from src.platforms.Level import Level
from src.menu.Menu import Menu
from src.menu.MenuHandler import *
from src.menu.MenuItem import Button, MenuText


class GameState:
    def __init__(self, driver):
        self.driver = driver

    def tick(self, events):
        pass

    def press_up(self, player: Player):
        pass

    def press_down(self, player: Player):
        pass

    def press_left(self, player: Player):
        pass

    def press_right(self, player: Player):
        pass

    def hold_up(self, player: Player):
        pass

    def hold_down(self, player: Player):
        pass

    def hold_left(self, player: Player):
        pass

    def hold_right(self, player: Player):
        pass

    def press_start(self, player: Player):
        pass

    def press_primary(self, player: Player):
        pass

    def press_secondary(self, player: Player):
        pass


class MenuState(GameState):
    def __init__(self, driver, menu: Menu):
        super().__init__(driver)
        self.menu: Menu = menu

    def tick(self, events):
        self.driver.screen.fill(MENU_BACKGROUND)
        self.menu.draw(self.driver.screen)
        return

    def press_up(self, player: Player):
        self.menu.select_previous()
        return

    def press_down(self, player: Player):
        self.menu.select_next()
        return

    def press_left(self, player: Player):
        self.menu.action_left(player)
        return

    def press_right(self, player: Player):
        self.menu.action_right(player)
        return

    def press_primary(self, player: Player):
        self.menu.select(player)
        return

    def press_secondary(self, player: Player):
        self.menu.unselect(player)
        return

    def press_start(self, player: Player):
        self.menu.start(player)
        return


class InStartScreen(MenuState):
    def __init__(self, driver):
        items = [
            MenuText(text="FrenCoins", size=120, color=TITLE_COLOR),
            MenuText(text="Press Z to start", size=40),
        ]
        super().__init__(driver, Menu(driver, items))

    def tick(self, events):
        super().tick(events)

        for event in events:
            if event.type == KEYDOWN and event.key == K_z:
                self.driver.main_menu()

        return


class InMainMenu(MenuState):
    def __init__(self, driver):
        items = [
            MenuText(text="FrenCoins", size=100, color=TITLE_COLOR),
            Button(handler=StartGame(driver), text="Start Game"),
            Button(handler=MainMenuHandler(driver), text="Instructions"),
            Button(handler=QuitGame(driver), text="Exit", color=(170, 0, 0), hover_color=(220, 0, 0)),
        ]
        super().__init__(driver, Menu(driver, items))

    def press_secondary(self, player: Player):
        self.driver.reset_game()
        return


class InGame(GameState):
    def __init__(self, driver, level: Level):
        super().__init__(driver)

        self.level: Level = level
        self.char = self.driver.player.char
        self.char.move_to(380, 200)
        self.char.vy = 0

    def tick(self, events):
        char = self.char
        level = self.level

        # mov automático
        char.update()
        level.update()

        # colisiones
        level.detect_collisions(char)

        # dibujar
        level.draw(self.driver.screen)
        char.draw(self.driver.screen)
        pass

    def press_up(self, player: Player):
        player.char.jump()
        return

    def hold_down(self, player: Player):
        player.char.fall()
        return

    def hold_left(self, player: Player):
        player.char.move_left()
        return

    def hold_right(self, player: Player):
        player.char.move_right()
        return

    def press_start(self, player: Player):
        self.driver.pause(self)
        return

    def press_primary(self, player: Player):
        # TODO entrar en puerta?
        return


class Paused(MenuState):
    def __init__(self, driver, prev_state: InGame):
        items = [
            MenuText("Pause", size=100, color=SUBTITLE_COLOR),
            Button(handler=ContinueGame(driver), text="Continue"),
            Button(handler=StartGame(driver), text="Restart"),
            Button(handler=MainMenuHandler(driver), text="Main menu"),
            Button(handler=QuitGame(driver), text="Exit", color=(170, 0, 0), hover_color=(220, 0, 0)),
        ]
        super().__init__(driver, Menu(driver, items))

        self.prev_state = prev_state

        # oscurecer juego
        self.background = self.driver.screen.copy()
        self.background.fill((0, 0, 0))
        self.background.set_alpha(150)

    def tick(self, events):
        self.prev_state.level.draw(self.driver.screen)
        self.driver.screen.blit(self.background, (0, 0))
        self.menu.draw(self.driver.screen)
        return

    def press_secondary(self, player: Player):
        self.unpause()
        return

    def press_start(self, player: Player):
        self.unpause()
        return

    def unpause(self):
        self.driver.unpause(self.prev_state)
        return
