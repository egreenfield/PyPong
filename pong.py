
import pyglet
import logging
from pyglet.window import key
from enum import Enum
from pyglet.gl import *

####################################################################################
# CONSTANTS
####################################################################################

BOARD_WIDTH = 800
BOARD_HEIGHT = 300

####################################################################################
# Setup
####################################################################################
class Direction(Enum):
    Still = 0
    Up = 1
    Down = 2
    Left = 3
    Right = 4

class Board():
    def __init__(self):
        self.width = BOARD_WIDTH
        self.height = BOARD_HEIGHT

class Visuals():
    def __init__(self):
        self.label = pyglet.text.Label('Hello, world!',
                          font_name='Arial',
                          font_size=36,
                          x=window.width // 2,
                          y=window.height // 2,
                          anchor_x='center',
                          anchor_y='center')
        return

class Player():
    def __init__(self):
        self.direction = Direction.Still
        self.position = 0

class State():
    def __init__(self):
        self.board = Board()
        self.visuals = Visuals()
        self.logger = None
        self.player1 = Player()



def initGameState():
    return State()

def initScreen(state,window):
    window.set_size(state.board.width,state.board.height) 
    window.set_minimum_size(state.board.width,state.board.height)
    window.set_maximum_size(state.board.width,state.board.height)
    return

####################################################################################
# Drawing
####################################################################################

def drawBox(left,top,right,bottom,color):
    glBegin(GL_QUADS)
    glColor3f(((color & 0xFF0000)>>16) / 255.0,((color & 0x00FF00)>>8) / 255.0,(color & 0x0000FF) / 255.0)
    glVertex3f(left,top,0)
    glVertex3f(right,top,0)
    glVertex3f(right,bottom,0)
    glVertex3f(left,bottom,0)
    glEnd()


def drawState(state):
    glClear(GL_COLOR_BUFFER_BIT)
    drawBox(100,state.player1.position,200,state.player1.position+100,color = 0xFF0000)
    drawBox(300,100,400,200,color = 0x0088FF)
    state.visuals.label.draw()
    return


    
####################################################################################
# Game Logic
####################################################################################

def updatePlayerPosition(player):
    if(player.direction == Direction.Down):
        player.position -= .5
    elif(player.direction == Direction.Up):
        player.position += .5

def updateState(state,dt):
    updatePlayerPosition(state.player1)
    return

def checkInput(state,keys):

    if(keys[key.S]):
        state.player1.direction = Direction.Down
    elif(keys[key.W]):
        state.player1.direction = Direction.Up
    else:
        state.player1.direction = Direction.Still
    return

####################################################################################
# Messy Initialization stuff
####################################################################################
#region

####################################################################################
# Initialization
####################################################################################
def initLogging(state):
    logger = logging.getLogger(__file__)
    hdlr = logging.FileHandler(__file__ + ".log","w+")
    print("logging file is " + __file__ + ".log")
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)
    logger.info("begin")
    state.logger = logger


def update(dt):
    checkInput(state,keys)
    updateState(state,dt)
    return

window = pyglet.window.Window()
keys = key.KeyStateHandler()
window.push_handlers(keys)
pyglet.clock.schedule_interval(update, 1/60.0)

####################################################################################
# Main Game Loop
####################################################################################

@window.event
def on_draw():
    window.clear()
    drawState(state)



state = initGameState()
initScreen(state,window)
initLogging(state)


pyglet.app.run()
#endregion
