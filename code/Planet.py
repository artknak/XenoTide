import random
import pygame

from code.Const import BACKGROUND, SCREEN


class Planet:
    """Represent a planet that moves vertically across the screen."""

    # Cache planets to avoid reloading from disk
    _cache = {}

    def __init__(self):
        """Initialize a planet by resetting its properties."""
        self.reset()

    def reset(self):
        """Randomize img, x position and move rate."""
        num = random.randint(1, 14)

        if num not in Planet._cache:
            img_path = f'{BACKGROUND['PLANET']}{num}.png'
            Planet._cache[num] = pygame.image.load(img_path)

        self.img = Planet._cache[num]
        self.x = random.randint(int(SCREEN['WIDTH'] * 0.1),  # Spawn planet within bounds
                                int(SCREEN['WIDTH'] * 0.9))
        self.y = SCREEN['HEIGHT'] * -0.9                     # Start above the screen
        self.move_rate = random.randint(3, max(3, BACKGROUND['MOVE_RATE']))

    def update(self):
        """Move the planet downwards; reset if height boundary is hit."""
        self.y += self.move_rate

        if self.y > SCREEN['HEIGHT']:
            self.reset()

    def draw(self, screen):
        """
        Blit planet to the screen.

        :param screen: Game screen.
        """
        screen.blit(self.img, (self.x, self.y))