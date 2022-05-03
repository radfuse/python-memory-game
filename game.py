import random
import pygame
import datetime
import settings
import constants

from image import Image
from scene import _Scene

class Game(_Scene):
    final_time = None
    size = constants.SIZE_4X4

    def __init__(self):
        _Scene.__init__(self, constants.STATE_END)
        self.reset()

    def reset(self):
        _Scene.reset(self)
        Image.last_click = None
        Image.flipped1 = None
        Image.flipped2 = None
        Image.all_cards = []

    def startup(self, now: int):
        _Scene.startup(self, now)
        self.load_images()

    def get_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONUP:
            for image in Image.all_cards:
                image.check_collision()

    def update(self, now: int):
        _Scene.update(self, now)
        showCount = 0
        
        for image in Image.all_cards:
            if (image.visible == True):
                showCount += 1

        if (showCount <= 2 and Image.flipped1 != None and Image.flipped2 != None):
            Game.final_time = self.get_time(pygame.time.get_ticks() - self.start_time)
            self.done = True

    def draw(self, surface: pygame.surface.Surface):
        surface.fill(settings.BACKGROUND_COLOR)

        font = pygame.font.SysFont(settings.FONT_FAMILY, settings.BUTTON_FONT_SIZE)
        timer = font.render(self.get_time(pygame.time.get_ticks() - self.start_time), True, settings.FONT_COLOR)
        timer_text_rect = timer.get_rect(topleft=(10,10))

        surface.blit(timer, timer_text_rect)
        
        for image in Image.all_cards:
            image.draw(surface)
            
    def load_images(self):
        images = [] # type: list[Image]
        game_size = Game.size.split('x')
        max_cards = int(int(game_size[0]) * int(game_size[1]) / 2)

        for image_name in range(1, max_cards + 1):
            src = pygame.image.load('assets/%d.jpg'%image_name)
            images.append(Image(src, image_name))
            images.append(Image(src, image_name))

        random.shuffle(images)

        for index, image in enumerate(images):
            image.setup(index, int(game_size[0]), int(game_size[1]))
            images[index] = image

        Image.all_cards = images

    def get_time(self, milliseconds: int) -> str:
        seconds = int((milliseconds/1000)%60)
        minutes = int((milliseconds/(1000*60))%60)
        dt = datetime.time(0, minutes, seconds)

        return dt.strftime('%M:%S')