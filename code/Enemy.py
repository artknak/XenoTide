import random
import pygame

from code.Entity import Entity
from code.Const import ENEMY, SCREEN


class Enemy(Entity):
    """Enemy entity that moves horizontally and steps down at screen edges."""

    def __init__(self):
        """Initialize an enemy with random position and default movement."""
        random_x = random.randint(int(SCREEN['WIDTH'] * 0.1), int(SCREEN['WIDTH'] * 0.9))
        random_y = random.randint(int(SCREEN['HEIGHT'] * 0.1), int(SCREEN['HEIGHT'] * 0.2))

        img = pygame.image.load(ENEMY['IMG'])
        super().__init__(
            img=img,
            x=random_x,
            y=random_y,
            move_rate=ENEMY['MOVE_RATE']
        )
        self.dir_x = 1
        self.step_down = ENEMY['STEP_DOWN']

    def move(self):
        """Move enemy horizontally; reverse direction and step down at screen edges."""
        self.x += self.move_rate * self.dir_x

        if self.x <= 0 or self.x >= SCREEN['WIDTH'] - self.img.get_width():
            self.dir_x *= -1
            self.y += self.step_down

        self.move_rate += ENEMY['ACCEL']
        self.update_rect()

    def reset(self):
        """Reset enemy position randomly near the top and update rect."""
        random_x = random.randint(int(SCREEN['WIDTH'] * 0.1), int(SCREEN['WIDTH'] * 0.9))
        random_y = random.randint(int(SCREEN['HEIGHT'] * 0.1), int(SCREEN['HEIGHT'] * 0.2))

        self.x = random_x
        self.y = random_y
        self.update_rect()
