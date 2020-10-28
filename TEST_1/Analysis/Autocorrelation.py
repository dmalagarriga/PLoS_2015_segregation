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

#Kv = os.getenv('K_Conn')
alpha=float(os.getenv('alpha'))
beta=float(os.getenv('beta'))
nNodes = int(os.getenv('Nodes')) # Column 0 also counts


Trans=2500
path = os.getenv('P_Dir')

font = {'family' : 'monospace',
        'weight' : 'bold',
        'size'   : 12}
rc('xtick', labelsize=11) 
rc('ytick', labelsize=11)

rc('font', **font)

infiles = sorted(glob.glob( '%s/Data_*.dat' %path), cmp=comparacio)
total=zeros([401])
for infile in infiles:
	
	#Load data sets
	
	s = loadtxt(infile, unpack=True) # Voxels 1,2,3
	
	#Compute the auto-correlation and plot it.
	
	for i in range(1,nNodes+1):
		b=acorr(s[i][Trans:]-s[i][Trans:].mean(),normed=True,usevlines=False,maxlags=200,ls='-',marker='None')
		fout1=open('%s/A.dat' %(path),'w')
		fout=open('%s/A_%s.dat' %(path,i),'w')
		#xlim([-200,200])
		#savefig(pjoin(path,'Autocorrelation_%i.pdf' %i))
		close()
		
		for j in range(len(b[1])):
			total[j]=total[j]+b[1][j]
			print >>fout, str(b[1][j]).strip('[]')
			print >>fout1, total[j]/(nNodes)
			
	fout1.close()
	fout.close()
	plot(total/(nNodes))
	savefig(pjoin(path,'Autocorr_mean_alpha_%s_beta_%s.pdf' %(alpha,beta)))
	close()
	
		
		
		
		
		
		
				

					
		


