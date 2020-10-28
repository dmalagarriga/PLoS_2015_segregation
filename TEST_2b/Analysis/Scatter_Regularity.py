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

#rc('font',**{'family':'sans-serif','size':20,'sans-serif':['Helvetica']})
#rc('text', usetex=True)
pylab.rcParams['xtick.major.pad']='8'
pylab.rcParams['ytick.major.pad']='8'
Trans=5000
	
nNodes=int(os.getenv('Nodes'))
initial_nodes=int(os.getenv('Initial_Nodes'))
Which_network=os.getenv('Network')

Mean1=[]
ColorMap = []
if(Which_network=='BARABASI'):
	Mean=[]
	in_Degree=[]
	for Seed in range(1,51):
		path = 'Output_Scale_free_1_init_node/Output_Network_Seed_%04i/Output_0001/Output_alpha_20.00/Output_beta_30.00/' %Seed
		G=nx.barabasi_albert_graph(nNodes,initial_nodes,seed=Seed)
		H=G.to_directed()
		A = np.loadtxt('%s/Data_0155.dat' %path,unpack=True)
		C = np.loadtxt('%s/List_Reg_not_sorted.dat' %path,unpack=True)
		C.view('f8,f8,f8').sort(order=['f0'], axis=-1)
		
		
		
		for i in range(1,nNodes+1):
			Mean.append(A[i][Trans:].mean())
			
		for i in range(nNodes):
			in_Degree.append(H.in_degree(i))
			ColorMap.append(C[2][i])

fig = matplotlib.pyplot.gcf()
axes = fig.add_subplot(111)
fig.set_size_inches(14.5,10.5)
plt.scatter(in_Degree, Mean,s=50, c=np.array(ColorMap), cmap=matplotlib.cm.gnuplot,alpha=0.6,lw=0)

cb=plt.colorbar()
cb.set_alpha(1)
cb.set_ticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
cb.set_ticklabels([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
for a in cb.ax.get_yticklabels():
	a.set_fontsize(25)
plt.clim([0.0,1.0])
cb.set_label('Reg',fontsize=25,labelpad=15)
	#plt.annotate('%i' %(i),xy=(in_Degree[i],Mean[i]),fontsize=8)
	#plt.legend([a,b],['Excitatory columns','Inhibitory columns'],prop={'size':10})
	#plt.legend([a],['Excitatory columns'])
	#plt.legend([b],['Inhibitory columns'])
plt.xlabel('In-degree',fontsize=25,labelpad=15)
	#plt.xlabel(r'$\mathrm{Inhibitory\ in-degree}$',fontsize=20)
plt.ylabel(r'$<y_1(t)-y_2(t)>$',fontsize=30,labelpad=15)
plt.xlim([0,25])
for label in axes.get_xticklabels()+axes.get_yticklabels():
	label.set_fontsize(25)

#plt.tick_params(axis='both', which='major', labelsize=25,labelbottom=5)
#divider = make_axes_locatable(axScatter)
#axHisty = divider.append_axes("right", size=1.2, pad=0.3,sharey=axScatter)
#axHisty.hist(Mean1, bins=25,normed=1,orientation='horizontal',facecolor='green')
#n, bins, patches = axHisty.hist(Mean1, bins=10, normed=1, orientation='horizontal',facecolor='green')	
#axHisty.set_xlim(0,0.6)	
	
plt.savefig('./Output_Scale_free_1_init_node/Scatter_alpha_20_beta_30_1.eps')
plt.close()
