import pygame
from player import *
from enemy import *


class Menu:
    """Classe qui représente le menu d'accueil du jeu"""

    def __init__(self, game):
        """Constructeur de classe"""
        self.game = game
        self.title = pygame.image.load('assets/title.png').convert_alpha()
        self.title = pygame.transform.scale(self.title, (800, 300))
        self.title_rect = self.title.get_rect()
        self.title_rect.x = game.width / 2 - self.title_rect.width / 2
        self.title_rect.y = game.height / 4

        self.start = pygame.image.load('assets/button.png').convert_alpha()
        self.start = pygame.transform.scale(self.start, (400, 400))
        self.start_rect = self.start.get_rect()
        self.start_rect.x = game.width / 2 - self.start_rect.width / 2
        self.start_rect.y = game.height / 2

    def start_menu(self, screen):
        screen.blit(self.start, self.start_rect)
        screen.blit(self.title, self.title_rect)
