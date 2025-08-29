import pygame

from code.AudioManager import AudioManager
from code.Const import COLOR, SCREEN, SOUND, FONT, BACKGROUND, PLAYER, ENEMY
from code.EventHandler import EventHandler


class Menu:
    """Handle the main menu screen."""

    @staticmethod
    def show(screen, score):
        """
        Display the menu and wait for the player to start the game.

        :param screen: Game screen.
        :param score: ScoreManager instance for fetching best score.
        """
        bg_img = pygame.image.load(BACKGROUND['IMG'])
        player_img = pygame.image.load(PLAYER['IMG'])
        enemy_img = pygame.image.load(ENEMY['IMG'])

        title_font = pygame.font.Font(FONT['04B_30'], 110)
        info_font = pygame.font.Font(FONT['UPHEAVAL'], 35)

        best_score = score.get_best()
        AudioManager.play_music(SOUND['MENU'])

        menu_running = True
        while menu_running:
            screen.blit(bg_img, (0, 0))

            # Render texts
            title_shadow = title_font.render('Xeno Tide', True, COLOR['DARK_ALIEN_GREEN'])
            title = title_font.render('Xeno Tide', True, COLOR['ALIEN_GREEN'])
            prompt = info_font.render('Press SPACE to play!', True, COLOR['WHITE'])
            score_text = info_font.render(f'Best score: {best_score}', True, COLOR['WHITE'])

            # Draw title with shadow
            title_x = (SCREEN['WIDTH'] - title.get_width()) // 2
            title_y = (SCREEN['HEIGHT'] - title.get_height() // 2) * 0.1
            screen.blit(title_shadow, (title_x + 6, title_y + 6))
            screen.blit(title, (title_x, title_y))

            # Draw prompt
            prompt_x = (SCREEN['WIDTH'] - prompt.get_width()) // 2
            prompt_y = (SCREEN['HEIGHT'] - prompt.get_height() // 2) * 0.5
            screen.blit(prompt, (prompt_x, prompt_y))

            # Draw side images (player, enemy)
            center_x = SCREEN['WIDTH'] // 2
            side_y = (SCREEN['HEIGHT'] - player_img.get_height()) * 0.5
            offset = 500
            screen.blit(player_img, (center_x - offset - player_img.get_width() // 2, side_y))
            screen.blit(enemy_img, (center_x + offset - enemy_img.get_width() // 2, side_y))

            # Draw best score at the bottom
            score_x = (SCREEN['WIDTH'] - score_text.get_width()) // 2
            score_y = (SCREEN['HEIGHT'] - score_text.get_height() // 2) * 0.9
            screen.blit(score_text, (score_x, score_y))

            pygame.display.flip()

            # Handle menu input. If process_menu() returns false, Game starts
            menu_running = EventHandler.process_menu()

        AudioManager.play_sound(SOUND['MENU_SELECT'])
        AudioManager.play_music(None)