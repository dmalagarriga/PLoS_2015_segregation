#!/usr/bin/python

import matplotlib
matplotlib.use('Agg')
import networkx as nx
import matplotlib.pyplot as plt
import pylab
import os
import numpy as np
from matplotlib import rc
import matplotlib.mlab as mlab
import spectrum

#rc('font',**{'family':'sans-serif','size':18,'sans-serif':['Helvetica']})
#rc('text', usetex=True)
pylab.rcParams['xtick.major.pad']='8'
pylab.rcParams['ytick.major.pad']='8'

Trans=1000
#path=os.getenv('P_Dir')

nNodes=int(os.getenv('Nodes'))
#A = np.loadtxt('%s/Data_0155.dat' %path,unpack=True)
Mean=[]
for Seed in range(1,2):
	path = 'Output_Scale_free_1_init_node/Output_Network_Seed_%04i/Output_0001/Output_alpha_%05.2f/Output_beta_%05.2f/' %(Seed,alpha,beta)
		
	A = np.loadtxt('%s/Data_0155.dat' %path,unpack=True)
	for i in range(1,nNodes+1):
		Mean.append(A[i][Trans:].mean())
		
n, bins,patches = plt.hist(Mean, 50, facecolor='green',  normed=False, alpha=0.75)

for patch, rightside, leftside in zip(patches, bins[1:], bins[:-1]):
    if rightside < 0:
        patch.set_facecolor('red')
    elif leftside > 0:
        patch.set_facecolor('green')


fig = matplotlib.pyplot.gcf()
fig.set_size_inches(11.5,10.5)

Peak_values=[]

#Calculate the relative maxima
this = np.zeros([len(n)+2])


for i in range(len(n)):
	this[i+1] = n[i]	
	this[len(n)+1]=this[len(n)]
	this[-1]=this[0]

MaxTab,MinTab= spectrum.peakdet(this,0.01)
indexmax1=[]
valuemax = []
for i in range(len(MaxTab)):
		indexmax,posmax=MaxTab[i]
		indexmax1.append(indexmax)
		valuemax.append(posmax)


MaxTab=MaxTab[::-1]
valuemax.sort()
valuemax=valuemax[::-1]

print MaxTab
plt.annotate('%05.3f' %(valuemax[0]),xy=(bins[MaxTab[0][0]],valuemax[0]),fontsize=16)
plt.annotate('%05.3f' %(valuemax[1]),xy=(bins[MaxTab[2][0]],valuemax[1]),fontsize=16)
'''
plt.annotate('%05.3f' %(valuemax[0]),xy=(MaxTab[0][0]-1,MaxTab[0][1]),fontsize=16)
plt.annotate('%05.3f' %(valuemax[1]),xy=(MaxTab[1][0]-1,MaxTab[1][1]),fontsize=16)
'''
# add a 'best fit' line
#y = mlab.normpdf( bins, 0, 10)
#l = plt.plot(bins, y, 'r--', linewidth=1)

#plt.axvline(x=5.7132117003617999, ymin=0, ymax=1, color='black')


#plt.xlim([-15,15])
#plt.ylim([0,1.1])
plt.xlabel(r'$<y_1(t)-y_2(t)>$',fontsize=30,labelpad=15)
#plt.ylabel(r'$\mathrm{Probability}$')
plt.ylabel('Probability',fontsize=25,labelpad=15)
#plt.title(r'$\mathrm{Histogram\ of\ EIS}$')
#plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.tick_params(axis='both', which='major', labelsize=25,labelbottom=5)
plt.savefig('Output_Scale_free_1_init_node/Histogram_alpha_%05.2f_beta_%05.2f_large_maxima.eps' %(alpha,beta))
plt.close()
