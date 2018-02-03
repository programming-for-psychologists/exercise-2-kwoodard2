'''Output the response times (in ms, e.g., 453 for 453 ms) and accuracy 
(1 for correct, 0 for incorrect) to a file output.txt. Output one line per 
trial: each line should contain the accuracy (1 or 0) and the response 
time (in milliseconds).'''

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
    Accuracy = ''
    RT_capturer.reset()
    if nameCategory == firstNames:
        response = event.waitKeys(maxWait=1.0,keyList='fql')
        if response == None:
            RT = 'None'
            Accuracy = '0'
            incorrect.draw()
            win.flip()
            core.wait(.5)
        elif 'q' in response:
            break
        elif 'f' in response:
            RT = RT_capturer.getTime()*1000
            Accuracy = '1'
            correct.draw()
            win.flip()
            core.wait(.5)
        elif 'l' in response:
            RT = RT_capturer.getTime()*1000
            Accuracy = '0'
            incorrect.draw()
            win.flip()
            core.wait(.5)  
    if nameCategory == lastNames:
        response = event.waitKeys(maxWait=1.0,keyList='lqf')
        if response == None:
            RT = 'None'
            Accuracy = '0'
            incorrect.draw()
            win.flip()
            core.wait(.5)
        elif 'q' in response:
            break
        elif 'l' in response:
            RT = RT_capturer.getTime()*1000
            Accuracy = '1'
            correct.draw()
            win.flip()
            core.wait(.5)
        elif 'f' in response:
            RT = RT_capturer.getTime()*1000
            Accuracy = '0'
            incorrect.draw()
            win.flip()
            core.wait(.5)
    win.flip()
    core.wait(.15)
    with open('output.txt','a') as f:
        f.write(Accuracy + ' ' + str(RT) + '\n')
