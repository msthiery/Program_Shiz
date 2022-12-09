"""
125212 December 2022
Scene module that holds every
function used to create and
animate my Q2 Python Project
"""

from graphics import *
from random import *
from time import *
from playsound import playsound

# Random color generator
def randColor():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = color_rgb(red, green, blue)
    return color

# Window creation
win = GraphWin('Monty Hall\'s Game Show', 1200, 600)
win.setBackground(color_rgb(142, 229, 238))

# Every list I created stored as global variables
doorList = []
knobList = []
numberList = []
num1 = []
num2 = []
num3 = []
closedLeft = []
closedRight = []

# Create floor of game show scene
def floorBoards():
    x = 2
    for i in range(80):
        p1 = Point(x, 480)
        p2 = Point(x+15, 600)
        plank = Rectangle(p1, p2)
        plank.setFill('chocolate4')
        plank.setOutline('black')
        plank.setWidth(2)
        plank.draw(win)
        x += 15

# Create the 3 doors
def doors():
    # Loop to create each door
    x = 310    
    for i in range(3):
        p1 = Point(x, 200)
        p2 = Point(x+120, 479)
        door = Rectangle(p1, p2)
        door.setFill(color_rgb(128, 0, 0))
        door.setOutline('black')
        door.setWidth(1)
        door.draw(win)
        x += 230
        doorList.append(door)
    
    # Loop to creat each door handle
    x = 405
    for j in range(3):
        c1 = Point(x, 350)
        knob = Circle(c1, 7)
        knob.setFill(color_rgb(205, 205, 0))
        knob.setOutline('black')
        knob.setWidth(2)
        knob.draw(win)
        x += 230
        knobList.append(knob)
    
    # create the door numbers
    x1 = 370
    y1 = 280
    # Door Number #1
    vert = Line(Point(x1, y1), Point(x1, y1+30))
    vert.setOutline(color_rgb(139, 137, 137))
    vert.setWidth(3)
    vert.draw(win)
    num1.append(vert)
    hor1 = Line(Point(x1-10, y1), Point(x1+10, y1))
    hor1.setOutline(color_rgb(139, 137, 137))
    hor1.setWidth(3)
    hor1.draw(win)
    num1.append(hor1)
    hor2 = Line(Point(x1-10, y1+30), Point(x1+10, y1+30))
    hor2.setOutline(color_rgb(139, 137, 137))
    hor2.setWidth(3)
    hor2.draw(win)
    num1.append(hor2)

    x2 = 590
    # Door Number #2
    vertL = Line(Point(x2, y1), Point(x2, y1+30))
    vertL.setOutline(color_rgb(139, 137, 137))
    vertL.setWidth(3)
    vertL.draw(win)
    num2.append(vertL)
    vertR = Line(Point(x2+20, y1), Point(x2+20, y1+30))
    vertR.setOutline(color_rgb(139, 137, 137))
    vertR.setWidth(3)
    vertR.draw(win)
    num2.append(vertR)
    hor1 = Line(Point(x2-10, y1), Point(x2+30, y1))
    hor1.setOutline(color_rgb(139, 137, 137))
    hor1.setWidth(3)
    hor1.draw(win)
    num2.append(hor1)
    hor2 = Line(Point(x2-10, y1+30), Point(x2+30, y1+30))
    hor2.setOutline(color_rgb(139, 137, 137))
    hor2.setWidth(3)
    hor2.draw(win)
    num2.append(hor2)
    
    x3 = 830
    # Door Number #3
    vert1 = Line(Point(x3-20, y1), Point(x3-20, y1+30))
    vert1.setOutline(color_rgb(139, 137, 137))
    vert1.setWidth(3)
    vert1.draw(win)
    num3.append(vert1)
    vert2 = Line(Point(x3, y1), Point(x3, y1+30))
    vert2.setOutline(color_rgb(139, 137, 137))
    vert2.setWidth(3)
    vert2.draw(win)
    num3.append(vert2)
    vert3 = Line(Point(x3+20, y1), Point(x3+20, y1+30))
    vert3.setOutline(color_rgb(139, 137, 137))
    vert3.setWidth(3)
    vert3.draw(win)
    num3.append(vert3)
    hor1 = Line(Point(x3-30, y1), Point(x3+30, y1))
    hor1.setOutline(color_rgb(139, 137, 137))
    hor1.setWidth(3)
    hor1.draw(win)
    num3.append(hor1)
    hor2 = Line(Point(x3-30, y1+30), Point(x3+30, y1+30))
    hor2.setOutline(color_rgb(139, 137, 137))
    hor2.setWidth(3)
    hor2.draw(win)
    num3.append(hor2)
    
    
