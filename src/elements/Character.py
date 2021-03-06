from typing import Union

import pygame

from settings.GUI import CHAR_SIZE, CHAR_COIN_SIZE
from settings.Game import CHAR_LIFE, CHAR_GRAVITY, CHAR_SPEED, CHAR_JUMPSPEED, CHAR_JUMPTRIES
from src.elements.Cannon import Bullet
from src.elements.Coin import Coin
from src.elements.Sound import play_coin, play_hit, play_jump


class Character(pygame.sprite.Sprite):
    LEFT = 0
    RIGHT = 1

    def __init__(self, img, x=0, y=0, g=CHAR_GRAVITY, jumpspeed=CHAR_JUMPSPEED):
        super().__init__()

        # imagen a mostrar cada vez que se llama draw()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.smoothscale(self.image, (CHAR_SIZE, CHAR_SIZE))
        self.direction = self.LEFT

        # posición
        self.width = CHAR_SIZE
        self.height = CHAR_SIZE
        self.rect = self.image.get_rect().move(x, y)
        self.old_rect = self.rect.copy()

        # vida
        self.max_life = CHAR_LIFE
        self.life = CHAR_LIFE

        self.life_frame = pygame.Surface([CHAR_SIZE, 4])
        self.life_frame.fill((255, 0, 0))
        self.life_bar = pygame.Surface([CHAR_SIZE, 4])
        self.life_bar.fill((0, 255, 0))

        # objetivos
        self.objectives = set()

        # saltos y gravedad
        self.g = g
        self.jumpspeed = jumpspeed
        self.vy = 0

        self.jumptries = 0
        self.maxjumptries = CHAR_JUMPTRIES
        self.standing = False
        self.falling = False

    # ---------------- movimiento ---------------

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
        image = self.image
        if self.direction == self.RIGHT:
            image = pygame.transform.flip(image, True, False)

        screen.blit(image, self.rect)

        self.draw_life(screen)
        self.draw_objectives(screen)

        self.old_rect = self.rect.copy()
        return

    def draw_life(self, screen):
        screen.blit(self.life_frame, self.rect.move(0, -10))
        current_width = int(self.width * self.life / self.max_life)
        screen.blit(pygame.transform.smoothscale(self.life_bar, (current_width, 4)),
                    self.rect.move(0, -10))
        return

    def draw_objectives(self, screen):
        if len(self.objectives) > 0:
            img = list(self.objectives)[0].image.copy()
            img = pygame.transform.smoothscale(img, (CHAR_COIN_SIZE, CHAR_COIN_SIZE))

            for i in range(len(self.objectives)):
                screen.blit(img, self.rect.move(2, 2 + 12 * i).topright)

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

    def circle_collide(self, sprite: Union[Coin, Bullet]):
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
        bullet.impact(self)
        play_hit()

        if self.life <= 0:
            self.kill()
        return

    # ---------------- objetivos ---------------

    def detect_objectives(self, group):
        collisions = pygame.sprite.spritecollide(self, group, dokill=False)

        for sprite in collisions:
            if self.circle_collide(sprite):
                self.get_objective(sprite)

    def get_objective(self, objective):
        if objective not in self.objectives:
            self.objectives.add(objective)
            play_coin()
        return

    def clear_objectives(self):
        self.objectives.clear()
        return
