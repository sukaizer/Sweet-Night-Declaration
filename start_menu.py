import pygame
from player import *
from enemy import *


class Menu:
    """Classe qui représente le menu d'accueil du jeu"""

    def __init__(self, game):
        """Constructeur de classe"""
        self.game = game
        self.start = pygame.image.load('assets/ngnl.jpg')
        self.start = pygame.transform.scale(self.start, (200, 200))
        self.start_rect = self.start.get_rect()
        self.start_rect.x = game.width / 2
        self.start_rect.y = game.height / 2

    def start_menu(self,screen):
        screen.blit(self.start, self.start_rect)
