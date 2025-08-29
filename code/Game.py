import sys

import pygame

from code.AudioManager import AudioManager
from code.Background import Background
from code.Bullet import Bullet
from code.Collision import Collision
from code.Const import PLAYER, SCREEN, SOUND, COLOR, FONT
from code.EventHandler import EventHandler
from code.Menu import Menu
from code.ScoreManager import ScoreManager
from code.Spawner import Spawner


class Game:
    """Main game class handling setup, loop, drawing and collisions."""

    @staticmethod
    def setup():
        """Initialize screen, background, clock and score manager."""
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
        """Update positions of all entities and background."""
        background.update()
        bullet.update()
        for enemy in enemies:
            enemy.move()

    @staticmethod
    def draw_entities(screen, player, enemies, bullet, background):
        """Draw all entities and background on screen."""
        background.draw(screen)
        player.draw(screen)
        bullet.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

    @staticmethod
    def handle_collisions(player, enemies, bullet, score):
        """Check collisions and update score, bullets and enemies."""
        collision_occured = False

        for enemy in enemies[:]:
            # Bullet -> Enemy collision
            if bullet.state == Bullet.FIRED:
                result_bullet = Collision.check(bullet, enemy)
                if result_bullet == Collision.HIT:
                    bullet.state = Bullet.READY
                    score.add()
                    collision_occured = True
                    break

            # Player -> Enemy collision
            result_player = Collision.check(player, enemy)
            if result_player == Collision.CLEAR_ENEMIES:
                enemies.clear()
                player.x = -9999
                score.save()
                collision_occured = True
                break

        return collision_occured

    @staticmethod
    def game_over(screen, score):
        """Display the game over screen for 5 seconds."""
        start_time = pygame.time.get_ticks()
        go_font = pygame.font.Font(FONT['04B_30'], 105)
        go_text = go_font.render('GAME OVER!', True, COLOR['PALE_RED'])

        score_font = pygame.font.Font(FONT['UPHEAVAL'], 35)
        score_text = score_font.render(f'Score: {score.current}', True, COLOR['WHITE'])

        while pygame.time.get_ticks() - start_time < 5000:
            screen.fill((0, 0, 0))

            screen.blit(go_text, ((SCREEN['WIDTH'] - go_text.get_width()) // 2,
                                  (SCREEN['HEIGHT'] - go_text.get_height()) // 2 - 50))
            screen.blit(score_text, ((SCREEN['WIDTH'] - score_text.get_width()) // 2,
                                     (SCREEN['HEIGHT'] - score_text.get_height()) // 2 + 50))

            pygame.display.flip()
            pygame.time.delay(16)  # ~60 FPS, hold screen for 5 seconds

    @staticmethod
    def run():
        """Main game loop."""
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
                action = EventHandler.process_game(player, bullet)
                if action == EventHandler.QUIT:
                    score.save()
                    pygame.quit()
                    sys.exit()

                if action == EventHandler.ESC_PRESSED:
                    score.save()
                    running_level = False

                if action == EventHandler.BULLET_FIRED and not bullet.sound_played:
                    AudioManager.play_sound(SOUND['SHOOT'], 0.1)
                    bullet.sound_played = True

                # Update and draw all entities
                Game.update_entities(enemies, bullet, background)
                Game.draw_entities(screen, player, enemies, bullet, background)

                # Handle collisions and collision sounds
                collision = Game.handle_collisions(player, enemies, bullet, score)
                if collision:
                    AudioManager.play_sound(SOUND['COLLISION'], 0.2)
                    if not enemies:
                        AudioManager.play_music(None)
                        AudioManager.play_sound(SOUND['GAME_OVER'])
                        Game.game_over(screen, score)
                        break

                # Draw score on screen
                score.draw(screen)

                clock.tick(60)
                pygame.display.flip()

