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
