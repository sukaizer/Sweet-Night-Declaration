from ast import arg
from mimetypes import init
import pygame


class Text:
    """
    Class used to simplify text rendering
    Use pygame.font.Font for custom fonts, or SysFont
    """

    def __init__(self, text_value, font_string, font_size, color, origin):
        self.text_value = text_value
        self.font_string = font_string
        self.font_size = font_size
        self.color = color
        self.origin = origin

        self.font = pygame.font.Font(self.font_string, self.font_size)
        self.text = self.font.render(self.text_value, True, self.color)

    def set_color(self, color):
        self.color = color
        self.text = self.font.render(self.text_value, True, self.color)

    def draw(self, *args):
        if len(args) == 2 and isinstance(args[1], tuple):
            self.color = args[1]
        self.text = self.font.render(self.text_value, True, self.color)
        args[0].blit(self.text, self.origin)

    def set_text(self, text_value):
        self.text_value = text_value
        self.text = self.font.render(self.text_value, True, self.color)
