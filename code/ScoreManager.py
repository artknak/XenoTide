import pygame.font

from code.Const import COLOR, SCREEN, FONT
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

    def get_current(self):
        return self.score

    def draw(self, screen):
        score_font = pygame.font.Font(FONT['UPHEAVAL'], 30)
        score_text = score_font.render(f'Score: {self.score}', True, COLOR['WHITE'])

        screen.blit(score_text, (((SCREEN['WIDTH'] - score_text.get_width()) // 2) * 0.05,
                                 (SCREEN['HEIGHT'] - score_text.get_height() // 2) * 0.95))

