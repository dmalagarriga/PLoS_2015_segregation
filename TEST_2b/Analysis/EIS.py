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
#################################################################################
# There are two versions of EIS here. One is EIS=CM_exc*Area_exc*CM_inh*Area_Inh
# which takes into account centers of mass and Areas of the distribution, and
# EIS = X_exc*H_exc*X_inh*H_inh, which takes into account the position (X) of the
# maximum of the distributions. In fact it takes the 2 absolute maximas in the dis-
# tribution, which is not a good measure to see segregation as we have multi-modal
# probability distributions.
#################################################################################
Trans=0

alpha=float(os.getenv('alpha'))
beta=float(os.getenv('beta'))
nNodes = int(os.getenv('Nodes')) # Column 0 also counts
#path = os.getenv('P_Dir')
alpha_old=float(os.getenv('alpha_old'))
fout=open('Output_Scale_free_1_init_node_2/EIS_4.dat','a')
Mean=[]
for Seed in range(1,50):
	path_2 = 'Output_Scale_free_1_init_node_2/Output_Network_Seed_%04i/Output_0001/Output_alpha_%05.2f/Output_beta_%05.2f/' %(Seed,alpha,beta)

	
	A = np.loadtxt('%s/Data_0155.dat' %path_2,unpack=True)
	for i in range(1,nNodes+1):
		Mean.append(A[i][Trans:].mean())
	
n, bins,patches = plt.hist(Mean, 50, facecolor='green',  normed=True, alpha=0.75)


for patch, rightside, leftside in zip(patches, bins[1:], bins[:-1]):
    if rightside < 0:
       patch.set_facecolor('red')
       
    elif leftside >= 0:
       patch.set_facecolor('green')
Area_inh=[]
Area_exc=[]
CM_inh=[]
CM_exc=[] #Centers of mass (=1/M*SUM(m_i*r_i))

#bins[i]-bins[i-1] is the width of each bin in the distribution. The total area is SUM(bin_width*height_i)

bin_width=bins[3]-bins[2]
for i in range(len(n)):
    if(bins[i]>0):
	Area_exc.append(bin_width*n[i])
	CM_exc.append(bin_width*bins[i]*n[i])
	
    elif(bins[i]<0):
	Area_inh.append(bin_width*n[i])
	CM_inh.append(bin_width*bins[i]*n[i])

EIS = abs(sum(Area_exc)*(sum(CM_exc))*sum(Area_inh)*(sum(CM_inh)))



if(alpha_old!=alpha):
		print >> fout, " "
print >>fout,alpha, beta, EIS 


#########################################
# Second version of EIS
#
#########################################


'''

#Calculate the relative maxima of the histogram
this = np.zeros([len(n)+2])


for i in range(len(n)):
	this[i+1] = n[i] #Contour conditions
	this[len(n)+1]=this[len(n)]
	this[-1]=this[0]
		


MaxTab,MinTab= spectrum.peakdet(this,0.01)
indexmax1=[]
valuemax = []
for i in range(len(MaxTab)):
	indexmax,posmax=MaxTab[i]
	indexmax1.append(indexmax)
	valuemax.append(posmax)



valuemax.sort()
valuemax=valuemax[::-1]
MaxTab.sort(key=lambda x: x[1])
MaxTab=MaxTab[::-1]

A_e=valuemax[0]
if(len(valuemax)<2):
	A_i=0
else:
	A_i=valuemax[1]
P_e=MaxTab[0][0]
if(len(MaxTab)<2):
	P_i=0 #positition of (y_1-y_2)	
else:
	P_i=MaxTab[1][0]





# bins[MaxTab] is the value of the mean in the histogram (the base)
# valuemax is the actual peak of the histogram (the altitude)
	
EIS = bins[P_e]*bins[P_i]*A_e*A_i

# EIS marks the degree of separation of the two major peaks of the distribution.
# The more separated (x-axis), the higher. Also if the peaks have different
# heights it will be more or less bi-multi-modal.

if(alpha_old!=alpha):
		print >> fout, " "
print >>fout,alpha, beta, EIS 

plt.annotate('%05.3f, %05.3f' %(valuemax[0],bins[MaxTab[0][0]]),xy=(bins[MaxTab[0][0]],valuemax[0]),fontsize=16)
plt.annotate('%05.3f, %05.3f' %(A_i,bins[P_i]),xy=(bins[P_i],A_i),fontsize=16)

plt.xlabel(r'$<y_1(t)-y_2(t)>$',fontsize=30,labelpad=15)
#plt.ylabel(r'$\mathrm{Probability}$')
plt.ylabel('Probability',fontsize=25,labelpad=15)
#plt.title(r'$\mathrm{Histogram\ of\ EIS}$')
#plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.tick_params(axis='both', which='major', labelsize=25,labelbottom=5)
plt.savefig('Output_Scale_free_1_init_node_2/Histograms/Histogram_alpha_%05.2f_beta_%05.2f_large_maxima.eps' %(alpha,beta))
plt.close()
'''
