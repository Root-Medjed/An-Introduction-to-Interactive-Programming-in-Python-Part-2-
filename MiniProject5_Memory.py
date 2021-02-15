#Mini Project 5

# implementation of card game - Memory

import simplegui
import random

state = 0
turn = 0

# helper function to initialize globals
def new_game():
    global card_list, card_1, card_2, exposed_list, turn   #card_1,card_2: mouse pos mod 50
    card_list = range(8) * 2  
    random.shuffle(card_list)
    turn = 0
    card_1 = 0
    card_2 = 0
    exposed_list = []      #exposed = true, otherwise: false
    for i in range(len(card_list)):
        exposed_list.append(False)
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global card_1, card_2, turn, state

    if state == 0:
        card_1 = pos[0]//50
        exposed_list[card_1] = True
        state = 1
        
    elif state == 1 and exposed_list[pos[0]//50] == False:
        card_2 = pos[0]//50
        exposed_list[card_2] = True
        state = 2
        turn += 1
        
    elif exposed_list[pos[0]//50] ==False:
        if card_list[card_1] != card_list[card_2]:
            exposed_list[card_1] = False
            exposed_list[card_2] = False
        card_1 = pos[0]//50
        exposed_list[card_1] = True
        state = 1
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    #Draw secret num
    for i in range(len(card_list)):
        if exposed_list[i] == True:
            canvas.draw_text(str(card_list[i]), (50 * i + 10, 66), 54, 'White')
        else:
            canvas.draw_polygon([(50 * i, 0), (50 + 50 * i, 0),
                                 (50 + 50 * i, 100), (50 * i, 100)],
                                2, 'serif', 'Green')
            
    label.set_text('Turns: ' + str(turn)) 


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
