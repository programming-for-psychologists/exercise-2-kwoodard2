'''Extend the task by requiring the subject to respond by pressing a spacebar
 (the key is called 'space'), as quickly as possible anytime the name on the 
 screen matches the name you entered into the box (so if I enter 'Gary' 
 I would have to press 'space' anytime the name 'Gary' shows up. If the 
 participant presses 'space' to the wrong name (false alarm), or misses 
 the name (a miss), show a red X'''

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1].strip() for name in names]

nameChoice = [firstNames,lastNames]

popup = gui.Dlg()
popup.addText('Enter a first name:')
popup.addField('Name:')
errorBox = gui.Dlg()
errorBox.addText('Name does not exist')

#show box
popup.show()
if popup.OK and popup.data[0] not in firstNames:
    errorBox.show()

win = visual.Window([800,600],color="black", units='pix')
nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
fixationCross = visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])
correct = visual.TextStim(win,text="O", height=40, color="green",pos=[0,0])
incorrect = visual.TextStim(win,text="X", height=40, color="red",pos=[0,0])

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
        response = event.waitKeys(maxWait=1.0,keyList='fqlspace')
        if response == None:
            incorrect.draw()
            win.flip()
            core.wait(.5)
        elif 'q' in response:
            break
        elif nameShown in popup.data[0] and 'space' not in response:
            incorrect.draw()
            win.flip()
            core.wait(.5)
        elif 'space' in response and popup.data[0] in nameShown:
            correct.draw()
            win.flip()
            core.wait(.5)
        elif 'space' in response and popup.data[0] not in nameShown:
            incorrect.draw()
            win.flip()
            core.wait(.5)
        elif 'f' in response:
            correct.draw()
            win.flip()
            core.wait(.5)
        elif 'l' in response:
            incorrect.draw()
            win.flip()
            core.wait(.5)  
    if nameCategory == lastNames:
        response = event.waitKeys(maxWait=1.0,keyList='lqfspace')
        if response == None:
            incorrect.draw()
            win.flip()
            core.wait(.5)
        elif 'q' in response:
            break
        elif nameShown in popup.data[0] and 'space' not in response:
            incorrect.draw()
            win.flip()
            core.wait(.5)
        elif 'space' in response and popup.data[0] in nameShown:
            correct.draw()
            win.flip()
            core.wait(.5)
        elif 'space' in response and popup.data[0] not in nameShown:
            incorrect.draw()
            win.flip()
            core.wait(.5)
        elif 'l' in response:
            correct.draw()
            win.flip()
            core.wait(.5)
        elif 'f' in response:
            incorrect.draw()
            win.flip()
            core.wait(.5)
    win.flip()
    core.wait(.15)
    
    
#in future, keyList =['space','l','f'] the brackets fixes it