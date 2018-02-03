'''Pop up a box that accepts a first name, and check to make sure that the 
name exists. If it doesn't, pop-up a 'Name does not exist'error box'''

import time
import sys
import random
from psychopy import visual,event,core,gui

names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1].strip() for name in names]

#setup
popup = gui.Dlg()
popup.addText('Enter a first name:')
popup.addField('Name:')
errorBox = gui.Dlg()
errorBox.addText('Name does not exist')

#show box
popup.show()
if popup.OK and popup.data not in firstNames:
    errorBox.show()
