from Enemies.Little_UFO import *
from Enemy_bullet_pattern import *
from Game import *


class Stage01(Game):

    def __init__(self, width, height):
        super().__init__(width, height)

    def update(self, screen):
        self.script_0()
        self.skelet(screen)

    def script_0(self):
        if not self.is_paused:
            for enemies in self.all_enemies:
                simple_move(self, enemies)
                if self.time % 80 == 0:
                    bulletpattern_curve(enemies, 'assets/enemies/circle.png')

            if self.time % 80 == 0:
                self.spawn_enemy(Little_UFO, 0, 20, 1, 0, random.randint(3, 9))
