'''Showing the last name instead of the first name'''

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1].strip() for name in names]
#added in strip because there was an extra line at the end messing stuff up

win = visual.Window([800,600],color="black", units='pix')
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
lastNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
fixationCross = visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])
while True:
    nameShown = random.choice(lastNames)
    lastNameStim.setText(nameShown)
    fixationCross.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    lastNameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)

    if event.getKeys(['q']):
        break