import json

from settings.GUI import BACKGROUND_COLOR
from src.elements.Block import Block, Platform
from src.elements.Cannon import Cannon
from src.elements.Coin import Coin
from src.elements.Group import CustomGroup


class Level:

    def __init__(self, coins=CustomGroup(), cannons=CustomGroup(), blocks=CustomGroup(), platforms=CustomGroup()):
        self.coins = coins

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

        self.blocks.detect_impacts(self.bullets)
        char.detect_impacts(self.bullets)

        char.detect_objectives(self.coins)

        return

    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)

        self.blocks.draw(screen)
        self.platforms.draw(screen)

        self.cannons.draw(screen)

        for objective in self.coins:
            objective.draw(screen)

        self.bullets.draw(screen)
        return


def load_level(level_json):
    with open(level_json) as f:
        level = json.load(f)

    blocks = CustomGroup()
    for block in level["blocks"]:
        blocks.add(Block(**block))

    platforms = CustomGroup()
    for platform in level["platforms"]:
        platforms.add(Platform(**platform))

    cannons = CustomGroup()
    for cannon in level["cannons"]:
        cannons.add(Cannon(**cannon))

    coins = CustomGroup()
    for coin in level["coins"]:
        coins.add(Coin(**coin))

    return Level(coins=coins, cannons=cannons, blocks=blocks, platforms=platforms)


def load_level2(level):
    blocks = CustomGroup()
    for block in level["blocks"]:
        blocks.add(Block(**block))

    platforms = CustomGroup()
    for platform in level["platforms"]:
        platforms.add(Platform(**platform))

    cannons = CustomGroup()
    for cannon in level["cannons"]:
        cannons.add(Cannon(**cannon))

    coins = CustomGroup()
    for coin in level["coins"]:
        coins.add(Coin(**coin))

    return Level(coins=coins, cannons=cannons, blocks=blocks, platforms=platforms)