# Create the curtains
# Left curtain
def leftCurtainClosed():
    x1 = 2
    for i in range(10):
        p1 = Point(x1, 2)
        p2 = Point(x1+30, 598)
        cLight = Rectangle(p1, p2)
        cLight.setFill(color_rgb(255, 0, 0))
        cLight.setOutline('black')
        cLight.setWidth(4)
        cLight.draw(win)
        x1 += 60
        closedLeft.append(cLight)
    
    x2 = 32
    for j in range(10):
        p1 = Point(x2, 2)
        p2 = Point(x2+30, 598)
        cDark = Rectangle(p1, p2)
        cDark.setFill(color_rgb(205, 0, 0))
        cDark.setOutline('black')
        cDark.setWidth(4)
        cDark.draw(win)
        x2 += 60
        closedLeft.append(cDark)

# Right Curtain
def rightCurtainClosed():
    x1 = 1198
    for i in range(10):
        p1 = Point(x1, 2)
        p2 = Point(x1-30, 598)
        cLight = Rectangle(p1, p2)
        cLight.setFill(color_rgb(255, 0, 0))
        cLight.setOutline('black')
        cLight.setWidth(4)
        cLight.draw(win)
        x1 -= 60
        closedRight.append(cLight)
    
    x2 = 1168
    for j in range(10):
        p1 = Point(x2, 2)
        p2 = Point(x2-30, 598)
        cDark = Rectangle(p1, p2)
        cDark.setFill(color_rgb(205, 0, 0))
        cDark.setOutline('black')
        cDark.setWidth(4)
        cDark.draw(win)
        x2 -= 60
        closedRight.append(cDark)

# Animation to open curtains
def openCurtains():
    for i in range(170):
        for j in closedLeft:
            j.move(-3, 0)
        for l in closedRight:
            l.move(3, 0)

# Import car image
def car(x, y):
# The following code is from
# https://stackoverflow.com/questions/19249859/importing-custom-images-into-graphics-py
    car = Image(Point(x, y), 'car-small.png')
    car.draw(win)

# Import goat image
def goat(x, y):
# The following code is from
# https://stackoverflow.com/questions/19249859/importing-custom-images-into-graphics-py
    goat = Image(Point(x, y), 'goat-small.png')
    goat.draw(win)

# Animation for the doors opening
def doorOpen(dDoor, dKnob, dNum):
    door = doorList[dDoor]
    door.undraw(win)
    knob = knobList[dKnob]
    knob.undraw(win)
    if dNum == 1:
        num1.undraw(win)
    elif dNum == 2:
        num2.undraw(win)
    elif dNum == 3:
        num3.undraw(win)
    
# Play applause sound
def playApplause():
    # Sound came from
    # https://mixkit.co/free-sound-effects/applause/
    open('applause.wav')
    playsound('applause.wav')

def scene():
    floorBoards()
    doors()
    leftCurtainClosed()
    rightCurtainClosed()
    playApplause()
    openCurtains()


scene()
win.getMouse()
win.close()

"""
All colors came from
https://www.webucator.com/article/python-color-constants-module/
"""
