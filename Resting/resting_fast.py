#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
A preliminary version of this experiment was created using
PsychoPy2 Experiment Builder (v1.81.03), Tue Jan 20 10:30:57 2015

This script was then further modified by JTM (Jan-Feb 2015). 

If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import core, data, event, logging, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys
import csv
import glob


configFile=os.path.abspath( os.path.join(os.path.abspath(__file__), '../..'))
configFile=os.path.join(configFile,'config.csv')
if os.path.exists(configFile):
    with open(configFile, 'rb') as csvfile:
   	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
   	for row in spamreader:
  		if row[0]=="output":
 			output=row[1]
else:
    output=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../..',"tfMRI_output"))

    
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
expName = 'Resting'

# Collect run mode and participant ID
expInfo = {}
#check if current subject files already exists (by checking files created today)
date_stamp = data.getDateStr(format="%Y_%b_%d")
existingCurrentBANDA = glob.glob('C:/Users/banda/Documents/tfMRI_output/**/*'+date_stamp+'*')
selectedRuns = []

if not existingCurrentBANDA:
    dlg1 = gui.Dlg(title="Participant ID")
    dlg1.addField('Participant')
    dlg1.addField('Mode', choices=["Scanner", "Practice"])
    #dlg1.addField('Group', choices=["HC", "MDD"])
    #dlg1.addField('Session', choices=["ABCD","IPAT2","CMRR"])
    dlg1.addField('Run(Default)', choices= ["AB", "CD"])
    dlg1.addField('Custom Select Runs?', initial=False)
    dlg1.show()
    if dlg1.OK:  # then the user pressed OK
        # add the new entries to expInfo
        expInfo['participant'] = dlg1.data[0]
        expInfo['runMode'] = dlg1.data[1]
        #Custom Runs
        if dlg1.data[3]:
            dlg1Runs = gui.Dlg(title="Select Runs")
            dlg1Runs.addField('A',initial=False)
            dlg1Runs.addField('B',initial=False)
            dlg1Runs.addField('C',initial=False)
            dlg1Runs.addField('D',initial=False)
            dlg1Runs.show()
            if dlg1Runs.OK:
                expInfo["run"] = "Custom"
                for index in range(len(dlg1Runs.data)):
                    if index == 0 and dlg1Runs.data[index]: selectedRuns.append("A")
                    elif index == 1 and dlg1Runs.data[index]: selectedRuns.append("B")
                    elif index == 2 and dlg1Runs.data[index]: selectedRuns.append("C")
                    elif index == 3 and dlg1Runs.data[index]: selectedRuns.append("D")
                print selectedRuns
        else:
            expInfo['run'] = dlg1.data[2]
        expInfo['CB'] = "1" #dlg2.data[2]
        RunMode = expInfo['runMode']
    else:
        core.quit() # user pressed cancel
else:
    #retrieving participant ID from existing files
    BANDAfileSplit = existingCurrentBANDA[0].split('\\')
    currentBANDAname = BANDAfileSplit[1]
    print "Current Participant ID: " + currentBANDAname
    
    dlg1 = gui.Dlg(title=currentBANDAname)
    dlg1.addField('Participant ID',currentBANDAname)
    dlg1.addField('Mode', choices=["Scanner", "Practice"])
    #dlg1.addField('Group', choices=["HC", "MDD"])
    #dlg1.addField('Session', choices=["ABCD","IPAT2","CMRR"])
    dlg1.addField('Run(Default)', choices= ["AB", "CD"])
    dlg1.addField('Custom Select Runs?', initial=False)
    dlg1.show()
    if dlg1.OK:  # then the user pressed OK
        # add the new entries to expInfo
        expInfo['participant'] = currentBANDAname
        print dlg1.data[0]
        if dlg1.data[0]: expInfo['participant'] = dlg1.data[0]
        expInfo['runMode'] = dlg1.data[1]
        expInfo['CB'] = "1" #dlg2.data[2]
        #Custom Runs
        if dlg1.data[3]:
            dlg1Runs = gui.Dlg(title="Select Runs")
            dlg1Runs.addField('A',initial=False)
            dlg1Runs.addField('B',initial=False)
            dlg1Runs.addField('C',initial=False)
            dlg1Runs.addField('D',initial=False)
            dlg1Runs.show()
            if dlg1Runs.OK:
                expInfo["run"] = "Custom"
                for index in range(len(dlg1Runs.data)):
                    if index == 0 and dlg1Runs.data[index]: selectedRuns.append("A")
                    elif index == 1 and dlg1Runs.data[index]: selectedRuns.append("B")
                    elif index == 2 and dlg1Runs.data[index]: selectedRuns.append("C")
                    elif index == 3 and dlg1Runs.data[index]: selectedRuns.append("D")
                print selectedRuns
        else:
            expInfo['run'] = dlg1.data[2]

        RunMode = expInfo['runMode']
    else:
        core.quit() # user pressed cancel
        
