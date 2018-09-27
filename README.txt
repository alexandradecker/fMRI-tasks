2/21/2017
-added 'sad' face trials to face matching task
	* 6 more trials for each block in each run (18 more trials each for runs A and B)
-change 'percentage' calculator on terminal feed for face_matching and conflict. now includes skipped trials

12/7/2016
-Starting prompt changes:
	* Auto-fill participant ID if already exists
	* Revised 'Run' choices to reflect actual scans (only AB for gambling/facematching, ABCD for conflict)
	* Allow customizable runs (can pick and choose which runs to start)
-Adding "space" key exit for conflict task

12/1/2016
- Now that protocol calibration is over, several fields from the prompt ('CMRR, ABCD, etc.') were deleted
- Changed starting prompt so user does not have to input full participant ID each time when beginning a task


11/15/2016
- resting task: changed task time on practice mode from 4 seconds to 10 seconds
- face matching task: added real time notification of participant inputs, added notification of correct key per trial and total percentage correct in real time (before thisExp.nextEntry of each trial)
- gambling task: added real time notification of participant inputs ('print allPressedKeys')
- conflict task: added notification of correct key per trial and total percentage correct in real time (before thisExp.nextEntry of each trial)

All tasks: 
- added saveAsWideText for temporary data file at end of each trial set (after 1 run of 'trials') - for crash insurance
- added logging.flush() to end of each trial set (for resting state, added to end of questionnaire) 
- removed "waiting for..." screens on practice mode
        * resting: added if expInfo['runMode']!="Practice": qualifier (from "Message 1:waiting for experimenter" through "Message 2:waiting for scanner")
	* gambling: added if expInfo['runMode']!='Practice': qualifier (from "Prepare to start routine trigger" through "End routine trigger")
	* faceMatching: added if expInfo['runMode']!='Practice': qualifier (from "Prepare to start routine trigger")
	* conflict: added WaitingForExperimenter qualifier. WaitingForScanner already existed 



Older version
- We modified the outputs to save every key that was press. Two new columns were added with a list of keys that were pressed, and another column with a list of the onsets each key was pressed.
- There is a config file at the Banda folder level that specifies the output path for every task. 
- We added instructions to the conflict task, explaining what the vertical and horizonal white squares means. 
- There are few questions we added at the end of Gambling, and between the different runs of resting.
- Scanner start is 'equal' for the mgh scanner. Answers/botton box goes from 0 to 4 right hand ( one is index, 2 is middle finger), and goes from 5 to 9 on the left hand (9 is index and 8 is middle finger).





For any questions you can contact Viviana Siless at vsiless@mgh.harvard.edu.


