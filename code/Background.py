import pygame

from code.Const import BACKGROUND, SCREEN
from code.Planet import Planet


class Background:
    def __init__(self):
        self.img = pygame.image.load(BACKGROUND['IMG'])
        self.y1 = 0
        self.y2 = -SCREEN['HEIGHT']
        self.move_rate = BACKGROUND['MOVE_RATE']
        self.planet = Planet()

    def update(self):
        self.y1 += self.move_rate
        self.y2 += self.move_rate

        if self.y1 >= SCREEN['HEIGHT']:
            self.y1 = self.y2 - SCREEN['HEIGHT']
        if self.y2 >= SCREEN['HEIGHT']:
            self.y2 = self.y1 - SCREEN['HEIGHT']

        self.planet.update()

    def draw(self, screen):
        screen.blit(self.img, (0, self.y1))
        screen.blit(self.img, (0, self.y2))
        self.planet.draw(screen)

    def stop(self):
        self.move_rate = 0
        self.planet.move_rate = 0