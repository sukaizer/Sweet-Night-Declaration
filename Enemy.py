import pygame
import random
import numpy as np
from Enemy_bullet import *
from Enemy_bullet_pattern import *


class Enemy(pygame.sprite.Sprite):
    """Classe représentant les ennemis"""

    def __init__(self, game, x, y, vx, vy, velocity):
        """Constructeur de classe"""

        super().__init__()
        self.game = game
        self.health = 30
        self.max_health = 30
        self.velocity = velocity
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy

    def move(self):
        self.rect.x += self.velocity * self.vx
        self.rect.y += self.velocity * self.vy

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
    def create_bullet(self, asset):
        self.game.all_enemy_bullets.add(EnemyBullet(self.game, asset, self.f1, a= random.random() * 2 * np.pi, b= random.random() * 2 * np.pi, xx=self.rect.x, yy=self.rect.y,  time=50))

    def f1(self, a, b, xx, yy, time):
        return xx + time*np.cos(a), yy +time*np.sin(b)