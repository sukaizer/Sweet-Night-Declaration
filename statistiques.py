import pygame


class Stats:

    def __init__(self, game, player):
        self.player = player
        self.game = game
        self.stats = pygame.image.load('assets/Stats.png')

    def start_menu(self, screen):
        screen.blit(self.stats, (self.game.real_width, 0))
