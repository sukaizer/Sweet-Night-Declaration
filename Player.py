import pygame
from Game import *
from Player_bullets import *


class Player(pygame.sprite.Sprite):
    """Classe représentant le joueur"""

    def __init__(self, game):
        """Constructeur de classe"""

        super().__init__()
        self.game = game
        self.nb_bomb = 0
        self.health = 3
        self.max_health = 3
        self.attack = 20
        self.max_velocity = 8  # pixels
        self.velocity = 8
        self.slow_velocity = 4
        self.all_bullets = pygame.sprite.Group()
        self.image = pygame.image.load('assets/animated_sprites/d1.png')
        self.walkRight = [pygame.image.load('assets/animated_sprites/d1.png').convert_alpha(),
                          pygame.image.load('assets/animated_sprites/d2.png').convert_alpha(),
                          pygame.image.load('assets/animated_sprites/d3.png').convert_alpha(),
                          pygame.image.load('assets/animated_sprites/d4.png').convert_alpha(),
                          pygame.image.load('assets/animated_sprites/d5.png').convert_alpha(),
                          pygame.image.load('assets/animated_sprites/d6.png').convert_alpha(),
                          pygame.image.load('assets/animated_sprites/d7.png').convert_alpha(),
                          pygame.image.load('assets/animated_sprites/d8.png').convert_alpha()]
        self.walkLeft = [pygame.image.load('assets/animated_sprites/g1.png').convert_alpha(),
                         pygame.image.load('assets/animated_sprites/g2.png').convert_alpha(),
                         pygame.image.load('assets/animated_sprites/g3.png').convert_alpha(),
                         pygame.image.load('assets/animated_sprites/g4.png').convert_alpha(),
                         pygame.image.load('assets/animated_sprites/g5.png').convert_alpha(),
                         pygame.image.load('assets/animated_sprites/g6.png').convert_alpha(),
                         pygame.image.load('assets/animated_sprites/g7.png').convert_alpha(),
                         pygame.image.load('assets/animated_sprites/g8.png').convert_alpha()]
        self.standing = [pygame.image.load('assets/animated_sprites/m1.png').convert_alpha(),
                         pygame.image.load('assets/animated_sprites/m2.png').convert_alpha(),
                         pygame.image.load('assets/animated_sprites/m3.png').convert_alpha(),
                         pygame.image.load('assets/animated_sprites/m4.png').convert_alpha(),
                         pygame.image.load('assets/animated_sprites/m5.png').convert_alpha(),
                         pygame.image.load('assets/animated_sprites/m6.png').convert_alpha(),
                         pygame.image.load('assets/animated_sprites/m7.png').convert_alpha(),
                         pygame.image.load('assets/animated_sprites/m8.png').convert_alpha()]
        self.rect = self.image.get_rect()
        self.rect.x = self.game.real_width / 2
        self.rect.y = self.game.height / 2
        self.hitbox = self.rect.width // 25  # rayon
        self.time_bullet = 0

    def shoot(self):
        self.all_bullets.add(PlayerBullet(self, self.game, self.attack))

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

        self.velocity = self.slow_velocity

    def normal_velocity(self):
        """Redonne au joueur sa vitesse de base"""

        self.velocity = self.max_velocity

    def check_player_collision(self):
        if self.game.check_collision_player(self.game.all_enemies) or self.game.check_collision_player(self.game.all_enemy_bullets):
            self.health -= 1
            return True
        else:
            return False

    def place_player(self):
        self.rect.x = self.game.real_width / 2
        self.rect.y = self.game.height / 2
