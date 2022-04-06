import pygame
import random
import numpy as np
from EnemyBullet import *
from EnemyBulletPattern import *
from Emitter import *


class Enemy(Emitter):
    """Class representing all enemies"""

    def __init__(self, game, fun, **kwargs):
        """Class constructor"""

        super().__init__(game, fun, **kwargs)
        self.game = game
        self.health = 30
        self.max_health = 30
        self.fun = fun
        self.args = kwargs

    def move(self):
        self.args["time"] += 1
        self.rect.x, self.rect.y = self.fun(**self.args)

    def remove(self):
        """removes the current enemy from the group"""
        self.game.all_enemies.remove(self)
        super().remove()

    def add(self):
        self.game.all_enemies.add(self)
        super().add()

    def set_move(self, vx, vy, velocity):
        self.vx = vx
        self.vy = vy
        self.velocity = velocity

    def damage(self, amount):
        # the sound is very loud !
        self.game.hit_sound.play()
        self.health -= amount
        if self.health <= 0:
            self.remove()
