import os
import csv
import numpy as np
import itertools
import subprocess


#See conditions nname below

def register_images(subject_dir, subject_id):
	fmA_infile =os.path.join(subject_dir)
	fmA_outfile = os.path.join(subject_dir, 'model', 'model001','onsets','task002_run001')
	fmB_infile =os.path.join(subject_dir)
	fmB_outfile = os.path.join(subject_dir, 'model', 'model001','onsets','task002_run002')
   
	if not os.path.exists(fmA_outfile):
		print 'Creating: %s folder' % fmA_outfile
		cmd = 'mkdir -p  %s' % str(subject_dir)+'/model/model001/onsets/task002_run001'
		print cmd		
		os.system(cmd)
	if not os.path.exists(fmB_outfile):
		print 'Creating: %s folder' % fmB_outfile
		cmd = 'mkdir -p  %s' % str(subject_dir)+'/model/model001/onsets/task002_run002'
		os.system(cmd)



	fmA_name = str(subject_id)  #raw_input("Please enter subect number for BreathCounting: ")
	#os.system('echo '+BC_infile+'/BreathCount_'+str(session)+'_'+str(BC_name)+'*_events.csv')	
	fmA_file=subprocess.check_output('echo '+fmA_infile+'/'+str(fmA_name)+'*_A_VSR_BANDA*.csv', shell=True)
	fmB_file=subprocess.check_output('echo '+fmB_infile+'/'+str(fmA_name)+'*_B_VSR_BANDA*.csv', shell=True)
	#BC_file=subprocess.check_output('echo *'+str(BC_name)+'*.csv', shell=True)
	fmA_file= fmA_file[:-1]
	fmB_file= fmB_file[:-1]

	print 'found file: ',fmA_file
	print 'found file: ',fmB_file


	#looking for run A events
	reward_events=[]
	loss_events=[]
	
	
        
	rewardA_file= open(str(fmA_outfile)+'/cond001.txt', 'wb')
	rewardA=[]
	    
	lossA_file=open(str(fmA_outfile)+'/cond002.txt', 'wb')
	lossA=[]  

	fixationA_file=open(str(fmA_outfile)+'/fixation.txt', 'wb')
 	
	with open(fmA_file, 'rU') as f:
	    reader=csv.reader(f)
	    my_dataA=map(tuple,reader)
	    
	    count=0
	    fixation_sum=0
	    fixations=[0,11,20,29]
	    for i in (0,3,11,12,20,21,29,30): #block_starts:
		   
	        rewardA_write = csv.writer(rewardA_file, delimiter=' ', lineterminator='\n')
		lossA_write = csv.writer(lossA_file, delimiter=' ', lineterminator='\n')
		fixationA_write = csv.writer(fixationA_file, delimiter=' ', lineterminator='\n')
		
	  
	    	
		if 'reward' in my_dataA[i][0] and i not in fixations:
		    print count,my_dataA[i][0],count+fixation_sum,28,1
		    count+=28
		    rewardA_write.writerow((count+fixation_sum,28,1))
		elif 'loss' in my_dataA[i][0] and i not in fixations:
		    print count,my_dataA[i][0],count+fixation_sum,28,1
		    lossA_write.writerow((count+fixation_sum,28,1))
		    count+=28

		else:
		    print count, 'fixation',count+fixation_sum,15,1
		    fixationA_write.writerow((count+fixation_sum,15,1))
		    fixation_sum+=15   	
		
		

	#looking for run B events
	reward_events=[]
	loss_events=[]
	
	
        
	rewardB_file= open(str(fmB_outfile)+'/cond001.txt', 'wb')
	rewardB=[]
	    
	lossB_file=open(str(fmB_outfile)+'/cond002.txt', 'wb')
	lossB=[]  

	fixationB_file=open(str(fmB_outfile)+'/fixation.txt', 'wb')
 	
	with open(fmB_file, 'rU') as f:
	    reader=csv.reader(f)
	    my_dataB=map(tuple,reader)
	    
	    count=0
	    fixation_sum=0
	    fixations=[0,11,20,29]
	    for i in (0,3,11,12,20,21,29,30): #block_starts:
		   
	        rewardB_write = csv.writer(rewardB_file, delimiter=' ', lineterminator='\n')
		lossB_write = csv.writer(lossB_file, delimiter=' ', lineterminator='\n')
		fixationB_write = csv.writer(fixationB_file, delimiter=' ', lineterminator='\n')
		
	  
	    	
		if 'reward' in my_dataB[i][0] and i not in fixations:
		    print count,my_dataB[i][0],count+fixation_sum,28,1
		    count+=28
		    rewardB_write.writerow((count+fixation_sum,28,1))
		elif 'loss' in my_dataB[i][0] and i not in fixations:
		    print count,my_dataB[i][0],count+fixation_sum,28,1
		    lossB_write.writerow((count+fixation_sum,28,1))
		    count+=28

		else:
		    print count, 'fixation',count+fixation_sum,15,1
		    fixationB_write.writerow((count+fixation_sum,15,1))
		    fixation_sum+=15   	
			



	print count
	print "####################"

	print "#####    A     ####"
	print "succesfully created:\n ",rewardA_file
	print "succesfully created:\n ",lossA_file
	print "succesfully created:\n ",fixationA_file

	print "####################"
	print "####################"

	print "#####    B     ####"
	print "succesfully created:\n ",rewardB_file
	print "succesfully created:\n ",lossB_file
	print "succesfully created:\n ",fixationB_file

	print "####################"


if __name__ == "__main__":
    import argparse
    defstr = ' (default %(default)s)'
    parser = argparse.ArgumentParser(prog='Reward_get_conditions_om.py',
                                     description=__doc__)
    parser.add_argument('-dir', dest='subject_dir', required=True,
                        help='BANDA subject dir')
    parser.add_argument('-id', dest='subject_id', required=True,
                        help="subject id")
    
    args = parser.parse_args()
    register_images(args.subject_dir, args.subject_id) 
        
       


