import pygame
import sys
import time
from board import Board
from dice import Dice
from button import Button
from place import Place
from piece import Piece
from gui import Gui

pygame.init()
win = pygame.display.set_mode((800, 700))
pygame.display.set_caption("PyKimble")

clock = pygame.time.Clock()

board = Board(400, 350)
dice = Dice(370, 320)
maxMoves = 32
valueOfDice = 0
rolled = 0
startButtonColor = (0, 255, 0)
startButtonClicked = (0, 155, 0)
buttonOff = (60, 60, 60)
startButton = Button (startButtonColor, 370, 434, 60, 20, "Roll!", 18, 4)
turnButton = Button(startButtonColor, 10, 670, 60, 20, "Turn!", 18, 4)
buttons_off = False

# Arena
place0 = Place("1", 1, 15, 375, 589, (150, 60, 60))
place1 = Place("2", 2, 16, 330, 580, (120, 120, 120))
place2 = Place("3", 3, 17, 270, 552, (120, 120, 120))
place3 = Place("4", 4, 18, 230, 520, (120, 120, 120))
place4 =  Place("5", 5, 19, 197, 482, (120, 120, 120))
place5 = Place("6", 6, 20, 172, 425, (120, 120, 120))
place6 = Place("7", 7, 21, 162, 380, (120, 120, 120))
place7 = Place("8", 8, 22, 162, 322, (120, 120, 120))
place8 = Place("9", 9, 23, 172, 277, (120, 120, 120))  
place9 =  Place("10", 10, 24, 197, 222, (120, 120, 120)) 
place10 = Place("11", 11, 25, 230, 177, (120, 120, 120))
place11 = Place("12", 12, 26, 270, 147, (120, 120, 120))
place12 = Place("13", 13, 27, 330, 120, (120, 120, 120))
place13 = Place("14", 14, 28, 375, 112, (120, 120, 120))

place14 = Place("15", 15, 1, 425, 112, (60, 60, 150))
place15 = Place("16", 16, 2, 470, 120, (120, 120, 120))
place16 = Place("17", 17, 3, 530, 147, (120, 120, 120))
place17 = Place("18", 18, 4, 570, 177, (120, 120, 120))
place18 =  Place("19", 19, 5, 602, 222, (120, 120, 120)) 
place19 = Place("20", 20, 6, 627, 277, (120, 120, 120))  
place20 = Place("21", 21, 7, 638, 322, (120, 120, 120))
place21 = Place("22", 22, 8, 638, 380, (120, 120, 120))
place22 = Place("23", 23, 9, 627, 425, (120, 120, 120))
place23 =  Place("24", 24, 10, 602, 482, (120, 120, 120))
place24 = Place("25", 25, 11, 570, 520, (120, 120, 120))
place25 = Place("26", 26, 12, 530, 552, (120, 120, 120))
place26 = Place("27", 27, 13, 470, 580, (120, 120, 120))
place27 = Place("28", 28, 14, 425, 589, (120, 120, 120))

places = [place0, place1, place2, place3, place4, place5, place6, place7, place8, place9, place10, place11, place12, place13,
          place14, place15, place16, place17, place18, place19, place20, place21, place22, place23, place24, place25, place26,
          place27
         ]

# Blue player's end places and pieces
blueEnd0 = Place("Y", 33, 1000, 400, 150, (0, 0, 255))
blueEnd1 = Place("Y", 34, 1001, 400, 175, (0, 0, 255))
blueEnd2 = Place("Y", 35, 1002, 400, 200, (0, 0, 255))
blueEnd3 = Place("Y", 36, 1003, 400, 225, (0, 0, 255))
blueEndPlaces = [blueEnd0, blueEnd1, blueEnd2, blueEnd3]

piece_x = 345
reds_y = 630
blues_y = 70

bluePiece0 = Piece(0, piece_x + (35 * 0), blues_y, (0, 0, 255))
bluePiece1 = Piece(1, piece_x + (35 * 1), blues_y, (0, 0, 255))
bluePiece2 = Piece(2, piece_x + (35 * 2), blues_y, (0, 0, 255))
bluePiece3 = Piece(3, piece_x + (35 * 3), blues_y, (0, 0, 255))
bluePieces = [bluePiece0, bluePiece1, bluePiece2, bluePiece3]

