import pygame
import numpy as np

class EnemyBullet(pygame.sprite.Sprite):

    def __init__(self, game, x, y, angle, v, asset):
        super().__init__()
        self.game = game
        self.image = pygame.image.load(asset).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = angle
        self.v = v

    def move(self):
        self.rect.x += self.v*np.cos(self.angle)
        self.rect.y += self.v*np.sin(self.angle)

    def setAngle(self, angle):
        self.angle = angle
        
    