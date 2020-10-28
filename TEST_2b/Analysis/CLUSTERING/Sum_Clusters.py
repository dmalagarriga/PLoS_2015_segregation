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


x = numpy.loadtxt('%s/Data_0155.dat' %path,unpack=True)

D = scipy.zeros([nNodes,nNodes])
Trans=5000
Sum_Exc=0
Sum_Inh=0
fout=open('%s/Suma_Clusters.dat' %path,'w')
fout1=open('%s/Which_cluster_Exc_Inh.dat' %path,'a')

for i in range(1,51): # This is to skip time column!!
	if(x[i].mean()>0):
		Sum_Exc+=1
		print >>fout1, i-1, 'Exc'
	if(x[i].mean()<0):
		Sum_Inh+=1
		print >> fout1, i-1, 'Inh'
if(alpha_old!=alpha):
		print >> fout, " "
print >>fout, alpha, beta, Sum_Exc, Sum_Inh
 








