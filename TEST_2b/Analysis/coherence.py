#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
from scipy import *
from scipy.signal import hilbert
from pylab import *
from numpy import * 
import glob
import os
from os.path import join as pjoin
import cmath
import spectrum
#import matplotlib.pyplot as plt

################################################
# Computing the Coherence value
################################################

def comparacio(a,b):
        
	(Sepa,numa) = a.split('_')
	(pa,exta) = numa.split('.')	

	(Sepb,numb) = b.split('_')
	(pb,extb) = numb.split('.')
        value=float(pa)-float (pb)
        return int(value/abs(value))

alpha=float(os.getenv('alpha'))
beta=float(os.getenv('beta'))
nNodes = int(os.getenv('Nodes')) # Column 0 also counts

Trans=5000
path = os.getenv('P_Dir')

nRemove=100 # Number of elements to remove from Hilbert Transform to avoid edge effects

#fout=open('%s/Coherence.dat' %path,'w')
fout=open('%s/Coherence_sorted_by_pairs.dat' %path,'w')

font = {'family' : 'monospace',
        'weight' : 'bold',
        'size'   : 12}
rc('xtick', labelsize=11) 
rc('ytick', labelsize=11)

rc('font', **font)

infiles = sorted(glob.glob( '%s/Data_0155.dat' %path), cmp=comparacio)

for infile in infiles:
	iterator=[]
	#Load data sets
	for i in range(1,nNodes+1):
		iterator.append(i)
	s = loadtxt(infile, unpack=True,usecols=(iterator)) # Voxels 1,2,3
	
	Matrix =zeros([len(s),len(s)])
	Coherence = zeros([len(s),len(s)])
	time = loadtxt(infile, unpack=True, usecols = [0])
	for i in range(len(s)):
			
		for j in range(i):
			
			cxy, f = spectrum.coherence(time[Trans:],s[i][Trans:]-s[i][Trans:].mean(),s[j][Trans:]-s[j][Trans:].mean())
			C = list(cxy)
			MAX1 = C.index(max(C))
			freqlagvalue=list(f)
				
			freq = freqlagvalue[MAX1]
	
	

			C = list(cxy)
			MAX1 = C.index(max(C))
			freqlagvalue=list(f)
				
			freq = freqlagvalue[MAX1]
			
			Matrix[i,j]= freq
			Coherence[i,j]=max(C)
	
	for i in range(len(Coherence)):
		for j in range(i):
			print >> fout, i, j, Coherence[i,j], Matrix[i,j]
	savetxt(pjoin(path,'Frequency_Matrix.dat'),Matrix)
	savetxt(pjoin(path,'Coherence_Matrix.dat'),Coherence)	
