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
        x1 = [0, 400, 400, 200, 200, 400, 800]
        y1 = [100, 100, 200, 200, 100, 100, 100]
        t1 = [0, 20, 40, 60, 80, 100, 120]
        if not self.is_paused:
            for enemies in self.all_enemies:
                if self.time % 20 == 0:
                    bulletpattern_curve(enemies, 'assets/enemies/enbullet1.png')

            if self.time % 80 == 0:
                self.spawn_enemy(Little_UFO, lagcurve_gen, x=x1, y=y1, t=t1, time=0)
