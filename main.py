import pygame
import settings
from control import Control

def main():
    pygame.init()
    pygame.display.set_caption(settings.TITLE)
    pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    Control().main_loop()
    pygame.quit()

if __name__ == "__main__":
    main()