import pygame

from settings.Game import FPS
from src.control.GameState import GameState, InMainMenu, InGame, InStartScreen, Paused
from src.control.Player import Player
from src.platforms.Room import load_room

from src.utils import path


class Driver:
    def __init__(self, screen: pygame.Surface):
        self.player: Player = Player(self)

        self.screen: pygame.Surface = screen

        self.state: GameState = InStartScreen(self)
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.fps: int = FPS

    def tick(self):
        pressed = pygame.key.get_pressed()
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.quit_game()

        self.player.actions(events, pressed)

        self.state.tick(events)

        self.clock.tick(self.fps)
        pygame.display.flip()
        return

    def set_state(self, state):
        self.state = state
        return

    # ----------- acciones -------------

    def press_up(self, player: Player):
        self.state.press_up(player)
        return

    def press_down(self, player: Player):
        self.state.press_down(player)
        return

    def press_left(self, player: Player):
        self.state.press_left(player)
        return

    def press_right(self, player: Player):
        self.state.press_right(player)
        return

    def hold_up(self, player: Player):
        self.state.hold_up(player)
        return

    def hold_down(self, player: Player):
        self.state.hold_down(player)
        return

    def hold_left(self, player: Player):
        self.state.hold_left(player)
        return

    def hold_right(self, player: Player):
        self.state.hold_right(player)
        return

    def press_primary(self, player: Player):
        self.state.press_primary(player)
        return

    def press_secondary(self, player: Player):
        self.state.press_secondary(player)
        return

    def press_start(self, player: Player):
        self.state.press_start(player)
        return

    # ----------- control del juego -------------

    def reset_game(self):
        self.player = []
        self.set_state(InStartScreen(self))
        return

    def main_menu(self):
        self.set_state(InMainMenu(self))
        return

    def start_game(self):
        level = load_room(path('static/maps/room1.json'), self)
        self.set_state(InGame(self, level))
        return

    def pause(self, prev_state):
        self.set_state(Paused(self, prev_state))
        return

    def unpause(self, prev_state):
        self.set_state(prev_state)
        return

    @staticmethod
    def quit_game():
        pygame.quit()
        exit(0)
        return
