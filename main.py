import sys
import pygame
from Game import *
from Start_menu import *
from End_menu import *

pygame.init()

width = 1200
height = 980

# on set la fenetre
pygame.display.set_caption("Sweet Night Declaration")
screen = pygame.display.set_mode((width, height))

game = Game()
start = Start_menu(game)
clock = pygame.time.Clock()
end = End_menu(game)

# image du background
background = pygame.image.load('assets/background/background.png').convert_alpha()
background = pygame.transform.scale(background, (1200, 980))

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
