import pygame
import sys

class Piece(object):
    def __init__(self, x, y, color):
        self.x =  x
        self.y = y
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), 16)
        pygame.draw.circle(win, self.color, (self.x, self.y), 14)
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), 12)
        pygame.draw.circle(win, self.color, (self.x, self.y), 10)