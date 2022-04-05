import sys

import numpy
import pygame

from Enemy_bullet_pattern import *
from Player import *
from Enemy import *
from Player import Player
from Stats import *
from Enemy_pattern import *


class Game:
    """Class containing all game elements"""

    def __init__(self, width, height):
        """Class constructor"""
        self.width = width
        # the main game screen (3/4 of total width)
        self.real_width = 3 * self.width / 4
        self.height = height
        self.player = Player(self)  # player instance
        # game stats display
        self.stats = Stats(self, self.player)
        self.is_running = True  # game is launched
        self.is_playing = False  # game is being played
        self.is_dead = False  # player is dead
        self.all_enemies = pygame.sprite.Group()  # sprite group with enemies
        self.all_enemy_bullets = pygame.sprite.Group()
        self.pressed = {}  # dictionnary of pressed keys

        self.is_slow = False
        # time variables

        self.wait_bullet_time = 2
        self.wait_bomb_time = 200
        self.time_collision = 120
        self.wait_collision_time = self.time_collision
        self.time = 0

        self.is_immune = False  # player is immune
        self.immune_count = 0

        # Variables animation sprite joueur

        self.left = False
        self.right = False
        self.walkCount = 0
        self.number_frames = 10  # an animation every X frames

        self.bulletSound = pygame.mixer.Sound('../assets/sound/attack.wav')
        self.hitSound = pygame.mixer.Sound('../assets/sound/damage.wav')
        self.hitSound.set_volume(0.01)
        self.SONG_END = pygame.USEREVENT + 1  # end of music event
        self.song_played = False
        self.pause = pygame.image.load(
            '../assets/title/pause.png').convert_alpha()
        self.pause_rect = self.pause.get_rect()  # pause image
        self.pause_rect.x = self.width / 2 - 2 * self.pause_rect.width / 3
        self.pause_rect.y = self.height / 2 - self.pause_rect.height / 2
        self.is_paused = False

    def main_loop(self, screen):
        """main loop of events"""
        pygame_event = pygame.event.get()

        self.exited_screen()
        self.draw_pause_screen(screen)

        # Animation sprite player
        self.draw_player(screen)
        # drawing of objects
        self.all_enemies.draw(screen)
        self.player.all_bullets.draw(screen)
        self.all_enemy_bullets.draw(screen)
        self.stats.stat_menu(screen)

        # bullets movement
        self.move_bullets()

        # ennemies movement
        self.move_enemies()

        # update player (movement, shoot)
        self.update_player(pygame_event)

        self.remove_bullet_collision()

        # looping song (needs fix)
        self.loop_song(pygame_event)

        if not self.is_paused:
            self.time += 1

        # close programm if window is closed
        self.closing_detection(pygame_event)

    def draw_pause_screen(self, screen):
        """draw pause screen"""
        if self.is_paused:
            screen.blit(self.pause, self.pause_rect)

    def exited_screen(self):
        """removes element that exited the visible screen"""
        for enemies in self.all_enemies:
            if enemies.rect.x > (self.real_width + enemies.rect.width) or enemies.rect.x < (
                    0 - enemies.rect.width) or enemies.rect.y > (
                    self.height + enemies.rect.height) or enemies.rect.y < (0 - enemies.rect.height):
                enemies.remove()
        for enemy_bullet in self.all_enemy_bullets:
            if enemy_bullet.rect.x > (self.real_width + enemy_bullet.rect.width) or enemy_bullet.rect.x < (
                    0 - enemy_bullet.rect.width) or enemy_bullet.rect.y > (
                    self.height + enemy_bullet.rect.height) or enemy_bullet.rect.y < (0 - enemy_bullet.rect.height):
                enemy_bullet.remove()
        for player_bullet in self.player.all_bullets:
            if player_bullet.rect.x > (self.real_width + player_bullet.rect.width) or player_bullet.rect.x < (
                    0 - player_bullet.rect.width) or player_bullet.rect.y > (
                    self.height + player_bullet.rect.height) or player_bullet.rect.y < (0 - player_bullet.rect.height):
                player_bullet.remove()

    def update_player(self, pygame_event):
        """update the state of the player"""

        if not self.is_paused and self.pressed.get(pygame.K_RIGHT) and self.pressed.get(
                pygame.K_UP):
            if self.player.rect.x + self.player.rect.width * 1.2 < self.real_width and self.player.rect.y > 0:
                self.player.move_upright()
                self.left = False
                self.right = True
            elif self.player.rect.x + self.player.rect.width * 1.2 < self.real_width:
                self.player.move_right()
                self.left = False
                self.right = True
            elif self.player.rect.y > 0:
                self.player.move_up()
                self.left = False
                self.right = False

        elif not self.is_paused and self.pressed.get(pygame.K_RIGHT) and self.pressed.get(
                pygame.K_DOWN):
            if self.player.rect.x + self.player.rect.width * 1.2 < self.real_width and \
                    self.player.rect.y + self.player.rect.height < self.height:
                self.player.move_downright()
                self.left = False
                self.right = True
            elif self.player.rect.x + self.player.rect.width * 1.2 < self.real_width:
                self.player.move_right()
                self.left = False
                self.right = True
            elif self.player.rect.y + self.player.rect.height < self.height:
                self.player.move_down()
                self.left = False
                self.right = False

        elif not self.is_paused and self.pressed.get(pygame.K_LEFT) and self.pressed.get(
                pygame.K_UP):
            if self.player.rect.x > 0 and self.player.rect.y > 0:
                self.player.move_upleft()
                self.left = True
                self.right = False
            elif self.player.rect.x > 0:
                self.player.move_left()
                self.left = True
                self.right = False
            elif self.player.rect.y > 0:
                self.player.move_up()
                self.left = False
                self.right = False

        elif not self.is_paused and self.pressed.get(pygame.K_LEFT) and self.pressed.get(
                pygame.K_DOWN):
            if self.player.rect.x > 0 and self.player.rect.y + self.player.rect.height < self.height:
                self.player.move_downleft()
                self.left = True
                self.right = False
            elif self.player.rect.x > 0:
                self.player.move_left()
                self.left = True
                self.right = False
            elif self.player.rect.y + self.player.rect.height < self.height:
                self.player.move_down()
                self.left = False
                self.right = False

        # update the position of the player when inputs detected
        elif not self.is_paused and self.pressed.get(pygame.K_RIGHT) and not self.pressed.get(
            pygame.K_LEFT) and not self.pressed.get(
                pygame.K_UP) and not self.pressed.get(
                pygame.K_DOWN) and self.player.rect.x + self.player.rect.width * 1.2 < self.real_width:
            self.player.move_right()
            self.left = False
            self.right = True
        elif not self.is_paused and self.pressed.get(pygame.K_LEFT) and not self.pressed.get(
            pygame.K_RIGHT) and not self.pressed.get(
                pygame.K_UP) and not self.pressed.get(
                pygame.K_DOWN) and self.player.rect.x > 0:
            self.player.move_left()
            self.left = True
            self.right = False
        else:
            self.left = False
            self.right = False
        if not self.is_paused and self.pressed.get(pygame.K_UP) and not self.pressed.get(
            pygame.K_DOWN) and not self.pressed.get(
                pygame.K_LEFT) and not self.pressed.get(
                pygame.K_RIGHT) and self.player.rect.y > 0:
            self.player.move_up()
        elif not self.is_paused and self.pressed.get(pygame.K_DOWN) and not self.pressed.get(
            pygame.K_UP) and not self.pressed.get(
                pygame.K_LEFT) and not self.pressed.get(
                pygame.K_RIGHT) and self.player.rect.y + self.player.rect.height < self.height:
            self.player.move_down()
        if not self.is_paused and self.pressed.get(pygame.K_x) and self.player.time_bomb > self.wait_bomb_time:
            print(self.player.time_bomb)
            self.player.time_bomb = 0

        # player shoot if shoot is not on cooldown
        if not self.is_paused and self.pressed.get(pygame.K_SPACE) and self.player.time_bullet > self.wait_bullet_time:
            self.bulletSound.play()
            self.player.shoot()
            self.player.time_bullet = 0
        # shoot cooldown
        if not self.is_paused:
            self.player.time_bullet += 1
            self.player.time_bomb += 1

        for event in pygame_event:
            # for focus mode
            if event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
                if not self.is_paused and event.key == pygame.K_q:
                    self.player.slow_player()
                    self.is_slow = True
                if not self.is_paused and event.key == pygame.K_ESCAPE:
                    self.is_paused = True
                elif self.is_paused and event.key == pygame.K_ESCAPE:
                    self.is_paused = False
            # key released
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False
                if not self.is_paused and event.key == pygame.K_q:
                    self.player.normal_velocity()
                    self.is_slow = False

        # disables immune mode if player got last hit since long enough
        if self.time_collision > self.wait_collision_time:
            self.is_immune = False

        if not self.is_immune:
            if self.player.check_player_collision():  # player collision
                self.time_collision = 0
                self.is_immune = True
                if self.player.health == 0:
                    self.is_dead = True
                    self.is_playing = False

        if self.is_immune:
            self.immune_count += 1

        if not self.is_paused:
            self.time_collision += 1

    def draw_player(self, screen):
        """draws the player's sprite and animates it"""
        if self.is_immune:
            if self.immune_count % 2 == 0:
                if self.left:
                    screen.blit(
                        self.player.walkLeft[self.walkCount // self.number_frames], self.player.rect)
                    self.walkCount += 1
                elif self.right:
                    screen.blit(
                        self.player.walkRight[self.walkCount // self.number_frames], self.player.rect)
                    self.walkCount += 1
                else:
                    screen.blit(
                        self.player.standing[self.walkCount // self.number_frames], self.player.rect)
                    self.walkCount += 1
        else:
            if self.left:
                screen.blit(
                    self.player.walkLeft[self.walkCount // self.number_frames], self.player.rect)
                self.walkCount += 1
            elif self.right:
                screen.blit(
                    self.player.walkRight[self.walkCount // self.number_frames], self.player.rect)
                self.walkCount += 1
            else:
                screen.blit(
                    self.player.standing[self.walkCount // self.number_frames], self.player.rect)
                self.walkCount += 1

        if self.is_slow:
            pygame.draw.circle(screen, (0, 255, 0, 0.1), (
                self.player.rect.x + self.player.rect.width // 2, self.player.rect.y + self.player.rect.height // 2),
                self.player.hitbox + 7)
        if self.walkCount >= self.number_frames * len(self.player.walkLeft):
            self.walkCount = 0

    def closing_detection(self, pygame_event):
        """detection de la fermeture de la fenetre"""
        for event in pygame_event:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def loop_song(self, pygame_event):
        """loops the main song"""
        for event in pygame_event:
            if event.type == self.SONG_END:
                if not self.song_played:
                    pygame.mixer.music.load('../assets/music/stage01start.ogg')
                    pygame.mixer.music.play(1)
                    self.song_played = True
                else:
                    pygame.mixer.music.load(
                        '../assets/music/stage01repeat.ogg')
                    pygame.mixer.music.play(1)

    def spawn_enemy(self, EnemyType, fun, **kwargs):
        """Spawns an ennemy, considering a specific enemy and his movement function"""

        self.all_enemies.add(EnemyType(self, fun, **kwargs))

    def move_enemies(self):
        """updates enemies position"""
        if not self.is_paused:
            for enemies in self.all_enemies:
                enemies.move()

    def move_bullets(self):
        """updtaes bullets position"""
        if not self.is_paused:
            for bullets in self.player.all_bullets:
                bullets.move()

            for enemy_bullet in self.all_enemy_bullets:
                enemy_bullet.move()

    def remove_bullet_collision(self):
        """removes from screen bullet sprites which collide with enemies"""
        bullet = self.check_collision_player(self.all_enemy_bullets)
        if bullet is not None:
            bullet.remove()

    def check_collision(self, sprite, group):
        """returns all colliding sprites with a specific sprite"""
        return pygame.sprite.spritecollide(sprite, group, False, collided=pygame.sprite.collide_rect)

    def check_collision_player(self, group):
        """check collision between any group of sprite and player"""
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
                testY = y
            elif cy > y + h:
                testY = y + h
            distX = cx - testX
            distY = cy - testY
            distance = numpy.sqrt((distX * distX) + (distY * distY))
            if distance <= self.player.hitbox:
                return enemy

    def new_game(self):
        """initializes all the variables for starting a level"""
        self.player = Player(self)  # initialize player
        self.stats = Stats(self, self.player)
        self.all_enemies = pygame.sprite.Group()
        self.all_enemy_bullets = pygame.sprite.Group()
        self.pressed = {}  # dictionnary of pressed keys
        self.player.time_bullet = 0
        self.wait_bullet_time = 2
        self.time_collision = 120
        self.wait_collision_time = self.time_collision
        self.is_immune = False
        self.immune_count = 0
        # movement is not set
        self.left = False
        self.right = False

        self.walkCount = 0
        self.number_frames = 10  # an animation every X frames
        self.bulletSound = pygame.mixer.Sound('../assets/sound/attack.wav')
        self.hitSound = pygame.mixer.Sound('../assets/sound/damage.wav')
        self.hitSound.set_volume(0.05)
        self.is_slow = False
