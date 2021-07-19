import pygame
import numpy as np


class EnemyBullet(pygame.sprite.Sprite):

    def __init__(self, game, asset, fun, **kwargs):
        super().__init__()
        self.game = game
        self.image = pygame.image.load(asset).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.fun = fun
        self.args = kwargs

    def move(self):
        self.args["time"] += 0.1
        self.rect.x, self.rect.y = self.fun(**self.args)
        

    def setAngle(self, angle):
        self.angle = angle

    def remove(self):
        self.game.all_enemy_bullets.remove(self)
