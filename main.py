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

isRunning = True

# boucle principale
while isRunning:

    screen.blit(background, (0, 0))
    screen.blit(stats, (game.real_width, 0))

    screen.blit(game.player.image, game.player.rect)

    game.all_enemies.draw(screen)
    game.player.all_bullets.draw(screen)

    clock.tick(75)

    for enemies in game.all_enemies:
        enemies.simple_move()

    for bullets in game.player.all_bullets:
        bullets.move()

    # verif des deplacements
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width * 1.2 < game.real_width:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_up()
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.height < game.height:
        game.player.move_down()

    if game.pressed.get(pygame.K_SPACE):
        bullet_clock.tick()
        # ralentir le nombre de balles
        if bullet_clock.get_time() > 5:  # TODO
            game.player.shoot()

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
