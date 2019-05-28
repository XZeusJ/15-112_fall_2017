##############################################
## Lab5
##############################################

from cs112_f16_wk5 import assertEqual, assertAlmostEqual, lintAll, testAll
import math, string, copy, random

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Problems
#################################################

def removeRowAndCol(A, row, col):
    return 42

def destructiveRemoveRowAndCol(A, row, col):
    return 42

def wordSearchWithIntegerWildcards(board, word):
    return 42

def isLegalSudoku(board):
    return 42

##############################################
## ignore_rest: graphics go below here!
##############################################

from tkinter import *

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def make2dList(rows, cols):
    # helper function to create a 2d list 
    a=[]
    for row in range(rows): a += [[0]*cols]
    return a

def randomlyPlaceValue(data, value):
    # In an infinite loop, pick a random row,col on
    # the board (stored in data.board), and if it is
    # non-empty, place value there and then return (row, col).
    # Note that this function never returns if the board is full!
    return (0,0)

def init(data):
    minRowsOrCols = 5
    maxRowsOrCols = 10
    data.rows = random.randint(minRowsOrCols, maxRowsOrCols)
    data.cols = random.randint(minRowsOrCols, maxRowsOrCols)
    data.board = make2dList(data.rows, data.cols)
    data.EMPTY = 0
    data.PLAYER = 1
    data.WALL = 2
    data.FOOD = 3
    (data.playerRow, data.playerCol) = randomlyPlaceValue(data, data.PLAYER)
    randomlyPlaceValue(data, data.FOOD)
    minWalls = 10
    maxWalls = 20
    for i in range(random.randint(minWalls, maxWalls)):
        randomlyPlaceValue(data, data.WALL)
    data.score = 0

def mousePressed(event, data):
    # ignore mousePressed events
    pass

def doMove(data, drow, dcol):
    # Compute the new row and new col of the player (whose
    # current position is stored in data.playerRow and
    # data.playerCol).  If that new position is off the board,
    # or occupied by a wall, simply return without making any
    # changes.  Otherwise, move the player (which takes two
    # steps -- (1) update data.playerRow and data.playerCol,
    # and (2) remove data.PLAYER from its old location in
    # data.board (instead placing data.EMPTY there), and then
    # set data.PLAYER to the current location in data.board.
    # Finally, deal with food -- if there was food in the
    # new location, eat it, update the score, and randomly
    # place new food (just like we did in the init function).
    pass

def keyPressed(event, data):
    if (event.keysym == 'r'): init(data)
    elif (event.keysym == 'Up'): doMove(data, -1, 0)
    elif (event.keysym == 'Down'): doMove(data, +1, 0)
    elif (event.keysym == 'Left'): doMove(data, 0, -1)
    elif (event.keysym == 'Right'): doMove(data, 0, +1)

def timerFired(data):
    # ignore timerFired events
    pass

def drawCell(canvas, data, row, col):
    margin = 40
    rowHeight =  (data.height - 2*margin) / data.rows 
    columnWidth = (data.width - 2*margin) / data.cols
    x0 = margin + col * columnWidth
    x1 = margin + (col+1) * columnWidth
    y0 = margin + row * rowHeight
    y1 = margin + (row+1) * rowHeight
    # Now actually draw the cell at the given row, col (which
    # is stored in data.board[row][col])...
    # First, draw a properly-colored rectangle from (x0,y0) to (x1,y1)
    # and then if the cell contains a player or food, draw
    # a properly-colored oval inside that rectangle.
    pass

def drawBoard(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            drawCell(canvas, data, row, col)

def drawScore(canvas, data):
    msg = "Score = " + str(data.score)
    canvas.create_text(data.width/2, 20, text=msg)

def drawInstructions(canvas, data):
    msg = 'Silly Game: Use arrow keys to find food; Press r to reset.'
    canvas.create_text(data.width/2, data.height-20, text=msg)

def redrawAll(canvas, data):
    drawBoard(canvas, data)
    drawScore(canvas, data)
    drawInstructions(canvas, data)

def runSillyGame(width=600, height=600):
    # DO NOT MODIFY THIS FUNCTION!!!!
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

##############################################
## ignore_rest: tests and main go below here
##############################################

def testRemoveRowAndCol():
    print('Testing removeRowAndCol()...', end='')
    a = [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]]
    assertEqual(removeRowAndCol(a, 1, 2), [[2, 3, 5], [0, 1, 3]])
    assertEqual(a, [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]])
    assertEqual(removeRowAndCol(a, 0, 0), [[7, 6, 5], [1, 2, 3]])
    assertEqual(a, [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]])
    B=[[37, 78, 29, 70, 21, 62, 13, 54, 5],
    [6,     38, 79, 30, 71, 22, 63, 14, 46],
    [47,    7,  39, 80, 31, 72, 23, 55, 15],
    [16,    48, 8,  40, 81, 32, 64, 24, 56],
    [57,    17, 49, 9,  41, 73, 33, 65, 25],
    [26,    58, 18, 50, 1,  42, 74, 34, 66], 
    [67,    27, 59, 10, 51, 2,  43, 75, 35],
    [36,    68, 19, 60, 11, 52, 3,  44, 76],
    [77,    28, 69, 20, 61, 12, 53, 4,  45]]

    C=[[37, 78, 29, 70, 21, 62,     54, 5],
    [6,     38, 79, 30, 71, 22,     14, 46],
    [47,    7,  39, 80, 31, 72,     55, 15],
    [16,    48, 8,  40, 81, 32,     24, 56],
    [57,    17, 49, 9,  41, 73,     65, 25],
    [26,    58, 18, 50, 1,  42,     34, 66], 
    [67,    27, 59, 10, 51, 2,      75, 35],
    [36,    68, 19, 60, 11, 52, 44, 76]]
    assertEqual(removeRowAndCol(B,8,6), C)
    print('Passed!')

