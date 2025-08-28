import pygame

from code.AudioManager import AudioManager
from code.Const import COLOR, SCREEN, SOUND, FONT, BACKGROUND
from code.InputHandler import InputHandler


class Menu:

    @staticmethod
    def show(screen, score):
        bg_img = pygame.image.load(BACKGROUND['IMG'])

        title_font = pygame.font.Font(FONT['04B_30'], 110)
        info_font = pygame.font.Font(FONT['UPHEAVAL'], 35)
        best_score = score.get_best()

        AudioManager.play_music(SOUND['MENU'])

        menu_running = True
        while menu_running:
            screen.blit(bg_img, (0, 0))

            title = title_font.render('Xeno Tide', True, COLOR['WHITE'])
            prompt = info_font.render('Press SPACE to play!', True, COLOR['WHITE'])
            score = info_font.render(f'Best score: {best_score}', True, COLOR['WHITE'])

            screen.blit(title, ((SCREEN['WIDTH'] - title.get_width()) // 2,
                                (SCREEN['HEIGHT'] - title.get_height() // 2) * 0.1))
            screen.blit(prompt, ((SCREEN['WIDTH'] - prompt.get_width()) // 2,
                                 (SCREEN['HEIGHT'] - prompt.get_height() // 2) * 0.5))
            screen.blit(score, ((SCREEN['WIDTH'] - score.get_width()) // 2,
                                (SCREEN['HEIGHT'] - score.get_height() // 2) * 0.9))

            pygame.display.flip()

            menu_running = InputHandler.process_menu()

        AudioManager.play_sound(SOUND['MENU_SELECT'])
        AudioManager.play_music(None)