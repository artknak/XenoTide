import random

import pygame.image

from code.Const import PLANET_IMG, SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_MOVE_RATE


class Planet:
    def __init__(self):
        self.reset()

    def reset(self):
        img_path = random.choice(PLANET_IMG)
        self.img = pygame.image.load(img_path)
        self.x = random.randint(int(SCREEN_WIDTH * 0.1), int(SCREEN_WIDTH * 0.9))
        self.y = SCREEN_HEIGHT * -0.9
        self.move_rate = random.randint(3, BACKGROUND_MOVE_RATE)

    def update(self):
        self.y += self.move_rate
        if self.y > SCREEN_HEIGHT:  # saiu da tela → reset
            self.reset()

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
