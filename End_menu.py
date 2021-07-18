import sys
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

        self.restart1 = pygame.image.load('assets/buttons/restart1.png').convert_alpha()
        self.restart1 = pygame.transform.scale(self.restart1, (300, 200))
        self.restart_rect1 = self.restart1.get_rect()
        self.restart_rect1.x = self.restart_rect1.width / 2
        self.restart_rect1.y = game.height / 2

        self.restart2 = pygame.image.load('assets/buttons/restart2.png').convert_alpha()
        self.restart2 = pygame.transform.scale(self.restart2, (300, 200))
        self.restart_rect2 = self.restart2.get_rect()
        self.restart_rect2.x = self.restart_rect2.width / 2
        self.restart_rect2.y = game.height / 2

        self.menu1 = pygame.image.load('assets/buttons/menu1.png').convert_alpha()
        self.menu1 = pygame.transform.scale(self.menu1, (300, 200))
        self.menu_rect1 = self.menu1.get_rect()
        self.menu_rect1.x = game.width - 3 * self.menu_rect1.width / 2
        self.menu_rect1.y = game.height / 2

        self.menu2 = pygame.image.load('assets/buttons/menu2.png').convert_alpha()
        self.menu2 = pygame.transform.scale(self.menu2, (300, 200))
        self.menu_rect2 = self.menu2.get_rect()
        self.menu_rect2.x = game.width - 3 * self.menu_rect2.width / 2
        self.menu_rect2.y = game.height / 2
        self.selected = 0
        self.music_is_playing = False

    def end_menu(self, screen):
        if not self.music_is_playing:
            pygame.mixer.music.load('assets/music/deathscreenv2.ogg')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.3)
            self.music_is_playing = True
        self.game.all_enemies.empty()
        screen.blit(self.title, self.title_rect)
        if self.selected == 0:
            screen.blit(self.menu1, self.menu_rect1)
            screen.blit(self.restart2, self.restart_rect2)
        else:
            screen.blit(self.menu2, self.menu_rect2)
            screen.blit(self.restart1, self.restart_rect1)

        for event in pygame.event.get():
            # detection de la fermeture de la fenetre
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.selected == 0:
                        self.game.is_playing = True
                        self.game.is_dead = False
                        self.music_is_playing = False
                        pygame.mixer.music.stop()
                        self.game.new_game()
                    else:
                        self.game.is_playing = False
                        self.game.is_dead = False
                        self.music_is_playing = False
                        pygame.mixer.music.stop()
                elif event.key == pygame.K_RIGHT:
                    if self.selected == 0:
                        self.selected = 1
                    else:
                        break
                elif event.key == pygame.K_LEFT:
                    if self.selected == 1:
                        self.selected = 0
                    else:
                        break
