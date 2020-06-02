import sys

import numpy
import pygame

from Enemy_bullet_pattern import *
from Player import *
from Enemy import *
from Stats import *
from Enemy_pattern import *
from Game import *
from Enemies.Little_UFO import *


class Stage01(Game):

    def __init__(self):
        super().__init__()

    def update(self, screen):
        self.script_0()
        self.skelet(screen)

    def script_0(self):
        if not self.is_paused:
            for enemies in self.all_enemies:
                simple_move(self, enemies)
                if self.time % 80 == 0:
                    bulletpattern_circle(self, enemies, 5, 30, 'assets/enemies/circle.png')
                            
            if self.time % 80 == 0:
                self.spawn_enemy(Little_UFO, 0, 20, 1, 0, random.randint(3, 9))