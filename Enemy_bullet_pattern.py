import pygame
import numpy as np
from Enemy import *
from Game import *
import random


def bullet_to_player(game, enemy):
    return angle_direction(enemy.rect.x + enemy.rect.width/2, enemy.rect.y + enemy.rect.height/2, game.player.rect.x + game.player.rect.width/2, game.player.rect.y + game.player.rect.height/2)


def angle_direction(x1, y1, x2, y2):
    line = np.array([1, 0])
    d = np.array([x2 - x1, y2 - y1])
    angle = np.arctan2(d[1] - line[1], d[0] - line[0])
    return angle


"""
param equations
"""
def f1(a, b, xx, yy, time):
    return xx + 5*time*np.cos(a*time*0.01), yy + 5*time*np.sin(b*time*0.01)


"""
lagrange interpolation to generate curve passing by array of points
- x is array for x coordinates
- y is array for y coordinates
- t is array to indicate the time the curve reach each coordinate 
"""
def lagcurve_gen(x, y, t, time):
    poly = np.ones(len(x))
    xaxis = 0
    yaxis = 0
    for i in range(len(poly)):
        for j in range(len(poly)):
            if i != j:
                poly[i] *= (time-t[j])/(t[i]-t[j])
        xaxis += x[i]*poly[i]
        yaxis += y[i]*poly[i]
    return xaxis, yaxis




def bulletPattern0():
    """bullet shot randomly"""
    angle = random.random() * 2 * np.pi
    return angle


aa = [300, 350, 250, 300, 350, 250]
bb = [100, 200, 300, 400, 500, 600]
tt = [0, 5, 10, 15, 20, 25]

def shift_table(tab, r):
    r = random.randint(-r, r)
    newTab = []
    for i in range(len(tab)):
        newTab.append(tab[i] + r)
    return newTab


def bulletpattern_player(stage, enemy, v, cooldown, asset):
    if stage.time % cooldown == 0:
        enemy.create_bullet(asset, f1, a= random.random() * 2 * np.pi, b= random.random() * 2 * np.pi, xx=enemy.rect.x, yy=enemy.rect.y,  time=0)

def bulletpattern_circle(stage, enemy, v, qtt, asset):
    for i in range(qtt):
        enemy.create_bullet(asset, f1, a= random.random() * 2 * np.pi, b= random.random() * 2 * np.pi, xx=enemy.rect.x, yy=enemy.rect.y,  time=0)
        
        
def bulletpattern_curve(enemy, asset):
    enemy.create_bullet(asset, lagcurve_gen, x=shift_table(aa,250), y= bb, t=tt, time=0)