import pygame
import sys
import time
from board import Board
from dice import Dice
from button import Button
from place import Place
from piece import Piece

pygame.init()
win = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Kimble")

clock = pygame.time.Clock()

board = Board(400, 350)
dice = Dice(370, 320)
rolled = 0
startButtonColor = (0, 255, 0)
startButtonClicked = (0, 155, 0)
startButton = Button (startButtonColor, 370, 434, 60, 20, "Roll!", 18, 4)
turnButton = Button(startButtonColor, 10, 670, 60, 20, "Turn!", 18, 4)

# Arena
place0 = Place(360, 587, (120, 120, 120))
place1 = Place(290, 562, (120, 120, 120))
place2 = Place(235, 522, (120, 120, 120))
place3 = Place(195, 477, (120, 120, 120))
place4 = Place(195, 437, (120, 120, 120))
place23 = Place(615, 437, (120, 120, 120))
place24 = Place(605, 477, (120, 120, 120))
place25 = Place(565, 522, (120, 120, 120))
place26 = Place(440, 587, (120, 120, 120))
place27 = Place(510, 562, (120, 120, 120))

places = [place0, place1, place2, place3, place4, place23, place24, place25, place26, place27]

# Blue player's end places and pieces
blueEnd0 = Place(400, 480, (0, 0, 255))
blueEnd1 = Place(400, 505, (0, 0, 255))
blueEnd2 = Place(400, 530, (0, 0, 255))
blueEnd3 = Place(400, 555, (0, 0, 255))
blueEndPlaces = [blueEnd0, blueEnd1, blueEnd2, blueEnd3]

bluePiece0 = Piece(345, 70, (0, 0, 255))
bluePiece1 = Piece(380, 70, (0, 0, 255))
bluePiece2 = Piece(415, 70, (0, 0, 255))
bluePiece3 = Piece(450, 70, (0, 0, 255))
bluePieces = [bluePiece0, bluePiece1, bluePiece2, bluePiece3]

# Red player's end places and pieces
redEnd0 = Place(400, 150, (255, 0, 0))
redEnd1 = Place(400, 175, (255, 0, 0))
redEnd2 = Place(400, 200, (255, 0, 0))
redEnd3 = Place(400, 225, (255, 0, 0))
redEndPlaces = [redEnd0, redEnd1, redEnd2, redEnd3]

redPiece0 = Piece(345, 630, (255, 0, 0))
redPiece1 = Piece(380, 630, (255, 0, 0))
redPiece2 = Piece(415, 630, (255, 0, 0))
redPiece3 = Piece(450, 630, (255, 0, 0))
redPieces = [redPiece0, redPiece1, redPiece2, redPiece3]

def redrawGameWindow():
    win.fill((255, 255, 255))
    board.draw(win)
    dice.draw(win)
    startButton.draw(win)
    turnButton.draw(win)
    for place in places:
        place.draw(win)
    for place in blueEndPlaces:
        place.draw(win)
    for place in redEndPlaces:
        place.draw(win)
    for piece in bluePieces:
        piece.draw(win)
    for piece in redPieces:
        piece.draw(win)
    pygame.display.update()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    """ Button activity """
    cur = pygame.mouse.get_pos()
    if startButton.x + startButton.width > cur[0] > startButton.x and startButton.y + startButton.height > cur[1] > startButton.y:
        startButton.setColor((0, 200, 0))
        if (rolled == 0):
            if pygame.mouse.get_pressed()[0]:
                rolled = 1
                startButton.setColor(startButtonClicked)
                newNumber = dice.randValue()
                print(newNumber)
                dice.setValue(newNumber)
                dice.drawDots(win, newNumber)
    else:
        startButton.setColor(startButtonColor)

    if turnButton.x + turnButton.width > cur[0] > turnButton.x and turnButton.y + turnButton.height > cur[1] > turnButton.y:
        turnButton.setColor((0, 200, 0))
        if (rolled == 1):
            if pygame.mouse.get_pressed()[0]:
                rolled = 0
                turnButton.setColor(startButtonClicked)
    else:
        turnButton.setColor(startButtonColor)
    """ Button activity ends here """

    redrawGameWindow()

pygame.quit()