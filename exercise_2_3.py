'''Alternate between randomly showing first name and last name'''

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1].strip() for name in names]

nameChoice = [firstNames,lastNames]

win = visual.Window([800,600],color="black", units='pix')
#firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
#lastNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
fixationCross = visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])

while True:
    nameCategory = random.choice(nameChoice) #pick random list
    nameShown = random.choice(nameCategory) #pick random item from list
    nameStim.setText(nameShown)
    fixationCross.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    nameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)

    if event.getKeys(['q']):
        break