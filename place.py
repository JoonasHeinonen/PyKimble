import pygame
import sys

class Place(object):

    font = pygame.font.SysFont("arial", 12)

    def __init__(self, string, red_index, blue_index, x, y, color):
        self.string = string
        self.red_index = red_index
        self.blue_index = blue_index
        self.x =  x
        self.y = y
        self.color = color
        self.text = self.font.render(string, True, (255, 255, 255))

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), 12)
        pygame.draw.circle(win, self.color, (self.x, self.y), 10)
        if (len(self.string) > 1):
            win.blit(self.text, (self.x - 7, self.y - 6))
        else:
            win.blit(self.text, (self.x - 3, self.y - 6))