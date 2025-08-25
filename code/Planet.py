import random
import pygame

from code.Const import BACKGROUND, SCREEN


class Planet:
    def __init__(self):
        self.reset()

    def reset(self):
        num = random.randint(1, 14)
        img_path = f"{BACKGROUND['PLANET']}{num}.png"

        self.img = pygame.image.load(img_path)
        self.x = random.randint(int(SCREEN['WIDTH'] * 0.1), int(SCREEN['WIDTH'] * 0.9))
        self.y = SCREEN['HEIGHT'] * -0.9
        self.move_rate = random.randint(3, BACKGROUND['MOVE_RATE'])

    def update(self):
        self.y += self.move_rate
        if self.y > SCREEN['HEIGHT']:
            self.reset()

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))