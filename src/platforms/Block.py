from typing import Tuple

import pygame

from settings.GUI import BLOCK_COLOR, PLATFORM_COLOR, DOOR_COLOR


class Block(pygame.sprite.Sprite):

    def __init__(self, width, height, x, y, color=BLOCK_COLOR):
        super().__init__()

        # imagen a mostrar cada vez que se llama draw()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # posición
        self.rect = self.image.get_rect().move(x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        return

    # choque con el lado izquierdo
    def collide_left(self, moving_sprite):
        if moving_sprite.old_rect.right <= self.rect.left:
            moving_sprite.rect.right = self.rect.left
            return True
        return False

    # choque con el lado derecho
    def collide_right(self, moving_sprite):
        if moving_sprite.old_rect.left >= self.rect.right:
            moving_sprite.rect.left = self.rect.right
            return True
        return False

    # choque con el lado superior
    def collide_top(self, moving_sprite):
        if moving_sprite.old_rect.bottom <= self.rect.top:
            moving_sprite.rect.bottom = self.rect.top
            return True
        return False

    # choque con el lado inferior
    def collide_bottom(self, moving_sprite):
        if moving_sprite.old_rect.top >= self.rect.bottom:
            moving_sprite.rect.top = self.rect.bottom
            return True
        return False

    def detect_impacts(self, group, dokill=True):
        pygame.sprite.spritecollide(self, group, dokill=dokill)
        return


class Platform(Block):

    def __init__(self, width, height, x, y, color=PLATFORM_COLOR):
        super().__init__(width, height, x, y, color)

    def collide_left(self, moving_sprite):
        return False

    def collide_right(self, moving_sprite):
        return False

    def collide_bottom(self, moving_sprite):
        return False

    def collide_top(self, moving_sprite):
        if moving_sprite.falling:
            return False
        return Block.collide_top(self, moving_sprite)


class Door(Block):

    def __init__(self, driver, width, height, x, y, color=DOOR_COLOR,
                 next_level: str = '', entering_pos: Tuple[int, int] = (0, 0)):
        super().__init__(width, height, x, y, color)

        self.driver = driver
        self.next_level = next_level
        self.entering_pos = entering_pos

    def enter_room(self, player):
        from src.platforms.Level import load_level
        self.driver.state.level = load_level(f'static/maps/{self.next_level}.json', self.driver)
        player.char.move_to(*self.entering_pos)
        return

    def collide_left(self, moving_sprite):
        self.enter_room(self.driver.player)
        return

    def collide_right(self, moving_sprite):
        self.enter_room(self.driver.player)
        return

    def collide_bottom(self, moving_sprite):
        self.enter_room(self.driver.player)
        return

    def collide_top(self, moving_sprite):
        self.enter_room(self.driver.player)
        return
