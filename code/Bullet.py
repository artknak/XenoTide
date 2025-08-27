import pygame

from code.Entity import Entity
from code.Const import BULLET


class Bullet(Entity):
    def __init__(self):
        img = pygame.image.load(BULLET['IMG'])
        super().__init__(
            img=img,
            x=0,
            y=0,
            move_rate=BULLET['MOVE_RATE']
        )
        self.state = 'ready'
        self.sound_played = False

    def fire(self, player):
        if self.state == 'ready':
            self.state = 'fired'
            self.x = player.x + player.img.get_width() // 2 - self.img.get_width() // 2
            self.y = player.y
            self.update_rect()

    def update(self):
        if self.state == 'fired':
            self.y -= self.move_rate
            self.update_rect()

            if self.y <= 0:
                self.state = 'ready'
                self.sound_played = False
        else:
            self.sound_played = False

    def draw(self, screen):
        if self.state == 'fired':
            super().draw(screen)