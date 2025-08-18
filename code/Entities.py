import pygame
import random

class Entity:
    def __init__(self, image_path, s_width, s_height, x, y, move_rate):
        # Load entity image
        self.img = pygame.image.load(image_path)

        # Stores screen size (used for boundaries / x and y coordinates calcs)
        self.s_width = s_width
        self.s_height = s_height

        # Initial position
        self.x = x
        self.y = y

        # Sets how fast the entity can move across the screen in px values
        self.move_rate = move_rate

    def draw(self, screen):
        """Draws the entity in the screen."""
        screen.blit(self.img, (self.x, self.y))


class Player(Entity):
    def __init__(self, s_width, s_height):
        super().__init__(
            'assets/player.png',
            s_width=s_width,
            s_height=s_height,
            x=(s_width // 2) - 32,  # Horizontally centered (image is 64px, so half = 32)
            y=int(s_height * 0.8),  # Vertical position = 80% of the screen height
            move_rate=5
        )

    def move(self, direction):
        """Makes the player able to move. Sets screen width boundary."""
        if direction == 'left':
            self.x -= self.move_rate
        elif direction == 'right':
            self.x += self.move_rate

        # Calculates width boundary
        self.x = max(0, min(self.x, self.s_width - self.img.get_width()))


class Enemy(Entity):
    def __init__(self, s_width, s_height):
        super().__init__(
            'assets/enemy.png',
            s_width=s_width,
            s_height=s_height,
            x=random.randint(int(s_width * 0.1), int(s_width * 0.9)),
            y=random.randint(int(s_height * 0.1), int(s_height * 0.2)),
            move_rate=6
        )
        self.dir_x = 1
        self.step_down = 40

    def move(self):
        """Makes the player able to move. Sets screen width boundary and step down."""
        self.x += self.move_rate * self.dir_x

        # Calculates width boundary
        if self.x <= 0 or self.x >= self.s_width - self.img.get_width():
            self.dir_x *= -1            # If boundary is hit, inverts movement direction
            self.y += self.step_down    # and moves the enemy downwards
