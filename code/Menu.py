import pygame

from code.Const import COLOR, SCREEN
from code.InputHandler import InputHandler


class Menu:
    @staticmethod
    def show(screen, score):
        pygame.font.init()

        title_font = pygame.font.SysFont('Arial', 60)
        info_font = pygame.font.SysFont('Arial', 30)

        best_score = score.get_best()

        menu_running = True
        while menu_running:
            screen.fill((0, 0, 0))

            title = title_font.render("Xeno Tide", True, COLOR['WHITE'])
            prompt = info_font.render("Press SPACE to play!", True, COLOR['WHITE'])
            score = info_font.render(f"Best score: {best_score}", True, COLOR['WHITE'])

            screen.blit(title, ((SCREEN['WIDTH'] - title.get_width()) // 2, SCREEN['HEIGHT'] * 0.1))
            screen.blit(prompt, ((SCREEN['WIDTH'] - prompt.get_width()) // 2, SCREEN['HEIGHT'] // 2))
            screen.blit(score, ((SCREEN['WIDTH'] - score.get_width()) // 2, SCREEN['HEIGHT'] * 0.9))

            pygame.display.flip()

            menu_running = InputHandler.process_menu()