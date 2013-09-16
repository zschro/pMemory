# Implementation of Memory the card game.
# Uses codeSkulptor's SimpleGUI http://www.codeskulptor.org/
# @author zschro - Zachary Schroeder

import simplegui
import random
WIDTH = 800
HEIGHT = 1000

# helper function to initialize globals
def init():
    global cards_showing, card_nums, game_state, last_card, counter
    last_card = [0,0]
    cards_showing = [False] * 16
    game_state = 0
    counter = 0
    label.set_text("Moves = " + str(counter))
    card_nums = range(1,9)+range(1,9)
    random.shuffle(card_nums)

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global cards_showing, game_state, last_card, counter
    #creates a variable containing the position and number
    card_index = ((pos[0]//200)*4) + pos[1] //250
    the_card = [card_index,card_nums[card_index]]

    #after not getting a match go back to one card
    if game_state == 2 and cards_showing[the_card[0]] == False:
        cards_showing[last_card[0]]=False
        cards_showing[last_card[2]]=False
        cards_showing[the_card[0]] = True
        onecard.play()
        last_card = the_card
        game_state = 1
    #start the game opening 1 card
    elif game_state == 0 and cards_showing[the_card[0]] == False:        
        cards_showing[the_card[0]] = True
        onecard.play()
        game_state +=1
        last_card = the_card
    #when opening the second card increment the turn counter and check for a match
    elif game_state == 1 and cards_showing[the_card[0]] == False:
        cards_showing[the_card[0]] = True
        counter +=1
        label.set_text("Moves = " + str(counter))
        if last_card[1] == the_card[1]:
            game_state =0
            match.play()
            if False not in cards_showing:
                tada.play()
        else:
            game_state = 2
            last_card += the_card
            nomatch.play()
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    #loop through x and y for each card
    for x in range(0,4):
        for y in range(0,4):
            # draw the card border
            canvas.draw_polygon([(x * 200, y * 250), ((x+1) * 200, y * 250), ((x+1) * 200, (y+1) * 250), (x * 200, (y+1) * 250)], 12, "Blue")
    for x in range(0,4):
        for y in range(0,4):
            i = ((x+1)*4)+(y+1) -5
            #canvas.draw_text(str(i), ((x*200)+10, (y*250)+65), 52, "Red")
            if cards_showing[i]:
                canvas.draw_image(card_images[card_nums[i]-1], (100,125), (200,250), ((x * 200)+100, (y * 250)+125), (200,250))
                canvas.draw_polygon([(x * 200, y * 250), ((x+1) * 200, y * 250), ((x+1) * 200, (y+1) * 250), (x * 200, (y+1) * 250)], 12, "Aqua")
                #canvas.draw_text(str(card_nums[i]), ((x*200)+100, (y*250)+125), 70, "Green")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

#initialize sounds
match = simplegui.load_sound("http://zschro.com/games/memory/match.wav")
nomatch = simplegui.load_sound("http://zschro.com/games/memory/nomatch.wav")
onecard = simplegui.load_sound("http://zschro.com/games/memory/onecard.wav")
tada = simplegui.load_sound("http://zschro.com/games/memory/tada.wav")

#initialize graphics
dragonCard = simplegui.load_image("http://zschro.com/games/memory/dragoncard.jpg")
puppyCard = simplegui.load_image("http://zschro.com/games/memory/puppycard.jpg")
eggCard = simplegui.load_image("http://zschro.com/games/memory/EggCard.jpg")
dragon3dcard = simplegui.load_image("http://zschro.com/games/memory/dragon3dcard.jpg")
birdCard = simplegui.load_image("http://zschro.com/games/memory/birdcard.jpg")
pegasuscard = simplegui.load_image("http://zschro.com/games/memory/pegasuscard.jpg")
pumpcard = simplegui.load_image("http://zschro.com/games/memory/pumpcard.jpg")
babydragoncard = simplegui.load_image("http://zschro.com/games/memory/babydragoncard.jpg")

card_images = [dragonCard,puppyCard,eggCard,dragon3dcard,birdCard,pegasuscard,pumpcard,babydragoncard]

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()