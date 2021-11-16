import pygame
import numpy as np
from Enemy import *
from Game import *
from Enemy_bullet_pattern import *
import random


def enemy_to_player(game, enemy):
    return direction(enemy.rect.x, enemy.rect.y, game.player.rect.x, game.player.rect.y)


def direction(x1, y1, x2, y2):
    x = x1 - x2
    y = y1 - y2
    return x / np.sqrt(x ** 2 + y ** 2), y / np.sqrt(x ** 2 + y ** 2)


def simple_move(game, enemy):
    """Effectue un mouvement vertical simple de l'ennemi"""
    if enemy.vx <= 0 and enemy.rect.x < 10:
        enemy.set_move(1, np.sin(game.time), enemy.velocity)
    if enemy.vx > 0 and enemy.rect.x > game.real_width:
        enemy.set_move(-1, np.sin(game.time), enemy.velocity)


