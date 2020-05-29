import pygame
from Player import *
from Enemy import *


class Start_menu:
    """Classe qui représente le menu d'accueil du jeu"""

    def __init__(self, game):
        """Constructeur de classe"""
        self.game = game
        self.title = pygame.image.load('assets/title/title.png').convert_alpha()
        self.title_rect = self.title.get_rect()
        self.title_rect.x = game.width / 2 - self.title_rect.width / 2
        self.title_rect.y = game.height / 4

        self.start = pygame.image.load('assets/buttons/button.png').convert_alpha()
        self.start = pygame.transform.scale(self.start, (400, 400))
        self.start_rect = self.start.get_rect()
        self.start_rect.x = game.width / 2 - self.start_rect.width / 2
        self.start_rect.y = game.height / 2
        self.menu_repeat_music()

    def start_menu(self, screen):
        screen.blit(self.start, self.start_rect)
        screen.blit(self.title, self.title_rect)
        for event in pygame.event.get():
            # detection de la fermeture de la fenetre
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # détection de pression d'une touche
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_rect.collidepoint(event.pos):
                    self.game.is_playing = True
                    pygame.mixer.music.stop()
                    self.game.new_game()
            elif event.type == self.game.SONG_END:
                pygame.mixer.music.load('assets/music/menumusicrepeat.ogg')
                pygame.mixer.music.play(-1)

    def menu_repeat_music(self):
        pygame.mixer.music.set_endevent(self.game.SONG_END)
        pygame.mixer.music.load('assets/music/menumusicstart.ogg')
        pygame.mixer.music.play(0)
