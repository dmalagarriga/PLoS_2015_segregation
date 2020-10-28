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
path=os.getenv('P_Dir')

nNodes=int(os.getenv('Nodes'))
initial_nodes=int(os.getenv('Initial_Nodes'))
Which_network=os.getenv('Network')
if(Which_network=='BARABASI'):
	G=nx.barabasi_albert_graph(nNodes,initial_nodes,seed=6)
	H=G.to_directed()
	A = np.loadtxt('%s/Data_0155.dat' %path,unpack=True)
	Mean=[]
	
	in_Degree=[]
	
	axScatter = plt.subplot(111)
	for i in range(1,nNodes+1):
		Mean.append(A[i][Trans:].mean())
	for i in range(nNodes):
		in_Degree.append(H.in_degree(i))	
	    
		if(Mean[i]>0):	
			a,=plt.plot(in_Degree[i],Mean[i],'go',label='Excitatory columns')
		
		if(Mean[i]<0):
			b,=plt.plot(in_Degree[i],Mean[i],'ro',label='Inhibitory columns')
	axScatter.scatter(in_Degree, Mean)
	#axScatter.set_aspect(1.)	
		#plt.annotate('%i' %(i),xy=(in_Degree[i],Mean[i]),fontsize=8)
	plt.legend([a,b],['Excitatory columns','Inhibitory columns'],prop={'size':10})
	#plt.legend([a],['Excitatory columns'])
	#plt.legend([b],['Inhibitory columns'])
	plt.xlabel(r'$\mathrm{Inhibitory\ in-degree}$',fontsize=20)
	plt.ylabel(r'$|y_1(t)-y_2(t)|$',fontsize=20)
	divider = make_axes_locatable(axScatter)
	axHisty = divider.append_axes("right", size=1.2, pad=0.3,sharey=axScatter)
	#axHisty.hist(Mean, bins=40, orientation='horizontal',facecolor='green')
	n, bins, patches = axHisty.hist(Mean, bins=30, normed=1, orientation='horizontal',facecolor='green')	
	axHisty.set_xlim(0,1)
	# make some labels invisible
	plt.setp(axHisty.get_yticklabels(),
         visible=False)
        #axHisty.axis["left"].major_ticklabels.set_visible(False)
	for tl in axHisty.get_yticklabels():
    		tl.set_visible(False)
		axHisty.set_xticks([0,0.5,1])
	# add a 'best fit' line
	#(mu,sigma) = norm.fit(Mean)
	#y = mlab.normpdf( bins, .5, .5)
	#x = mlab.normpdf( bins, -1.3, 1.0)
	#bimodal_pdf = 	0.7*x+0.4*y+0.1
	#axHisty.plot(bins, y, 'r-', linewidth=5)
	#axHisty.plot(bimodal_pdf,bins, 'r--', linewidth=1)	
	plt.savefig('%s/Scatter_2.eps' %path)
	plt.close()
