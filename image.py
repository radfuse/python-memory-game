import math
import pygame
import settings

class Image(object):
    last_click = None
    flipped1 = None # type: Image
    flipped2 = None # type: Image
    all_cards = [] # type: list[Image]

    def __init__(self, src: pygame.Surface, name):
        self.src = src
        self.visible = True
        self.name = name

    def setup(self, index, columns, rows):
        self.x = index % columns
        self.y = math.floor(index / rows)
        self.index = index

        card_width = 100
        card_height = 100
        x_offset = (settings.WINDOW_WIDTH - (columns * card_width)) / 2
        y_offset = (settings.WINDOW_HEIGHT - (rows * card_height)) / 2

        left = x_offset + ((card_width + settings.GRID_GAP) * self.x)
        top = y_offset + ((card_height + settings.GRID_GAP) * self.y)

        rect = self.src.get_rect(topleft=(left, top))

        self.rect = rect

    def draw(self, surface):
        if (self.visible == True):
            if ((Image.flipped1 != None and Image.flipped1.index == self.index) or (Image.flipped2 != None and Image.flipped2.index == self.index)):
                surface.blit(self.src, self.rect)
            else:
                pygame.draw.rect(surface, settings.CARD_COLOR, pygame.Rect(self.rect.left, self.rect.top, 100, 100))

    def check_collision(self):
        if (self.rect.collidepoint(pygame.mouse.get_pos()) and self.visible == True):
            if (Image.flipped1 != None and Image.flipped2 != None):
                if (Image.flipped1.name == Image.flipped2.name):
                    Image.flipped1.visible = False
                    Image.flipped2.visible = False

                Image.flipped1 = None
                Image.flipped2 = None
                Image.last_click = None
            
            if ((Image.flipped1 == None or self.index != Image.flipped1.index) and (Image.last_click == None or Image.last_click != self.index)):
                if (Image.flipped1):
                    Image.flipped2 = self
                else:
                    Image.flipped1 = self

                Image.last_click = self.index