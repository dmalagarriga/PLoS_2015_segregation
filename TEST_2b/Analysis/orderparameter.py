#!/usr/bin/python
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

Kv = os.getenv('K_Conn')
nNodes = int(os.getenv('Nodes')) # Column 0 also counts


Trans=1
path = os.getenv('P_Dir')


infiles = sorted(glob.glob( '%s/Data_*.dat' %path), cmp=comparacio)

RsynN=[]
rN=[]

for infile in infiles:
	
	#Load data sets
	
	s = loadtxt(infile, unpack=True) # Voxels 1,2,3,...
	for i in range(1,nNodes):
		
		r=0
		rN.append(var(s[i][Trans:]))
		R=mean(rN)
		#r+=(s[i][Trans:].std())**2
		Rsyn= var(s[nNodes][Trans:])/R
		#RsynN.append(Rsyn)
	print Rsyn