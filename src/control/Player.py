from pygame.locals import *

from src.elements.Character import Character
from src.utils import path


class Player:
    def __init__(self, driver, img: str = 'Anouk'):
        self.driver = driver
        self.char = Character(path(f'static/img/{img}.png'), x=400, y=300)

    def actions(self, events, pressed):
        # controles presionados
        if pressed[K_UP]:
            self.driver.hold_up(self)
        if pressed[K_DOWN]:
            self.driver.hold_down(self)
        if pressed[K_LEFT]:
            self.driver.hold_left(self)
        if pressed[K_RIGHT]:
            self.driver.hold_right(self)

        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self.driver.press_up(self)
                if event.key == K_DOWN:
                    self.driver.press_down(self)
                if event.key == K_LEFT:
                    self.driver.press_left(self)
                if event.key == K_RIGHT:
                    self.driver.press_right(self)

                if event.key == K_z or event.key == K_RETURN:
                    self.driver.press_primary(self)
                if event.key == K_x:
                    self.driver.press_secondary(self)
                if event.key == K_ESCAPE:
                    self.driver.press_start(self)
        return
