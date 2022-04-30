import random
import pygame
import settings

from image import Image
from scene import _Scene

GAP = 2

class Game(_Scene):
    def __init__(self):
        _Scene.__init__(self, "WIN")
        self.reset()

    def reset(self):
        _Scene.reset(self)
        Image.last_click = None
        Image.flipped1 = None
        Image.flipped2 = None
        Image.all_cards = []

        self.load_images()

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            for image in Image.all_cards:
                image.check_collision()

    def update(self, now):
        _Scene.update(self, now)
        showCount = 0
        
        for image in Image.all_cards:
            if (image.visible == True):
                showCount += 1

        if (showCount <= 2 and Image.flipped1 != None and Image.flipped2 != None):
            self.done = True

    def draw(self, surface):
        surface.fill(settings.BACKGROUND_COLOR)
        
        for image in Image.all_cards:
            image.draw(surface)
            
    def load_images(self):
        images = [] # type: list[Image]

        for image_name in range(1, 9):
            src = pygame.image.load('assets/%d.jpg'%image_name)
            images.append(Image(src, image_name))
            images.append(Image(src, image_name))

        random.shuffle(images)

        for index, image in enumerate(images):
            image.setup(index, 4, 4)
            images[index] = image

        Image.all_cards = images