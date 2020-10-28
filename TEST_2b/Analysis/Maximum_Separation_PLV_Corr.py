#!/usr/bin/python
import matplotlib
#matplotlib.use('Agg')
from scipy import *
from pylab import *
from numpy import * 
from matplotlib.collections import LineCollection
import glob
import os



path = os.getenv('P_Dir')

PLV=loadtxt('%s/PLV_sync.dat' %path,unpack=True)
Corr=loadtxt('%s/Correlation_Sorted_By_Pairs.dat' %path,unpack=True)
infile = ('%s/Data_0155.dat' %path)
Trans=5000
Separation=[]
s = loadtxt(infile, unpack=True) # Voxels 1,2,3
for i in range(len(PLV[2])):
	Separation.append(PLV[2][i]-Corr[2][i])

a=xcorr(s[35][Trans:]-s[35][Trans:].mean(),s[7][Trans:]-s[7][Trans:].mean(),normed=True, usevlines=False, maxlags=None, ls='-', marker='None')
'''
print max(Separation), Separation.index(max(Separation)), min(Separation), Separation.index(min(Separation))
print PLV[0][567], Corr[1][567]
'''
xlabel('Lags (ms)')
ylabel('Cross-correlation')
#ylim([-1,1])
xlim([-1000,1000])
show()