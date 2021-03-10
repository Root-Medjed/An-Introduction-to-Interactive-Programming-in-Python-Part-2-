# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
            # create Hand object

    def __str__(self):
        s = ''
        for card in self.cards:
            s += str(c)
            s += ' '
        return 'Hand contains ' + s
        # return a string representation of a hand

    def add_card(self, card):
        self.cards.append(card)
            # add a card object to a hand

    def get_value(self):
        #initialize total value and number of aces
        hand_value = 0 
        aces_count = 0
        
        for value in self.cards:
            hand_value += VALUES[value.get_rank()]
            if value.get_rank() == 'A':
                aces_count += 1
        
        if aces_count > 0 and hand_value + 10 <= 21:
            hand_value += 10
            return hand_value
        else:
            return hand_value
            
        
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
            # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        
        for card in self.cards:
            card.draw(canvas, pos)        
            pos[0] += 100
            
            # draw a hand on the canvas, use the draw method for cards
 
        
# define deck clasts t
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS: 
            for rank in RANKS:
                deck = Card(suit, rank)
                self.deck.append(deck)
        # create a Deck object

    def shuffle(self):
        return random.shuffle(self.deck)
        # shuffle the deck 
        # use random.shuffle()

    def deal_card(self):
        return self.deck.pop()
        # deal a card object from the deck
    
    def __str__(self):
        sdeck = ''
        for d_card in self.deck:
            sdeck += str(d_card) 
            sdeck += ' '
        return sdeck
        
        # return a string representing the deck



#define event handlers for buttons
def deal():
    # your code goes here
    
    global outcome, in_play, my_deck, dealer_hand, player_hand, score
    """
    2.We suggest adding a global outcome string that is drawn in the draw handler 
    using draw_text. 
    3. Add logic using the global variable in_play that keeps track of whether 
    the player's hand is still being played. If the round is still in play, 
    you should draw an image of the back of a card (provided in the template) 
    over the dealer's first (hole) card to hide it. Once the round is over, 
    the dealer's hole card should be displayed.
   
    #1 pt - Pressing the "Deal" button in the middle of the round causes the
    # player to lose the current round
    """
    
    if in_play == True:
        outcome = "Pressed the 'Deal' button in the middle of the round. You lose."
        score -= 1

    else:
        
        my_deck = Deck() #create an deck object
        my_deck.shuffle() #apply shuffle method 
        
        dealer_hand = Hand()
        dealer_hand.add_card(my_deck.deal_card())
        dealer_hand.add_card(my_deck.deal_card())
        
        player_hand = Hand()
        player_hand.add_card(my_deck.deal_card())
        player_hand.add_card(my_deck.deal_card())
        
        outcome = 'Hit or stand? New deal?'
        
    in_play = True

def hit():
    global outcome, in_play, score
    
    if in_play == True:
        # if the hand is in play, hit the player
        
        player_hand.add_card(my_deck.deal_card())
        
        # replace with your code below
 
        if player_hand.get_value() > 21:
            in_play = False
            outcome = 'You have busted!'
            score -= 1
        else:
            outcome = 'Hit or stand?'
            
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # replace with your code below
    global in_play, outcome, score
    
    if in_play == True:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(my_deck.deal_card())
        in_play = False
        
        if dealer_hand.get_value() > 21:
            outcome = 'Dealer has busted. You win!'
            score += 1
            in_play = False
        else: 
            if player_hand.get_value() > dealer_hand.get_value():
                outcome = 'You won!'
                score += 1
                in_play = False
            elif player_hand.get_value() <= dealer_hand.get_value():
                outcome = 'Dealer won.'
                score -= 1
                in_play = False
                
    if player_hand.get_value() > 21:
        outcome = 'You have busted!'
        in_play = False
        
    if player_hand.get_value() == 21:
        outcome = 'Blackjack! You won!'
        in_play = False

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    player_hand.draw(canvas, [100, 390])  
    dealer_hand.draw(canvas, [100, 180]) 
    
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_CENTER[0], 180 + CARD_CENTER[1]], CARD_BACK_SIZE)
     
    canvas.draw_text(outcome, (50, 310), 20, 'Purple')
    canvas.draw_text('Blackjack', (180, 50), 50, 'Yellow')
    canvas.draw_text('Dealer', (50, 160), 30, 'Black')
    canvas.draw_text('Player', (50, 360), 30, 'Black')
    canvas.draw_text('Your Score ' + str(score), (400, 50), 25, 'Black')
    
    
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
