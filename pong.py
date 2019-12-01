
import pyglet
import logging
from pyglet.window import key

####################################################################################
# CONSTANTS
####################################################################################

BOARD_WIDTH = 800
BOARD_HEIGHT = 300

gLogger = None

####################################################################################
# Setup
####################################################################################

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

class State():
    def __init__(self):
        self.board = Board()
        self.visuals = Visuals()
        self.logger = None


def initGameState():
    return State()

def initScreen(state,window):
    window.set_size(state.board.width,state.board.height) 
    return

####################################################################################
# Drawing
####################################################################################

def drawState(state):
    state.visuals.label.draw()
    return


    
####################################################################################
# Game Logic
####################################################################################

def updateState(state,dt):
    return

def checkInput(state,keys):
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
