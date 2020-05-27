import pygame
from player import *
from enemy import *


class Game:
    """Classe comportant tous les elements du jeu"""

    def __init__(self):
        """Constructeur de classe"""

        self.is_running = True
        self.is_playing = False
        self.width = 1080
        self.real_width = 4 * self.width / 6  # the main game screen = 900
        self.height = 980
        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.all_enemies = pygame.sprite.Group()
        self.spawn_enemy()
        # dictionnaire contenant les touches pressées
        self.pressed = {}

    def update(self, screen, stats):
        screen.blit(stats, (self.real_width, 0))

        screen.blit(self.player.image, self.player.rect)

        self.all_enemies.draw(screen)
        self.player.all_bullets.draw(screen)

        for enemies in self.all_enemies:
            enemies.simple_move()

        for bullets in self.player.all_bullets:
            bullets.move()

        # verif des deplacements
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width * 1.2 < self.real_width:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        if self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
            self.player.move_up()
        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.height < self.height:
            self.player.move_down()

        if self.pressed.get(pygame.K_SPACE):
            # ralentir le nombre de balles
            self.player.shoot()

    def spawn_enemy(self):
        """Permet de faire apparaitre un ennemi"""

        self.all_enemies.add(Enemy(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, collided=pygame.sprite.collide_rect)  # change hitbox
