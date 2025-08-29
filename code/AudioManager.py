import pygame


class AudioManager:
    """Manage background music and sound effects with caching."""

    # Cache sounds to avoid reloading from disk
    _cache = {}

    @staticmethod
    def play_music(path=None, volume=0.5, loop=-1):
        """
        Play or stop background music.

        :param path: Path to music file. If None, stops the current music.
        :param volume: Music volume (0.0 to 1.0).
        :param loop: Number of repetitions (-1 = infinite).
        """
        if path is None:
            pygame.mixer.music.stop()
        else:
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(loop)

    @staticmethod
    def play_sound(path, volume=0.5):
        """
        Play a sound. Uses caching to avoid reloading from disk.

        :param path: Path to sound file.
        :param volume: Sound volume (0.0 to 1.0).
        """
        if path not in AudioManager._cache:
            AudioManager._cache[path] = pygame.mixer.Sound(path)

        sound = AudioManager._cache[path]
        sound.set_volume(volume)
        sound.play()

