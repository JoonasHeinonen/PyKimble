import pygame
import sys

pygame.init()

class Button(object):

    font = pygame.font.SysFont("arial", 12)

    def __init__(self, color, x, y, width, height, string, intenderx, intendery):
        self.color = color
        self.x =  x
        self.y = y
        self.width = width
        self.height = height
        self.string = string
        self.intenderx = intenderx
        self.intendery = intendery
        self.text = self.font.render(string, True, (0, 0, 0))
    
    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y , (self.width), self.height))
        pygame.draw.rect(win, self.color, (self.x + 1, self.y + 1, (self.width - 2), self.height - 2))
        win.blit(self.text, (self.x + self.intenderx, self.y + self.intendery))

    def setColor(self, color):
        self.color = color