def testDestructiveRemoveRowAndCol():
    print("Testing destructiveRemoveRowAndCol()...", end='')
    A = [ [ 2, 3, 4, 5],
          [ 8, 7, 6, 5],
          [ 0, 1, 2, 3]
        ]
    B = [ [ 2, 3, 5],
          [ 0, 1, 3]
        ]
    assertEqual(destructiveRemoveRowAndCol(A, 1, 2), None)
    assertEqual(A, B) # but now A is changed!
    A = [ [ 1, 2 ], [3, 4] ]
    B = [ [ 4 ] ]
    assertEqual(destructiveRemoveRowAndCol(A, 0, 0), None)
    assertEqual(A, B)
    A = [ [ 1, 2 ] ]
    B = [ ]
    assertEqual(destructiveRemoveRowAndCol(A, 0, 0), None)
    assertEqual(A, B)
    print("Passed!")

def testWordSearchWithIntegerWildcards():
    print("Testing wordSearchWithIntegerWildcards()...", end='')
    board = [ [ 'd', 'o', 'g' ],
              [ 't', 'a', 'c' ],
              [ 'o', 'a', 't' ],
              [ 'u', 'r', 'k' ],
            ]
    assertEqual(wordSearchWithIntegerWildcards(board, "dog"), True)
    assertEqual(wordSearchWithIntegerWildcards(board, "cat"), True)
    assertEqual(wordSearchWithIntegerWildcards(board, "tad"), True)
    assertEqual(wordSearchWithIntegerWildcards(board, "cow"), False)
    board = [ [ 'd', 'o',  1  ],
              [  3 , 'a', 'c' ],
              [ 'o', 'q' ,'t' ],
            ]
    assertEqual(wordSearchWithIntegerWildcards(board, "z"), True)
    assertEqual(wordSearchWithIntegerWildcards(board, "zz"), False)
    assertEqual(wordSearchWithIntegerWildcards(board, "zzz"), True)
    assertEqual(wordSearchWithIntegerWildcards(board, "dzzzo"), True)
    assertEqual(wordSearchWithIntegerWildcards(board, "dzzo"), True)
    assertEqual(wordSearchWithIntegerWildcards(board, "zzzd"), True)
    assertEqual(wordSearchWithIntegerWildcards(board, "zzzo"), True)
    board = [ [ 3 ] ]
    assertEqual(wordSearchWithIntegerWildcards(board, "zz"), False)
    assertEqual(wordSearchWithIntegerWildcards(board, "zzz"), True)
    assertEqual(wordSearchWithIntegerWildcards(board, "zzzz"), False)
    board = [ [ 'a', 'b', 'c' ],
              [ 'd',  2 , 'e' ],
              [ 'f', 'g', 'h' ]]
    assertEqual(wordSearchWithIntegerWildcards(board, "aqqh"), True)
    assertEqual(wordSearchWithIntegerWildcards(board, "aqqhh"), False)
    assertEqual(wordSearchWithIntegerWildcards(board, "zz"), True)
    assertEqual(wordSearchWithIntegerWildcards(board, "zzc"), True)
    assertEqual(wordSearchWithIntegerWildcards(board, "zaz"), False)
    print("Passed!")

