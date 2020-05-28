import sys

import numpy
import pygame
from Player import *
from Enemy import *
from Stats import *


class Game:
    """Classe comportant tous les elements du jeu"""

    def __init__(self):
        """Constructeur de classe"""
        self.width = 1080
        self.real_width = 2 * self.width / 3  # the main game screen = 900
        self.height = 980
        self.player = Player(self)  # instance de joueur
        self.stats = Stats(self, self.player)  # affichage des statistiques de partie
        self.is_running = True  # si le jeu est lancé
        self.is_playing = False  # si on joue
        self.is_dead = False  # si on est mort
        self.all_enemies = pygame.sprite.Group()  # groupe comprenant les ennemis
        self.pressed = {}  # dictionnaire contenant les touches pressées

        self.is_slow = False
        # Variables de temps

        self.time_bullet = 0
        self.wait_bullet_time = 2
        self.time_collision = 120
        self.wait_collision_time = self.time_collision

        self.is_immune = False  # si le joueur a subi des dégats et est immunisé
        self.immune_count = 0

        # Variables animation sprite joueur

        self.left = False
        self.right = False
        self.walkCount = 0
        self.number_frames = 5  # toutes les X frames, une animation

        self.bulletSound = pygame.mixer.Sound('assets/sound/attack.wav')
        self.hitSound = pygame.mixer.Sound('assets/sound/damage.wav')
        self.hitSound.set_volume(0.05)
        self.SONG_END = pygame.USEREVENT + 1  # event de fin de musique
        self.pause = pygame.image.load('assets/title/pause.png').convert_alpha()
        self.pause_rect = self.pause.get_rect()  # image de pause
        self.pause_rect.x = self.width / 2 - self.pause_rect.width / 2
        self.pause_rect.y = self.height / 2
        self.is_paused = False

    def update(self, screen):
        if self.is_paused:
            screen.blit(self.pause, self.pause_rect)
        if not self.is_paused:
            self.time_bullet += 1
            self.time_collision += 1
        self.stats.stat_menu(screen)

        if self.walkCount >= self.number_frames * len(self.player.walkLeft):
            self.walkCount = 0

        # Animation sprite joueur
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

        if self.is_slow:
            pygame.draw.circle(screen, (255, 0, 0, 0.1), (
            self.player.rect.x + self.player.rect.width // 2, self.player.rect.y + self.player.rect.height // 2),
                               self.player.hitbox + 3)

        self.all_enemies.draw(screen)
        self.player.all_bullets.draw(screen)

        if not self.is_paused:
            for enemies in self.all_enemies:
                enemies.simple_move()

            for bullets in self.player.all_bullets:
                bullets.move()

        # verif des deplacements

        if not self.is_paused and self.pressed.get(pygame.K_RIGHT) and not self.pressed.get(
                pygame.K_LEFT) and self.player.rect.x + self.player.rect.width * 1.2 < self.real_width:
            self.player.move_right()
            self.left = False
            self.right = True
        elif not self.is_paused and self.pressed.get(pygame.K_LEFT) and not self.pressed.get(
                pygame.K_RIGHT) and self.player.rect.x > 0:
            self.player.move_left()
            self.left = True
            self.right = False
        else:
            self.left = False
            self.right = False
        if not self.is_paused and self.pressed.get(pygame.K_UP) and not self.pressed.get(
                pygame.K_DOWN) and self.player.rect.y > 0:
            self.player.move_up()
        elif not self.is_paused and self.pressed.get(pygame.K_DOWN) and not self.pressed.get(
                pygame.K_UP) and self.player.rect.y + self.player.rect.height < self.height:
            self.player.move_down()

        if not self.is_paused and self.pressed.get(pygame.K_SPACE) and self.time_bullet > self.wait_bullet_time:
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
                if self.player.health == 0:
                    self.is_dead = True
                    self.is_playing = False

        for event in pygame.event.get():
            # detection de la fermeture de la fenetre
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # détection de pression d'une touche
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
                if not self.is_paused and event.key == pygame.K_q:
                    self.player.slow_player()
                    self.is_slow = True
                if not self.is_paused and event.key == pygame.K_ESCAPE:
                    self.is_paused = True
                elif self.is_paused and event.key == pygame.K_ESCAPE:
                    self.is_paused = False
            # si on lache une touche
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False
                if not self.is_paused and event.key == pygame.K_q:
                    self.player.normal_velocity()
                    self.is_slow = False
            elif event.type == self.SONG_END:
                pygame.mixer.music.load('assets/music/stage01repeat.ogg')
                pygame.mixer.music.play(-1)

    def spawn_enemy(self):
        """Permet de faire apparaitre un ennemi"""

        self.all_enemies.add(Enemy(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, collided=pygame.sprite.collide_rect)

    def check_collision_player(self, group):
        cx = self.player.rect.x + self.player.rect.width / 2
        cy = self.player.rect.y + self.player.rect.height / 2
        for enemy in group:
            x = enemy.rect.x
            y = enemy.rect.y
            w = enemy.rect.width
            h = enemy.rect.height
            testX = cx
            testY = cy
            if cx < x:
                testX = x
            elif cx > x + w:
                testX = x + w
            if cy < y:
                testX = y
            elif cy > y + h:
                testX = y + h
            distX = cx - testX
            distY = cy - testY
            distance = numpy.sqrt((distX * distX) + (distY * distY))
            if distance <= self.player.hitbox:
                return True
        return False

    def new_game(self):
        self.player = Player(self)
        self.stats = Stats(self, self.player)
        self.all_enemies = pygame.sprite.Group()
        self.spawn_enemy()
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
