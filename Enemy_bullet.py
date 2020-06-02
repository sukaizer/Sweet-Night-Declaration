import pygame
import numpy as np


class EnemyBullet(pygame.sprite.Sprite):

    def __init__(self, game, x, y, angle, v, asset):
        super().__init__()
        self.game = game
        self.image = pygame.image.load(asset).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.fx = x
        self.fy = y
        self.angle = angle
        print(angle)
        self.v = v
        self.bullet_time = 0

    def move(self):
        self.rect.x = self.fx + np.cos(self.angle) * self.v * self.bullet_time 
        self.rect.y = self.fy + np.sin(self.angle) * self.v * self.bullet_time
        self.bullet_time += 1
        

    def setAngle(self, angle):
        self.angle = angle

    def remove(self):
        self.game.all_enemy_bullets.remove(self)
