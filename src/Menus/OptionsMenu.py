import sys
from turtle import update
import pygame
from Music import *
from Components.Text import *


class OptionsMenu:
    """Options Menu of the game"""

    def __init__(self, game):
        """Class constructor"""
        self.game = game
        self.selected = 0
        self.start_music = Music(
            '../assets/music/menumusicstart.ogg', self.game.music_volume)

        self.music_volume = 100
        self.sound_volume = 100

        self.options_title = Text("Options", self.game.font, 50, (0, 0, 0),
                                  (self.game.width/2 - 100, self.game.height / 10))

        self.music_text = Text("Music Volume", self.game.font, 30, (0, 0, 0),
                               (self.game.width/4, self.game.height / 4))

        self.sound_text = Text("Sound Volume", self.game.font, 30, (0, 0, 0),
                               (self.game.width/4, 2*self.game.height / 4))

        self.back_text = Text("Back", self.game.font, 30, (0, 0, 0),
                              (self.game.width/4, 3*self.game.height / 4))

        self.music_value = Text(str(self.music_volume), self.game.font, 30, (0, 0, 0),
                                (3 * self.game.width / 4, self.game.height / 4))

        self.sound_value = Text(str(self.sound_volume), self.game.font, 30, (0, 0, 0),
                                (3 * self.game.width / 4, 2*self.game.height / 4))

    def options_menu(self, screen):
        self.options_title.draw(screen)
        self.music_value.draw(screen)
        self.sound_value.draw(screen)

        if self.selected == 0:
            self.music_text.draw(screen, (255, 0, 0))
            self.sound_text.draw(screen, (0, 0, 0))
            self.back_text.draw(screen, (0, 0, 0))

        elif self.selected == 1:
            self.music_text.draw(screen, (0, 0, 0))
            self.sound_text.draw(screen, (255, 0, 0))
            self.back_text.draw(screen, (0, 0, 0))

        else:
            self.music_text.draw(screen, (0, 0, 0))
            self.sound_text.draw(screen, (0, 0, 0))
            self.back_text.draw(screen, (255, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.selected == 2:
                    self.game.in_options = False
                if event.key == pygame.K_LEFT:
                    if self.selected == 0 and self.music_volume > 0:
                        self.game.menu_sound.play()
                        self.music_volume -= 5
                    elif self.selected == 1 and self.sound_volume > 0:
                        self.game.menu_sound.play()
                        self.sound_volume -= 5
                    else:
                        break
                if event.key == pygame.K_RIGHT:
                    if self.selected == 0 and self.music_volume < 100:
                        self.game.menu_sound.play()
                        self.music_volume += 5
                    elif self.selected == 1 and self.sound_volume < 100:
                        self.game.menu_sound.play()
                        self.sound_volume += 5
                    else:
                        break
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
                self.start_music.play(-1)
            self.update()

    def update(self):
        self.music_value.set_text(str(self.music_volume))
        self.sound_value.set_text(str(self.sound_volume))

        self.game.music_volume = self.music_volume / 100
        self.game.sound_volume = self.sound_volume / 100
        self.game.update_volume()
