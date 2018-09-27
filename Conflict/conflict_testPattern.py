#!/usr/bin/env python2

# This script shows boxes in the stimulus locations for the conflict task
# Press "q" to exit
# This can be put on the screen while putting the subject in the scanner
# in order to make sure the relevant locations are visible and centered.

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import core, data, event, logging, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys
from psychopy import visual, sound

# Setup the Window
win = visual.Window(size=(1200, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, waitBlanking=True
    )

# General stimulus parameters: image size and position in units of screen height
imageWidth = 0.24 
imageHeight = 0.32
posNorth = [0, 0.22]
posSouth = [0, -0.22]
posWest = [-0.30, 0]
posEast = [0.30, 0]

CueImage1 = visual.Rect(win=win, name='FrameNorth',units='height', 
    width=imageWidth, height=imageHeight,
    ori=0, pos=posNorth,
    lineWidth=0, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[0.5,0.5,0.5], fillColorSpace='rgb',
    opacity=1,interpolate=True)

# Visual test image (to make sure all positions are fully visibls)
CueImage1.pos = posNorth
CueImage1.draw()
CueImage1.pos = posSouth
CueImage1.draw()
CueImage1.pos = posWest
CueImage1.draw()
CueImage1.pos = posEast
CueImage1.draw()
win.flip()
event.waitKeys(keyList=["q"])
