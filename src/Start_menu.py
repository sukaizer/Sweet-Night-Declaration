import pygame
from Player import *
from Enemy import *


class Start_menu:
    """Classe qui représente le menu d'accueil du jeu"""

    def __init__(self, game):
        """Constructeur de classe"""
        self.game = game
        self.title = pygame.image.load(
            '../assets/title/title.png').convert_alpha()
        self.title_rect = self.title.get_rect()
        self.title_rect.x = game.width / 2 - self.title_rect.width / 2
        self.title_rect.y = game.height / 4

        self.start1 = pygame.image.load(
            '../assets/buttons/start1.png').convert_alpha()
        self.start1 = pygame.transform.scale(self.start1, (300, 200))
        self.start_rect1 = self.start1.get_rect()
        self.start_rect1.x = game.width / 4 - self.start_rect1.width / 2
        self.start_rect1.y = game.height / 2 + 50

        self.start2 = pygame.image.load(
            '../assets/buttons/start2.png').convert_alpha()
        self.start2 = pygame.transform.scale(self.start2, (300, 200))
        self.start_rect2 = self.start2.get_rect()
        self.start_rect2.x = game.width / 4 - self.start_rect2.width / 2
        self.start_rect2.y = game.height / 2 + 50

        self.quit1 = pygame.image.load(
            '../assets/buttons/quit1.png').convert_alpha()
        self.quit1 = pygame.transform.scale(self.quit1, (300, 200))
        self.quit_rect1 = self.quit1.get_rect()
        self.quit_rect1.x = 3*game.width / 4 - self.quit_rect1.width / 2
        self.quit_rect1.y = game.height / 2 + 50

        self.quit2 = pygame.image.load(
            '../assets/buttons/quit2.png').convert_alpha()
        self.quit2 = pygame.transform.scale(self.quit2, (300, 200))
        self.quit_rect2 = self.quit2.get_rect()
        self.quit_rect2.x = 3*game.width / 4 - self.quit_rect2.width / 2
        self.quit_rect2.y = game.height / 2 + 50

        self.selected = 0

        self.menu_repeat_music()

    def start_menu(self, screen):
        screen.blit(self.title, self.title_rect)

        if self.selected == 0:
            screen.blit(self.start2, self.start_rect2)
            screen.blit(self.quit1, self.quit_rect1)
        else:
            screen.blit(self.start1, self.start_rect1)
            screen.blit(self.quit2, self.quit_rect2)

        for event in pygame.event.get():
            # detection de la fermeture de la fenetre
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.selected == 0:
                        self.game.is_playing = True
                        pygame.mixer.music.stop()
                        self.game.new_game()
                    else:
                        pygame.quit()
                        sys.exit()
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
            elif event.type == self.game.SONG_END:
                pygame.mixer.music.load('../assets/music/menumusicrepeat.ogg')
                pygame.mixer.music.play(-1)

    def menu_repeat_music(self):
        pygame.mixer.music.set_endevent(self.game.SONG_END)
        pygame.mixer.music.load('../assets/music/menumusicstart.ogg')
        pygame.mixer.music.play(0)
