import random

from code.Bullet import Bullet
from code.Const import SCREEN
from code.Enemy import Enemy
from code.Player import Player


class Collision:
    @staticmethod
    def check(ent1, ent2):
        ent1_rect = ent1.img.get_rect(topleft=(ent1.x, ent1.y))
        ent2_rect = ent2.img.get_rect(topleft=(ent2.x, ent2.y))

        if isinstance(ent1, Bullet) and isinstance(ent2, Enemy):
            if ent1.state == 'fired' and ent1_rect.colliderect(ent2_rect):
                ent2.x = random.randint(int(SCREEN['WIDTH'] * 0.1), int(SCREEN['WIDTH'] * 0.9))
                ent2.y = random.randint(int(SCREEN['HEIGHT'] * 0.1), int(SCREEN['HEIGHT'] * 0.2))
                return 'hit'

        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            if ent1_rect.colliderect(ent2_rect):
                return 'clear_enemies'

        return None