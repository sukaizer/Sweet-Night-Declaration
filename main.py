import pygame
from game import *
from start_menu import *

pygame.init()

game = Game()
start = Menu(game)
clock = pygame.time.Clock()

# on set la fenetre
pygame.display.set_caption("Sweet night declaration")
screen = pygame.display.set_mode((game.width, game.height))

# image du background
background = pygame.image.load('assets/background.png')

# boucle principale
while game.is_running:

    screen.blit(background, (0, 0))
    clock.tick(60)

    if game.is_playing:
        game.update(screen)
    else:
        start.start_menu(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        # detection de la fermeture de la fenetre
        if event.type == pygame.QUIT:
            isRunning = False
            pygame.quit()
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