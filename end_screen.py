import pygame
import settings
import constants

from scene import _Scene
from game import Game

class EndScreen(_Scene):
    def __init__(self):
        _Scene.__init__(self, constants.STATE_GAME)

        self.font = pygame.font.SysFont(settings.FONT_FAMILY, settings.FONT_SIZE)

        self.make_text()
        self.make_button()
        self.reset()

    def make_text(self):
        self.main = self.font.render("You won!", True, settings.FONT_COLOR)
        self.main_rect = self.main.get_rect(centerx=settings.WINDOW_WIDTH / 2, top=100)

    def make_stats(self):
        self.stat = self.font.render("Your time: " + str(Game.final_time), True, settings.FONT_COLOR)
        self.stat_rect = self.stat.get_rect(centerx=settings.WINDOW_WIDTH / 2, centery=settings.WINDOW_HEIGHT / 2)

    def make_button(self):
        self.button = self.font.render("Play again", True, settings.FONT_COLOR)
        self.button_text_rect = self.button.get_rect(centerx=settings.WINDOW_WIDTH / 2, bottom=settings.WINDOW_HEIGHT - 100)
        self.button_background_rect = pygame.Rect(
            self.button_text_rect.left - settings.BUTTON_PADDING_X,
            self.button_text_rect.top - settings.BUTTON_PADDING_Y,
            self.button_text_rect.width + (settings.BUTTON_PADDING_X * 2),
            self.button_text_rect.height + (settings.BUTTON_PADDING_Y * 2)
        )

    def draw(self, surface):
        self.make_stats()

        surface.fill(settings.BACKGROUND_COLOR)
        surface.blit(self.main, self.main_rect)
        surface.blit(self.stat, self.stat_rect)
        pygame.draw.rect(surface, settings.CARD_COLOR, self.button_background_rect)
        surface.blit(self.button, self.button_text_rect)

    def update(self, now):
        _Scene.update(self, now)

    def get_event(self, event):
        if (event.type == pygame.MOUSEBUTTONUP):
            if (self.button_background_rect.collidepoint(pygame.mouse.get_pos())):
                self.done = True