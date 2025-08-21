import pygame
from code.Entity import Entity
from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_MOVE_RATE, PLAYER_IMG


class Player(Entity):
    def __init__(self):
        img = pygame.image.load(PLAYER_IMG)
        super().__init__(
            img_path=PLAYER_IMG,
            x=(SCREEN_WIDTH // 2) - img.get_width() // 2,
            y=int(SCREEN_HEIGHT * 0.8),
            move_rate=PLAYER_MOVE_RATE
        )

    def move(self, direction):
        if direction == 'left':
            self.x -= self.move_rate
        elif direction == 'right':
            self.x += self.move_rate

        # Limite de tela
        self.x = max(0, min(self.x, SCREEN_WIDTH - self.img.get_width()))
        self.update_rect()