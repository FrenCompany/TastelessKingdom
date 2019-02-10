import pygame

from settings.GUI import BUTTON_MARGIN, BUTTON_PADDING, BUTTON_TEXT_COLOR, BUTTON_HOVER_COLOR, BUTTON_COLOR, \
    BUTTON_WIDTH, TEXT_MARGIN
from src.platforms.Text import Text


class MenuItem:

    def action_right(self, player):
        pass

    def action_left(self, player):
        pass

    def select(self, player):
        pass

    def unselect(self, player):
        pass

    def draw(self, screen, x, y, selected=False):
        pass

    def get_height(self):
        pass

    def get_margin(self):
        pass

    @staticmethod
    def is_selectable():
        return True


class Button(MenuItem):
    padding = BUTTON_PADDING
    margin = BUTTON_MARGIN

    def __init__(self, handler, text, width=BUTTON_WIDTH, text_size=30,
                 color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR, text_color=BUTTON_TEXT_COLOR):
        self.handler = handler
        self.text = Text(text, color=text_color, size=text_size)

        self.height = text_size + 2 * self.padding
        self.width = max(width, self.text.rect.right + 2 * self.padding)

        self.background = pygame.Surface([self.width, self.height])
        self.color = color
        self.hover_color = hover_color

    def select(self, player):
        self.handler.handle()

    def draw(self, screen, x, y, selected=False):
        if selected:
            self.background.fill(self.hover_color)
        else:
            self.background.fill(self.color)

        screen.blit(self.background, (x - self.width / 2, y))

        self.text.set_pos(x, y + self.height / 2, center=True)
        self.text.draw(screen)
        return

    def get_height(self):
        return self.height

    def get_margin(self):
        return self.margin


class MenuText(MenuItem):

    def __init__(self, text, size=30, color=(0, 0, 0), margin=TEXT_MARGIN):
        self.text = Text(text, color=color, size=size)
        self.height = size
        self.margin = margin

    @staticmethod
    def is_selectable():
        return False

    def draw(self, screen, x, y, selected=False):
        self.text.set_pos(x, y + self.height / 2, center=True)
        self.text.draw(screen)
        return

    def get_height(self):
        return self.height

    def get_margin(self):
        return self.margin