# Red player's end places and pieces
redEnd0 = Place("X", 29, 1004, 400, 480, (255, 0, 0))
redEnd1 = Place("X", 30, 1005, 400, 505, (255, 0, 0))
redEnd2 = Place("X", 31, 1006, 400, 530, (255, 0, 0))
redEnd3 = Place("X", 32, 1007, 400, 555, (255, 0, 0))
redEndPlaces = [redEnd0, redEnd1, redEnd2, redEnd3]

redPiece0 = Piece(4, piece_x + (35 * 0), reds_y, (255, 0, 0))
redPiece1 = Piece(5, piece_x + (35 * 1), reds_y, (255, 0, 0))
redPiece2 = Piece(6, piece_x + (35 * 2), reds_y, (255, 0, 0))
redPiece3 = Piece(7, piece_x + (35 * 3), reds_y, (255, 0, 0))
redPieces = [redPiece0, redPiece1, redPiece2, redPiece3]

red = (255, 0, 0)
blue = (0, 0, 255)
gui = Gui(red)
current_red_piece = 0
current_blue_piece = 0
current_turn = 0 # 0 is red, 1 is blue
red_victory = False
blue_victory = False

font = pygame.font.SysFont("arial", 12)
text = "Start your game!"
gui_text = font.render(text, True, (0, 0, 0))

moveSound = pygame.mixer.Sound('sounds/move.wav')
diceSound = pygame.mixer.Sound('sounds/dice.wav')
eatSound = pygame.mixer.Sound('sounds/eat.wav')

green_area_1 = [(0, 0), (0, 268), (268, 0)]
green_area_2 = [(800, 700), (530, 700), (800, 430)]
green_area_3 = [(0, 700), (0, 430), (270, 700)]
green_area_4 = [(800, 0), (530, 0), (800, 270)]
green_area_1a = [(750, 50), (50, 700)]
green_area_1b = [(0, 0), (800, 50)]
green_area_1c = [(0, 0), (50, 700)]



