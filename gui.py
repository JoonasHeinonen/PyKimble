import pygame
import sys

class Gui(object):
    def __init__(self, color):
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (0, 650, 800, 50))

    def set_color(self, color):
        self.color = color