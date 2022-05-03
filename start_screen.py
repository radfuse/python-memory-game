import math
import pygame
import settings
import constants

from scene import _Scene
from game import Game

class StartScreen(_Scene):
    def __init__(self):
        _Scene.__init__(self, constants.STATE_GAME)

        self.text_font = pygame.font.SysFont(settings.FONT_FAMILY, settings.FONT_SIZE)
        self.button_font = pygame.font.SysFont(settings.FONT_FAMILY, settings.BUTTON_FONT_SIZE)
        self.button_types = [constants.SIZE_4X4, constants.SIZE_5X4, constants.SIZE_6X4, constants.SIZE_6X5]

        self.init_text()
        self.init_buttons()
        self.reset()

    def init_text(self):
        self.main = self.text_font.render("Select size", True, settings.FONT_COLOR)
        self.main_rect = self.main.get_rect(centerx=settings.WINDOW_WIDTH / 2, centery=settings.WINDOW_HEIGHT / 4)

    def init_buttons(self):
        self.buttons = []

        for index, button_type in enumerate(self.button_types):
            x_multiplier = -1 if index % 2 == 0 else 1
            y_multiplier = -1 if math.floor(index / 2) == 0 else 1

            button_text = self.button_font.render(button_type, True, settings.FONT_COLOR)
            button_text_rect = button_text.get_rect()

            if (index % 2 == 0):
                button_text_rect.right = settings.WINDOW_WIDTH / 2 - settings.BUTTON_PADDING_X - settings.GRID_GAP
            else:
                button_text_rect.left = settings.WINDOW_WIDTH / 2 + settings.BUTTON_PADDING_X + settings.GRID_GAP

            if (math.floor(index / 2) == 0):
                button_text_rect.bottom = settings.WINDOW_HEIGHT / 2 - settings.BUTTON_PADDING_Y - settings.GRID_GAP
            else:
                button_text_rect.top = settings.WINDOW_HEIGHT / 2 + settings.BUTTON_PADDING_Y + settings.GRID_GAP

            self.buttons.append({
                'size': button_type,
                'text': button_text,
                'text_rect': button_text_rect,
                'background': self.get_button_background_rect(button_text_rect)
            })

    def get_button_background_rect(self, button_text_rect: pygame.rect.Rect) -> pygame.rect.Rect:
        return pygame.Rect(
            button_text_rect.left - settings.BUTTON_PADDING_X,
            button_text_rect.top - settings.BUTTON_PADDING_Y,
            button_text_rect.width + (settings.BUTTON_PADDING_X * 2),
            button_text_rect.height + (settings.BUTTON_PADDING_Y * 2)
        )

    def draw(self, surface: pygame.surface.Surface):
        surface.fill(settings.BACKGROUND_COLOR)
        surface.blit(self.main, self.main_rect)

        for button in self.buttons:
            pygame.draw.rect(surface, settings.CARD_COLOR, button['background'])
            surface.blit(button['text'], button['text_rect'])

    def update(self, now: int):
        _Scene.update(self, now)

    def get_event(self, event: pygame.event.Event):
        if (event.type == pygame.MOUSEBUTTONUP):
            for button in self.buttons:
                if (button['background'].collidepoint(pygame.mouse.get_pos())):
                    Game.size = button['size']
                    self.done = True