def redrawGameWindow():
    win.fill((0, 0, 150))
    pygame.draw.rect(win, (0, 180, 0), green_area_1a)
    pygame.draw.rect(win, (0, 180, 0), green_area_1b)
    pygame.draw.rect(win, (0, 180, 0), green_area_1c)
    pygame.draw.polygon(win, (0, 180, 0), green_area_1)
    pygame.draw.polygon(win, (0, 180, 0), green_area_2)
    pygame.draw.polygon(win, (0, 180, 0), green_area_3)
    pygame.draw.polygon(win, (0, 180, 0), green_area_4)
    gui.draw(win)
    pygame.draw.line(win, (0, 0, 0), (0, 650), (800, 650), 2)
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
    pygame.draw.rect(win, (0, 0, 0), (89, 664, 232, 27))
    pygame.draw.rect(win, (255, 255, 255), (90, 665, 230, 25))
    win.blit(gui_text, (100, 670))
    pygame.display.update()
    
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    """ Button activity """
    cur = pygame.mouse.get_pos()
    if buttons_off == False:
        if startButton.x + startButton.width > cur[0] > startButton.x and startButton.y + startButton.height > cur[1] > startButton.y:
            startButton.setColor((0, 200, 0))
            if (rolled == 0):
                if pygame.mouse.get_pressed()[0]:
                    diceSound.play()
                    rolled = 1
                    startButton.setColor(startButtonClicked)
                    newNumber = dice.randValue()
                    dice.setValue(newNumber)
                    valueOfDice = newNumber
                    if (current_turn == 0):
                        text = "Red turn!"
                        gui_text = font.render(text, True, (0, 0, 0))
                        gui.set_color(red)
                        if (current_red_piece == 0):
                            print("Red turn!")
                        elif (current_red_piece == 1):
                            redPiece0.moves += valueOfDice
                        elif (current_red_piece == 2):
                            redPiece1.moves += valueOfDice
                        elif (current_red_piece == 3):
                            redPiece2.moves += valueOfDice
                        elif (current_red_piece == 4):
                            redPiece3.moves += valueOfDice
                    elif (current_turn == 1):
                        text = "Blue turn!"
                        gui_text = font.render(text, True, (0, 0, 0))
                        gui.set_color(blue)
                        if (current_blue_piece == 0):
                            print("Blue turn!")
                        elif (current_blue_piece == 1):
                            bluePiece0.moves += valueOfDice
                        elif (current_blue_piece == 2):
                            bluePiece1.moves += valueOfDice
                        elif (current_blue_piece == 3):
                            bluePiece2.moves += valueOfDice
                        elif (current_blue_piece == 4):
                            bluePiece3.moves += valueOfDice
                    dice.drawDots(win, newNumber)
        else:
            startButton.setColor(startButtonColor)

    for red_piece in redPieces:
        for blue_piece in bluePieces:
            if (current_turn == 0):
                if (red_piece.x == blue_piece.x):
                    if (red_piece.y == blue_piece.y):
                        eatSound.play()
                        print(blue_piece)
                        print("Red piece eats blue piece!")
                        if (blue_piece.index == 0):
                            blue_piece.x = piece_x + (35 * 0)
                            blue_piece.y = blues_y
                            blue_piece.moves = 0
                        elif (blue_piece.index == 1):
                            blue_piece.x = piece_x + (35 * 1)
                            blue_piece.y = blues_y
                            blue_piece.moves = 0
                        elif (blue_piece.index == 2):
                            blue_piece.x = piece_x + (35 * 2)
                            blue_piece.y = blues_y
                            blue_piece.moves = 0
                        elif (blue_piece.index == 3):
                            blue_piece.x = piece_x + (35 * 3)
                            blue_piece.y = blues_y
                            blue_piece.moves = 0
            elif (current_turn == 1):
                if (blue_piece.x == red_piece.x):
                    if (blue_piece.y == red_piece.y):
                        eatSound.play()
                        print(red_piece)
                        print("Blue piece eats red piece!")
                        if (red_piece.index == 0):
                            red_piece.x = piece_x + (35 * 0)
                            red_piece.y = reds_y
                            red_piece.moves = 0
                        elif (red_piece.index == 1):
                            red_piece.x = piece_x + (35 * 1)
                            red_piece.y = reds_y
                            red_piece.moves = 0
                        elif (red_piece.index == 2):
                            red_piece.x = piece_x + (35 * 2)
                            red_piece.y = reds_y
                            red_piece.moves = 0
                        elif (red_piece.index == 3):
                            red_piece.x = piece_x + (35 * 3)
                            red_piece.y = reds_y
                            red_piece.moves = 0

    for place in places:
        if place.x + 16 > cur[0] > place.x and place.y + 16 > cur[1] > place.y:
            if (current_turn == 0):
                if (rolled == 1):
                    text = "Red player's piece: " + str(current_red_piece)
                    print(text)
                    gui_text = font.render(text, True, (0, 0, 0))
                    print("Value of moves (1): " + str(redPiece0.moves))
                    print("Value of moves (2): " + str(redPiece1.moves))
                    print("Value of moves (3): " + str(redPiece2.moves))
                    print("Value of moves (4): " + str(redPiece3.moves))
                    if (current_red_piece == 0):
                        text = "Please start your turn, RED player!"
                        print(text)
                        gui_text = font.render(text, True, (0, 0, 0))
                    if (current_red_piece == 1):
                        if (redPiece0.moves == place.red_index):
                            redPiece0.x = place.x
                            redPiece0.y = place.y
                            moveSound.play()
                        elif (redPiece0.moves >= 28):
                            redPiece0.x = place27.x
                            redPiece0.y = place27.y
                            moveSound.play()
                    elif (current_red_piece == 2):
                        if (redPiece1.moves == place.red_index):
                            redPiece1.x = place.x
                            redPiece1.y = place.y
                            moveSound.play()
                        elif (redPiece1.moves >= 28):
                            redPiece1.x = place27.x
                            redPiece1.y = place27.y
                            moveSound.play()
                    elif (current_red_piece == 3):
                        if (redPiece2.moves == place.red_index):
                            redPiece2.x = place.x
                            redPiece2.y = place.y
                            moveSound.play()
                        elif (redPiece2.moves >= 28):
                            redPiece2.x = place27.x
                            redPiece2.y = place27.y
                            moveSound.play()
                    elif (current_red_piece == 4):
                        if (redPiece3.moves == place.red_index):
                            redPiece3.x = place.x
                            redPiece3.y = place.y
                            moveSound.play()
                        elif (redPiece3.moves >= 28):
                            redPiece3.x = place27.x
                            redPiece3.y = place27.y
                            moveSound.play()
                    if (redPiece0.x == place27.x and redPiece0.x == place27.x):
                        if (redPiece1.x == place27.x and redPiece1.x == place27.x):
                            if (redPiece2.x == place27.x and redPiece2.x == place27.x):
                                if (redPiece3.x == place27.x and redPiece3.x == place27.x):
                                    text = "Red player is the winner!"
                                    print(text)
                                    gui_text = font.render(text, True, (255, 0, 0))
                                    red_victory = True
            elif (current_turn == 1):
                if (rolled == 1):
                    text = "Blue player's piece: " + str(current_blue_piece)
                    print(text)
                    gui_text = font.render(text, True, (0, 0, 0))
                    print("Value of moves (1): " + str(bluePiece0.moves))
                    print("Value of moves (2): " + str(bluePiece1.moves))
                    print("Value of moves (3): " + str(bluePiece2.moves))
                    print("Value of moves (4): " + str(bluePiece3.moves))
                    if (current_blue_piece == 0):
                        text = "Please start your turn, BLUE player!"
                        print(text)
                        gui_text = font.render(text, True, (0, 0, 0))
                    if (current_blue_piece == 1):
                        if (bluePiece0.moves == place.blue_index):
                            bluePiece0.x = place.x
                            bluePiece0.y = place.y
                            moveSound.play()
                        elif (bluePiece0.moves >= 28):
                            bluePiece0.x = place13.x
                            bluePiece0.y = place13.y
                            moveSound.play()
                    elif (current_blue_piece == 2):
                        if (bluePiece1.moves == place.blue_index):
                            bluePiece1.x = place.x
                            bluePiece1.y = place.y
                            moveSound.play()
                        elif (bluePiece1.moves >= 28):
                            bluePiece1.x = place13.x
                            bluePiece1.y = place13.y
                            moveSound.play()
                    elif (current_blue_piece == 3):
                        if (bluePiece2.moves == place.blue_index):
                            bluePiece2.x = place.x
                            bluePiece2.y = place.y
                            moveSound.play()
                        elif (bluePiece2.moves >= 28):
                            bluePiece2.x = place13.x
                            bluePiece2.y = place13.y
                            moveSound.play()
                    elif (current_blue_piece == 4):
                        if (bluePiece3.moves == place.blue_index):
                            bluePiece3.x = place.x
                            bluePiece3.y = place.y
                            moveSound.play()
                        elif (bluePiece3.moves >= 28):
                            bluePiece3.x = place13.x
                            bluePiece3.y = place13.y
                            moveSound.play()
                    if (bluePiece0.x == place13.x and bluePiece0.x == place13.x):
                        if (bluePiece1.x == place13.x and bluePiece1.x == place13.x):
                            if (bluePiece2.x == place13.x and bluePiece2.x == place13.x):
                                if (bluePiece3.x == place13.x and bluePiece3.x == place13.x):
                                    text = "Blue player is the winner!"
                                    print(text)
                                    gui_text = font.render(text, True, (0, 0, 255))
                                    blue_victory = True
        if buttons_off == False:
            if turnButton.x + turnButton.width > cur[0] > turnButton.x and turnButton.y + turnButton.height > cur[1] > turnButton.y:
                turnButton.setColor((0, 200, 0))
                if current_red_piece == 5:
                    current_turn = 1
                    current_red_piece = 0
                if current_blue_piece == 5:
                    current_turn = 0
                    current_blue_piece = 0
                if (rolled == 1):
                    if (current_turn == 0):
                        if pygame.mouse.get_pressed()[0]:
                            current_red_piece += 1
                            rolled = 0
                            turnButton.setColor(startButtonClicked)
                    elif (current_turn == 1):
                        if pygame.mouse.get_pressed()[0]:
                            current_blue_piece += 1
                            rolled = 0
                            turnButton.setColor(startButtonClicked)
            else:
                turnButton.setColor(startButtonColor)
        """ Button activity ends here """

    if ((red_victory == True) or (blue_victory == True)):
        turnButton.setColor(buttonOff)
        startButton.setColor(buttonOff)
        buttons_off = True

    redrawGameWindow()

pygame.quit()