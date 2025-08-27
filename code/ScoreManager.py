import pygame.font

from code.Const import COLOR, SCREEN
from code.DbProxy import DbProxy


class ScoreManager:
    def __init__(self):
        self.score = 0
        self.db_proxy = DbProxy()

    def add(self):
        self.score += 1

    def save(self):
        self.db_proxy.insert_score(self.score)

    def get_best(self):
        return self.db_proxy.fetch_best_score()

    def draw(self, screen):
        score_font = pygame.font.SysFont('Arial', 30)
        score_text = score_font.render(f'Score: {self.score}', True, COLOR['WHITE'])

        screen.blit(score_text, (SCREEN['WIDTH'] * 0.03, SCREEN['HEIGHT'] * 0.9))

