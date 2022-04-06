from Enemies.Little_UFO import *
from Enemies.BasicEmitter import *
from EnemyBulletPattern import *
from Game import *


def script_0(game):
    tab0 = [(0, 100, 0), (400, 100, 10), (400, 800, 11), (800, 200, 80),
            (800, 200, 81), (800, 400, 130), (600, 400, 131), (400, 600, 180)]

    tab1 = [(0, 100, 0), (200, 100, 10), (900, 800, 11), (800, 200, 80),
            (800, 100, 81), (800, 400, 130), (600, 400, 131), (400, 600, 180)]
    if not game.is_paused:
        for emitter in game.all_emitters:
            if game.time % 20 == 0:
                if isinstance(emitter, Enemy):
                    bulletpattern_curve(
                        emitter, '../assets/enemies/enbullet1.png')
                else:
                    bulletpattern_curve(
                        emitter, '../assets/enemies/knofe.png')

        if game.time % 80 == 0:
            game.spawn_enemy(Little_UFO, bezier_curve,
                             X=tab0, degree=3, time=0)
            game.spawn_enemy(BasicEmitter, bezier_curve,
                             X=tab1, degree=1, time=0)


scripts = [script_0]
# think about removing the basic emitters after T time
