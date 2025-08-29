import pygame

from code.Entity import Entity
from code.Const import PLAYER, SCREEN


class Player(Entity):
    """Represent the player with horizontal movement and screen boundaries."""

    LEFT = 'left'
    RIGHT = 'right'

    def __init__(self):
        """Initialize the player at the bottom center of the screen."""
        img = pygame.image.load(PLAYER['IMG'])
        super().__init__(
            img=img,
            x=(SCREEN['WIDTH'] // 2) - img.get_width() // 2,
            y=int(SCREEN['HEIGHT'] * 0.8),
            move_rate=PLAYER['MOVE_RATE']
        )

    def move(self, direction):
        """
        Move the player left or right and clamp position within screen boundaries.

        :param direction: 'left' or 'right'
        """
        if direction == Player.LEFT:
            self.x -= self.move_rate
        elif direction == Player.RIGHT:
            self.x += self.move_rate

        # Keep player inside screen boundaries
        self.x = max(0, min(self.x, SCREEN['WIDTH'] - self.img.get_width()))
        self.update_rect()