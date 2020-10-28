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

################################################
# Computing the PLV value:
# - First we compute the Hilbert transform to obtain the signal in real and imaginary domains
# - Second we compute the phase as the arctan of the real and imaginary components of the Hilbert transform
# - PLV = 1/N_fast*(Sum(exp(i(phase1-phase2)))), which is the complex matrix
#
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

fout=open('%s/PLV_1.dat' %path,'w')
fout2=open('%s/PLV_sync_1.dat' %path,'w')
font = {'family' : 'monospace',
        'weight' : 'bold',
        'size'   : 12}
rc('xtick', labelsize=11) 
rc('ytick', labelsize=11)

rc('font', **font)

infiles = sorted(glob.glob( '%s/Data_*.dat' %path), cmp=comparacio)

PLV_matrix = zeros([nNodes,nNodes])
phase=[]
diffase=[]
for infile in infiles:
	
	#Load data sets
	
	s = loadtxt(infile, unpack=True) # Voxels 1,2,3
	
	for i in range(1,nNodes+1):
		phase.append(angle(hilbert(s[i][Trans:]-s[i][Trans:].mean()),deg=False))
	#print len(phase[0][nRemove::])


	for k in range(len(phase)):
		for j in range(k):
			diffase.append(phase[k]-phase[j])
	

			PLV_matrix[k,j] = (abs(sum(exp((phase[k]-phase[j])*1j))))/len(diffase[0])
			#if(PLV_matrix[k,j]>=0.9):
	for i in range(len(PLV_matrix)):
		for j in range(i):
			print >> fout2,i,j,PLV_matrix[i,j]
	for i in range(len(PLV_matrix)):
		for j in range(len(PLV_matrix[0])):
			
			print >>fout, PLV_matrix[i,j],
			if j!= len(PLV_matrix)-1:
           			print >>fout," ",
        	else:
           			print >>fout
   
						
	fout.close()
	fout2.close()
	
	

			