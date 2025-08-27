import pygame


class AudioManager:
    @staticmethod
    def play_music(path=None, volume=0.5, loop=-1):
        if path is None:
            pygame.mixer.music.stop()
        else:
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(loop)

    @staticmethod
    def play_sound(path, volume=0.5):
        sound = pygame.mixer.Sound(path)
        sound.set_volume(volume)
        sound.play()

