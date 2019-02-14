from abc import ABC, abstractmethod
from typing import Tuple

import pygame

from settings.GUI import DOOR_COLOR
from src.platforms.Door import Door
from src.platforms.Collectible import Collectible
from src.platforms.Text import Text


class Interactable(ABC):

    @abstractmethod
    def primary_action(self, player):
        pass

    @abstractmethod
    def secondary_action(self, player):
        pass


class Backdoor(Door, Interactable, pygame.sprite.Sprite):

    def __init__(self, driver, width, height, x, y, color=DOOR_COLOR,
                 next_room: str = '', entering_pos: Tuple[int, int] = (0, 0)):
        Door.__init__(self, driver, next_room, entering_pos)
        pygame.sprite.Sprite.__init__(self)

        # imagen
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # posición
        self.rect = self.image.get_rect().move(x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        return

    def primary_action(self, player):
        self.enter_room(player)
        return

    def secondary_action(self, player):
        return


class InventoryItem(Collectible, Interactable):

    def __init__(self, x, y, ingredient, player):
        super().__init__(x, y, ingredient.name)
        self.ingredient = ingredient
        self.player = player

    def draw(self, screen):
        super().draw(screen)

        inv_amount = self.player.inventory.get_item(self.ingredient)
        strg_amount = self.player.storage.get_item(self.ingredient)

        pos = self.rect.move(self.rect.width / 2, -10)
        text = f'{inv_amount} / {inv_amount + strg_amount}'

        Text(text, x=pos[0], y=pos[1], size=15, center=True).draw(screen)
        return

    def primary_action(self, player):
        if self.player.inventory.has_space():
            if self.player.storage.substract_item(self.ingredient):
                self.player.inventory.add_item(self.ingredient)
        return

    def secondary_action(self, player):
        if self.player.inventory.substract_item(self.ingredient):
            self.player.storage.add_item(self.ingredient)
        return
