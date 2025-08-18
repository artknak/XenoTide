import pygame
from pygame import mixer


class Bullet:
    def __init__(self):
        # Load bullet image
        self.img = pygame.image.load('assets/bullet.png')

        # Bullet position (will be set when fired)
        self.x = 0
        self.y = 0

        # Sets how fast the entity can move upwards in px values
        self.move_rate = 10

        # State: "ready" = can fire, not visible; "fired" = moving
        self.state = 'ready'

    def fire(self, player):
        """Set bullet position and change state if ready."""
        # Initialize bullet and sound
        if self.state == 'ready':
            self.state = 'fired'

            # Bullet sound
            bullet_sound = mixer.Sound('assets/bullet_sfx.wav')
            bullet_sound.play()

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
