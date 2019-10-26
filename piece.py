import pygame
import sys

class Piece(object):
    moves = 0

    def __init__(self, index, x, y, color):
        self.index = index
        self.x =  x
        self.y = y
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), 16)
        pygame.draw.circle(win, self.color, (self.x, self.y), 14)
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), 12)
        pygame.draw.circle(win, self.color, (self.x, self.y), 10)

    def ilmoita_piece(self, piece):
        print("Piece: " + str(piece))

    def inc_moves(self, inc):
        self.moves += inc
        if (moves > 28):
            moves = 28

    def get_moves(self):
        return self.moves