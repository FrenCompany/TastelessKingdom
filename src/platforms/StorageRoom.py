import json

from settings.GUI import COLLECTIBLE_SIZE
from src.platforms.Block import Block, Platform
from src.platforms.Interactable import Backdoor, InventoryItem
from src.platforms.Group import CustomGroup
from src.platforms.Room import Room


class StorageRoom(Room):
    def __init__(self, blocks=CustomGroup(), platforms=CustomGroup(), backdoors=CustomGroup(), items=CustomGroup(),
                 background: str = ""):
        super().__init__(blocks=blocks, platforms=platforms, backdoors=backdoors, background=background)
        self.items = items

        self.interactables = [backdoors, items]

    def update(self):
        return

    def detect_collisions(self, char):
        char.detect_collisions(self.blocks)
        char.detect_collisions(self.platforms)
        return

    def draw(self, screen, char):
        screen.blit(self.background, (0, 0))

        self.blocks.draw(screen)
        self.platforms.draw(screen)
        self.backdoors.draw(screen)

        char.draw(screen)

        self.items.draw(screen)
        return


def load_storage_room(prev_level, driver):
    with open('static/maps/storage.json') as f:
        level = json.load(f)

    blocks = CustomGroup()
    for block in level["blocks"]:
        blocks.add(Block(**block))

    platforms = CustomGroup()
    item_spaces = []
    for platform in level["platforms"]:
        platforms.add(Platform(**platform))
        item_spaces.append(platform)

    backdoors = CustomGroup(Backdoor(driver, **level["backdoor"],
                                     next_room=prev_level, entering_pos=driver.player.char.rect.topleft))

    items = CustomGroup()

    place = item_spaces.pop(0)
    for ingredient in driver.player.storage.items:
        items.add(InventoryItem(place['x'] + 20, place['y'] - COLLECTIBLE_SIZE[1] - 10,
                                ingredient=ingredient, player=driver.player))

        if place['width'] > 160:
            place['x'] += 80
            place['width'] -= 80
        else:
            place = item_spaces.pop(0)

    return StorageRoom(blocks=blocks, platforms=platforms, backdoors=backdoors, items=items,
                       background=level["background"])
