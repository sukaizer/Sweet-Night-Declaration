import sys
import pygame
from Player import *
from Enemy import *
from Stages.StageScripts import *
from Music import *


class StartMenu:
    """Start Menu of the game"""

    def __init__(self, game):
        """Class constructor"""
        self.game = game
        self.import_assets()
        self.selected = 0
        self.start_music = Music(
            '../assets/music/menumusicstart.ogg', self.game.music_volume)
        self.menu_repeat_music()
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.text1 = self.myfont.render('Options', False, (0, 0, 0))
        self.text2 = self.myfont.render('Options', False, (255, 0, 0))

    def import_assets(self):
        """import all assets"""
        self.title = pygame.image.load(
            '../assets/title/title.png').convert_alpha()
        self.title_rect = self.title.get_rect()
        self.title_rect.x = self.game.width / 2 - self.title_rect.width / 2
        self.title_rect.y = self.game.height / 4

        self.start1 = pygame.image.load(
            '../assets/buttons/start1.png').convert_alpha()
        self.start1 = pygame.transform.scale(self.start1, (300, 200))
        self.start_rect1 = self.start1.get_rect()
        self.start_rect1.x = self.game.width / 4 - self.start_rect1.width / 2
        self.start_rect1.y = self.game.height / 2 + 50

        self.start2 = pygame.image.load(
            '../assets/buttons/start2.png').convert_alpha()
        self.start2 = pygame.transform.scale(self.start2, (300, 200))
        self.start_rect2 = self.start2.get_rect()
        self.start_rect2.x = self.game.width / 4 - self.start_rect2.width / 2
        self.start_rect2.y = self.game.height / 2 + 50

        self.quit1 = pygame.image.load(
            '../assets/buttons/quit1.png').convert_alpha()
        self.quit1 = pygame.transform.scale(self.quit1, (300, 200))
        self.quit_rect1 = self.quit1.get_rect()
        self.quit_rect1.x = 3*self.game.width / 4 - self.quit_rect1.width / 2
        self.quit_rect1.y = self.game.height / 2 + 50

        self.quit2 = pygame.image.load(
            '../assets/buttons/quit2.png').convert_alpha()
        self.quit2 = pygame.transform.scale(self.quit2, (300, 200))
        self.quit_rect2 = self.quit2.get_rect()
        self.quit_rect2.x = 3*self.game.width / 4 - self.quit_rect2.width / 2
        self.quit_rect2.y = self.game.height / 2 + 50

    def start_menu(self, screen):
        """makes all updates within the startmenu"""
        screen.blit(self.title, self.title_rect)

        if self.selected == 0:
            screen.blit(self.start2, self.start_rect2)
            screen.blit(self.text1,
                        (self.game.width / 2, 2*self.game.height / 3))
            screen.blit(self.quit1, self.quit_rect1)
        elif self.selected == 1:
            screen.blit(self.start1, self.start_rect1)
            screen.blit(self.text2,
                        (self.game.width / 2, 2*self.game.height / 2))
            screen.blit(self.quit1, self.quit_rect1)
        else:
            screen.blit(self.start1, self.start_rect1)
            screen.blit(self.text1,
                        (self.game.width / 2, 2*self.game.height / 2))
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
                        self.start_music.stop()
                        self.game.new_game()
                    elif self.selected == 1:
                        self.game.in_options = True
                    else:
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_RIGHT:
                    if self.selected == 0:
                        self.selected = 1
                    else:
                        self.selected = 2
                elif event.key == pygame.K_LEFT:
                    if self.selected == 2:
                        self.selected = 1
                    else:
                        self.selected = 0
            elif event.type == self.game.SONG_END:
                self.start_music.play(-1)

    def menu_repeat_music(self):
        """loops the music"""
        self.start_music.set_endevent(self.game.SONG_END)
        self.start_music.play(0)
