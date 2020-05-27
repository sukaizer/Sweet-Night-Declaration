import pygame
from game import *

pygame.init()

game = Game()
clock = pygame.time.Clock()
bullet_clock = pygame.time.Clock()
bullet_bool = True

# on set la fenetre
pygame.display.set_caption("Sweet night declaration")
screen = pygame.display.set_mode((game.width, game.height))

# image du background
background = pygame.image.load('assets/background.png')

stats = pygame.image.load('assets/Stats.png')
start = pygame.image.load('assets/ngnl.jpg')
start = pygame.transform.scale(start, (200, 200))
start_rect = start.get_rect()
start_rect.x = game.width/2
start_rect.y = game.height/2

isRunning = True

# boucle principale
while isRunning:

    screen.blit(background, (0, 0))

    if game.is_playing:
        game.update(screen, stats)
    else:
        screen.blit(start, start_rect)

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
            if start_rect.collidepoint(event.pos):
                game.is_playing = True