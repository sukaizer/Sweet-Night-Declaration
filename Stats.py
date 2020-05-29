import pygame


class Stats:

    def __init__(self, game, player):
        self.player = player
        self.game = game
        self.stats = pygame.image.load('assets/Stats.png').convert_alpha()
        self.stats = pygame.transform.scale(self.stats, (int(self.game.width - self.game.real_width), 980))
        self.lp = pygame.image.load('assets/char_life.png').convert_alpha()
        self.lp = pygame.transform.scale(self.lp, (80, 80))
        self.lp_rect1 = self.lp.get_rect()
        self.lp_rect2 = self.lp.get_rect()
        self.lp_rect3 = self.lp.get_rect()
        self.lp_rect1.x = self.game.real_width + 10
        self.lp_rect2.x = self.game.real_width + (self.game.width - self.game.real_width) / 2 - self.lp_rect2.width / 2
        self.lp_rect3.x = self.game.width - (10 + self.lp_rect3.width)
        self.lp_rect1.y = self.game.height / 2
        self.lp_rect2.y = self.game.height / 2
        self.lp_rect3.y = self.game.height / 2

        self.bomb = pygame.image.load('assets/bomb.png').convert_alpha()
        self.bomb1 = self.bomb.get_rect()
        self.bomb2 = self.bomb.get_rect()
        self.bomb3 = self.bomb.get_rect()
        self.bomb1.x = self.game.real_width + 10
        self.bomb2.x = self.game.real_width + (self.game.width - self.game.real_width) / 2 - self.lp_rect2.width / 2
        self.bomb3.x = self.game.width - (10 + self.lp_rect3.width)
        self.bomb1.y = 2 * self.game.height / 3
        self.bomb2.y = 2 * self.game.height / 3
        self.bomb3.y = 2 * self.game.height / 3

    def stat_menu(self, screen):
        screen.blit(self.stats, (self.game.real_width, 0))
        self.life_points(screen)
        self.bombs(screen)

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

    def bombs(self, screen):
        if self.player.nb_bomb == 3:
            screen.blit(self.bomb, self.bomb1)
            screen.blit(self.bomb, self.bomb2)
            screen.blit(self.bomb, self.bomb3)
        elif self.player.nb_bomb == 2:
            screen.blit(self.bomb, self.bomb1)
            screen.blit(self.bomb, self.bomb2)
        else:
            screen.blit(self.bomb, self.bomb1)
