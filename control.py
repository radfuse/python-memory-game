import pygame
import settings
import constants

from start_screen import StartScreen
from end_screen import EndScreen
from game import Game

class Control(object):
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.done = False
        self.states = {
            constants.STATE_START : StartScreen(),
            constants.STATE_GAME : Game(),
            constants.STATE_END : EndScreen()
        }
        self.state = self.states[constants.STATE_START] # type: StartScreen | Game | EndScreen

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
                
            self.state.get_event(event)

    def update(self):
        now = pygame.time.get_ticks()
        self.state.update(now)

        if self.state.done:
            self.state.reset()
            self.state = self.states[self.state.next]

    def draw(self):
        if self.state.start_time:
            self.state.draw(self.screen)

    def main_loop(self):
        self.screen.fill(settings.BACKGROUND_COLOR)

        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pygame.display.update()