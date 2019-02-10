import json

from settings.GUI import BACKGROUND_COLOR
from src.platforms.Block import Block, Platform, Door
from src.platforms.Cannon import Cannon
from src.platforms.Coin import Coin
from src.platforms.Group import CustomGroup


class Level:

    def __init__(self, blocks=CustomGroup(), platforms=CustomGroup(),
                 cannons=CustomGroup(), coins=CustomGroup(), doors=CustomGroup()):

        self.coins = coins
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

        char.detect_objectives(self.coins)
        return

    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)

        self.blocks.draw(screen)
        self.platforms.draw(screen)
        self.doors.draw(screen)

        self.cannons.draw(screen)

        for objective in self.coins:
            objective.draw(screen)

        self.bullets.draw(screen)
        return


def load_level(level_json, driver):
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

    cannons = CustomGroup()
    for cannon in level["cannons"]:
        cannons.add(Cannon(**cannon))

    coins = CustomGroup()
    for coin in level["coins"]:
        coins.add(Coin(**coin))

    return Level(blocks=blocks, platforms=platforms, doors=doors, coins=coins, cannons=cannons)
