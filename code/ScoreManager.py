import pygame.font

from code.Const import COLOR, SCREEN, FONT
from code.DbProxy import DbProxy


class ScoreManager:
    """Manage the current and highest score."""

    def __init__(self):
        self.score = 0
        self.db_proxy = DbProxy()
        self.font = pygame.font.Font(FONT['UPHEAVAL'], 30)

    def add(self, points=1):
        """
        Add points to the score.

        :param points: Points to be added.
        """
        self.score += points

    def save(self):
        """Save the current score to the database."""
        self.db_proxy.insert_score(self.score)

    def get_best(self):
        """Fetch the best score from the database."""
        return self.db_proxy.fetch_best_score()

    @property
    def current(self):
        """Return the current score."""
        return self.score

    def draw(self, screen):
        """
        Draw the score at the bottom left of the screen.

        :param screen: Game screen.
        """
        score_text = self.font.render(f'Score: {self.score}',
                                      True, COLOR['WHITE'])

        screen.blit(score_text, (((SCREEN['WIDTH'] - score_text.get_width()) // 2) * 0.05,
                                 (SCREEN['HEIGHT'] - score_text.get_height() // 2) * 0.95))

