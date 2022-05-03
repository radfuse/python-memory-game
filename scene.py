import pygame

class _Scene(object):
    def __init__(self, next_state=None):
        self.next = next_state
        self.done = False
        self.start_time = None
        self.screen_copy = None

    def startup(self, now: int):
        self.start_time = now
        self.screen_copy = pygame.display.get_surface().copy()

    def reset(self):
        self.done = False
        self.start_time = None
        self.screen_copy = None

    def get_event(self, event: pygame.event.Event):
        pass

    def update(self, now: int):
        if not self.start_time:
            self.startup(now)