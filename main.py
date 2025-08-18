import pygame
from pygame import mixer
import random

from code.Bullet import Bullet
from code.Entities import Player, Enemy
from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()

# Screen configuration
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Xeno Tide')
icon = pygame.image.load('assets/player.png')
pygame.display.set_icon(icon)

# Background
# background = pygame.image.load('assets/background.png')

# Create player
player = Player()

# Create enemies
enemies = [Enemy() for _ in range(10)]

# Create bullet
bullet = Bullet()

fps = pygame.time.Clock()
running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                bullet.fire(player)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move('left')
    if keys[pygame.K_RIGHT]:
        player.move('right')

    player.draw(screen)

    bullet.update()
    bullet.draw(screen)

    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)

        if bullet.state == 'fired':
            bullet_rect = bullet.img.get_rect(topleft=(bullet.x, bullet.y))
            enemy_rect = enemy.img.get_rect(topleft=(enemy.x, enemy.y))

            # Check for bullet collision
            if bullet_rect.colliderect(enemy_rect):
                # Reset bullet
                bullet.state = 'ready'

                # Respawn enemy at a new random position (like in Enemy.__init__)
                enemy.x = random.randint(int(SCREEN_WIDTH * 0.1), int(SCREEN_WIDTH * 0.9))
                enemy.y = random.randint(int(SCREEN_HEIGHT * 0.1), int(SCREEN_HEIGHT * 0.2))

    fps.tick(60)
    pygame.display.flip()

pygame.quit()
quit()