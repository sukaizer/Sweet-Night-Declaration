import pygame


class PlayerBullet(pygame.sprite.Sprite):

    def __init__(self, player, game, attack):
        super().__init__()
        self.player = player
        self.game = game
        self.velocity = 50
        self.image = pygame.image.load("../assets/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.rect.width / 2 - self.rect.width/2
        self.rect.y = player.rect.y - 5
        self.attack = attack

    def remove(self):
        self.player.all_bullets.remove(self)

    def move(self):
        self.rect.y -= self.velocity

        for enemies in self.game.check_collision(self, self.game.all_enemies):
            enemies.damage(self.attack)
            self.remove()
            