import pygame
import random
import numpy as np
from EnemyBullet import *
from EnemyBulletPattern import *


class Emitter(pygame.sprite.Sprite):
    """Class representing an emitter, used only for firing bullets"""

    def __init__(self, game, fun, **kwargs):
        """Class constructor"""
        super().__init__()
        self.game = game
        self.x = 0
        self.y = 0
        self.fun = fun
        self.args = kwargs

    def remove(self):
        """removes the current enemy from the group"""
        self.game.all_emitters.remove(self)

    def add(self):
        self.game.all_emitters.add(self)

    def set_move(self, vx, vy, velocity):
        self.vx = vx
        self.vy = vy
        self.velocity = velocity

    def create_bullet(self, asset, fun, **kwargs):
        """when giving parametric equation, you need a named argument called time,
        for the other, you can give any number of them you want as long as you give them a name"""
        self.game.all_enemy_bullets.add(
            EnemyBullet(self.game, asset, fun, **kwargs))
