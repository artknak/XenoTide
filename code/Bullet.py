import pygame

from code.Entity import Entity
from code.Const import BULLET


class Bullet(Entity):
    """Represent a bullet fired by the player, with ready/fired state."""

    READY = 'ready'
    FIRED = 'fired'

    def __init__(self):
        """Initialize the bullet in the 'ready' state."""
        img = pygame.image.load(BULLET['IMG'])
        super().__init__(
            img=img,
            x=0,
            y=0,
            move_rate=BULLET['MOVE_RATE']
        )
        self.state = Bullet.READY
        self.sound_played = False

    def fire(self, player):
        """Fire the bullet from the player's current position if ready."""
        if self.state == Bullet.READY:
            self.state = Bullet.FIRED
            self.x = player.x + player.img.get_width() // 2 - self.img.get_width() // 2
            self.y = player.y
            self.update_rect()

    def update(self):
        """Move the bullet upwards if fired. Reset to 'ready' when off-screen."""
        if self.state == Bullet.FIRED:
            self.y -= self.move_rate
            self.update_rect()

            if self.y <= 0:
                self.state = Bullet.READY
                self.sound_played = False
        else:
            self.sound_played = False

    def draw(self, screen):
        """Draw the bullet only if it is in the 'fired' state."""
        if self.state == Bullet.FIRED:
            super().draw(screen)