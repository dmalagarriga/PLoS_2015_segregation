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


'''
def comparacio(a,b):
        
	(Sepa,numa) = a.split('_')
	(pa,exta) = numa.split('.')	

	(Sepb,numb) = b.split('_')
	(pb,extb) = numb.split('.')
        value=float(pa)-float (pb)
        return int(value/abs(value))
'''
#Kv =float(os.getenv('K_Conn'))
alpha=float(os.getenv('alpha'))
beta=float(os.getenv('beta'))
nNodes=int(os.getenv('Nodes'))


Trans=2000
path = os.getenv('P_Dir')


infile = ( '%s/XCorr_Matrix_2.dat' %path)
S=[]
s = loadtxt(infile, unpack=True) 
for i in range(1,nNodes+1):
			
		for j in range(1,nNodes):
			if i!=j:
				S=s[i][j]
Smean=mean(S)
print Smean
#savetxt(pjoin(path,'XCORR_%s.dat' %Kv),Smean)
#close()
