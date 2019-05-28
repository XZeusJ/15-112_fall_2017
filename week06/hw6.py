# hw6.py
# name + andrewId + section

#Place the Autograded solutions here




######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#Place the manually graded solutions here

from tkinter import *

####################################
# Othello
####################################

def othelloInit(data):
    # load data.xyz as appropriate
    pass

def othelloMousePressed(event, data):
    # use event.x and event.y
    pass

def othelloKeyPressed(event, data):
    # use event.char and event.keysym
    pass

def othelloTimerFired(data):
    pass

def othelloRedrawAll(canvas, data):
    # draw in canvas
    pass

####################################
# run function for Othello
####################################

def runOthello(width=600, height=600):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        othelloRedrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        othelloMousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        othelloKeyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        othelloTimerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    othelloInit(data)
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

####################################
# FancyWheels
####################################

def fancyWheelsInit(data):
    # load data.xyz as appropriate
    pass

def fancyWheelsMousePressed(event, data):
    # use event.x and event.y
    pass

def fancyWheelsKeyPressed(event, data):
    # use event.char and event.keysym
    pass

def fancyWheelsTimerFired(data):
    pass

def fancyWheelsRedrawAll(canvas, data):
    # draw in canvas
    pass

####################################
# run function for FancyWheels
####################################

def runFancyWheels(width=600, height=600):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        fancyWheelsRedrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        fancyWheelsMousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        fancyWheelsKeyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        fancyWheelsTimerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    fancyWheelsInit(data)
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
