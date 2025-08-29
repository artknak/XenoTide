import pygame


class EventHandler:
    """Handle Pygame events for Menu and Game."""

    ESC_PRESSED = 'esc_pressed'
    BULLET_FIRED = 'bullet_fired'

    @staticmethod
    def exit_menu():
        """Quit the game safely."""
        pygame.quit()
        quit()

    @staticmethod
    def process_menu():
        """Process events in Menu. Returns False if Game should start."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                EventHandler.exit_menu()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    EventHandler.exit_menu()
                if event.key == pygame.K_SPACE:
                    return False
        return True

    @staticmethod
    def process_game(player, bullet):
        """Process events in Game. Returns event type."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                EventHandler.exit_menu()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return EventHandler.ESC_PRESSED
                if event.key == pygame.K_SPACE:  # Bullet fire (SPACE)
                    bullet.fire(player)
                    return EventHandler.BULLET_FIRED

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move('left')
        if keys[pygame.K_RIGHT]:
            player.move('right')

        return None