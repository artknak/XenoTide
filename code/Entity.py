import pygame


class Entity:
    def __init__(self, img_path, x, y, move_rate):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.move_rate = move_rate
        self.rect = self.img.get_rect(topleft=(x, y))

    def update_rect(self):
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))