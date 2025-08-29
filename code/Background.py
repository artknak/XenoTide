import pygame

from code.Const import BACKGROUND, SCREEN
from code.Planet import Planet


class Background:
    """Manage scrolling background and planet."""

    def __init__(self):
        self.img = pygame.image.load(BACKGROUND['IMG'])
        self.y = 0
        self.move_rate = BACKGROUND['MOVE_RATE']
        self.planet = Planet()

    def update(self):
        """Update background position and "resets" the planet."""
        # Continuous background scroll effect
        self.y = (self.y + self.move_rate) % SCREEN['HEIGHT']

        self.planet.update()

    def draw(self, screen):
        """
        Blit background and planet to the screen.

        :param screen: Game screen.
        """
        screen.blit(self.img, (0, self.y - SCREEN['HEIGHT']))
        screen.blit(self.img, (0, self.y))
        self.planet.draw(screen)