def testIsLegalSudoku():
    # From Leon Zhang!
    print("Testing isLegalSudoku()...", end="")
    board = [[0]]
    assertEqual(isLegalSudoku(board), True)
    board = [[1]]
    assertEqual(isLegalSudoku(board), True)

    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    assertEqual(isLegalSudoku(board), True)
    board = [[0, 4, 0, 0],
             [0, 0, 3, 0],
             [1, 0, 0, 0],
             [0, 0, 0, 2]]
    assertEqual(isLegalSudoku(board), True)
    board = [[1, 2, 3, 4],
             [3, 4, 1, 2],
             [2, 1, 4, 3],
             [4, 3, 2, 1]]
    assertEqual(isLegalSudoku(board), True)
    board = [[1, 2, 3, 4],
             [3, 4, 4, 2],
             [2, 4, 4, 3],
             [4, 3, 2, 1]]    
    assertEqual(isLegalSudoku(board), False)

    board = [
    [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
    ]
    assertEqual(isLegalSudoku(board), True)
    
    board = [
    [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 9, 7, 9 ] # two 9's in this row!
    ]
    assertEqual(isLegalSudoku(board), False)
    board = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    assertEqual(isLegalSudoku(board), True)
    board = [
    [ 2,11, 9, 5, 8,16,13, 4,12, 3,14, 7,10, 6,15, 1],
    [ 4,12,15,10, 3, 6, 9,11,13, 5, 8, 1,16, 7,14, 2],
    [ 1,14, 6, 7,15, 2, 5,12,11, 9,10,16, 3,13, 8, 4],
    [16,13, 8, 3,14, 1,10, 7, 4, 6, 2,15, 9,11, 5,12],
    [12, 2,16, 9,10,14,15,13, 8, 1, 5, 3, 6, 4,11, 7],
    [ 6, 7, 1,11, 5,12, 8,16, 9,15, 4, 2,14,10, 3,13],
    [14, 5, 4,13, 6,11, 1, 3,16,12, 7,10, 8, 9, 2,15],
    [ 3, 8,10,15, 4, 7, 2, 9, 6,14,13,11, 1,12,16, 5],
    [13, 9, 2,16, 7, 8,14,10, 3, 4,15, 6,12, 5, 1,11],
    [ 5, 4,14, 6, 2,13,12, 1,10,16,11, 8,15, 3, 7, 9],
    [ 7, 1,11,12,16, 4, 3,15, 5,13, 9,14, 2, 8,10, 6],
    [10,15, 3, 8, 9, 5,11, 6, 2, 7, 1,12, 4,14,13,16],
    [11,10,13,14, 1, 9, 7, 8,15, 2, 6, 4, 5,16,12, 3],
    [15, 3, 7, 4,12,10, 6, 5, 1, 8,16,13,11, 2, 9,14],
    [ 8, 6, 5, 1,13, 3,16, 2,14,11,12, 9, 7,15, 4,10],
    [ 9,16,12, 2,11,15, 4,14, 7,10, 3, 5,13, 1, 6, 8]]
    assertEqual(isLegalSudoku(board), True)
    # last number is supposed to be 8, not 10
    board = [
    [ 2,11, 9, 5, 8,16,13, 4,12, 3,14, 7,10, 6,15, 1],
    [ 4,12,15,10, 3, 6, 9,11,13, 5, 8, 1,16, 7,14, 2],
    [ 1,14, 6, 7,15, 2, 5,12,11, 9,10,16, 3,13, 8, 4],
    [16,13, 8, 3,14, 1,10, 7, 4, 6, 2,15, 9,11, 5,12],
    [12, 2,16, 9,10,14,15,13, 8, 1, 5, 3, 6, 4,11, 7],
    [ 6, 7, 1,11, 5,12, 8,16, 9,15, 4, 2,14,10, 3,13],
    [14, 5, 4,13, 6,11, 1, 3,16,12, 7,10, 8, 9, 2,15],
    [ 3, 8,10,15, 4, 7, 2, 9, 6,14,13,11, 1,12,16, 5],
    [13, 9, 2,16, 7, 8,14,10, 3, 4,15, 6,12, 5, 1,11],
    [ 5, 4,14, 6, 2,13,12, 1,10,16,11, 8,15, 3, 7, 9],
    [ 7, 1,11,12,16, 4, 3,15, 5,13, 9,14, 2, 8,10, 6],
    [10,15, 3, 8, 9, 5,11, 6, 2, 7, 1,12, 4,14,13,16],
    [11,10,13,14, 1, 9, 7, 8,15, 2, 6, 4, 5,16,12, 3],
    [15, 3, 7, 4,12,10, 6, 5, 1, 8,16,13,11, 2, 9,14],
    [ 8, 6, 5, 1,13, 3,16, 2,14,11,12, 9, 7,15, 4,10],
    [ 9,16,12, 2,11,15, 4,14, 7,10, 3, 5,13, 1, 6,10]]
    assertEqual(isLegalSudoku(board), False)
    print("Passed!")

#################################################
# Main
#################################################

def main():
    lintAll()
    runSillyGame()
    testAll(
        testRemoveRowAndCol, 
        testDestructiveRemoveRowAndCol,
        testWordSearchWithIntegerWildcards,
        testIsLegalSudoku,
    )

if __name__ == '__main__':
    main()
