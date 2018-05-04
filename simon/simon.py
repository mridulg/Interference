#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.1),
    on Fri May  4 13:48:23 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'simon'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u'', u'counterbalance': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text="SIMON TASK\n\nallowed keys = 'm', 'z'\n\nif Correlation = 0\nX = right\nO = left\n\nif Correlation = 1\nX = left\nO = right\n",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "setup"
setupClock = core.Clock()


# Initialize components for Routine "simonTrial"
simonTrialClock = core.Clock()
leftStim = visual.TextStim(win=win, name='leftStim',
    text='default text',
    font='Arial',
    pos=(-0.5, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
rightStim = visual.TextStim(win=win, name='rightStim',
    text='default text',
    font='Arial',
    pos=(0.5, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
ITI = visual.ImageStim(
    win=win, name='ITI',
    image='/Users/mridul/Downloads/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instrResponse = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsComponents = [text, instrResponse]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *instrResponse* updates
    if t >= 0.0 and instrResponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrResponse.tStart = t
        instrResponse.frameNStart = frameN  # exact frame index
        instrResponse.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if instrResponse.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('experiment.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "setup"-------
    t = 0
    setupClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if expInfo['counterbalance']=='0':
     bindings = {'X':'m', 'O':'z'}
     if thisTrial['condition']=='incongruent' and thisTrial['stim']=='X':
      leftStimText = thisTrial['stim']
      rightStimText = ''
      ans = 'm'
     elif thisTrial['condition']=='incongruent' and thisTrial['stim']=='0':
      rightStimText = thisTrial['stim']
      leftStimText = ''
      ans = 'z'
    
     elif thisTrial['condition']=='congruent' and thisTrial['stim']=='X':
      rightStimText = thisTrial['stim']
      leftStimText = ''
      ans = 'm'
     elif thisTrial['condition']=='congruent' and thisTrial['stim']=='0':
      leftStimText = thisTrial['stim']
      rightStimText = ''
      ans = 'z'
    elif expInfo['counterbalance']=='1':
     bindings = {'X':'z', 'O':'m'}
     if thisTrial['condition']=='incongruent' and thisTrial['stim']=='X':
      rightStimText = thisTrial['stim']
      leftStimText = ''
      ans = 'z'
     elif thisTrial['condition']=='incongruent' and thisTrial['stim']=='0':
      leftStimText = thisTrial['stim']
      rightStimText = ''
      ans = 'm'
    
     elif thisTrial['condition']=='congruent' and thisTrial['stim']=='X':
      leftStimText = thisTrial['stim']
      rightStimText = ''
      ans = 'z'
     elif thisTrial['condition']=='congruent' and thisTrial['stim']=='0':
      rightStimText = thisTrial['stim']
      leftStimText = ''
      ans = 'm'
    # keep track of which components have finished
    setupComponents = []
    for thisComponent in setupComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "setup"-------
    while continueRoutine:
        # get current time
        t = setupClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in setupComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "setup"-------
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "simonTrial"-------
    t = 0
    simonTrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    leftStim.setText(leftStimText)
    rightStim.setText(rightStimText)
    response = event.BuilderKeyResponse()
    # keep track of which components have finished
    simonTrialComponents = [leftStim, rightStim, ITI, response, fixation]
    for thisComponent in simonTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "simonTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = simonTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *leftStim* updates
        if t >= 0.0 and leftStim.status == NOT_STARTED:
            # keep track of start time/frame for later
            leftStim.tStart = t
            leftStim.frameNStart = frameN  # exact frame index
            leftStim.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if leftStim.status == STARTED and t >= frameRemains:
            leftStim.setAutoDraw(False)
        
        # *rightStim* updates
        if t >= 0.0 and rightStim.status == NOT_STARTED:
            # keep track of start time/frame for later
            rightStim.tStart = t
            rightStim.frameNStart = frameN  # exact frame index
            rightStim.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if rightStim.status == STARTED and t >= frameRemains:
            rightStim.setAutoDraw(False)
        
        # *ITI* updates
        if t >= 1.0 and ITI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ITI.tStart = t
            ITI.frameNStart = frameN  # exact frame index
            ITI.setAutoDraw(True)
        frameRemains = 1.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ITI.status == STARTED and t >= frameRemains:
            ITI.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.2 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.2 + 1.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if response.status == STARTED and t >= frameRemains:
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['z', 'm'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                response.keys = theseKeys[-1]  # just the last key pressed
                response.rt = response.clock.getTime()
                # was this 'correct'?
                if (response.keys == str(ans)) or (response.keys == ans):
                    response.corr = 1
                else:
                    response.corr = 0
        
        # *fixation* updates
        if t >= 0.0 and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t
            fixation.frameNStart = frameN  # exact frame index
            fixation.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation.status == STARTED and t >= frameRemains:
            fixation.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in simonTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "simonTrial"-------
    for thisComponent in simonTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys=None
        # was no response the correct answer?!
        if str(ans).lower() == 'none':
           response.corr = 1  # correct non-response
        else:
           response.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('response.keys',response.keys)
    trials.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        trials.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 3 repeats of 'trials'


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
