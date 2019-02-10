import json
import pygame

from settings.GUI import BACKGROUND_COLOR
from src.platforms.Block import Block, Platform, Door
from src.platforms.Interactable import Backdoor, InventoryItem
from src.platforms.Cannon import Cannon
from src.platforms.Collectible import Collectible
from src.platforms.Group import CustomGroup


class Room:

    def __init__(self, blocks=CustomGroup(), platforms=CustomGroup(), doors=CustomGroup(),
                 cannons=CustomGroup(), collectibles=CustomGroup(), backdoors=CustomGroup()):

        self.collectibles = collectibles
        self.backdoors = backdoors

        """
        inventory = {
            1: 2,
            2: 4,
            3: 1,
        }
        self.items = CustomGroup(
            InventoryItem(200, 500, inventory, 1),
            InventoryItem(300, 500, inventory, 2),
            InventoryItem(400, 500, inventory, 3))
        """

        self.interactables = [backdoors]

        self.doors = doors
        self.blocks = blocks
        self.platforms = platforms

        self.cannons = cannons
        self.bullets = CustomGroup()
        for cannon in cannons:
            cannon.set_bullet_group(self.bullets)

    def update(self):
        self.cannons.update()
        self.bullets.update()
        return

    def detect_collisions(self, char):
        char.detect_collisions(self.blocks)
        char.detect_collisions(self.platforms)
        char.detect_collisions(self.cannons)
        char.detect_collisions(self.doors)

        self.blocks.detect_impacts(self.bullets)
        char.detect_impacts(self.bullets)

        char.detect_collectibles(self.collectibles)
        return

    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)

        self.blocks.draw(screen)
        self.platforms.draw(screen)
        self.doors.draw(screen)
        self.backdoors.draw(screen)

        # self.items.draw(screen)

        self.cannons.draw(screen)

        for objective in self.collectibles:
            objective.draw(screen)

        self.bullets.draw(screen)
        return

    def primary_action(self, player):
        for interactable in self.interactables:
            collisions = pygame.sprite.spritecollide(player.char, interactable, dokill=False)
            if len(collisions) > 0:
                collisions[0].primary_action(player)
                return
        return

    def secondary_action(self, player):
        for interactable in self.interactables:
            collisions = pygame.sprite.spritecollide(player.char, interactable, dokill=False)
            if len(collisions) > 0:
                collisions[0].secondary_action(player)
                return
        return


def load_room(level_json, driver):
    with open(level_json) as f:
        level = json.load(f)

    blocks = CustomGroup()
    for block in level["blocks"]:
        blocks.add(Block(**block))

    platforms = CustomGroup()
    for platform in level["platforms"]:
        platforms.add(Platform(**platform))

    doors = CustomGroup()
    for door in level["doors"]:
        doors.add(Door(driver, **door))

    backdoors = CustomGroup()
    for backdoor in level["backdoors"]:
        backdoors.add(Backdoor(driver, **backdoor))

    cannons = CustomGroup()
    for cannon in level["cannons"]:
        cannons.add(Cannon(**cannon))

    collectibles = CustomGroup()
    for collectible in level["collectibles"]:
        collectibles.add(Collectible(**collectible))

    return Room(blocks=blocks, platforms=platforms, doors=doors, backdoors=backdoors, collectibles=collectibles,
                cannons=cannons)
