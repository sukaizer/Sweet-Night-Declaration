import sys
import pygame
from Player import *
from Enemy import *
from Music import *
from Components.Text import *


class EndMenu:
    """Class representing the death menu"""

    def __init__(self, game):
        """Constructeur de classe"""
        self.game = game
        self.import_assets()
        self.selected = 0
        self.music_is_playing = False
        self.restart_text = Text("Restart", self.game.font, 30, (0, 0, 0),
                                 (self.game.width/4, 3*self.game.height / 5))

        self.menu_text = Text("Menu", self.game.font, 30, (0, 0, 0),
                              (self.game.width/2 + 200, 3*self.game.height / 5))

    def import_assets(self):
        self.title = pygame.image.load(
            '../assets/title/game_over.png').convert_alpha()
        self.title = pygame.transform.scale(self.title, (740, 200))
        self.title_rect = self.title.get_rect()
        self.title_rect.x = self.game.width / 2 - self.title_rect.width / 2
        self.title_rect.y = self.game.height / 8

    def end_menu(self, screen):
        """makes all updates within the startmenu"""
        if not self.music_is_playing:
            self.game.end_music.play(-1)
            self.music_is_playing = True

        self.game.all_enemies.empty()  # TODO change that
        self.game.all_emitters.empty()
        screen.blit(self.title, self.title_rect)

        self.restart_text.draw(screen)
        self.menu_text.draw(screen)
        if self.selected == 0:
            self.restart_text.set_color((255, 0, 0))
            self.menu_text.set_color((0, 0, 0))
        else:
            self.restart_text.set_color((0, 0, 0))
            self.menu_text.set_color((255, 0, 0))

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
                        self.game.menu_sound.play()
                    else:
                        break
                elif event.key == pygame.K_LEFT:
                    if self.selected == 1:
                        self.selected = 0
                        self.game.menu_sound.play()
                    else:
                        break
