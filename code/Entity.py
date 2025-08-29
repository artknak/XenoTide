class Entity:
    """Base class for game entities with position, image and movement."""
    def __init__(self, img, x, y, move_rate):
        """
        Initialize an entity.

        :param img: Pygame surface for the entity.
        :param x: Initial x position.
        :param y: Initial y position.
        :param move_rate: Movement speed per update.
        """
        self.img = img
        self.x = x
        self.y = y
        self.move_rate = move_rate
        self.rect = self.img.get_rect(topleft=(x, y))

    def draw(self, screen):
        """
        Draw the entity on the screen.

        :param screen: Game screen.
        """
        screen.blit(self.img, (self.x, self.y))

    def update_rect(self):
        """Update the rect position after moving the entity."""
        self.rect.topleft = (self.x, self.y)