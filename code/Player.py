import pygame

from code.Entity import Entity
from code.Const import PLAYER, SCREEN


class Player(Entity):
    def __init__(self):
        img = pygame.image.load(PLAYER['IMG'])
        super().__init__(
            img=img,
            x=(SCREEN['WIDTH'] // 2) - img.get_width() // 2,
            y=int(SCREEN['HEIGHT'] * 0.8),
            move_rate=PLAYER['MOVE_RATE']
        )

    def move(self, direction):
        if direction == 'left':
            self.x -= self.move_rate
        elif direction == 'right':
            self.x += self.move_rate

        # Limite de tela
        self.x = max(0, min(self.x, SCREEN['WIDTH'] - self.img.get_width()))
        self.update_rect()