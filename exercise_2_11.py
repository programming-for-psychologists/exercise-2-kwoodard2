'''Rainbow Font'''

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1].strip() for name in names]
colorList = ['red','green','white','blue','yellow','gray','cyan','crimson','indigo']

nameChoice = [firstNames,lastNames]


win = visual.Window([800,600],color="black", units='pix')
nameStim = visual.TextStim(win,text="", height=40,pos=[0,0])
fixationCross = visual.TextStim(win,text="+", height=40, pos=[0,0])
correct = visual.TextStim(win,text="O", height=40, pos=[0,0])
incorrect = visual.TextStim(win,text="X", height=40, pos=[0,0])

RT_capturer = core.Clock()
while True:
    nameCategory = random.choice(nameChoice)
    nameShown = random.choice(nameCategory)
    nameStim.setColor(random.choice(colorList))
    nameStim.setText(nameShown)
    fixationCross.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    nameStim.draw()
    win.flip()
    if nameCategory == firstNames:
        response = event.waitKeys(maxWait=1.0,keyList='fql')
        if response == None:
            incorrect.setColor(random.choice(colorList))
            incorrect.draw()
            win.flip()
            core.wait(.5)
        elif 'q' in response:
            break
        elif 'f' in response:
            correct.setColor(random.choice(colorList))
            correct.draw()
            win.flip()
            core.wait(.5)
        elif 'l' in response:
            incorrect.setColor(random.choice(colorList))
            incorrect.draw()
            win.flip()
            core.wait(.5)  
    if nameCategory == lastNames:
        response = event.waitKeys(maxWait=1.0,keyList='lqf')
        if response == None:
            incorrect.setColor(random.choice(colorList))
            incorrect.draw()
            win.flip()
            core.wait(.5)
        elif 'q' in response:
            break
        elif 'l' in response:
            correct.setColor(random.choice(colorList))
            correct.draw()
            win.flip()
            core.wait(.5)
        elif 'f' in response:
            incorrect.setColor(random.choice(colorList))
            incorrect.draw()
            win.flip()
            core.wait(.5)
    win.flip()
    core.wait(.15)