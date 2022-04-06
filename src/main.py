import sys
from Menus.OptionsMenu import OptionsMenu
import pygame
from Game import *
from Menus.StartMenu import *
from Menus.EndMenu import *
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
options = OptionsMenu(game)
clock = pygame.time.Clock()
end = EndMenu(game)

# background image
background = pygame.image.load(
    '../assets/background/background.png').convert_alpha()
background = pygame.transform.scale(background, (width, height))

# main loop
while game.is_running:

    screen.blit(background, (0, 0))
    clock.tick(60)
    # game loop
    if game.is_playing and not game.is_dead and not game.in_options:
        game.update(screen)
    # menu
    elif not game.is_playing and not game.is_dead and not game.in_options:
        start.start_menu(screen)
    elif not game.is_playing and not game.is_dead and game.in_options:
        options.options_menu(screen)
    else:
        end.end_menu(screen)

    pygame.display.flip()
