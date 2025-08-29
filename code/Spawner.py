from code.Bullet import Bullet
from code.Const import ENEMY
from code.Enemy import Enemy
from code.Player import Player


class Spawner:
    """Static class to spawn game entities."""

    @staticmethod
    def spawn_entities():
        """Spawn player, enemies and a bullet."""

        player = Player()
        enemies = [Enemy() for _ in range(ENEMY['COUNT'])]
        bullet = Bullet()

        return player, enemies, bullet