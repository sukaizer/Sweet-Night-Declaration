import sys
import pygame
from game import *
from start_menu import *

pygame.init()

width = 1080
height = 980

# on set la fenetre
pygame.display.set_caption("Sweet night declaration")
screen = pygame.display.set_mode((width, height))

game = Game()
start = Menu(game)
clock = pygame.time.Clock()

# image du background
background = pygame.image.load('assets/background.png').convert_alpha()

# boucle principale
while game.is_running:

    screen.blit(background, (0, 0))
    clock.tick(60)

    # boucle de jeu
    if game.is_playing:
        game.update(screen)
        for event in pygame.event.get():
            # detection de la fermeture de la fenetre
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
                sys.exit()
            # détection de pression d'une touche
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                if event.key == pygame.K_q:
                    game.player.slow_player()
            # si on lache une touche
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
                if event.key == pygame.K_q:
                    game.player.normal_velocity()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start.start_rect.collidepoint(event.pos):
                    game.is_playing = True
            elif event.type == start.SONG_END:
                pygame.mixer.music.load('assets/music/stage01repeat.ogg')
                pygame.mixer.music.play(-1)
    # boucle du menu
    else:
        start.start_menu(screen)
        for event in pygame.event.get():
            # detection de la fermeture de la fenetre
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
                sys.exit()
            # détection de pression d'une touche
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start.start_rect.collidepoint(event.pos):
                    game.is_playing = True
                    pygame.mixer.music.stop()
            elif event.type == start.SONG_END:
                pygame.mixer.music.load('assets/music/menumusicrepeat.ogg')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.load('assets/music/stage01start.ogg')
                pygame.mixer.music.play(0)
    pygame.display.flip()
