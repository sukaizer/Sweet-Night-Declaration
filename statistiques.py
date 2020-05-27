import pygame


class Stats:

    def __init__(self, game, player):
        self.player = player
        self.game = game
        self.stats = pygame.image.load('assets/Stats.png')
        self.lp = pygame.image.load('assets/player.png')
        self.lp = pygame.transform.scale(self.lp, (40, 40))
        self.lp_rect1 = self.lp.get_rect()
        self.lp_rect2 = self.lp.get_rect()
        self.lp_rect3 = self.lp.get_rect()
        self.lp_rect1.x = self.game.real_width + 10
        self.lp_rect2.x = self.game.real_width + (self.game.width - self.game.real_width) / 2 - self.lp_rect2.width / 2
        self.lp_rect3.x = self.game.width - (10 + self.lp_rect3.width)
        self.lp_rect1.y = self.game.height / 2
        self.lp_rect2.y = self.game.height / 2
        self.lp_rect3.y = self.game.height / 2

    def stat_menu(self, screen):
        screen.blit(self.stats, (self.game.real_width, 0))
        self.life_points(screen)

    def life_points(self, screen):
        if self.player.health == 3:
            screen.blit(self.lp, self.lp_rect1)
            screen.blit(self.lp, self.lp_rect2)
            screen.blit(self.lp, self.lp_rect3)
        elif self.player.health == 2:
            screen.blit(self.lp, self.lp_rect1)
            screen.blit(self.lp, self.lp_rect2)
        else:
            screen.blit(self.lp, self.lp_rect1)
