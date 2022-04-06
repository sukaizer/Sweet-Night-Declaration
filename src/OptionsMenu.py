import sys
from turtle import update
import pygame
from Music import *


class OptionsMenu:
    """Options Menu of the game"""

    def __init__(self, game):
        """Class constructor"""
        self.game = game
        self.selected = 0
        self.start_music = Music(
            '../assets/music/menumusicstart.ogg', self.game.music_volume)

        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.music_volume = 100
        self.sound_volume = 100
        self.music_unselected = self.myfont.render(
            'Music Volume', False, (0, 0, 0))
        self.sound_unselected = self.myfont.render(
            'Sound Effects Volume', False, (0, 0, 0))
        self.music_selected = self.myfont.render(
            'Music Volume', False, (255, 0, 0))
        self.sound_selected = self.myfont.render(
            'Sound Effects Volume', False, (255, 0, 0))
        self.options = self.myfont.render(
            'Options', False, (0, 0, 0))
        self.back_unselected = self.myfont.render(
            'Back', False, (0, 0, 0))
        self.back_selected = self.myfont.render(
            'Back', False, (255, 0, 0))

        self.music_value = self.myfont.render(
            str(self.music_volume), False, (0, 0, 0))
        self.sound_value = self.myfont.render(
            str(self.sound_volume), False, (0, 0, 0))

    def options_menu(self, screen):
        screen.blit(self.options, (self.game.width/2, 0))
        screen.blit(self.music_value,
                    (self.game.width/2, self.game.height / 4))
        screen.blit(self.sound_value,
                    (self.game.width/2, 2*self.game.height / 4))

        if self.selected == 0:
            screen.blit(self.music_selected,
                        (self.game.width/4, self.game.height / 4))

            screen.blit(self.sound_unselected,
                        (self.game.width/4, 2*self.game.height / 4))
            screen.blit(self.back_unselected,
                        (self.game.width/4, 3*self.game.height / 4))
        elif self.selected == 1:
            screen.blit(self.music_unselected,
                        (self.game.width/4, self.game.height / 4))
            screen.blit(self.sound_selected,
                        (self.game.width/4, 2*self.game.height / 4))
            screen.blit(self.back_unselected,
                        (self.game.width/4, 3*self.game.height / 4))
        else:
            screen.blit(self.music_unselected,
                        (self.game.width/4, self.game.height / 4))
            screen.blit(self.sound_unselected,
                        (self.game.width/4, 2*self.game.height / 4))
            screen.blit(self.back_selected,
                        (self.game.width/4, 3*self.game.height / 4))
        # TODO add sound effect to menus and create list of sounds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.selected == 2:
                    self.game.in_options = False
                if event.key == pygame.K_LEFT:
                    if self.selected == 0 and self.music_volume > 0:
                        self.music_volume -= 5
                    elif self.selected == 1 and self.sound_volume > 0:
                        self.sound_volume -= 5
                    else:
                        break
                if event.key == pygame.K_RIGHT:
                    if self.selected == 0 and self.music_volume < 100:
                        self.music_volume += 5
                    elif self.selected == 1 and self.sound_volume < 100:
                        self.sound_volume += 5
                    else:
                        break
                elif event.key == pygame.K_DOWN:
                    if self.selected == 0:
                        self.selected = 1
                    else:
                        self.selected = 2
                elif event.key == pygame.K_UP:
                    if self.selected == 2:
                        self.selected = 1
                    else:
                        self.selected = 0

            elif event.type == self.game.SONG_END:
                self.start_music.play(-1)
            self.update()

    def update(self):
        self.music_value = self.myfont.render(
            str(self.music_volume), False, (0, 0, 0))
        self.sound_value = self.myfont.render(
            str(self.sound_volume), False, (0, 0, 0))
        self.game.music_volume = self.music_volume / 100
        self.game.sound_volume = self.sound_volume / 100
        self.game.update_volume()
