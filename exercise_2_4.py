'''On each presentation of a name, wait for a response 
('f' for first name, 'l' for last-name) and only proceed to the next name if
 the response is correct. Hint: if you've done steps 2-3 properly, 
 this should be really easy. Refer to event.waitKeys() if you have trouble.'''

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1].strip() for name in names]

nameChoice = [firstNames,lastNames]

win = visual.Window([800,600],color="black", units='pix')
nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
fixationCross = visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])

while True:
    nameCategory = random.choice(nameChoice)
    nameShown = random.choice(nameCategory)
    nameStim.setText(nameShown)
    fixationCross.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    nameStim.draw()
    win.flip()
    if nameCategory == firstNames:
        response = event.waitKeys(keyList='fq')
        if 'q' in response:
            break
    if nameCategory == lastNames:
        response = event.waitKeys(keyList='lq')
        if 'q' in response:
            break
        win.flip()
    core.wait(.15)
    '''had to put the event.getKeys('q') in the above if statements, otherwise
    it was never being called and I could not quit the program'''