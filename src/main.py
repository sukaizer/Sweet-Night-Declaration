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
# on set la fenetre
pygame.display.set_caption("Sweet Night Declaration")
screen = pygame.display.set_mode((width, height))

game = Stage01(width, height)
start = Start_menu(game)
clock = pygame.time.Clock()
end = End_menu(game)

# image du background
background = pygame.image.load(
    '../assets/background/background.png').convert_alpha()
background = pygame.transform.scale(background, (width, height))

# boucle principale
while game.is_running:

    screen.blit(background, (0, 0))
    clock.tick(60)
    # boucle de jeu
    if game.is_playing and not game.is_dead:
        game.update(screen)
    # boucle du menu
    elif not game.is_playing and not game.is_dead:
        start.start_menu(screen)
    else:
        end.end_menu(screen)

    pygame.display.flip()
