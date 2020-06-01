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
        self.angle = angle
        print(angle)
        self.v = v

    def move(self):
        self.rect.x += np.cos(self.angle) * self.v
        self.rect.y += np.sin(self.angle) * self.v
        

    def setAngle(self, angle):
        self.angle = angle

    def remove(self):
        self.game.all_enemy_bullets.remove(self)
