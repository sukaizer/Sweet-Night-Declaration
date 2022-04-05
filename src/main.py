import sys
import pygame
from Game import *
from StartMenu import *
from EndMenu import *
from Stages.StageScripts import *

pygame.init()

width = 1300
height = 760
pygame.mouse.set_visible(False)
# window setting
pygame.display.set_caption("Sweet Night Declaration")
screen = pygame.display.set_mode((width, height))

game = Game(width, height)
start = StartMenu(game)
clock = pygame.time.Clock()
end = EndMenu(game)

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
