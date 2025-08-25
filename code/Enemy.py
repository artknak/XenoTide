import random
import pygame

from code.Entity import Entity
from code.Const import ENEMY, SCREEN


class Enemy(Entity):
    def __init__(self):
        img = pygame.image.load(ENEMY['IMG'])
        super().__init__(
            img=img,
            x=random.randint(int(SCREEN['WIDTH'] * 0.1), int(SCREEN['WIDTH'] * 0.9)),
            y=random.randint(int(SCREEN['HEIGHT'] * 0.1), int(SCREEN['HEIGHT'] * 0.2)),
            move_rate=ENEMY['MOVE_RATE']
        )
        self.dir_x = 1
        self.step_down = ENEMY['STEP_DOWN']

    def move(self):
        self.x += self.move_rate * self.dir_x

        if self.x <= 0 or self.x >= SCREEN['WIDTH'] - self.img.get_width():
            self.dir_x *= -1
            self.y += self.step_down

        self.move_rate += ENEMY['ACCEL']
        self.update_rect()
