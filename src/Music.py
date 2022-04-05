import pygame


class Music():
    """Music class to store musics and play them"""

    def __init__(self, source, volume):
        """Class constructor"""
        self.volume = volume
        self.source = source

    def play(self, iterations):
        pygame.mixer.music.load(self.source)
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(iterations)

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def set_endevent(self, event):
        pygame.mixer.music.set_endevent(event)
