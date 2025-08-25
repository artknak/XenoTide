from code.Bullet import Bullet
from code.Const import ENEMY
from code.Enemy import Enemy
from code.Player import Player


class Spawner:
    @staticmethod
    def spawn_entities():
        player = Player()
        enemies = [Enemy() for _ in range(ENEMY['COUNT'])]
        bullet = Bullet()

        return player, enemies, bullet