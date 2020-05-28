import pygame


class PlayerBullet(pygame.sprite.Sprite):

    def __init__(self, player, game):
        super().__init__()
        self.player = player
        self.game = game
        self.velocity = 45
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.rect.width / 2 - self.rect.width/2
        self.rect.y = player.rect.y - 5

    def remove(self):
        self.player.all_bullets.remove(self)

    def move(self):
        self.rect.y -= self.velocity

        for enemies in self.game.check_collision(self, self.game.all_enemies):
            self.remove()
            enemies.damage(self.player.attack)

        if self.rect.y < 0:
            # on supprime le sprite s'il sort de l'ecran
            self.remove()
