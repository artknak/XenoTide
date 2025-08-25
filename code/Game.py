import pygame

from code.Background import Background
from code.Collision import Collision
from code.Const import PLAYER, SCREEN
from code.InputHandler import InputHandler
from code.Menu import Menu
from code.ScoreManager import ScoreManager
from code.Spawner import Spawner


class Game:

    @staticmethod
    def setup():
        # Window
        screen = pygame.display.set_mode((SCREEN['WIDTH'], SCREEN['HEIGHT']))
        pygame.display.set_caption('Xeno Tide')
        icon = pygame.image.load(PLAYER['IMG'])
        pygame.display.set_icon(icon)

        background = Background()
        clock = pygame.time.Clock()
        score = ScoreManager()

        return screen, background, clock, score


    @staticmethod
    def update_entities(enemies, bullet, background):
        background.update()
        bullet.update()
        for enemy in enemies:
            enemy.move()


    @staticmethod
    def draw_entities(screen, player, enemies, bullet, background):
        background.draw(screen)
        player.draw(screen)
        bullet.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)


    @staticmethod
    def handle_collisions(player, enemies, bullet, score, background):
        for enemy in enemies[:]:
            if bullet.state == 'fired' and Collision.check(bullet, enemy) == 'hit':
                bullet.state = 'ready'
                score.add()

            if Collision.check(player, enemy) == 'clear_enemies':
                enemies.clear()
                background.stop()
                player.x = -9999
                score.save()


    @staticmethod
    def run():
        pygame.init()

        screen, background, clock, score = Game.setup()
        Menu.show(screen, score)
        player, enemies, bullet = Spawner.spawn_entities()

        running = True
        while running:
            screen.fill((0, 0, 0))

            # Input
            action = InputHandler.process_game(player, bullet)
            if action == 'quit':
                score.save()
                running = False

            # Update entities
            Game.update_entities(enemies, bullet, background)

            # Draw entities
            Game.draw_entities(screen, player, enemies, bullet, background)

            # Check for collisions
            Game.handle_collisions(player, enemies, bullet, score, background)

            clock.tick(60)
            pygame.display.flip()

        pygame.quit()
        quit()
