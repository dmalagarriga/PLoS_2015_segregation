import matplotlib
matplotlib.use('Agg')
import time
import scipy.cluster.hierarchy as hcluster
import numpy.random as random
import numpy
import scipy
import os

import pylab
pylab.ion()

alpha=float(os.getenv('alpha'))
beta=float(os.getenv('beta'))
nNodes = int(os.getenv('Nodes')) # Column 0 also counts
path = os.getenv('P_Dir')
alpha_old=float(os.getenv('alpha_old'))
path_reg=os.getenv('P_Reg')
fout=open('%s/Regularity.dat' %path_reg,'a')

x = numpy.loadtxt('%s/List_Reg.dat' %path,unpack=True)

if(alpha_old!=alpha):
		print >>fout, " "
print >>fout, alpha, beta, x[2].mean()
 








