import pygame
import random
from Enemy_bullet import *


class Enemy(pygame.sprite.Sprite):
    """Classe représentant les ennemis"""

    def __init__(self, game, x, y, vx, vy, velocity):
        """Constructeur de classe"""

        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.velocity = velocity
        self.image = pygame.image.load("assets/enemies/enemy1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy
        self.velocity = velocity

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

    def create_bullet(self, x, y, angle, v, asset):
        self.game.all_enemy_bullets.add(EnemyBullet(self.game, x, y, angle, v, asset))

    def create_bullet(self, x, y, angle, v, cooldown, asset):
        if self.game.time % cooldown == 0:
            self.game.all_enemy_bullets.add(EnemyBullet(self.game, x, y, angle, v, asset))
