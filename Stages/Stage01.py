import sys

import numpy
import pygame

from Enemy_bullet_pattern import *
from Player import *
from Enemy import *
from Stats import *
from Enemy_pattern import *
from Game import *


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
                enemies.create_bullet(enemies.rect.x, enemies.rect.y, bullet_to_player(self, enemies), 5, 20,
                                      'assets/enemies/circle.png')
            if self.time % 80 == 0:
                self.all_enemies.add(Enemy(self, 0, 20, 1, 0, random.randint(3, 9)))
