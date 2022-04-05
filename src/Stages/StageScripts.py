from Enemies.Little_UFO import *
from EnemyBulletPattern import *
from Game import *


def script_0(game):
    poingne = [(0, 100, 0), (400, 100, 10), (400, 800, 11), (800, 200, 80),
               (800, 200, 81), (800, 400, 130), (600, 400, 131), (400, 600, 180)]
    if not game.is_paused:
        for enemies in game.all_enemies:
            if game.time % 20 == 0:
                bulletpattern_curve(
                    enemies, '../assets/enemies/enbullet1.png')

        if game.time % 80 == 0:
            game.spawn_enemy(Little_UFO, bezier_curve,
                             X=poingne, degree=3, time=0)


scripts = [script_0]
