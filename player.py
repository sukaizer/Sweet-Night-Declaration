import pygame
from game import *
from bullets import Bullet


class Player(pygame.sprite.Sprite):
    """Classe représentant le joueur"""

    def __init__(self, game):
        """Constructeur de classe"""

        super().__init__()
        self.game = game
        self.health = 3
        self.max_health = 3
        self.attack = 5
        self.max_velocity = 10  # pixels
        self.velocity = 10
        self.all_bullets = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.game.real_width / 2
        self.rect.y = self.game.height / 2

    def shoot(self):
        self.all_bullets.add(Bullet(self, self.game))

    def move_right(self):
        """Permet de se déplacer vers la droite"""

        self.rect.x += self.velocity

    def move_left(self):
        """Permet de se déplacer vers la gauche"""

        self.rect.x -= self.velocity

    def move_up(self):
        """Permet de se déplacer vers le haut"""

        self.rect.y -= self.velocity

    def move_down(self):
        """Permet de se déplacer vers le bas"""

        self.rect.y += self.velocity

    def slow_player(self):
        """Ralentit le joueur pour permettre plus de précision"""

        self.velocity = 5

    def normal_velocity(self):
        """Redonne au joueur sa vitesse de base"""

        self.velocity = self.max_velocity
