import time
from pygame.locals import*
import sys

import numpy
import pygame

from Sound import *
from Music import *
from EnemyBulletPattern import *
from Player import *
from Enemy import *
from Player import Player
from Stats import *
from EnemyPattern import *

from Stages.StageScripts import *
from musics import *


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
        self.level = 0  # load script, first level by default
        self.is_running = True  # game is launched
        self.is_playing = False  # game is being played
        self.in_options = False
        self.is_dead = False  # player is dead
        self.all_enemies = pygame.sprite.Group()  # sprite group with enemies
        self.all_emitters = pygame.sprite.Group()
        self.all_enemy_bullets = pygame.sprite.Group()
        self.pressed = {}  # dictionnary of pressed keys

        self.is_slow = False
        # time variables

        self.wait_bullet_time = 2
        self.wait_bomb_time = 60
        self.time_collision = 120
        self.wait_collision_time = self.time_collision
        self.time = 0

        self.is_immune = False  # player is immune
        self.immune_count = 0

        # Variables animation sprite joueur

        self.player.init_movement()
        self.walkCount = 0
        self.number_frames = 10  # an animation every X frames

        self.sound_volume = 1
        self.music_volume = 1
        self.init_sounds()

        self.max_bomb_frames = 53
        self.bomb_frame = self.max_bomb_frames
        self.load_bomb_sprites()


        # self.font = "Herculanum"
        self.font = "../assets/fonts/font0.ttf"

        self.pause = pygame.image.load(
            '../assets/title/pause.png').convert_alpha()
        self.pause_rect = self.pause.get_rect()  # pause image
        self.pause_rect.x = self.width / 2 - 2 * self.pause_rect.width / 3
        self.pause_rect.y = self.height / 2 - self.pause_rect.height / 2
        self.is_paused = False

    def init_sounds(self):
        """initializes sounds and musics variables"""

        self.bullet_sound = Sound(
            '../assets/sound/attack.wav', self.sound_volume)
        self.hit_sound = Sound(
            '../assets/sound/damage.wav', self.sound_volume)
        self.menu_sound = Sound(
            '../assets/sound/menu.wav', self.sound_volume)
        self.pause_sound = Sound(
            '../assets/sound/pause.wav', self.sound_volume)

        self.debut_music = Music(
            debut_music, self.music_volume)
        self.loop_music = Music(
            loop_music, self.music_volume)
        self.end_music = Music(
            '../assets/music/deathscreenv2.ogg', self.music_volume)
        self.start_music = Music(
            '../assets/music/menumusicstart.ogg', self.music_volume)

        self.sounds = [self.bullet_sound, self.hit_sound,
                       self.menu_sound, self.pause_sound]
        self.musics = [self.debut_music, self.loop_music,
                       self.end_music, self.start_music]

        self.SONG_END = pygame.USEREVENT + 1  # end of music event
        self.song_played = False

    def main_loop(self, screen):
        """main loop of events"""
        pygame_event = pygame.event.get()

        self.exited_screen()

        # Animation sprite player
        self.player.draw(screen)
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

        if self.bomb_frame < self.max_bomb_frames:
            self.animate_bomb(screen)

        self.draw_pause_screen(screen)

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
            elif self.player.rect.x + self.player.rect.width * 1.2 < self.real_width:
                self.player.move_right()
            elif self.player.rect.y > 0:
                self.player.move_up()

        elif not self.is_paused and self.pressed.get(pygame.K_RIGHT) and self.pressed.get(
                pygame.K_DOWN):
            if self.player.rect.x + self.player.rect.width * 1.2 < self.real_width and \
                    self.player.rect.y + self.player.rect.height < self.height:
                self.player.move_downright()
            elif self.player.rect.x + self.player.rect.width * 1.2 < self.real_width:
                self.player.move_right()
            elif self.player.rect.y + self.player.rect.height < self.height:
                self.player.move_down()

        elif not self.is_paused and self.pressed.get(pygame.K_LEFT) and self.pressed.get(
                pygame.K_UP):
            if self.player.rect.x > 0 and self.player.rect.y > 0:
                self.player.move_upleft()
            elif self.player.rect.x > 0:
                self.player.move_left()
            elif self.player.rect.y > 0:
                self.player.move_up()

        elif not self.is_paused and self.pressed.get(pygame.K_LEFT) and self.pressed.get(
                pygame.K_DOWN):
            if self.player.rect.x > 0 and self.player.rect.y + self.player.rect.height < self.height:
                self.player.move_downleft()
            elif self.player.rect.x > 0:
                self.player.move_left()
            elif self.player.rect.y + self.player.rect.height < self.height:
                self.player.move_down()

        # update the position of the player when inputs detected
        elif not self.is_paused and self.pressed.get(pygame.K_RIGHT) and not self.pressed.get(
            pygame.K_LEFT) and not self.pressed.get(
                pygame.K_UP) and not self.pressed.get(
                pygame.K_DOWN) and self.player.rect.x + self.player.rect.width * 1.2 < self.real_width:
            self.player.move_right()
        elif not self.is_paused and self.pressed.get(pygame.K_LEFT) and not self.pressed.get(
            pygame.K_RIGHT) and not self.pressed.get(
                pygame.K_UP) and not self.pressed.get(
                pygame.K_DOWN) and self.player.rect.x > 0:
            self.player.move_left()
        else:
            self.player.init_movement()
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
            if self.player.use_bomb():
                if self.bomb_frame == self.max_bomb_frames:
                    self.bomb_frame = 0
                    (self.w_bomb_anim, self.h_bomb_anim) = (
                        (self.player.rect.left + self.player.rect.width/2) - self.bomb_rect.width / 2, (self.player.rect.top + self.player.rect.height/2) - self.bomb_rect.height / 2)
                self.player.time_bomb = 0
                self.all_emitters.empty()
                self.all_enemies.empty()
                self.all_enemy_bullets.empty()

        # player shoot if shoot is not on cooldown
        if not self.is_paused and self.pressed.get(pygame.K_SPACE) and self.player.time_bullet > self.wait_bullet_time:
            self.bullet_sound.play()
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
                    self.pause_sound.play()
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

    def closing_detection(self, pygame_event):
        """closing window detection"""
        for event in pygame_event:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def loop_song(self, pygame_event):
        """loops the main song"""
        for event in pygame_event:
            if event.type == self.SONG_END:
                if not self.song_played:
                    self.debut_music.play(1)
                    self.song_played = True
                else:
                    self.loop_music.play(1)

    def spawn_enemy(self, EnemyType, fun, **kwargs):
        """Spawns an ennemy, considering a specific enemy and his movement function"""
        if self.bomb_frame == self.max_bomb_frames:
            EnemyType(self, fun, **kwargs).add()

    def spawn_emitter(self, Emitter, fun, **kwargs):
        self.all_emitters.append(Emitter(self, fun, **kwargs))

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
        self.all_emitters = pygame.sprite.Group()
        self.all_enemy_bullets = pygame.sprite.Group()
        self.pressed = {}  # dictionnary of pressed keys
        self.player.time_bullet = 0
        self.wait_bullet_time = 2
        self.time_collision = 120
        self.wait_collision_time = self.time_collision
        self.is_immune = False
        self.immune_count = 0

        self.init_sounds()

        # movement is not set
        self.player.init_movement()
        self.walkCount = 0
        self.number_frames = self.number_frames  # an animation every X frames
        self.is_slow = False

    def update(self, screen):
        """make all updates considering the loaded level (script)"""
        scripts[self.level](self)
        self.main_loop(screen)  # update everything on screen

    def update_volume(self):
        for sound in self.sounds:
            sound.set_volume(self.sound_volume)

        for music in self.musics:
            music.set_volume(self.music_volume)

    def load_bomb_sprites(self):
        self.bomb_sprites = []
        self.bomb_rect = pygame.transform.scale(pygame.image.load(
            '../assets/explosion/explosion_0.png'),(613,625)).get_rect()
        for i in range(self.max_bomb_frames):
            self.bomb_sprites.append(pygame.transform.scale(pygame.image.load(
                '../assets/explosion/explosion_'+str(i)+'.png').convert_alpha(),(613,625)))

    def animate_bomb(self, screen):
        screen.blit(
            self.bomb_sprites[self.bomb_frame], (self.w_bomb_anim, self.h_bomb_anim))
        self.bomb_frame += 1
