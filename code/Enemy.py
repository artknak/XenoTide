import random
from code.Entity import Entity
from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_MOVE_RATE, ENEMY_STEP_DOWN, ENEMY_IMG


class Enemy(Entity):
    def __init__(self):
        super().__init__(
            img_path=ENEMY_IMG,
            x=random.randint(int(SCREEN_WIDTH * 0.1), int(SCREEN_WIDTH * 0.9)),
            y=random.randint(int(SCREEN_HEIGHT * 0.1), int(SCREEN_HEIGHT * 0.2)),
            move_rate=ENEMY_MOVE_RATE
        )
        self.dir_x = 1
        self.step_down = ENEMY_STEP_DOWN

    def move(self):
        self.x += self.move_rate * self.dir_x

        if self.x <= 0 or self.x >= SCREEN_WIDTH - self.img.get_width():
            self.dir_x *= -1
            self.y += self.step_down

        self.move_rate += 0.0005
        self.update_rect()
