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
fout=open('./Output_2_coupled_nodes/Output_0001/OrderParameter/Delay_SurfPlot.dat', 'a')

Trans=5000
path = os.getenv('P_Dir')


infile = ( '%s/Delay_Matrix.dat' %path)

s = loadtxt(infile, unpack=True) 


if(alpha_old!=alpha):
	print >>fout, " "
print >> fout, alpha, beta, abs(s[0][1]*0.001)
