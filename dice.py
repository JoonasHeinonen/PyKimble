import pygame
import random

class Dice(object):
    width = 60
    height = 60
    dotRadius = 6

    def __init__(self, x, y):
        self.x =  x
        self.y = y
        self.value = self.randValue()
        print(self.value)
    
    def draw(self, win):
        # pygame.draw.rect(win, (0, 0, 0), (self.x - 8, self.y - 8, (self.width + 16), self.height + 16))
        pygame.draw.rect(win, (255, 0, 0), (self.x - 8, self.y, (self.width + 16), self.height))
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y - 8, (self.width), self.height + 16))
        pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), 8)
        pygame.draw.circle(win, (255, 0, 0), (self.x + self.width, self.y), 8)
        pygame.draw.circle(win, (255, 0, 0), (self.x, self.y + self.height), 8)
        pygame.draw.circle(win, (255, 0, 0), (self.x + self.width, self.y + self.height), 8)
        if (self.value == 1):
            pygame.draw.circle(win, (255, 255, 255), (self.x + 30, self.y + 30), self.dotRadius)
        elif (self.value == 2):
            pygame.draw.circle(win, (255, 255, 255), (self.x + 15, self.y + 15), self.dotRadius)
            pygame.draw.circle(win, (255, 255, 255), (self.x + 45, self.y + 45), self.dotRadius)
        elif (self.value == 3):
            pygame.draw.circle(win, (255, 255, 255), (self.x + 10, self.y + 10), self.dotRadius)
            pygame.draw.circle(win, (255, 255, 255), (self.x + 30, self.y + 30), self.dotRadius)
            pygame.draw.circle(win, (255, 255, 255), (self.x + 50, self.y + 50), self.dotRadius)
        elif (self.value == 4):
            pygame.draw.circle(win, (255, 255, 255), (self.x + 10, self.y + 10), self.dotRadius)
            pygame.draw.circle(win, (255, 255, 255), (self.x + 10, self.y + 50), self.dotRadius)
            pygame.draw.circle(win, (255, 255, 255), (self.x + 50, self.y + 50), self.dotRadius)
            pygame.draw.circle(win, (255, 255, 255), (self.x + 50, self.y + 10), self.dotRadius)
        elif (self.value == 5):
            pygame.draw.circle(win, (255, 255, 255), (self.x + 10, self.y + 10), self.dotRadius)
            pygame.draw.circle(win, (255, 255, 255), (self.x + 10, self.y + 50), self.dotRadius)
            pygame.draw.circle(win, (255, 255, 255), (self.x + 30, self.y + 30), self.dotRadius)
            pygame.draw.circle(win, (255, 255, 255), (self.x + 50, self.y + 50), self.dotRadius)
            pygame.draw.circle(win, (255, 255, 255), (self.x + 50, self.y + 10), self.dotRadius)
        elif (self.value == 6):
            pygame.draw.circle(win, (255, 255, 255), (self.x + 10, self.y + 10), self.dotRadius)
            pygame.draw.circle(win, (255, 255, 255), (self.x + 10, self.y + 30), self.dotRadius)
            pygame.draw.circle(win, (255, 255, 255), (self.x + 10, self.y + 50), self.dotRadius)
            pygame.draw.circle(win, (255, 255, 255), (self.x + 50, self.y + 10), self.dotRadius)
            pygame.draw.circle(win, (255, 255, 255), (self.x + 50, self.y + 30), self.dotRadius)
            pygame.draw.circle(win, (255, 255, 255), (self.x + 50, self.y + 50), self.dotRadius)

    def randValue(self):
        rand = random.randrange(1, 7)
        return rand