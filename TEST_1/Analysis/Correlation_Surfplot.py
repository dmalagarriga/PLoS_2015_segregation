#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
from scipy import *
from pylab import *
from numpy import * 
from matplotlib.collections import LineCollection
import glob
import os

alpha=float(os.getenv('alpha'))
beta=float(os.getenv('beta'))
nNodes=int(os.getenv('Nodes'))
alpha_old=float(os.getenv('alpha_old'))
fout=open('./Output_3_coupled_nodes/Output_0001/OrderParameter/Correlation_SurfPlot.dat', 'a')

Trans=5000
path = os.getenv('P_Dir')


infile = ( '%s/Correlation_Sorted_By_Pairs.dat' %path)

s = loadtxt(infile, unpack=True) 


if(alpha_old!=alpha):
	print >>fout, " "
print >> fout, alpha, beta, s[2]
