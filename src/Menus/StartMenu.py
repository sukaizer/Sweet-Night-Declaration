from ssl import Options
import sys
import pygame
from Player import *
from Enemy import *
from Stages.StageScripts import *
from Components.Text import *
from Music import *


class StartMenu:
    """Start Menu of the game"""

    def __init__(self, game):
        """Class constructor"""
        self.game = game
        self.import_assets()
        self.selected = 0
        self.menu_repeat_music()
        self.play_text = Text("Play", self.game.font, 30, (0, 0, 0),
                              (3 * self.game.width / 4, 2*self.game.height / 5))

        self.options_text = Text("Options", self.game.font, 30, (0, 0, 0),
                                 (3 * self.game.width / 4, 3*self.game.height / 5))

        self.quit_text = Text("Quit", self.game.font, 30, (0, 0, 0),
                              (3 * self.game.width / 4, 4*self.game.height / 5))

    def import_assets(self):
        """import all assets"""
        self.title = pygame.image.load(
            '../assets/title/title.png').convert_alpha()
        self.title = pygame.transform.scale(self.title, (700, 185))
        self.title_rect = self.title.get_rect()
        self.title_rect.x = 3 * self.game.width / \
            4 - (3*self.title_rect.width / 5)
        self.title_rect.y = self.game.height / 4 - self.title_rect.height

        self.character = pygame.image.load(
            '../assets/title/zemmar.png').convert_alpha()
        self.character_rect = self.character.get_rect()
        self.character_rect.x = 1 * self.game.width / 4 - self.character_rect.width/2
        self.character_rect.y = 3 * self.game.height / 4 - self.character_rect.height

    def start_menu(self, screen):
        """makes all updates within the startmenu"""
        screen.blit(self.title, self.title_rect)
        screen.blit(self.character, self.character_rect)

        if self.selected == 0:
            self.play_text.draw(screen, (255, 0, 0))
            self.options_text.draw(screen, (0, 0, 0))
            self.quit_text.draw(screen, (0, 0, 0))
        elif self.selected == 1:
            self.play_text.draw(screen, (0, 0, 0))
            self.options_text.draw(screen, (255, 0, 0))
            self.quit_text.draw(screen, (0, 0, 0))
        else:
            self.play_text.draw(screen, (0, 0, 0))
            self.options_text.draw(screen, (0, 0, 0))
            self.quit_text.draw(screen, (255, 0, 0))

        for event in pygame.event.get():
            # detection de la fermeture de la fenetre
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.selected == 0:
                        self.game.is_playing = True
                        self.game.start_music.stop()
                        self.game.new_game()
                    elif self.selected == 1:
                        self.game.in_options = True
                    else:
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_DOWN:
                    if self.selected == 0:
                        self.game.menu_sound.play()
                        self.selected = 1
                    elif self.selected == 1:
                        self.game.menu_sound.play()
                        self.selected = 2
                elif event.key == pygame.K_UP:
                    if self.selected == 2:
                        self.game.menu_sound.play()
                        self.selected = 1
                    elif self.selected == 1:
                        self.game.menu_sound.play()
                        self.selected = 0
            elif event.type == self.game.SONG_END:
                self.game.start_music.play(-1)

    def menu_repeat_music(self):
        """loops the music"""
        self.game.start_music.set_endevent(self.game.SONG_END)
        self.game.start_music.play(0)
