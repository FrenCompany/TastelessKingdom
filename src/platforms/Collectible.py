import pygame

from settings.GUI import COLLECTIBLE_SIZE
from src.utils import path
from src.model.Ingredients import Ingredients


class Collectible(pygame.sprite.Sprite):

    def __init__(self, x, y, ingredient='TOMATO', size=COLLECTIBLE_SIZE):
        super().__init__()

        self.ingredient = Ingredients[ingredient]

        self.image = pygame.image.load(path(f'static/img/ingredients/{Ingredients.get_img(self.ingredient)}.png'))
        self.image = pygame.transform.scale(self.image, size)

        self.rect = self.image.get_rect().move((x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        return

    def move(self, dx=0, dy=0):
        self.rect.move_ip(dx, dy)
        return
