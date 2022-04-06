from operator import truediv
import pygame
from Game import *
from PlayerBullet import *


class Player(pygame.sprite.Sprite):
    """Class representing the player"""

    def __init__(self, game):
        """Class constructor"""

        super().__init__()
        self.game = game
        self.nb_bomb = 3
        self.health = 3
        self.max_health = 3
        self.attack = 20
        self.max_velocity = 8  # pixels
        self.velocity = 8
        self.slow_velocity = 4  # velocity with key pressed
        self.all_bullets = pygame.sprite.Group()
        self.import_assets()
        self.hitbox = self.rect.width // 25  # rayon
        self.time_bullet = 0
        self.time_bomb = 200
        self.left = False
        self.right = False

    def import_assets(self):
        """import all assets"""
        self.image = pygame.image.load('../assets/animated_sprites/d1.png')
        self.walkRight = [pygame.image.load('../assets/animated_sprites/d1.png').convert_alpha(),
                          pygame.image.load(
                              '../assets/animated_sprites/d2.png').convert_alpha(),
                          pygame.image.load(
                              '../assets/animated_sprites/d3.png').convert_alpha(),
                          pygame.image.load(
                              '../assets/animated_sprites/d4.png').convert_alpha(),
                          pygame.image.load(
                              '../assets/animated_sprites/d5.png').convert_alpha(),
                          pygame.image.load(
                              '../assets/animated_sprites/d6.png').convert_alpha(),
                          pygame.image.load(
                              '../assets/animated_sprites/d7.png').convert_alpha(),
                          pygame.image.load('../assets/animated_sprites/d8.png').convert_alpha()]
        self.walkLeft = [pygame.image.load('../assets/animated_sprites/g1.png').convert_alpha(),
                         pygame.image.load(
                             '../assets/animated_sprites/g2.png').convert_alpha(),
                         pygame.image.load(
                             '../assets/animated_sprites/g3.png').convert_alpha(),
                         pygame.image.load(
                             '../assets/animated_sprites/g4.png').convert_alpha(),
                         pygame.image.load(
                             '../assets/animated_sprites/g5.png').convert_alpha(),
                         pygame.image.load(
                             '../assets/animated_sprites/g6.png').convert_alpha(),
                         pygame.image.load(
                             '../assets/animated_sprites/g7.png').convert_alpha(),
                         pygame.image.load('../assets/animated_sprites/g8.png').convert_alpha()]
        self.standing = [pygame.image.load('../assets/animated_sprites/m1.png').convert_alpha(),
                         pygame.image.load(
                             '../assets/animated_sprites/m2.png').convert_alpha(),
                         pygame.image.load(
                             '../assets/animated_sprites/m3.png').convert_alpha(),
                         pygame.image.load(
                             '../assets/animated_sprites/m4.png').convert_alpha(),
                         pygame.image.load(
                             '../assets/animated_sprites/m5.png').convert_alpha(),
                         pygame.image.load(
                             '../assets/animated_sprites/m6.png').convert_alpha(),
                         pygame.image.load(
                             '../assets/animated_sprites/m7.png').convert_alpha(),
                         pygame.image.load('../assets/animated_sprites/m8.png').convert_alpha()]
        self.rect = self.image.get_rect()
        self.rect.x = self.game.real_width / 2
        self.rect.y = self.game.height / 2

    def shoot(self):
        self.all_bullets.add(PlayerBullet(self, self.game, self.attack))

    def move_upright(self):
        """Up Right movement"""
        self.rect.x += self.velocity * 0.7
        self.rect.y -= self.velocity * 0.7
        self.left = False
        self.right = True

    def move_upleft(self):
        """Up Left movement"""
        self.rect.x -= self.velocity * 0.7
        self.rect.y -= self.velocity * 0.7
        self.left = True
        self.right = False

    def move_downright(self):
        """Down Right movement"""
        self.rect.x += self.velocity * 0.7
        self.rect.y += self.velocity * 0.7
        self.left = False
        self.right = True

    def move_downleft(self):
        """Down Left movement"""
        self.rect.x -= self.velocity * 0.7
        self.rect.y += self.velocity * 0.7
        self.left = True
        self.right = False

    def move_right(self):
        """Right movement"""
        self.rect.x += self.velocity
        self.left = False
        self.right = True

    def move_left(self):
        """Left movement"""
        self.rect.x -= self.velocity
        self.left = True
        self.right = False

    def move_up(self):
        """Up movement"""
        self.rect.y -= self.velocity
        self.left = False
        self.right = False

    def move_down(self):
        """Down movement"""
        self.rect.y += self.velocity
        self.left = False
        self.right = False

    def slow_player(self):
        """Slows the player by modifing velocity"""

        self.velocity = self.slow_velocity

    def normal_velocity(self):
        """Re initializes base velocity"""

        self.velocity = self.max_velocity

    def check_player_collision(self):
        """checks all collisions between player and sprites"""
        if self.game.check_collision_player(self.game.all_enemies) or self.game.check_collision_player(
                self.game.all_enemy_bullets):
            self.health -= 1
            return True
        else:
            return False

    def place_player(self):
        """sets base position"""
        self.rect.x = self.game.real_width / 2
        self.rect.y = self.game.height / 2

    def use_bomb(self):
        if self.nb_bomb > 0:
            self.nb_bomb -= 1
            return True
        return False

    def get_bomb(self):
        return self.nb_bomb

    def draw(self, screen):
        """draws the player's sprite and animates it"""
        if self.game.is_immune:
            if self.game.immune_count % 2 == 0:
                if self.left:
                    screen.blit(
                        self.walkLeft[self.game.walkCount // self.game.number_frames], self.rect)
                    self.game.walkCount += 1
                elif self.right:
                    screen.blit(
                        self.walkRight[self.game.walkCount // self.game.number_frames], self.rect)
                    self.game.walkCount += 1
                else:
                    screen.blit(
                        self.standing[self.game.walkCount // self.game.number_frames], self.rect)
                    self.game.walkCount += 1
        else:
            if self.left:
                screen.blit(
                    self.walkLeft[self.game.walkCount // self.game.number_frames], self.rect)
                self.game.walkCount += 1
            elif self.right:
                screen.blit(
                    self.walkRight[self.game.walkCount // self.game.number_frames], self.rect)
                self.game.walkCount += 1
            else:
                screen.blit(
                    self.standing[self.game.walkCount // self.game.number_frames], self.rect)
                self.game.walkCount += 1

        if self.game.is_slow:
            pygame.draw.circle(screen, (0, 255, 0, 0.1), (
                self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2),
                self.hitbox + 7)
        if self.game.walkCount >= self.game.number_frames * len(self.walkLeft):
            self.game.walkCount = 0

    def init_movement(self):
        self.left = False
        self.right = False