if expInfo['runMode'] != "Practice":
        if expInfo["run"] == "Custom":
                runs = selectedRuns
                expInfo["run"] = ''.join(selectedRuns)
	elif expInfo["run"] == "AB":
		runs=["A","B"]
	elif expInfo["run"] == "CD":
		runs=["C","D"]
	
else:
	runs=["P"]

expInfo['expName'] = expName
expInfo['date'] = data.getDateStr()  # add a simple timestamp

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
#filename = 'data/'+expInfo['participant']+ os.path.sep + '%s_%s_%s_%s_%s' %(expInfo['participant'],expInfo['session'],expInfo['run'],expName,expInfo['date'])
filename = output + os.sep + expInfo['participant'] + os.sep +'%s_%s_%s_%s_%s' %(expInfo['participant'],expInfo['runMode'],expInfo['run'],expInfo['expName'],expInfo['date'])


# certain import statements were deferred till now because they
# interfere with dialog boxes
from psychopy import visual

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
# Setup the Window  
win = visual.Window(fullscr=True,size=(1200, 900), screen=1, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, waitBlanking=True
   )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess


# Initialize informational messages
msgInstr = visual.TextStim(win,text="Please keep your eyes open. This experiment will last 10 minutes.",
    pos=(0,0),alignHoriz='center',colorSpace='rgb',color=1,height=0.1,wrapWidth=1.5,depth=0.01)
msgExpter = visual.TextStim(win,text="Waiting for the experimenter.",
    pos=(0,0),colorSpace='rgb',color=1,height=0.1,wrapWidth=1.5,depth=0.01)
msgScanner = visual.TextStim(win,text="Waiting for the scanner.",
    pos=(0,0),colorSpace='rgb',color=1,height=0.1,wrapWidth=1.5,depth=0.01)
msgBlank = visual.TextStim(win,text="",
    pos=(0,0),colorSpace='rgb',color=1,height=0.1,wrapWidth=1.5,depth=0.01)
msgComplete = visual.TextStim(win,text="Task complete.",
    pos=(0,0),colorSpace='rgb',color=1,height=0.1,wrapWidth=1.5,depth=0.01)


#ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Fixation = visual.TextStim(win=win, ori=0, name='Fixation',
    text='+',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

msgInstr.draw()
win.flip()
event.waitKeys(keyList=["space"])

