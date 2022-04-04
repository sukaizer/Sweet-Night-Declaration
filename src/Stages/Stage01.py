from Enemies.Little_UFO import *
from Enemy_bullet_pattern import *
from Game import *


class Stage01(Game):

    def __init__(self, width, height):
        super().__init__(width, height)

    def update(self, screen):
        self.script_0()
        self.main_loop(screen)

    def script_0(self):
        poingne = [(0, 100, 0), (400, 100, 10), (400, 800, 11), (800, 200, 80),
                   (800, 200, 81), (800, 400, 130), (600, 400, 131), (400, 600, 180)]
        if not self.is_paused:
            for enemies in self.all_enemies:
                if self.time % 20 == 0:
                    bulletpattern_curve(
                        enemies, '../assets/enemies/enbullet1.png')

            if self.time % 80 == 0:
                self.spawn_enemy(Little_UFO, bezier_curve,
                                 X=poingne, degree=3, time=0)
