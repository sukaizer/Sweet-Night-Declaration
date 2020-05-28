import sys

import pygame
from Player import *
from Enemy import *
from Stats import *


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
        # dictionnaire contenant les touches pressées
        self.pressed = {}
        self.time_bullet = 0
        self.wait_bullet_time = 2
        self.time_collision = 120
        self.wait_collision_time = self.time_collision
        self.is_immune = False
        self.immune_count = 0
        self.left = False
        self.right = False
        self.walkCount = 0
        self.number_frames = 5  # toutes les 2 frames, une animation
        self.bulletSound = pygame.mixer.Sound('assets/sound/attack.wav')
        self.hitSound = pygame.mixer.Sound('assets/sound/damage.wav')
        self.hitSound.set_volume(0.05)

    def update(self, screen, start):
        self.time_bullet += 1
        self.time_collision += 1
        self.stats.stat_menu(screen)
        
        if self.walkCount >= self.number_frames * len(self.player.walkLeft):
            self.walkCount = 0

        if self.is_immune:
            self.immune_count += 1
            if self.immune_count % 2 == 0:
                if self.left:
                    screen.blit(self.player.walkLeft[self.walkCount // self.number_frames], self.player.rect)
                    self.walkCount += 1
                elif self.right:
                    screen.blit(self.player.walkRight[self.walkCount // self.number_frames], self.player.rect)
                    self.walkCount += 1
                else:
                    screen.blit(self.player.standing[self.walkCount // self.number_frames], self.player.rect)
                    self.walkCount += 1
        else:
            if self.left:
                screen.blit(self.player.walkLeft[self.walkCount // self.number_frames], self.player.rect)
                self.walkCount += 1
            elif self.right:
                screen.blit(self.player.walkRight[self.walkCount // self.number_frames], self.player.rect)
                self.walkCount += 1
            else:
                screen.blit(self.player.standing[self.walkCount // self.number_frames], self.player.rect)
                self.walkCount += 1

        self.all_enemies.draw(screen)
        self.player.all_bullets.draw(screen)

        for enemies in self.all_enemies:
            enemies.simple_move()

        for bullets in self.player.all_bullets:
            bullets.move()

        # verif des deplacements

        if self.pressed.get(pygame.K_RIGHT) and not self.pressed.get(
                pygame.K_LEFT) and self.player.rect.x + self.player.rect.width * 1.2 < self.real_width:
            self.player.move_right()
            self.left = False
            self.right = True
        elif self.pressed.get(pygame.K_LEFT) and not self.pressed.get(pygame.K_RIGHT) and self.player.rect.x > 0:
            self.player.move_left()
            self.left = True
            self.right = False
        else:
            self.left = False
            self.right = False
        if self.pressed.get(pygame.K_UP) and not self.pressed.get(pygame.K_DOWN) and self.player.rect.y > 0:
            self.player.move_up()
        elif self.pressed.get(pygame.K_DOWN) and not self.pressed.get(
                pygame.K_UP) and self.player.rect.y + self.player.rect.height < self.height:
            self.player.move_down()

        if self.pressed.get(pygame.K_SPACE) and self.time_bullet > self.wait_bullet_time:
            self.bulletSound.play()
            # ralentir le nombre de balles
            self.player.shoot()
            self.time_bullet = 0

        if self.time_collision > self.wait_collision_time:
            self.is_immune = False

        if not self.is_immune:
            if self.player.check_player_collision():  # collision du personnage
                self.time_collision = 0
                self.is_immune = True

        for event in pygame.event.get():
            # detection de la fermeture de la fenetre
            if event.type == pygame.QUIT:
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
            elif event.type == start.SONG_END:
                pygame.mixer.music.load('assets/music/stage01repeat.ogg')
                pygame.mixer.music.play(-1)

    def spawn_enemy(self):
        """Permet de faire apparaitre un ennemi"""

        self.all_enemies.add(Enemy(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, collided=pygame.sprite.collide_rect)  # change hitbox
