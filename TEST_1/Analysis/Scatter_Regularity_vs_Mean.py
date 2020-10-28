#!/usr/bin/python

import matplotlib
matplotlib.use('Agg')
import networkx as nx
import matplotlib.pyplot as plt
import pylab
import os
import numpy as np
from matplotlib import rc
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.mlab as mlab
from scipy.stats import norm
rc('font',**{'family':'sans-serif','size':18,'sans-serif':['Helvetica']})
rc('text', usetex=True)

Trans=5000
#path=os.getenv('P_Dir')
#path1='Output_Scale_free_1_init_node/Output_Network_Seed_0001/Output_0001/Output_alpha_180.00/Output_beta_50.00/'

	
nNodes=int(os.getenv('Nodes'))

Mean1=[]
ColorMap = []

Mean=[]
in_Degree=[]
for Seed in range(1,51):
	path = 'Output_Scale_free_1_init_node/Output_Network_Seed_%04i/Output_0001/Output_alpha_100.00/Output_beta_45.00/' %Seed
	
	A = np.loadtxt('%s/Data_0155.dat' %path,unpack=True)
	C = np.loadtxt('%s/List_Reg_not_sorted.dat' %path,unpack=True)
	C.view('f8,f8,f8').sort(order=['f0'], axis=-1)
	axScatter = plt.subplot(111)
	
	for i in range(1,nNodes+1):
		Mean.append(A[i][Trans:].mean())
	
	for i in range(nNodes):
		ColorMap.append(C[2][i])
		
		if(Mean[i]>5.7132117003617999):
			a,=plt.plot(ColorMap[i],Mean[i],'bo')
	
		if(Mean[i]<5.7132117003617999):
			b,=plt.plot(ColorMap[i],Mean[i],'ro')
		Mean1.append(Mean)	

axScatter.scatter(ColorMap, Mean,s=50,alpha=0.6)
axScatter.axhline(y=5.7132117003617999, xmin=-5, xmax=25, color='black')
#plt.legend([a,b],['Excitatory columns','Inhibitory columns'],prop={'size':10})

	#plt.annotate('%i' %(i),xy=(in_Degree[i],Mean[i]),fontsize=8)
	#plt.legend([a],['Excitatory columns'])
	#plt.legend([b],['Inhibitory columns'])
plt.xlabel('Regularity',fontsize=20)
	#plt.xlabel(r'$\mathrm{Inhibitory\ in-degree}$',fontsize=20)
plt.ylabel(r'$<y_1(t)-y_2(t)>$',fontsize=20)
plt.xlim([0,25])
	#divider = make_axes_locatable(axScatter)
	#axHisty = divider.append_axes("right", size=1.2, pad=0.3,sharey=axScatter)
	#axHisty.hist(Mean1, bins=25,normed=1,orientation='horizontal',facecolor='green')
	#n, bins, patches = axHisty.hist(Mean1, bins=10, normed=1, orientation='horizontal',facecolor='green')	
	#axHisty.set_xlim(0,0.6)	
	
plt.savefig('./Output_Scale_free_1_init_node/Scatter_Regularity_vs_Mean_alpha_100_beta_45_1.eps')
plt.close()
