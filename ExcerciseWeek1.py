##1. For each mouse click, print the position of the mouse click to the console.

import simplegui

def echo(pos):
    print "Mouse click at " + str(pos)
    
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(echo)

frame.start()
