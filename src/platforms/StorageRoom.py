import json

from settings.GUI import BACKGROUND_COLOR, COLLECTIBLE_SIZE
from src.platforms.Block import Block, Platform
from src.platforms.Interactable import Backdoor, InventoryItem
from src.platforms.Group import CustomGroup
from src.platforms.Room import Room


class StorageRoom(Room):
    def __init__(self, blocks=CustomGroup(), platforms=CustomGroup(), backdoors=CustomGroup(), items=CustomGroup()):
        super().__init__()
        self.backdoors = backdoors
        self.items = items

        self.interactables = [backdoors, items]

        self.blocks = blocks
        self.platforms = platforms

    def update(self):
        return

    def detect_collisions(self, char):
        char.detect_collisions(self.blocks)
        char.detect_collisions(self.platforms)
        return

    def draw(self, screen, char):
        screen.fill(BACKGROUND_COLOR)

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

    backdoors = CustomGroup(Backdoor(driver, **level["backdoor"], next_level=prev_level))

    items = CustomGroup()
    print(item_spaces)

    place = item_spaces.pop(0)
    for ingredient in driver.player.storage.items:
        items.add(InventoryItem(place['x'] + 20, place['y'] - COLLECTIBLE_SIZE[1] - 10,
                                ingredient=ingredient, player=driver.player))

        if place['width'] > 160:
            place['x'] += 80
            place['width'] -= 80
        else:
            place = item_spaces.pop(0)

    return StorageRoom(blocks=blocks, platforms=platforms, backdoors=backdoors, items=items)
