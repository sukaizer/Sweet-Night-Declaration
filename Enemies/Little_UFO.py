from Enemy import *

class Little_UFO(Enemy):

    def __init__(self, game, x, y, vx, vy, velocity):
        super().__init__(game, x, y, vx, vy, velocity)
        self.image = pygame.image.load("assets/enemies/little_ufo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 1
        self.max_health = 1