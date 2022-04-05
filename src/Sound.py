import pygame


class Sound(pygame.mixer.Sound):
    """Music class to store musics and play them"""

    def __init__(self, source, volume):
        """Class constructor"""
        super().__init__(source)
        self.volume = volume

    def play(self):
        self.set_volume(self.volume)
        print(self.volume)
        super().play()
