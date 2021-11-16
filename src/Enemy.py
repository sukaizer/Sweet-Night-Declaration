import pygame
import random
import numpy as np
from Enemy_bullet import *
from Enemy_bullet_pattern import *


class Enemy(pygame.sprite.Sprite):
    """Classe représentant les ennemis"""

    def __init__(self, game, fun, **kwargs):
        """Constructeur de classe"""

        super().__init__()
        self.game = game
        self.health = 30
        self.max_health = 30
        self.image = pygame.image.load("../assets/bullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.fun = fun
        self.args = kwargs

    def move(self):
        self.args["time"] += 1
        self.rect.x, self.rect.y = self.fun(**self.args)

    def remove(self):
        """Enlève l'ennemi (self) du groupe d'ennemis"""
        self.game.all_enemies.remove(self)

    def set_move(self, vx, vy, velocity):
        self.vx = vx
        self.vy = vy
        self.velocity = velocity

    def damage(self, amount):
        self.game.hitSound.play()
        self.health -= amount
        if self.health <= 0:
            self.remove()

    """
    when giving parametric equation, you need a named argument called time,
    for the other, you can give any number of them you want as long as you give them a name
    """
    def create_bullet(self, asset, fun , **kwargs):
        self.game.all_enemy_bullets.add(EnemyBullet(self.game, asset, fun, **kwargs))

