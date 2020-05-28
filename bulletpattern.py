import pygame
import numpy as np
from enemy import *
from game import *
import random


def enemyToPlayer(game, enemy):
    return direction(enemy.rect.x, enemy.rect.y, game.player.rect.x, game.player.rect.y)

def direction(x1, y1, x2, y2):
    line = np.array([1,0])
    d = np.array([x2-x1, y2-y1])
    angle = np.arctan2(d[1] - line[1], d[0] -line[0])
    return angle

def bulletPattern0():
    """bullet shot randomly"""
    angle = random.random()*2*np.pi
    return angle
