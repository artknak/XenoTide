import math
import random
import pygame

from code.Background import Background
from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_IMG, ENEMY_COUNT
from code.Entities import Player, Enemy, Bullet


class Game:

    @staticmethod
    def setup():
        # Setting up window
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Xeno Tide')
        icon = pygame.image.load(PLAYER_IMG)
        pygame.display.set_icon(icon)

        # Setting up background
        background = Background()

        # Setting up clock (FPS)
        clock = pygame.time.Clock()

        # Setting up score
        score = 0

        # Creating entities
        player = Player()
        enemies = [Enemy() for _ in range(ENEMY_COUNT)]
        bullet = Bullet()

        return screen, background, clock, player, enemies, bullet, score


    @staticmethod
    def collision_handler(ent1, ent2):
        ent1_rect = ent1.img.get_rect(topleft=(ent1.x, ent1.y))
        ent2_rect = ent2.img.get_rect(topleft=(ent2.x, ent2.y))

        if isinstance(ent1, Bullet) and isinstance(ent2, Enemy):
            if ent1.state == 'fired' and ent1_rect.colliderect(ent2_rect):
                ent2.x = random.randint(int(SCREEN_WIDTH * 0.1), int(SCREEN_WIDTH * 0.9))
                ent2.y = random.randint(int(SCREEN_HEIGHT * 0.1), int(SCREEN_HEIGHT * 0.2))
                return "hit"

        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            if ent1_rect.colliderect(ent2_rect):
                return "clear_enemies"

        return None

    @staticmethod
    def input_handler(player, bullet):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "quit"
                if event.key == pygame.K_SPACE:
                    bullet.fire(player)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move('left')
        if keys[pygame.K_RIGHT]:
            player.move('right')

        return None


    @staticmethod
    def run():
        pygame.init()

        # Game configuration
        screen, background, clock, player, enemies, bullet, score = Game.setup()

        running = True
        while running:
            screen.fill((0, 0, 0))
            background.update()
            background.draw(screen)

            action = Game.input_handler(player, bullet)
            if action == "quit":
                running = False

            player.draw(screen)
            bullet.update()
            bullet.draw(screen)

            for enemy in enemies:
                enemy.move()
                enemy.draw(screen)

                if bullet.state == 'fired':
                    result = Game.collision_handler(bullet, enemy)
                    if result == "hit":
                        bullet.state = 'ready'
                        score += 1

                result = Game.collision_handler(player, enemy)
                if result == "clear_enemies":
                    enemies.clear()
                    player.x = math.inf
                    background.move_rate = 0

                    # action = Game.game_over()

            clock.tick(60)
            pygame.display.flip()

        pygame.quit()
        quit()