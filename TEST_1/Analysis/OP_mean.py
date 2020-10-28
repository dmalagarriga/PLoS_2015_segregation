#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
from scipy import *
from pylab import *
from numpy import * 
from matplotlib.collections import LineCollection
import glob
import os
from os.path import join as pjoin




def comparacio(a,b):
        
	(Sepa,numa) = a.split('_')
	(pa,exta) = numa.split('.')	

	(Sepb,numb) = b.split('_')
	(pb,extb) = numb.split('.')
        value=float(pa)-float (pb)
        return int(value/abs(value))


path = os.getenv('P_OP')

#Kv=float(os.getenv('K_Conn'))
alpha=float(os.getenv('alpha'))
beta=float(os.getenv('beta'))
alpha_old=float(os.getenv('alpha_old'))

font = {'family' : 'monospace',
        'weight' : 'bold',
        'size'   : 12}
rc('xtick', labelsize=11) 
rc('ytick', labelsize=11)

rc('font', **font)



infiles = sorted(glob.glob( '%s/OP_alpha_%05.2f_beta_%05.2f.dat' %(path,alpha,beta)))
#fout=open('%s/OP_mean_alpha_%05.2f_beta_%05.2f.dat' %(path,alpha,beta),'a d')
fout=open('%s/OP_mean.dat' %path,'a d')

for infile in infiles:
	
	#Load data sets
	
	s = loadtxt(infile, unpack=False) # Order parameter for realizations 1,2,3...
	if(alpha_old!=alpha):
		print >> fout, " "		
	print >> fout, alpha, beta, mean(s)	
	
fout.close()
	

	
	
			
		
		
		
		
		
				

					
		


