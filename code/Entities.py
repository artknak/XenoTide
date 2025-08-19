import pygame
import random

from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_MOVE_RATE, ENEMY_MOVE_RATE, ENEMY_STEP_DOWN, PLAYER_IMG, \
    ENEMY_IMG, BULLET_MOVE_RATE, BULLET_IMG


class Entity:
    def __init__(self, x, y, move_rate):
        # Initial position
        self.x = x
        self.y = y

        # Sets how fast the entity can move across the screen in px values
        self.move_rate = move_rate

    def draw(self, screen):
        """Draws the entity in the screen."""
        pass


class Player(Entity):
    def __init__(self):
        self.img = pygame.image.load(PLAYER_IMG)

        super().__init__(x=(SCREEN_WIDTH // 2) - self.img.get_width() // 2,
                         y=int(SCREEN_HEIGHT * 0.8),
                         move_rate=PLAYER_MOVE_RATE)

    def move(self, direction):
        """Makes the player able to move. Sets screen width boundary."""
        if direction == 'left':
            self.x -= self.move_rate
        elif direction == 'right':
            self.x += self.move_rate

        # Calculates width boundary
        self.x = max(0, min(self.x, SCREEN_WIDTH - self.img.get_width()))

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))


class Enemy(Entity):
    def __init__(self):
        self.img = pygame.image.load(ENEMY_IMG)

        super().__init__(x=random.randint(int(SCREEN_WIDTH * 0.1), int(SCREEN_WIDTH * 0.9)),
                         y=random.randint(int(SCREEN_HEIGHT * 0.1), int(SCREEN_HEIGHT * 0.2)),
                         move_rate=ENEMY_MOVE_RATE)
        self.dir_x = 1
        self.step_down = ENEMY_STEP_DOWN

    def move(self):
        """Makes the enemy able to move. Sets screen width boundary and step down."""
        self.x += self.move_rate * self.dir_x

        # Calculates width boundary
        if self.x <= 0 or self.x >= SCREEN_WIDTH - self.img.get_width():
            self.dir_x *= -1            # If boundary is hit, inverts movement direction
            self.y += self.step_down    # and moves the enemy downwards

        self.move_rate += 0.0005

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))


class Bullet(Entity):
    def __init__(self):
        self.img = pygame.image.load(BULLET_IMG)
        super().__init__(x=0, y=0, move_rate=BULLET_MOVE_RATE)
        self.state = 'ready'

    def fire(self, player):
        """Set bullet position and change state if ready."""
        # Initialize bullet and sound
        if self.state == 'ready':
            self.state = 'fired'

            # Center bullet in the middle of the player
            self.x = player.x + player.img.get_width() // 2 - self.img.get_width() // 2
            self.y = player.y

    def update(self):
        """Moves bullet upwards if bullet's state is "fired" and sets bullet y boundary."""
        if self.state == 'fired':
            self.y -= self.move_rate

            # Make bullet available again when boundary is hit
            if self.y <= 0:
                self.state = 'ready'

    def draw(self, screen):
        """Draws bullet if fired."""
        if self.state == 'fired':
            screen.blit(self.img, (self.x, self.y))



