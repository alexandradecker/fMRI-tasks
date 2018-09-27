#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Thu Jul 14 10:25:47 2016
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
from datetime import datetime
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
expName = 'Gambling'

# Collect run mode and participant ID
expInfo = {}
#check if current subject files already exists (by checking files created today)
date_stamp = data.getDateStr(format="%Y_%b_%d")
existingCurrentBANDA = glob.glob('C:/Users/banda/Documents/tfMRI_output/**/*'+date_stamp+'*')
selectedruns = []

if not existingCurrentBANDA:
    dlg1 = gui.Dlg(title="Participant ID")
    dlg1.addField('Participant')
    dlg1.addField('Mode', choices=["Scanner", "Practice"])
    #dlg1.addField('Group', choices=["HC", "MDD"])
    #dlg1.addField('Session', choices=["ABCD","IPAT2","CMRR"])
    dlg1.addField('Run(Default)', choices= ["AB"])
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
            dlg1Runs.show()
            if dlg1Runs.OK:
                expInfo["run"] = "Custom"
                for index in range(len(dlg1Runs.data)):
                    if index == 0 and dlg1Runs.data[index]: selectedruns.append("A")
                    elif index == 1 and dlg1Runs.data[index]: selectedruns.append("B")

                print selectedruns
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
    dlg1.addField('Run(Default)', choices= ["AB"])
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
            dlg1Runs.show()
            if dlg1Runs.OK:
                expInfo["run"] = "Custom"
                for index in range(len(dlg1Runs.data)):
                    if index == 0 and dlg1Runs.data[index]: selectedruns.append("A")
                    elif index == 1 and dlg1Runs.data[index]: selectedruns.append("B")
                print selectedruns
        else:
            expInfo['run'] = dlg1.data[2]

        RunMode = expInfo['runMode']
    else:
        core.quit() # user pressed cancel

expName = 'Gambling'
expInfo['expName'] = expName
expInfo['date'] = data.getDateStr()  # add a simple timestamp


if expInfo['runMode'] != "Practice":
        if expInfo["run"] == "Custom":
                runs = selectedruns
                expInfo["run"] = ''.join(selectedruns)
	else:
		runs=["A","B"]	
else:
	runs=["Practice"]

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
#filename = 'data/'+expInfo['participant']+ os.path.sep + '%s_%s_%s_%s_%s' %(expInfo['participant'],expInfo['session'],expInfo['run'],expName,expInfo['date'])
filename = output + os.sep + expInfo['participant'] + os.sep +'%s_%s_%s_%s_%s' %(expInfo['participant'],expInfo['runMode'],expInfo['run'],expInfo['expName'],expInfo['date'])

money=0.0

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

# Start Code - component code to be run before the window creation

