import random

from code.Bullet import Bullet
from code.Const import SCREEN
from code.Enemy import Enemy
from code.Player import Player


class Collision:
    """Static methods to check collision between entities."""

    HIT = 'hit'
    CLEAR_ENEMIES = 'clear_enemies'

    @staticmethod
    def check(ent1, ent2):
        """
        Check for collision between two entities.

        :param ent1: First entity (Bullet or Player).
        :param ent2: Second entity (Enemy).
        :return: Collision.HIT, Collision.CLEAR_ENEMIES, or None
        """
        ent1.update_rect()
        ent2.update_rect()

        # Bullet -> Enemy
        if isinstance(ent1, Bullet) and isinstance(ent2, Enemy):
            if ent1.state == ent1.FIRED and ent1.rect.colliderect(ent2.rect):
                ent2.reset()
                ent2.update_rect()
                return Collision.HIT

        # Player -> Enemy
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            if ent1.rect.colliderect(ent2.rect):
                return Collision.CLEAR_ENEMIES

        return None