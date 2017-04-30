import sys, os, random, pygame
sys.path.append(os.path.join("objects"))
import SudokuSquare
from GameResources import *

digits = '123456789'
rows = 'ABCDEFGHI'


def play(values_list):
    pygame.init()


    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)

    background_image = pygame.image.load("./images/sudoku-board-bare.jpg").convert()

    clock = pygame.time.Clock()

    # The puzzleNumber sets a seed so either generate
    # a random number to fill in here or accept user
    # input for a duplicatable puzzle.
#    print("Value List =\n ", values_list)
    for values in values_list:
#        print("\n Values = ", values[0],values[1])
        pygame.event.pump()
        theSquares = []
        initXLoc = 0
        initYLoc = 0
        startX, startY, editable, number = 0, 0, "N", 0
        for y in range(9):
#            print("In Y ", y)
            for x in range(9):
#                print("In X " ,x)
                if x in (0, 1, 2):  startX = (x * 57) + 38
                if x in (3, 4, 5):  startX = (x * 57) + 99
                if x in (6, 7, 8):  startX = (x * 57) + 159

                if y in (0, 1, 2):  startY = (y * 57) + 35
                if y in (3, 4, 5):  startY = (y * 57) + 100
                if y in (6, 7, 8):  startY = (y * 57) + 165
                col = digits[x]
#                print("col =",col)
                row = rows[y]
#                print("row =", row)
                string_number = values[row + col]
                if len(string_number) > 1 or string_number == '' or string_number == '.':
                    number = None
                else:
                    number = int(string_number)
                theSquares.append(SudokuSquare.SudokuSquare(number, startX, startY, editable, x, y))

        screen.blit(background_image, (0, 0))
        for num in theSquares:
            num.draw()

        pygame.display.flip()
        pygame.display.update()
        clock.tick(5)

    # leave game showing until closed by user
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

if __name__ == "__main__":
    main()
    sys.exit()
##   values={'A1': '2', 'A2': '6', 'A3': '7', 'A4': '9', 'A5': '4', 'A6': '5', 'A7': '3', 'A8': '8', 'A9': '1', 'B1': '8', 'B2': '5', 'B3': '3', 'B4': '7', 'B5': '1', 'B6': '6', 'B7': '2', 'B8': '4', 'B9': '9', 'C1': '4', 'C2': '9', 'C3': '1', 'C4': '8', 'C5': '2', 'C6': '3', 'C7': '5', 'C8': '7', 'C9': '6', 'D1': '5', 'D2': '7', 'D3': '6', 'D4': '4', 'D5': '3', 'D6': '8', 'D7': '1', 'D8': '9', 'D9': '2', 'E1': '3', 'E2': '8', 'E3': '4', 'E4': '1', 'E5': '9', 'E6': '2', 'E7': '6', 'E8': '5', 'E9': '7', 'F1': '1', 'F2': '2', 'F3': '9', 'F4': '6', 'F5': '5', 'F6': '7', 'F7': '4', 'F8': '3', 'F9': '8', 'G1': '6', 'G2': '4', 'G3': '2', 'G4': '3', 'G5': '7', 'G6': '9', 'G7': '8', 'G8': '1', 'G9': '5', 'H1': '9', 'H2': '3', 'H3': '5', 'H4': '2', 'H5': '8', 'H6': '1', 'H7': '7', 'H8': '6', 'H9': '4', 'I1': '7', 'I2': '1', 'I3': '8', 'I4': '5', 'I5': '6', 'I6': '4', 'I7': '9', 'I8': '2', 'I9': '3'}
#   values={'A1': '2'}
#
#   play(values)
#   sys.exit()