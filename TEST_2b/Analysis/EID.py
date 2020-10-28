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

x = numpy.loadtxt('%s/Suma_Clusters.dat' %path,unpack=True)
fout=open('Output_Scale_free_1_init_node/EID_3.dat','a')
#EID = (x[2]+x[3])/(numpy.abs(x[2]-x[3])) - 1
EID = (x[2]+x[3])/((x[2]-x[3])) 
if(alpha_old!=alpha):
		print >> fout, " "
print >>fout, alpha, beta, EID
