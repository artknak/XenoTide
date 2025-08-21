import random
import pygame

from code.Background import Background
from code.Bullet import Bullet
from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_IMG, ENEMY_COUNT, COLOR_WHITE
from code.DbProxy import DbProxy
from code.Enemy import Enemy
from code.Player import Player


class Game:

    @staticmethod
    def setup():
        # Window
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Xeno Tide')
        icon = pygame.image.load(PLAYER_IMG)
        pygame.display.set_icon(icon)

        # Background
        background = Background()

        # FPS control
        clock = pygame.time.Clock()

        # Score
        score = 0

        # Database (saves score)
        db_proxy = DbProxy()

        return screen, background, clock, score, db_proxy


    @staticmethod
    def show_menu(screen, db_proxy):
        pygame.font.init()

        title_font = pygame.font.SysFont('Arial', 60)
        info_font = pygame.font.SysFont('Arial', 30)

        best_score = db_proxy.get_best_score()

        menu_running = True
        while menu_running:
            screen.fill((0, 0, 0))

            title_text = title_font.render("Xeno Tide", True, COLOR_WHITE)
            prompt_text = info_font.render("Press SPACE to play!", True, COLOR_WHITE)
            score_text = info_font.render(f"Best score: {best_score}", True, COLOR_WHITE)

            screen.blit(title_text, ((SCREEN_WIDTH - title_text.get_width()) // 2, 100))
            screen.blit(prompt_text, ((SCREEN_WIDTH - prompt_text.get_width()) // 2, SCREEN_HEIGHT // 2))
            screen.blit(score_text, ((SCREEN_WIDTH - score_text.get_width()) // 2, SCREEN_HEIGHT - 50))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        menu_running = False


    @staticmethod
    def entity_spawner():
        # Entities
        player = Player()
        enemies = [Enemy() for _ in range(ENEMY_COUNT)]
        bullet = Bullet()

        return player, enemies, bullet


    @staticmethod
    def input_handler(player, bullet):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'quit'
                if event.key == pygame.K_SPACE:
                    bullet.fire(player)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move('left')
        if keys[pygame.K_RIGHT]:
            player.move('right')

        return None


    @staticmethod
    def collision_handler(ent1, ent2):
        ent1_rect = ent1.img.get_rect(topleft=(ent1.x, ent1.y))
        ent2_rect = ent2.img.get_rect(topleft=(ent2.x, ent2.y))

        if isinstance(ent1, Bullet) and isinstance(ent2, Enemy):
            if ent1.state == 'fired' and ent1_rect.colliderect(ent2_rect):
                ent2.x = random.randint(int(SCREEN_WIDTH * 0.1), int(SCREEN_WIDTH * 0.9))
                ent2.y = random.randint(int(SCREEN_HEIGHT * 0.1), int(SCREEN_HEIGHT * 0.2))
                return 'hit'

        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            if ent1_rect.colliderect(ent2_rect):
                return 'clear_enemies'

        return None


    @staticmethod
    def run():
        pygame.init()

        screen, background, clock, score, db_proxy = Game.setup()
        Game.show_menu(screen, db_proxy)
        player, enemies, bullet = Game.entity_spawner()

        running = True
        while running:
            screen.fill((0, 0, 0))

            background.update()
            background.draw(screen)

            action = Game.input_handler(player, bullet)
            if action == 'quit':
                db_proxy.save_score(score)
                running = False

            player.draw(screen)

            bullet.update()
            bullet.draw(screen)

            for enemy in enemies:
                enemy.move()
                enemy.draw(screen)

                if bullet.state == 'fired':
                    result = Game.collision_handler(bullet, enemy)
                    if result == 'hit':
                        bullet.state = 'ready'
                        score += 1

                result = Game.collision_handler(player, enemy)
                if result == 'clear_enemies':
                    enemies.clear()
                    background.stop()
                    player.x = -9999
                    db_proxy.save_score(score)

            clock.tick(60)
            pygame.display.flip()

        pygame.quit()
        quit()
