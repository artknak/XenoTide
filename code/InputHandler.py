import pygame


class InputHandler:
    @staticmethod
    def process_menu():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_SPACE:
                    return False

        return True

    @staticmethod
    def process_game(player, bullet):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'esc_pressed'
                if event.key == pygame.K_SPACE:
                    bullet.fire(player)
                    return 'bullet_fired'

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move('left')
        if keys[pygame.K_RIGHT]:
            player.move('right')

        return None