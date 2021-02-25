############################################################
##1. For each mouse click, print the position of the mouse click to the console.

import simplegui

def echo(pos):
    print "Mouse click at " + str(pos)
    
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(echo)

frame.start()

###########################################################
##2. Modify the program template below so that clicking inside any of the three displayed circles prints the color of the clicked circle to the console. Hint: Use the 
## supplied function \color{red}{\verb|dist|}dist to compute the distance between the center of each circle and the mouse click.
import simplegui
import math

# define global constants
RADIUS = 20
RED_POS = [50, 100]
GREEN_POS = [150, 100]
BLUE_POS = [250, 100]

# define helper function
def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define mouseclick handler
def click(pos):
    if dist(pos, RED_POS) < RADIUS:
        print "Clicked red ball"
    elif dist(pos, GREEN_POS) < RADIUS:
        print "Clicked green ball"
    elif dist(pos, BLUE_POS) < RADIUS:
        print "Clicked blue ball"
          

# define draw
def draw(canvas):
    canvas.draw_circle(RED_POS, RADIUS, 1, "Red", "Red")
    canvas.draw_circle(GREEN_POS, RADIUS, 1, "Green", "Green")
    canvas.draw_circle(BLUE_POS, RADIUS, 1, "Blue", "Blue")
    
# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()

###########################################################

