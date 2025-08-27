import pygame

from code.AudioManager import AudioManager
from code.Background import Background
from code.Collision import Collision
from code.Const import PLAYER, SCREEN, SOUND, COLOR
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
        collision_occured = False

        for enemy in enemies[:]:
            if bullet.state == 'fired' and Collision.check(bullet, enemy) == 'hit':
                bullet.state = 'ready'
                score.add()
                collision_occured = True

            if Collision.check(player, enemy) == 'clear_enemies':
                enemies.clear()
                background.stop()
                player.x = -9999
                score.save()
                collision_occured = True

        return collision_occured


    @staticmethod
    def game_over(screen):
        start_time = pygame.time.get_ticks()
        font = pygame.font.SysFont('Arial', 60)
        text = font.render('GAME OVER!', True, COLOR['WHITE'])

        while pygame.time.get_ticks() - start_time < 5000:
            screen.fill((0, 0, 0))
            screen.blit(text, ((SCREEN['WIDTH'] - text.get_width()) // 2,
                               (SCREEN['HEIGHT'] - text.get_height()) // 2))
            pygame.display.flip()
            pygame.time.delay(16)  # ~60 FPS


    @staticmethod
    def run():
        pygame.init()
        pygame.font.init()

        while True:
            screen, background, clock, score = Game.setup()
            Menu.show(screen, score)
            player, enemies, bullet = Spawner.spawn_entities()
            AudioManager.play_music(SOUND['LEVEL'])

            running_level = True

            while running_level:
                screen.fill((0, 0, 0))

                # Handle inputs and bullet fire sounds
                action = InputHandler.process_game(player, bullet)
                if action == 'esc_pressed':
                    score.save()
                    running_level = False

                if action == 'bullet_fired' and not bullet.sound_played:
                    AudioManager.play_sound(SOUND['SHOOT'], 0.3)
                    bullet.sound_played = True

                # Update all entities
                Game.update_entities(enemies, bullet, background)

                # Draw all entities
                Game.draw_entities(screen, player, enemies, bullet, background)

                # Handle collisions and collision sounds
                collision = Game.handle_collisions(player, enemies, bullet, score, background)
                if collision:
                    AudioManager.play_sound(SOUND['COLLISION'], 0.1)
                    if not enemies:
                        AudioManager.play_music(None)
                        AudioManager.play_sound(SOUND['GAME_OVER'])
                        Game.game_over(screen)
                        running_level = False

                # Draw score on screen
                score.draw(screen)

                clock.tick(60)
                pygame.display.flip()

        # pygame.quit()
        # pygame.font.quit()
        # quit()
