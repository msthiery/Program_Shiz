"""
125212 December 2022
Main file for CSI Fall 22
Quarter 2 Python Project

The project is a game show based off of the Monty Hall Probability Problem.
3 Doors are placed in front of a contestant with a car behind 1 door and a
goat behind the other 2 doors. The contestant then chooses a door, a different
door is opened up to show a goat. Then, the contestant is offered the choice
of switching doors therefore increasing he/she's win probability from 33.33%
to 66.67%. This program will display the same options as the Monty Hall
problem with a real, computer-based probability system implemented. So, the
user doesn't always win if they switch doors, it's still down to the
probability of the game.
"""

from graphics import *
from random import *
from time import *
from playsound import playsound

# My created modules
from scene import *
from logic import *

win = GraphWin('Monty Hall\'s Game Show', 1200, 600)
win.setBackground(color_rgb(142, 229, 238))

def main():
    floorBoards()
    doors()
    leftCurtainClosed()
    rightCurtainClosed()
    playApplause()
    openCurtains()