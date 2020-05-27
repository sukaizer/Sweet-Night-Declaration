import pygame
from player import *
from enemy import *


class Menu:
    """Classe qui représente le menu d'accueil du jeu"""

    def __init__(self, game):
        """Constructeur de classe"""
        self.game = game
        self.title = pygame.image.load('assets/title.png').convert_alpha()
        self.title_rect = self.title.get_rect()
        self.title_rect.x = game.width / 2 - self.title_rect.width / 2
        self.title_rect.y = game.height / 4

        self.start = pygame.image.load('assets/button.png').convert_alpha()
        self.start = pygame.transform.scale(self.start, (400, 400))
        self.start_rect = self.start.get_rect()
        self.start_rect.x = game.width / 2 - self.start_rect.width / 2
        self.start_rect.y = game.height / 2
        self.SONG_END = pygame.USEREVENT + 1
        self.menu_repeat_music()

    def start_menu(self, screen):
        screen.blit(self.start, self.start_rect)
        screen.blit(self.title, self.title_rect)

    def menu_repeat_music(self):
        pygame.mixer.music.set_endevent(self.SONG_END)
        pygame.mixer.music.load('assets/music/menumusicstart.ogg')
        pygame.mixer.music.play(0)