# Setup the Window 
win = visual.Window(  fullscr=True,screen=1, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "block_creator_code"
block_creator_codeClock = core.Clock()
import random
import csv
#Trials pseudorandomization
"""
reward_blocks=['reward_ll.csv','reward_nl.csv','reward_nn.csv']
loss_blocks=['loss_rr.csv','loss_rn.csv','loss_nn.csv']

reward_blocks_A = random.sample(reward_blocks,2)
reward_blocks_B = random.sample(reward_blocks,2)
loss_blocks_A = random.sample(loss_blocks,2)
loss_blocks_B = random.sample(loss_blocks,2)

all_run_blocks_A=reward_blocks_A+loss_blocks_A
random.shuffle(all_run_blocks_A)

all_run_blocks_B=reward_blocks_B+loss_blocks_B
random.shuffle(all_run_blocks_B)

all_run_blocks_A=['loss_rr.csv','reward_ll.csv','reward_nl.csv','loss_rn.csv']
all_run_blocks_B=['reward_nn.csv','loss_nn.csv','loss_rr.csv','reward_ll.csv']


with open('all_blocks_list_A.csv', 'wb') as csvfile:
	    writer = csv.DictWriter(csvfile, fieldnames = ["trial_blocks"])
	    writer.writeheader()
	    for i in all_run_blocks_A:
	        print>>csvfile, i
with open('all_blocks_list_B.csv', 'wb') as csvfile:
	    writer = csv.DictWriter(csvfile, fieldnames = ["trial_blocks"])
	    writer.writeheader()
	    for i in all_run_blocks_B:
	        print>>csvfile, i

"""
down_targets=[1,2,3,4]
up_targets=[6,7,8,9]
all_targets=down_targets+up_targets
targets=random.sample(all_targets,8)

print targets

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()

instructions_text = visual.TextStim(win=win, ori=0, name='instructions_text',
    text='Instructions:\n\nWhen you see a "?", guess if the coming number is higher or lower than 5.\nIf you guess correctly you win $1. \nIf you guess incorrectly you lose $0.50. \nIf the number is 5 no money is won or lost.\n\nPress any button to start.',    font='Arial',
    pos=[0, 0], height=0.1,  wrapWidth=1.5,	
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
instructions_text_pressI = visual.TextStim(win=win, ori=0, name='instructions_text',
    text='If you think it is higher than 5, press your index finger button. (press it now!)',    font='Arial',
    pos=[0, 0], height=0.1,  wrapWidth=1.5,	
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
instructions_text_pressM = visual.TextStim(win=win, ori=0, name='instructions_text',
    text='If you think it is lower than 5, press your middle finger button. (press it now!)',    font='Arial',
    pos=[0, 0], height=0.1,  wrapWidth=1.5,	
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
# \n . \n \n\n

# Initialize components for Routine "trigger"
triggerClock = core.Clock()
trigger_text = visual.TextStim(win=win, ori=0, name='trigger_text',
    text=u'Waiting for the scanner.', 
    pos=[0, 0], height=0.1, wrapWidth=1.5,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_text = visual.TextStim(win=win, ori=0, name='fixation_text',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
ISI_text = visual.TextStim(win=win, ori=0, name='ISI_text',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial_sign"
trial_signClock = core.Clock()
trial_sing_text = visual.TextStim(win=win, ori=0, name='trial_sing_text',
    text=u'?',    font=u'Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial_card_code"
trial_card_codeClock = core.Clock()

# Initialize components for Routine "trial_card"
trial_cardClock = core.Clock()
trial_card_text = visual.TextStim(win=win, ori=0, name='trial_card_text',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trail_feedback"
trail_feedbackClock = core.Clock()
trial_feedback_image = visual.ImageStim(win=win, name='trial_feedback_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
feedback_text = visual.TextStim(win=win, ori=0, name='feedback_text',
    text='default text',    font=u'Arial',
    pos=[0, -0.3], height=0.15, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanks_text = visual.TextStim(win=win, ori=0, name='thanks_text',
    text=u'Thanks!',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "afterTriggerClock"
afterTriggerClock = core.Clock()


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "block_creator_code"-------
t = 0
block_creator_codeClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

# keep track of which components have finished
block_creator_codeComponents = []
for thisComponent in block_creator_codeComponents:
    if hasattr(thisComponent, 'status'):
	thisComponent.status = NOT_STARTED

#-------Start Routine "block_creator_code"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = block_creator_codeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
	break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block_creator_codeComponents:
	if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
	    continueRoutine = True
	    break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
	core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
	win.flip()

#-------Ending Routine "block_creator_code"-------
for thisComponent in block_creator_codeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
	thisComponent.setAutoDraw(False)

# the Routine "block_creator_code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instructions"-------
preinstructions_text = visual.TextStim(win=win, ori=0, name='preinstructions_text',
    text='You are going to play a guessing game, where you will get to win or lose actual money! \n\nPress any key to continue.',    font='Arial',
    pos=[0, 0], height=0.1,  wrapWidth=1.5,	
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
preinstructions_text.draw()	
win.flip()
event.waitKeys(keyList=["1","2","3","4","5","6","7","8","9","0","space", "escape"])  
t = 0
instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instructions_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instructions_key_resp.status = NOT_STARTED
# keep track of which components have finished
instructionsComponents = []
instructionsComponents.append(instructions_text)
instructionsComponents.append(instructions_key_resp)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
	thisComponent.status = NOT_STARTED

#-------Start Routine "instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_text* updates
    if t >= 0.0 and instructions_text.status == NOT_STARTED:
	# keep track of start time/frame for later
	instructions_text.tStart = t  # underestimates by a little under one frame
	instructions_text.frameNStart = frameN  # exact frame index
	instructions_text.setAutoDraw(True)
    
    # *instructions_key_resp* updates
    if t >= 0.0 and instructions_key_resp.status == NOT_STARTED:
	# keep track of start time/frame for later
	instructions_key_resp.tStart = t  # underestimates by a little under one frame
	instructions_key_resp.frameNStart = frameN  # exact frame index
	instructions_key_resp.status = STARTED
	# keyboard checking is just starting
	instructions_key_resp.clock.reset()  # now t=0
	event.clearEvents(eventType='keyboard')
    if instructions_key_resp.status == STARTED:
	theseKeys = event.getKeys(keyList=['1', '2', '9','8','3', '4','5','0','left', 'right', 'space'])
	
	# check for quit:
	if "escape" in theseKeys:
	    endExpNow = True
	if len(theseKeys) > 0:  # at least one key was pressed
	    instructions_key_resp.keys = theseKeys[-1]  # just the last key pressed
	    instructions_key_resp.rt = instructions_key_resp.clock.getTime()
	    # a response ends the routine
	    continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
	break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
	if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
	    continueRoutine = True
	    break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
	core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
	win.flip()

#-------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
	thisComponent.setAutoDraw(False)
# check responses
if instructions_key_resp.keys in ['', [], None]:  # No response was made
   instructions_key_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('instructions_key_resp.keys',instructions_key_resp.keys)
if instructions_key_resp.keys != None:  # we had a response
    thisExp.addData('instructions_key_resp.rt', instructions_key_resp.rt)

instructions_text_pressI.draw()
win.flip()
event.waitKeys(keyList=["1",'9'])


instructions_text_pressM.draw()
win.flip()
event.waitKeys(keyList=["2",'8'])

thisExp.nextEntry()
for r in runs:
	expInfo['run']=r
        if expInfo['runMode']!="Practice":
            msgExpter = visual.TextStim(win,text="Waiting for the experimenter.",
        pos=(0,0),colorSpace='rgb',color=1,height=0.1,wrapWidth=1.5,depth=0.01)
            msgExpter.draw()
            win.flip()
            event.waitKeys(keyList=["q"])
        # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
	routineTimer.reset()

        if expInfo['runMode']!="Practice":
            #------Prepare to start Routine "trigger"-------
            t = 0
            triggerClock.reset()  # clock 
            frameN = -1
            # update component parameters for each repeat
            triger_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
            triger_key_resp.status = NOT_STARTED
            # keep track of which components have finished
            triggerComponents = []
            triggerComponents.append(trigger_text)
            triggerComponents.append(triger_key_resp)
            for thisComponent in triggerComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            #-------Start Routine "trigger"-------
            continueRoutine = True
            while continueRoutine:
                # get current time
                t = triggerClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *trigger_text* updates
                if t >= 0.0 and trigger_text.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    trigger_text.tStart = t  # underestimates by a little under one frame
                    trigger_text.frameNStart = frameN  # exact frame index
                    trigger_text.setAutoDraw(True)
                
                # *triger_key_resp* updates
                if t >= 0.0 and triger_key_resp.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    triger_key_resp.tStart = t  # underestimates by a little under one frame
                    triger_key_resp.frameNStart = frameN  # exact frame index
                    triger_key_resp.status = STARTED
                    # keyboard checking is just starting
                    triger_key_resp.clock.reset()  # now t=0
                    event.clearEvents(eventType='keyboard')
                if triger_key_resp.status == STARTED:
                    theseKeys = event.getKeys(keyList=['equal', 'plus', 't', 'right', 'space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        triger_key_resp.keys = theseKeys[-1]  # just the last key pressed
                        triger_key_resp.rt = triger_key_resp.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in triggerComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            #-------Ending Routine "trigger"-------
            for thisComponent in triggerComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if triger_key_resp.keys in ['', [], None]:  # No response was made
               triger_key_resp.keys=None
            # store data for thisExp (ExperimentHandler)
            thisExp.addData('triger_key_resp.keys',triger_key_resp.keys)
            if triger_key_resp.keys != None:  # we had a response
                thisExp.addData('triger_key_resp.rt', triger_key_resp.rt)
            thisExp.nextEntry()
            # the Routine "trigger" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            #TEST TIMER testtimeClock = core.MonotonicClock()

	# set up handler to look after randomisation of conditions etc
	trials = data.TrialHandler(nReps=1, method='sequential', 
	    extraInfo=expInfo, originPath=None,
	    trialList=data.importConditions(u'all_blocks_list_'+expInfo['run']+'.csv'),
	    seed=None, name='trials')
        """
	if expInfo['run']=='A':
	    print  "run list A:",all_run_blocks_A
	else:
	    print  "run B:",all_run_blocks_B
	"""
	thisExp.addLoop(trials)  # add the loop to the experiment
	thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
	# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
	if thisTrial != None:
	    for paramName in thisTrial.keys():
		exec(paramName + '= thisTrial.' + paramName)




	for thisTrial in trials:
	    currentLoop = trials
	    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
	    if thisTrial != None:
		for paramName in thisTrial.keys():
		    exec(paramName + '= thisTrial.' + paramName)
	    
	    #------Prepare to start Routine "fixation"-------
	    t = 0
	    fixationClock.reset()  # clock 
	    frameN = -1
	    routineTimer.add(.1500000)
	    # update component parameters for each repeat
	    # keep track of which components have finished
	    fixationComponents = []
	    fixationComponents.append(fixation_text)
	    for thisComponent in fixationComponents:
		if hasattr(thisComponent, 'status'):
		    thisComponent.status = NOT_STARTED
	    
	    #-------Start Routine "fixation"-------
	    continueRoutine = True
	    while continueRoutine and routineTimer.getTime() > 0:
		# get current time
		t = fixationClock.getTime()
		frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
		# update/draw components on each frame
		
		# *fixation_text* updates
		if t >= 0.0 and fixation_text.status == NOT_STARTED:
		    # keep track of start time/frame for later
		    fixation_text.tStart = t  # underestimates by a little under one frame
		    fixation_text.frameNStart = frameN  # exact frame index
		    fixation_text.setAutoDraw(True)
		if fixation_text.status == STARTED and t >= (0.0 + (15-win.monitorFramePeriod*0.75)): #most of one frame period left
		    fixation_text.setAutoDraw(False)
		
		# check if all components have finished
		if not continueRoutine:  # a component has requested a forced-end of Routine
		    break
		continueRoutine = False  # will revert to True if at least one component still running
		for thisComponent in fixationComponents:
		    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
		        continueRoutine = True
		        break  # at least one component has not yet finished
		
		# check for quit (the Esc key)
		if endExpNow or event.getKeys(keyList=["escape"]):
		    core.quit()
		
		# refresh the screen
		if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
		    win.flip()
	    
	    #-------Ending Routine "fixation"-------
	    for thisComponent in fixationComponents:
		if hasattr(thisComponent, "setAutoDraw"):
		    thisComponent.setAutoDraw(False)

		
	     
	    
	    # set up handler to look after randomisation of conditions etc
	    current_trial = data.TrialHandler(nReps=1, method='sequential', 
		extraInfo=expInfo, originPath=None,
		trialList=data.importConditions(trial_blocks),
		seed=None, name='current_trial')
	    thisExp.addLoop(current_trial)  # add the loop to the experiment
	    thisCurrent_trial = current_trial.trialList[0]  # so we can initialise stimuli with some values
	    # abbreviate parameter names if possible (e.g. rgb=thisCurrent_trial.rgb)
	    if thisCurrent_trial != None:
		for paramName in thisCurrent_trial.keys():
		    exec(paramName + '= thisCurrent_trial.' + paramName)
	    
	    for thisCurrent_trial in current_trial:
		currentLoop = current_trial
		# abbreviate parameter names if possible (e.g. rgb = thisCurrent_trial.rgb)
		if thisCurrent_trial != None:
		    for paramName in thisCurrent_trial.keys():
		        exec(paramName + '= thisCurrent_trial.' + paramName)
		
		#------Prepare to start Routine "ISI"-------
		t = 0
		ISIClock.reset()  # clock 
		frameN = -1
		routineTimer.add(.1000000)
		# update component parameters for each repeat
		# keep track of which components have finished
		ISIComponents = []
		ISIComponents.append(ISI_text)
		for thisComponent in ISIComponents:
		    if hasattr(thisComponent, 'status'):
		        thisComponent.status = NOT_STARTED
	       
		#-------Start Routine "ISI"-------
		continueRoutine = True
		while continueRoutine and routineTimer.getTime() > 0:
		    # get current time
		    t = ISIClock.getTime()
		    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
		    # update/draw components on each frame
		    
		    # *ISI_text* updates
		    if t >= 0.0 and ISI_text.status == NOT_STARTED:
		        # keep track of start time/frame for later
		        ISI_text.tStart = t  # underestimates by a little under one frame
		        ISI_text.frameNStart = frameN  # exact frame index
		        ISI_text.setAutoDraw(True)
		    if ISI_text.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
		        ISI_text.setAutoDraw(False)
		    
		    # check if all components have finished
		    if not continueRoutine:  # a component has requested a forced-end of Routine
		        break
		    continueRoutine = False  # will revert to True if at least one component still running
		    for thisComponent in ISIComponents:
		        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
		            continueRoutine = True
		            break  # at least one component has not yet finished
		    
		    # check for quit (the Esc key)
		    if endExpNow or event.getKeys(keyList=["escape"]):
		        core.quit()
		    
		    # refresh the screen
		    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
		        win.flip()
		
		#-------Ending Routine "ISI"-------
		for thisComponent in ISIComponents:
		    if hasattr(thisComponent, "setAutoDraw"):
		        thisComponent.setAutoDraw(False)
		
		#------Prepare to start Routine "trial_sign"-------
		t = 0
		trial_signClock.reset()  # clock 
		frameN = -1
		routineTimer.add(.1500000)
		# update component parameters for each repeat
		trial_sign_key_reso = event.BuilderKeyResponse()  # create an object of type KeyResponse
		trial_sign_key_reso.status = NOT_STARTED
		# keep track of which components have finished
		trial_signComponents = []
		trial_sing_text.setText('?')
		trial_sing_text.hight=0.15
		trial_signComponents.append(trial_sing_text)
		trial_signComponents.append(trial_sign_key_reso)
		for thisComponent in trial_signComponents:
		    if hasattr(thisComponent, 'status'):
		        thisComponent.status = NOT_STARTED
		
		#-------Start Routine "trial_sign"-------
		continueRoutine = True
		allPressedKeys=[]	
		allPressedKeysTime=[]
		while continueRoutine and routineTimer.getTime() > 0:
		    # get current time
		    t = trial_signClock.getTime()
		    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
		    # update/draw components on each frame
		    
		    # *trial_sing_text* updates
		    if t >= 0.0 and trial_sing_text.status == NOT_STARTED:
		        # keep track of start time/frame for later
		        trial_sing_text.tStart = t  # underestimates by a little under one frame
		        trial_sing_text.frameNStart = frameN  # exact frame index
		        trial_sing_text.setAutoDraw(True)
		    if trial_sing_text.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
		        trial_sing_text.setAutoDraw(False)
		    
		    # *trial_sign_key_reso* updates
		    if t >= 0.0 and trial_sign_key_reso.status == NOT_STARTED:
		        # keep track of start time/frame for later
		        trial_sign_key_reso.tStart = t  # underestimates by a little under one frame
		        trial_sign_key_reso.frameNStart = frameN  # exact frame index
		        trial_sign_key_reso.status = STARTED
		        # keyboard checking is just starting
		        trial_sign_key_reso.clock.reset()  # now t=0
		        event.clearEvents(eventType='keyboard')
		    if trial_sign_key_reso.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
		        trial_sign_key_reso.status = STOPPED
		    if trial_sign_key_reso.status == STARTED:
		        theseKeys = event.getKeys(keyList=['1', '2','8','9'])
		        
		        # check for quit:
		        if "escape" in theseKeys:
		            endExpNow = True
		        if len(theseKeys) > 0:  # at least one key was pressed
		            trial_sign_key_reso.keys = theseKeys[-1]  # just the last key pressed
		            trial_sign_key_reso.rt = trial_sign_key_reso.clock.getTime()
		            print '+', trial_sing_text.setText('+')
		       	    for k in theseKeys:
				allPressedKeys.append(k)	
			    	allPressedKeysTime.append(trial_sign_key_reso.clock.getTime())  
		    
		    # check if all components have finished
		    if not continueRoutine:  # a component has requested a forced-end of Routine
		        break
		    continueRoutine = False  # will revert to True if at least one component still running
		    for thisComponent in trial_signComponents:
		        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
		            continueRoutine = True
		            break  # at least one component has not yet finished
		    
		    # check for quit (the Esc key)
		    if endExpNow or event.getKeys(keyList=["escape"]):
		        core.quit()
		    
		    # refresh the screen
		    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
		        win.flip()
		
		#-------Ending Routine "trial_sign"-------
		for thisComponent in trial_signComponents:
		    if hasattr(thisComponent, "setAutoDraw"):
		        thisComponent.setAutoDraw(False)
		# check responses
		if trial_sign_key_reso.keys in ['', [], None]:  # No response was made
		   trial_sign_key_reso.keys=None
		# store data for current_trial (TrialHandler)
		current_trial.addData('trial_sign_key_reso.keys',trial_sign_key_reso.keys)
		if trial_sign_key_reso.keys != None:  # we had a response
		    current_trial.addData('trial_sign_key_reso.rt', trial_sign_key_reso.rt)
		current_trial.addData('allPressedKeys',str(allPressedKeys).replace(",",":"))
		current_trial.addData('allPressedKeysTime',str(allPressedKeysTime).replace(",",":"))
		print "keys pressed: ", allPressedKeys
		#------Prepare to start Routine "trial_card_code"-------
		t = 0
		trial_card_codeClock.reset()  # clock 
		frameN = -1
		# update component parameters for each repeat
		# keep track of which components have finished
		trial_card_codeComponents = []
		for thisComponent in trial_card_codeComponents:
		    if hasattr(thisComponent, 'status'):
		        thisComponent.status = NOT_STARTED
		
		#-------Start Routine "trial_card_code"-------
		continueRoutine = True
		while continueRoutine:
		    # get current time
		    t = trial_card_codeClock.getTime()
		    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
		    # update/draw components on each frame
		    
		    # check if all components have finished
		    if not continueRoutine:  # a component has requested a forced-end of Routine
		        break
		    continueRoutine = False  # will revert to True if at least one component still running
		    for thisComponent in trial_card_codeComponents:
		        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
		            continueRoutine = True
		            break  # at least one component has not yet finished
		    
		    # check for quit (the Esc key)
		    if endExpNow or event.getKeys(keyList=["escape"]):
		        core.quit()
		    
		    # refresh the screen
		    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
		        win.flip()
		
		#-------Ending Routine "trial_card_code"-------
		for thisComponent in trial_card_codeComponents:
		    if hasattr(thisComponent, "setAutoDraw"):
		        thisComponent.setAutoDraw(False)
		# the Routine "trial_card_code" was not non-slip safe, so reset the non-slip timer
		routineTimer.reset()
		
		#------Prepare to start Routine "trial_card"-------
		t = 0
		trial_cardClock.reset()  # clock 
		frameN = -1
		routineTimer.add(0.0500000)
		# update component parameters for each repeat
		trial_card_text.setText(trial_card)
		# keep track of which components have finished
		trial_cardComponents = []
		trial_cardComponents.append(trial_card_text)
		#print trial_card_text.text
		if trial_card_text.text=='win':
		    if trial_sign_key_reso.keys=='1' or trial_sign_key_reso.keys=='9':
		        this_round_targets=up_targets
		        trial_card_text.setText(random.choice(up_targets))
		        money= money+1
		    elif trial_sign_key_reso.keys=='2' or trial_sign_key_reso.keys=='8':
		        this_round_targets=down_targets
		        trial_card_text.setText(random.choice(down_targets))
		        money= money+1
		    else:
		        this_round_targets=[5,5,5,5]
		        trial_card_text.setText('no answer')
		        trial_feedback_image.setImage('neutral.png')
		        feedback_text.setText(' ')
		                                  
		                
		elif trial_card_text.text=='loose':
		    if trial_sign_key_reso.keys=='1' or trial_sign_key_reso.keys=='9':
		        this_round_targets=down_targets
		        trial_card_text.setText(random.choice(down_targets))
		        money= money-0.5
		    elif trial_sign_key_reso.keys=='2' or trial_sign_key_reso.keys=='8':
		        this_round_targets=up_targets
		        trial_card_text.setText(random.choice(up_targets))
		        money= money-0.5
		    else:
		        trial_card_text.setText('no answer')
		        trial_feedback_image.setImage('neutral.png')
		        feedback_text.setText(' ')
		                
		else:
		    trial_card_text.setText('5')
		               
		        
		print "money",money
		current_trial.addData('MoneyEarned',"$"+str(money))
	       
		for thisComponent in trial_cardComponents:
		    if hasattr(thisComponent, 'status'):
		        thisComponent.status = NOT_STARTED
		
		#-------Start Routine "trial_card"-------
		continueRoutine = True
		while continueRoutine and routineTimer.getTime() > 0:
		    # get current time
		    t = trial_cardClock.getTime()
		    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
		    # update/draw components on each frame
		    
		    # *trial_card_text* updates
		    if t >= 0.0 and trial_card_text.status == NOT_STARTED:
		        # keep track of start time/frame for later
		        trial_card_text.tStart = t  # underestimates by a little under one frame
		        trial_card_text.frameNStart = frameN  # exact frame index
		        trial_card_text.setAutoDraw(True)
		    if trial_card_text.status == STARTED and t >= (0.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
		        trial_card_text.setAutoDraw(False)
		    
		    # check if all components have finished
		    if not continueRoutine:  # a component has requested a forced-end of Routine
		        break
		    continueRoutine = False  # will revert to True if at least one component still running
		    for thisComponent in trial_cardComponents:
		        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
		            continueRoutine = True
		            break  # at least one component has not yet finished
		    
		    # check for quit (the Esc key)
		    if endExpNow or event.getKeys(keyList=["escape"]):
		        core.quit()
		    
		    # refresh the screen
		    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
		        win.flip()
		
		#-------Ending Routine "trial_card"-------
		for thisComponent in trial_cardComponents:
		    if hasattr(thisComponent, "setAutoDraw"):
		        thisComponent.setAutoDraw(False)
		
		#------Prepare to start Routine "trail_feedback"-------
		t = 0
		trail_feedbackClock.reset()  # clock 
		frameN = -1
		routineTimer.add(0.0500000)
		# update component parameters for each repeat
		if trial_card_text.text=='no answer':
		        trial_feedback_image.setImage('neutral.png')
		        feedback_text.setText(' ')
		else:
		    trial_feedback_image.setImage(trial_image)
		    feedback_text.setText(trial_feedback_text)
		   
		# keep track of which components have finished
		trail_feedbackComponents = []
		trail_feedbackComponents.append(trial_feedback_image)
		trail_feedbackComponents.append(feedback_text)
		for thisComponent in trail_feedbackComponents:
		    if hasattr(thisComponent, 'status'):
		        thisComponent.status = NOT_STARTED
		
		#-------Start Routine "trail_feedback"-------
		continueRoutine = True
		while continueRoutine and routineTimer.getTime() > 0:
		    # get current time
		    t = trail_feedbackClock.getTime()
		    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
		    # update/draw components on each frame
		    
		    # *trial_feedback_image* updates
		    if t >= 0.0 and trial_feedback_image.status == NOT_STARTED:
		        # keep track of start time/frame for later
		        trial_feedback_image.tStart = t  # underestimates by a little under one frame
		        trial_feedback_image.frameNStart = frameN  # exact frame index
		        trial_feedback_image.setAutoDraw(True)
		    if trial_feedback_image.status == STARTED and t >= (0.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
		        trial_feedback_image.setAutoDraw(False)
		    
		    # *feedback_text* updates
		    if t >= 0.0 and feedback_text.status == NOT_STARTED:
		        # keep track of start time/frame for later
		        feedback_text.tStart = t  # underestimates by a little under one frame
		        feedback_text.frameNStart = frameN  # exact frame index
		        feedback_text.setAutoDraw(True)
		    if feedback_text.status == STARTED and t >= (0.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
		        feedback_text.setAutoDraw(False)
		    
		    # check if all components have finished
		    if not continueRoutine:  # a component has requested a forced-end of Routine
		        break
		    continueRoutine = False  # will revert to True if at least one component still running
		    for thisComponent in trail_feedbackComponents:
		        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
		            continueRoutine = True
		            break  # at least one component has not yet finished
		    
		    # check for quit (the Esc key)
		    if endExpNow or event.getKeys(keyList=["escape"]):
		        core.quit()
		    
		    # refresh the screen
		    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
		        win.flip()
		
		#-------Ending Routine "trail_feedback"-------
		for thisComponent in trail_feedbackComponents:
		    if hasattr(thisComponent, "setAutoDraw"):
		        thisComponent.setAutoDraw(False)

                #TEST TIMER print testtimeClock.getTime()

		thisExp.nextEntry()
	     
		
	    # completed 1 repeats of 'current_trial'
	    thisExp.nextEntry()


	# completed 1 repeats of 'trials'
        logging.flush()
        tempfilename = output + os.sep + expInfo['participant'] + os.sep +'TEMP_' + '%s_%s_%s_%s_%s' %(expInfo['participant'],expInfo['runMode'],expInfo['run'],expInfo['expName'],expInfo['date'])
        thisExp.saveAsWideText(tempfilename,fileCollisionMethod='overwrite')

#------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock 
frameN = -1
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = []
thanksComponents.append(thanks_text)
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
	thisComponent.status = NOT_STARTED

#-------Start Routine "thanks"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks_text* updates
    if t >= 0.0 and thanks_text.status == NOT_STARTED:
	# keep track of start time/frame for later
	thanks_text.tStart = t  # underestimates by a little under one frame
	thanks_text.frameNStart = frameN  # exact frame index
	thanks_text.setAutoDraw(True)
    if thanks_text.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
	thanks_text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
	break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
	if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
	    continueRoutine = True
	    break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        continueRoutine=False
	#core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
	win.flip()

#-------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
	thisComponent.setAutoDraw(False)



#questionaire gambling
if expInfo['runMode']=="Scanner":
    #saving questionnaire data
    PossibleAnswers=[]
    PossibleInputs=[]
    thisExp.nextEntry()
    
    #question #1
    qst1 = visual.TextStim(win,text="Overall, do you think you won money, lost money, or did not win or lose money (broke even)? \n\n Press index finger button for Won \n Press middle finger button for Lost \n Press ring finger for Even", pos=(0,0),colorSpace='rgb',color=1,height=0.1,wrapWidth=1.5,depth=0.01)
    qst1.draw()	
    win.flip()
    ans1 = event.waitKeys(keyList=["1","2","3","9","8","7","space", "escape"])
    PossibleAnswers = (['Won', 'Lost', 'Even'])
    PossibleInputs = (['1','2','3','9','8','7'])
    thisExp.addData('Question','Do you think you won money, lost money, or broke even?')
    thisExp.addData('Answer',ans1)
    thisExp.addData('Possible Answers', str(PossibleAnswers).replace(",",":"))
    thisExp.addData('Possible Inputs', str(PossibleInputs).replace(",",":"))
    thisExp.nextEntry()
    
    if ans1==['1']: 
   	#if won
   	qst2= visual.TextStim(win,text="How much money do you think you won? Press: \n\n- Index finger button for A Little \n- Middle finger button for Average \n- Ring finger button for A Lot ", pos=(0,0),colorSpace='rgb',color=1,height=0.1,wrapWidth=1.5,depth=0.01)
   	qst2.draw()	
   	win.flip()
   	ans2 = event.waitKeys(keyList=["1","2","3","9","8","7","space", "escape"])   
   	PossibleAnswers = (['A Little', 'Average', 'A Lot'])
   	PossibleInputs = (['1','2','3','9','8','7'])
   	thisExp.addData('Question','How much do you think you won?')
   	thisExp.addData('Answer',ans2)
   	thisExp.addData('Possible Answers', str(PossibleAnswers).replace(",",":"))
   	thisExp.addData('Possible Inputs', str(PossibleInputs).replace(",",":"))
   	thisExp.nextEntry() 
    
   	qst3= visual.TextStim(win,text="Guess how much money you think you won? Press: \n\n- Index finger if between $0 and $5 \n- Middle finger if between $5 and $10 \n- Ring finger if between $10 and $15 \n- Pinky finger if between $15 or more", pos=(0,0),colorSpace='rgb',color=1,height=0.1,wrapWidth=1.5,depth=0.01)
   	qst3.draw()	
   	win.flip()
   	ans3 = event.waitKeys(keyList=["1","2","3","4","9","8","7","6","space", "escape"]) 
   	PossibleAnswers = (['0-5', '5-10', '10-15', '15+'])
   	PossibleInputs = (['1','2','3','4','9','8','7','6'])       
   	thisExp.addData('Question','Guess how much you won?')
   	thisExp.addData('Answer',ans3)
   	thisExp.addData('Possible Answers', str(PossibleAnswers).replace(",",":"))
   	thisExp.addData('Possible Inputs', str(PossibleInputs).replace(",",":"))
   	thisExp.nextEntry()     
    
    elif ans1==['2']:  
   	#if lost
   	qst4= visual.TextStim(win,text="How much money do you think you lost? Press: \n\n- Index finger button for A Little \n- Middle finger button for Average \n- Ring finger button for A Lot ", pos=(0,0),colorSpace='rgb',color=1,height=0.1,wrapWidth=1.5,depth=0.01)
   	qst4.draw()	
   	win.flip()
   	ans4 = event.waitKeys(keyList=["1","2","3","9","8","7","space", "escape"])
   	PossibleAnswers = (['A Little', 'Average', 'A Lot'])
   	PossibleInputs = (['1','2','3','9','8','7'])  
   	thisExp.addData('Question','How much do you think you lost?')
   	thisExp.addData('Answer',ans4)
   	thisExp.addData('Possible Answers', str(PossibleAnswers).replace(",",":"))
   	thisExp.addData('Possible Inputs', str(PossibleInputs).replace(",",":"))
   	thisExp.nextEntry() 
    
   	qst5= visual.TextStim(win,text="Guess how much money you think you lost? Press: \n\n- Index finger if between $0 and $5 \n- Middle finger if between $5 and $10 \n- Ring finger if between $10 and $15 \n- Pinky finger if between $15 or more", pos=(0,0),colorSpace='rgb',color=1,height=0.1,wrapWidth=1.5,depth=0.01)
   	qst5.draw()	
   	win.flip()
   	ans5 = event.waitKeys(keyList=["1","2","3","4","9","8","7","6","space", "escape"]) 
   	PossibleAnswers = (['0-5', '5-10', '10-15', '15+'])
   	PossibleInputs = (['1','2','3','4','9','8','7','6'])       
   	thisExp.addData('Question','Guess how much you lost?')
   	thisExp.addData('Answer',ans5)
   	thisExp.addData('Possible Answers', str(PossibleAnswers).replace(",",":"))
   	thisExp.addData('Possible Inputs', str(PossibleInputs).replace(",",":"))
   	thisExp.nextEntry()  

win.close()
core.quit()
