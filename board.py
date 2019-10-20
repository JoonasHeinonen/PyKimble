import pygame
import random

class Board(object):

    incer = 110

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, win):
        # Circle Path
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), 260)
        # Circle Path Bordering
        pygame.draw.circle(win, (240, 240, 0), (self.x, self.y), 220)
        pygame.draw.circle(win, (0, 150, 255), (self.x, self.y), 210)
        # Circle including the dice added with the white background
        pygame.draw.rect(win, (255, 255, 255), (290, 270 , (220), 161))
        # Fill
        pygame.draw.rect(win, (255, 255, 255), (293, 267 , (216), 167))
        pygame.draw.rect(win, (255, 255, 255), (295, 265 , (212), 171))
        pygame.draw.rect(win, (255, 255, 255), (297, 263 , (207), 175))
        pygame.draw.rect(win, (255, 255, 255), (300, 260 , (202), 181))
        pygame.draw.rect(win, (255, 255, 255), (302, 258 , (197), 185))
        pygame.draw.rect(win, (255, 255, 255), (305, 255 , (192), 191))
        pygame.draw.rect(win, (255, 255, 255), (307, 253 , (187), 195))
        pygame.draw.rect(win, (255, 255, 255), (310, 250 , (182), 201))
        pygame.draw.rect(win, (255, 255, 255), (313, 247 , (176), 206))
        pygame.draw.rect(win, (255, 255, 255), (315, 245 , (172), 211))
        pygame.draw.rect(win, (255, 255, 255), (318, 242 , (166), 216))
        # Fill ends here
        pygame.draw.rect(win, (255, 255, 255), (320, 240 , (162), 220))
        pygame.draw.circle(win, (240, 240, 0), (self.x, self.y), 80)
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), 80, 1)
        # Lines        
        pygame.draw.line(win, (0, 0, 0), (self.x - 110, 160 + self.incer), (self.x - 110, 320 + self.incer), 2)
        pygame.draw.line(win, (0, 0, 0), (self.x + 110, 160 + self.incer), (self.x + 110, 320 + self.incer), 2)
        pygame.draw.line(win, (0, 0, 0), (self.x - 80, 130 + self.incer), (self.x + 80, 130 + self.incer), 2)
        pygame.draw.line(win, (0, 0, 0), (self.x - 80, 350 + self.incer), (self.x + 80, 350 + self.incer), 2)
        # Corners @1
        pygame.draw.line(win, (0, 0, 0), (self.x - 110, 160 + self.incer), (self.x - 80, 130 + self.incer), 2)
        pygame.draw.line(win, (0, 0, 0), (self.x + 110, 160 + self.incer), (self.x + 80, 130 + self.incer), 2)
        # Corners @2
        pygame.draw.line(win, (0, 0, 0), (self.x - 110, 320 + self.incer), (self.x - 80, 350 + self.incer), 2)
        pygame.draw.line(win, (0, 0, 0), (self.x + 110, 320 + self.incer), (self.x + 80, 350 + self.incer), 2)

        # Finish Lines
        pygame.draw.line(win, (0, 0, 0), (self.x, 350 + self.incer * 2), (self.x, 350 + self.incer), 28)
        pygame.draw.line(win, (0, 0, 0), (self.x, 350 - self.incer * 2), (self.x, 350 - self.incer), 28)
        pygame.draw.line(win, (0, 0, 0), ((400 - self.incer * 2), self.y), (self.x - 110, self.y), 28)
        pygame.draw.line(win, (0, 0, 0), ((400 + self.incer * 2), self.y), (self.x + 110, self.y), 28)
        pygame.draw.rect(win, (0, 0, 0), (314, 610 , (170), 40)) # First team spawn
        pygame.draw.rect(win, (0, 0, 0), (314, 50, (170), 40)) # Second team spawn


        # pygame.draw.line(win, (0, 0, 0), (self.x + 110, 160 + self.incer), (self.x + 110, 320 + self.incer), 9)