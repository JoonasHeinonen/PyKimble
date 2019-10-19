import pygame
import sys
from dice import Dice

pygame.init()
win = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Kimble")

clock = pygame.time.Clock()

dice = Dice(290, 210)

def redrawGameWindow():
    win.fill((255, 255, 255))
    dice.draw(win)
    pygame.display.update()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.time.delay(50)
    redrawGameWindow()

pygame.quit()