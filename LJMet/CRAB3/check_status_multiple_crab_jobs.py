import os, argparse, imp

parser = argparse.ArgumentParser()
parser.add_argument("--finalState",action="store", default="multiLep")
parser.add_argument("--resubmit",action="store_true", default=False)
option = parser.parse_args()

#Sample list file
sampleListPath = "sample_list_"+option.finalState+".py"
sample = imp.load_source("Sample",sampleListPath,open(sampleListPath,"r"))

CRABSUBMIT_DIR      = 'crabSubmitLogs'

def check_status_multiple_crab_jobs(sample_dict):

	for dataset in sample_dict:

		crab_submit_dir = CRABSUBMIT_DIR+'/'+option.finalState+'/crab_'+option.finalState+'_'+dataset+'/'

		if(option.resubmit):
			print '\nAttempting to resubmit ',dataset,':',sample_dict[dataset]
			os.system('crab resubmit '+crab_submit_dir)
		else:
			print '\nChecking status ',dataset,':',sample_dict[dataset]
			os.system('crab status '+crab_submit_dir)



if __name__ == '__main__':

	check_status_multiple_crab_jobs(sample.signaldict)
	check_status_multiple_crab_jobs(sample.bkgdict)
	check_status_multiple_crab_jobs(sample.ttbarbkgdict)
	check_status_multiple_crab_jobs(sample.datadict)
