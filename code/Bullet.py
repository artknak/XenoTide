from code.Entity import Entity
from code.Const import BULLET_MOVE_RATE, BULLET_IMG


class Bullet(Entity):
    def __init__(self):
        super().__init__(BULLET_IMG, 0, 0, BULLET_MOVE_RATE)
        self.state = 'ready'

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

    def draw(self, screen):
        if self.state == 'fired':
            super().draw(screen)