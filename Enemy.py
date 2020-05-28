import pygame
import random


class Enemy(pygame.sprite.Sprite):
    """Classe représentant les ennemis"""

    def __init__(self, game):
        """Constructeur de classe"""

        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.velocity = random.randint(3, 9)
        self.image = pygame.image.load("assets/enemies/enemy1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 50)
        self.rect.y = 50
        self.left_to_right = bool(random.getrandbits(1))

    def remove(self):
        """Enlève l'ennemi (self) du groupe d'ennemis"""
        self.game.all_enemies.remove(self)

    def simple_move(self):
        """Effectue un mouvement vertical simple de l'ennemi"""

        if self.left_to_right:
            if self.rect.x < self.game.real_width - (self.rect.width + self.velocity):
                self.rect.x += self.velocity
            else:
                self.left_to_right = False
        else:
            if self.rect.x > self.velocity:
                self.rect.x -= self.velocity
            else:
                self.left_to_right = True

    def damage(self, amount):
        self.game.hitSound.play()
        self.health -= amount
        if self.health <= 0:
            self.remove()
