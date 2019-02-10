from src.utils import path
import pygame
from settings.GUI import CHAR_SIZE


def load_and_scale(img, size):
    return pygame.transform.scale(pygame.image.load(path(img)), size)


class AnimatedSprite:

    def __init__(self, images, animation_timer=15):
        self.images = images
        self.animation_timer = animation_timer
        self.image_index = 0
        self.frame_counter = 0

    def get_image(self):
        self.frame_counter += 1
        if self.frame_counter == self.animation_timer:
            self.frame_counter = 0
            self.image_index += 1
            self.image_index %= len(self.images)

        return self.images[self.image_index]


class AnimatedCharacter(AnimatedSprite):

    def __init__(self, char: str, animation_timer=15):
        images = [
            load_and_scale(f'static/img/characters/{char} 1.png', CHAR_SIZE),
            load_and_scale(f'static/img/characters/{char} 2.png', CHAR_SIZE),
        ]
        super().__init__(images, animation_timer)

        self.char = char
        self.jump_img = load_and_scale(f'static/img/characters/{char} jump.png', CHAR_SIZE)

    def get_image(self, moving=False, jumping=False):
        if jumping:
            return self.jump_img
        if moving:
            return super().get_image()

        self.frame_counter = 14
        self.image_index = 0
        return self.images[self.image_index]


class AnimatedItem(pygame.sprite.Sprite):

    def __init__(self, item, destination, speed=8):
        super().__init__()
        self.item = item
        self.destination = destination
        self.speed = speed

    def draw(self, screen):
        self.animate()
        self.item.draw(screen)
        return

    def animate(self):
        pos = self.item.rect.topleft

        x_diff = self.destination[0] - pos[0]
        y_diff = self.destination[1] - pos[1]

        dist = (x_diff ** 2 + y_diff ** 2) ** (1 / 2)
        speed = min(self.speed, dist)

        if dist == 0:
            self.kill()
            return

        x_move = speed * x_diff / dist
        y_move = speed * y_diff / dist

        self.item.move(x_move, y_move)
        return
