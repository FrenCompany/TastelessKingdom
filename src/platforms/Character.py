from typing import Union

import pygame

from settings.Game import CHAR_GRAVITY, CHAR_SPEED, CHAR_JUMPSPEED, CHAR_JUMPTRIES
from src.platforms.Cannon import Bullet
from src.platforms.Collectible import Collectible
from src.platforms.Sound import play_jump
from src.platforms.Animation import AnimatedCharacter, AnimatedItem
from src.platforms.Group import CustomGroup


class Character(pygame.sprite.Sprite):
    LEFT = 0
    RIGHT = 1

    def __init__(self, player, char: str, x=0, y=0, g=CHAR_GRAVITY, jumpspeed=CHAR_JUMPSPEED):
        super().__init__()
        self.player = player

        # imagen a mostrar cada vez que se llama draw()
        self.direction = self.LEFT
        self.sprite = AnimatedCharacter(char)

        # animaciones causadas por el personaje
        self.animations = CustomGroup()

        # posición
        self.rect = self.sprite.get_image().get_rect().move(x, y)
        self.old_rect = self.rect.copy()

        # saltos y gravedad
        self.g = g
        self.jumpspeed = jumpspeed
        self.vy = 0

        self.jumptries = 0
        self.maxjumptries = CHAR_JUMPTRIES
        self.standing = False
        self.falling = False

    # ---------------- movimiento ---------------

    def move_to(self, x=0, y=0):
        self.rect.topleft = (x, y)
        return

    def move(self, dx=0, dy=0):
        self.rect.move_ip(dx, dy)
        return

    def move_right(self):
        self.move(dx=CHAR_SPEED)
        self.direction = self.RIGHT
        return

    def move_left(self):
        self.move(dx=-CHAR_SPEED)
        self.direction = self.LEFT
        return

    def jump(self):
        self.jumptries = self.maxjumptries
        return

    def fall(self):
        self.falling = True
        return

    def update(self):
        if self.standing and self.jumptries > 0:
            self.vy = -self.jumpspeed
            self.standing = False
            self.jumptries = 0
            play_jump()

        self.jumptries = max(self.jumptries - 1, 0)
        self.vy += self.g
        self.rect.y += self.vy
        self.standing = False
        return

    # ---------------- dibujar ---------------

    def draw(self, screen):
        self.animations.draw(screen)

        image = self.sprite.get_image(moving=self.old_rect != self.rect, jumping=not self.standing)
        if self.direction == self.LEFT:
            image = pygame.transform.flip(image, True, False)

        screen.blit(image, self.rect)

        self.old_rect = self.rect.copy()
        self.falling = False
        return

    # ---------------- colisiones ---------------

    def detect_collisions(self, group, dokill=False):
        collisions = pygame.sprite.spritecollide(self, group, dokill=dokill)

        for sprite in collisions:
            self.collide(sprite)
        return

    def collide(self, sprite):
        dx = self.rect.x - self.old_rect.x
        dy = self.rect.y - self.old_rect.y

        if dx > 0:  # choque hacia la derecha
            sprite.collide_left(self)

        elif dx < 0:  # choque hacia la izquierda
            sprite.collide_right(self)

        if dy > 0:  # choque hacia abajo
            if sprite.collide_top(self):
                self.vy = 0
                self.standing = True

        elif dy < 0:  # choque hacia arriba
            if sprite.collide_bottom(self):
                self.vy = 0

        return

    # choque con el lado izquierdo
    def collide_left(self, moving_sprite):
        if moving_sprite.old_rect.right <= self.old_rect.left:
            middle = (moving_sprite.old_rect.right + self.old_rect.left) / 2
            moving_sprite.rect.right = middle
            return True
        return False

    # choque con el lado derecho
    def collide_right(self, moving_sprite):
        if moving_sprite.old_rect.left >= self.old_rect.right:
            middle = (moving_sprite.old_rect.left + self.old_rect.right) / 2
            moving_sprite.rect.left = middle
            return True
        return False

    # choque con el lado superior
    def collide_top(self, moving_sprite):
        if moving_sprite.old_rect.bottom <= self.old_rect.top:
            middle = (moving_sprite.old_rect.bottom + self.old_rect.top) / 2
            moving_sprite.rect.bottom = middle
            return True
        return False

    # choque con el lado inferior
    def collide_bottom(self, moving_sprite):
        if moving_sprite.old_rect.top >= self.old_rect.bottom:
            middle = int((moving_sprite.old_rect.top + self.old_rect.bottom) / 2)
            moving_sprite.rect.top = middle
            return True
        return False

    # ---------------- impactos (balas) ---------------

    def circle_collide(self, sprite: Union[Collectible, Bullet]):
        closest_x = min(self.rect.right, max(self.rect.left, sprite.rect.centerx))
        closest_y = min(self.rect.bottom, max(self.rect.top, sprite.rect.centery))

        dist = (closest_x - sprite.rect.centerx) ** 2 + (closest_y - sprite.rect.centery) ** 2
        return dist <= (sprite.rect.width / 2) ** 2

    def detect_impacts(self, group, dokill=True):
        collisions = pygame.sprite.spritecollide(self, group, dokill=False)

        for sprite in collisions:
            if self.circle_collide(sprite):
                if dokill:
                    sprite.kill()
                self.impact(sprite)
        return

    def impact(self, bullet: Bullet):
        # TODO: ataques en el juego
        return

    # ---------------- recolectables ---------------

    def detect_collectibles(self, group):
        collisions = pygame.sprite.spritecollide(self, group, dokill=False)

        for sprite in collisions:
            if self.circle_collide(sprite):
                self.get_collectible(sprite)
        return

    def get_collectible(self, collectible):
        self.player.add_item_to_storage(collectible.ingredient)

        # TODO: cosas graficas aparte
        collectible.kill()
        self.animations.add(AnimatedItem(collectible, destination=(750, 10)))
        return
