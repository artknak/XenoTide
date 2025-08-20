import pygame

from code.Const import BACKGROUND_IMG, BACKGROUND_MOVE_RATE, SCREEN_HEIGHT
from code.Planet import Planet


class Background:
    def __init__(self):
        self.img = pygame.image.load(BACKGROUND_IMG)

        self.y1 = 0
        self.y2 = -720
        self.move_rate = BACKGROUND_MOVE_RATE

        self.planet = Planet()

    def update(self):
        self.y1 += self.move_rate
        self.y2 += self.move_rate

        if self.y1 >= SCREEN_HEIGHT:
            self.y1 = self.y2 - SCREEN_HEIGHT
        if self.y2 >= SCREEN_HEIGHT:
            self.y2 = self.y1 - SCREEN_HEIGHT

        self.planet.update()

    def draw(self, screen):
        screen.blit(self.img, (0, self.y1))
        screen.blit(self.img, (0, self.y2))

        self.planet.draw(screen)
