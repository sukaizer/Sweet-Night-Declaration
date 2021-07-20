from Enemy import *

class Little_UFO(Enemy):

    def __init__(self, game, fun, **kwargs):
        super().__init__(game, fun, **kwargs)
        self.image = pygame.image.load("assets/enemies/little_ufo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.health = 1
        self.max_health = 1