# set the cue positions
# Pre-block messages
# Message 1: waiting for the experimenter
for r in runs:
	expInfo['run'] = r
	if  expInfo['runMode'] != "Practice":
            msgExpter.draw()
            win.flip()
            event.waitKeys(keyList=["q"])
            # Message 2: waiting for the scanner
            msgScanner.draw()
            win.flip()
            event.waitKeys(keyList=["t","equal"])
	Fixation.draw()
	win.flip()
		  
	# check for quit (the Esc key)
	#event.waitKeys(keyList=["escape"])
	#TEST TIME testtimeClock = core.MonotonicClock()
	if  expInfo['runMode'] != "Practice":
		core.wait(1.0)
	else:
		core.wait(1)
 
	#msgComplete.draw()	
	#win.flip()
	#event.waitKeys(keyList=["q","space", "escape"])

	#saving questionnaire data
	PossibleAnswers=[]
	PossibleInputs=[]

	#questionaire resting 
	#question #1
	qst1 = visual.TextStim(win,text="Did you find yourself falling asleep or dozing off at any time during this task? \n\nPress index finger button for Yes \nPress middle finger button for No", pos=(0,0),colorSpace='rgb',color=1,height=0.1,wrapWidth=1.5,depth=0.01)
	qst1.draw()	
	win.flip()
	ans1 = event.waitKeys(keyList=["1","2","9","8","space", "escape"])
	PossibleAnswers = (['Yes', 'No'])
	PossibleInputs = (['1','2',"9","8"])
	thisExp.addData('Question','Fall asleep?')
	thisExp.addData('Answer',ans1)
	thisExp.addData('Possible Answers', str(PossibleAnswers).replace(",",":"))
	thisExp.addData('Possible Inputs', str(PossibleInputs).replace(",",":"))
	thisExp.nextEntry()


	#if event.getKeys(keyList=["1"]):
	if ans1 == ['1'] or ans1 == ['9']:
	    qst2= visual.TextStim(win,text="How many times? Press: \n\n- Thumb button for 1 time \n- Index finger button for 2 times \n- Middle finger button for 3 times \n- Ring finger button for 4 times \n- Pinky finger button for 5 or more times", pos=(0,0),colorSpace='rgb',color=1,height=0.1,wrapWidth=1.5,depth=0.01)
	    qst2.draw()	
	    win.flip()
	    ans2 = event.waitKeys(keyList=["1","2","3","4","5","0","9","8","7","6","space", "escape"]) 
	    PossibleAnswers = (['1 time', '2 times', '3 times', '4 times', '5 times'])
	    PossibleInputs = (['1','2','3','4','5',"0","9","8","7","6"])       
	    thisExp.addData('Question','How many times did you fall sleep?')
	    thisExp.addData('Answer',ans2)
	    thisExp.addData('Possible Answers', str(PossibleAnswers).replace(",",":"))
	    thisExp.addData('Possible Inputs', str(PossibleInputs).replace(",",":"))
	    thisExp.nextEntry()
    	
	qst3= visual.TextStim(win,text="Did you find your thoughts drifting/wandering between topics with no specific direction? \n\nPress index finger button for Yes \nPress middle finger button for No ", pos=(0,0),colorSpace='rgb',color=1,height=0.1,wrapWidth=1.5,depth=0.01)
	qst3.draw()	
	win.flip()
	ans3 = event.waitKeys(keyList=["1","2","9","8","space", "escape"]) 
	PossibleAnswers = (['Yes', 'No'])
	PossibleInputs = (['1','2',"9","8"])       
	thisExp.addData('Question','Thoughts drifted?')
	thisExp.addData('Answer',ans3)
	thisExp.addData('Possible Answers', str(PossibleAnswers).replace(",",":"))
	thisExp.addData('Possible Inputs', str(PossibleInputs).replace(",",":"))
	thisExp.nextEntry()


	#if event.getKeys(keyList=["1"]):
	if ans3 == ['1'] or ans3 == ['9']:
	    qst4= visual.TextStim(win,text="How often did you find your thoughts drifting/wandering? Press: \n\n- Thumb button for Almost Never \n- Index finger button for Sometimes \n- Middle finger button for Half the Time \n- Ring finger button for Often  \n- Pinky finger button for Always ", pos=(0,0),colorSpace='rgb',color=1,height=0.1,wrapWidth=1.5,depth=0.01)
	    qst4.draw()	
	    win.flip()       
	    ans4 = event.waitKeys(keyList=["1","2","3","4","5","0","9","8","7","6","space", "escape"])  
	    PossibleAnswers = (['Almost Never', 'Sometimes', 'Half the Time', 'Often', 'Always'])
	    PossibleInputs = (['1','2','3','4','5',"0",'9','8',"7","6"])      
	    thisExp.addData('Question','How many times did your thoughts drift?')
	    thisExp.addData('Answer',ans4)
	    thisExp.addData('Possible Answers', str(PossibleAnswers).replace(",",":"))
	    thisExp.addData('Possible Inputs', str(PossibleInputs).replace(",",":"))
	    thisExp.nextEntry()

        #save temporary log file
        logging.flush()
        tempfilename = output + os.sep + expInfo['participant'] + os.sep +'TEMP_' + '%s_%s_%s_%s_%s' %(expInfo['participant'],expInfo['runMode'],expInfo['run'],expInfo['expName'],expInfo['date'])
    	thisExp.saveAsWideText(tempfilename,fileCollisionMethod='overwrite')	
        #TEST TIME print testtimeClock.getTime()
  
# completed loop over runs

# Task-complete message


win.close()
core.quit()
