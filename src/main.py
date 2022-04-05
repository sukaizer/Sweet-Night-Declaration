import sys
import pygame
from Game import *
from Start_menu import *
from End_menu import *
from Stages.Stage01 import *

pygame.init()

width = 1300
height = 760
pygame.mouse.set_visible(False)
# window setting
pygame.display.set_caption("Sweet Night Declaration")
screen = pygame.display.set_mode((width, height))

game = Stage01(width, height)
start = Start_menu(game)
clock = pygame.time.Clock()
end = End_menu(game)

# background image
background = pygame.image.load(
    '../assets/background/background.png').convert_alpha()
background = pygame.transform.scale(background, (width, height))

# TODO variable with current level instead of level01 right away
# TODO variable with music volume and effects volume
# TODO class for sounds (music and sound effects)

# main loop
while game.is_running:

    screen.blit(background, (0, 0))
    clock.tick(60)
    # game loop
    if game.is_playing and not game.is_dead:
        game.update(screen)
    # menu
    elif not game.is_playing and not game.is_dead:
        start.start_menu(screen)
    else:
        end.end_menu(screen)

    pygame.display.flip()
