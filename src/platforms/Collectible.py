import pygame

from settings.GUI import COLLECTIBLE_SIZE
from src.utils import path


class Collectible(pygame.sprite.Sprite):

    def __init__(self, x, y, size=COLLECTIBLE_SIZE):
        super().__init__()
        self.image = pygame.image.load(path('static/img/FrenCoin.png'))
        self.image = pygame.transform.smoothscale(self.image, size)

        self.rect = self.image.get_rect().move((x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        return

    def move_to(self, x=0, y=0):
        self.rect.topleft = (x, y)
        return

    def move(self, dx=0, dy=0):
        self.rect.move_ip(dx, dy)
        return
