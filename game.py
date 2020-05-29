import sys

import pygame
import numpy as np
from player import *
from enemy import *
from statistiques import *
from enemybulletpattern import *
from enemypattern import *


class Game:
    """Classe comportant tous les elements du jeu"""

    def __init__(self):
        """Constructeur de classe"""
        self.width = 1080
        self.real_width = 4 * self.width / 6  # the main game screen = 900
        self.height = 980
        self.player = Player(self)
        self.stats = Stats(self, self.player)
        self.is_running = True
        self.is_playing = False
        self.all_enemies = pygame.sprite.Group()
        self.spawn_enemy()
        self.all_enemy_bullets = pygame.sprite.Group()
        # dictionnaire contenant les touches pressées
        self.pressed = {}
        self.time_bullet = 0
        self.wait_bullet_time = 2
        self.time = 0

    def update(self, screen, start):

        self.exited_screen()
        self.time_bullet += 1
        print(self.time_bullet)
        screen.blit(self.player.image, self.player.rect)
        self.all_enemies.draw(screen)
        self.player.all_bullets.draw(screen)
        self.all_enemy_bullets.draw(screen)

        for enemies in self.all_enemies:
            simple_move(self, enemies)
            enemies.create_bullet(enemies.rect.x, enemies.rect.y, bullet_to_player(self, enemies), 20, 6, 'assets/knofe.png')

        for bullets in self.player.all_bullets:
            bullets.move()

        for enemy_bullet in self.all_enemy_bullets:
            enemy_bullet.move()

        self.stats.stat_menu(screen)

        # verif des deplacements
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width * 1.2 < self.real_width:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        if self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
            self.player.move_up()
        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.height < self.height:
            self.player.move_down()

        if self.pressed.get(pygame.K_SPACE) and self.time_bullet > self.wait_bullet_time:
            # ralentir le nombre de balles
            self.player.shoot()
            self.time_bullet = 0

        for event in pygame.event.get():
            # detection de la fermeture de la fenetre
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
                sys.exit()
            # détection de pression d'une touche
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
                if event.key == pygame.K_q:
                    self.player.slow_player()
            # si on lache une touche
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False
                if event.key == pygame.K_q:
                    self.player.normal_velocity()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start.start_rect.collidepoint(event.pos):
                    self.is_playing = True
            elif event.type == start.SONG_END:
                pygame.mixer.music.load('assets/music/stage01repeat.ogg')
                pygame.mixer.music.play(-1)

        self.time += 1

    def exited_screen(self):
        for enemies in self.all_enemies:
            if enemies.rect.x > (self.real_width + enemies.rect.width) or enemies.rect.x < (0 - enemies.rect.width) or enemies.rect.y > (self.height + enemies.rect.height) or enemies.rect.y < (0 - enemies.rect.height) :
                enemies.remove()
        for enemy_bullet in self.all_enemy_bullets:
            if enemy_bullet.rect.x > (self.real_width + enemy_bullet.rect.width) or enemy_bullet.rect.x < (0 - enemy_bullet.rect.width) or enemy_bullet.rect.y > (self.height + enemy_bullet.rect.height) or enemy_bullet.rect.y < (0 - enemy_bullet.rect.height) :
                enemy_bullet.remove()
        for player_bullet in self.player.all_bullets:
            if player_bullet.rect.x > (self.real_width + player_bullet.rect.width) or player_bullet.rect.x < (0 - player_bullet.rect.width) or player_bullet.rect.y > (self.height + player_bullet.rect.height) or player_bullet.rect.y < (0 - player_bullet.rect.height) :
                player_bullet.remove()


    def spawn_enemy(self):
        """Permet de faire apparaitre un ennemi"""

        self.all_enemies.add(Enemy(self, 200, 200, 1, 0, random.randint(3, 9)))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, collided=pygame.sprite.collide_rect)  # change hitbox
    
