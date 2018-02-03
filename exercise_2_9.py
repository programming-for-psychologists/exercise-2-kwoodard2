'''Compute response times'''

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
correct = visual.TextStim(win,text="O", height=40, color="green",pos=[0,0])
incorrect = visual.TextStim(win,text="X", height=40, color="red",pos=[0,0])

RT_capturer = core.Clock()
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
    RT = ''
    RT_capturer.reset()
    if nameCategory == firstNames:
        response = event.waitKeys(maxWait=1.0,keyList='fqlspace')
        if response == None:
            RT = 'None'
            incorrect.draw()
            win.flip()
            core.wait(.5)
        elif 'q' in response:
            break
        elif 'f' in response:
            RT = RT_capturer.getTime()
            correct.draw()
            win.flip()
            core.wait(.5)
        elif 'l' in response:
            RT = RT_capturer.getTime()
            incorrect.draw()
            win.flip()
            core.wait(.5)  
    if nameCategory == lastNames:
        response = event.waitKeys(maxWait=1.0,keyList='lqfspace')
        if response == None:
            RT = 'None'
            incorrect.draw()
            win.flip()
            core.wait(.5)
        elif 'q' in response:
            break
        elif 'l' in response:
            RT = RT_capturer.getTime()
            correct.draw()
            win.flip()
            core.wait(.5)
        elif 'f' in response:
            RT = RT_capturer.getTime()
            incorrect.draw()
            win.flip()
            core.wait(.5)
    print RT
    win.flip()
    core.wait(.15)