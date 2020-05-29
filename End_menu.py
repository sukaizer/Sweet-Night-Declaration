import pygame
from Player import *
from Enemy import *


class End_menu:
    """Classe qui représente le menu d'accueil du jeu"""

    def __init__(self, game):
        """Constructeur de classe"""
        self.game = game
        self.title = pygame.image.load('assets/title/game_over.png').convert_alpha()
        self.title = pygame.transform.scale(self.title, (740, 200))
        self.title_rect = self.title.get_rect()
        self.title_rect.x = game.width / 2 - self.title_rect.width / 2
        self.title_rect.y = game.height / 6

        self.restart = pygame.image.load('assets/buttons/restart.png').convert_alpha()
        self.restart = pygame.transform.scale(self.restart, (200, 200))
        self.restart_rect = self.restart.get_rect()
        self.restart_rect.x = self.restart_rect.width / 2
        self.restart_rect.y = game.height / 2

        self.menu = pygame.image.load('assets/buttons/menu.png').convert_alpha()
        self.menu = pygame.transform.scale(self.menu, (200, 200))
        self.menu_rect = self.menu.get_rect()
        self.menu_rect.x = game.width - 3 * self.menu_rect.width/2
        self.menu_rect.y = game.height / 2

        self.music_is_playing = False

    def end_menu(self, screen):
        if not self.music_is_playing:
            pygame.mixer.music.load('assets/music/deathscreenv2.ogg')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.3)
            self.music_is_playing = True
        self.game.all_enemies.empty()
        screen.blit(self.restart, self.restart_rect)
        screen.blit(self.title, self.title_rect)
        screen.blit(self.menu, self.menu_rect)
        for event in pygame.event.get():
            # detection de la fermeture de la fenetre
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # détection de pression d'une touche
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.restart_rect.collidepoint(event.pos):
                    self.game.is_playing = True
                    self.game.is_dead = False
                    self.music_is_playing = False
                    pygame.mixer.music.stop()
                    self.game.new_game()
                if self.menu_rect.collidepoint(event.pos):
                    self.game.is_playing = False
                    self.game.is_dead = False
                    self.music_is_playing = False
                    pygame.mixer.music.stop()
