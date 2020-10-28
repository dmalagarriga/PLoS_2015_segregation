#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
from scipy import *
from pylab import *
from numpy import * 
from matplotlib.collections import LineCollection
import glob
import os
from os.path import join as pjoin



def comparacio(a,b):
        
	(Sepa,numa) = a.split('_')
	(pa,exta) = numa.split('.')	

	(Sepb,numb) = b.split('_')
	(pb,extb) = numb.split('.')
        value=float(pa)-float (pb)
        return int(value/abs(value))

#Kv = float(os.getenv('K_Conn'))

alpha=float(os.getenv('alpha'))
beta=float(os.getenv('beta'))
nNodes = int(os.getenv('Nodes')) # Column 0 also counts


Trans=5000
path = os.getenv('P_Dir')


font = {'family' : 'monospace',
        'weight' : 'bold',
        'size'   : 12}
rc('xtick', labelsize=11) 
rc('ytick', labelsize=11)

rc('font', **font)

infiles = sorted(glob.glob( '%s/Data_*.dat' %path), cmp=comparacio)
fout=open('%s/Correlation_Sorted_By_Pairs.dat' %path,'w')
#print >> fout, 'Pair1','Pair2','XCorr','Delay'
for infile in infiles:
	iterator=[]
	#Load data sets
	for i in range(1,nNodes+1):
		iterator.append(i)
	s = loadtxt(infile, unpack=True,usecols=(iterator)) # Voxels 1,2,3

	#subplots_adjust(wspace = 0.4, hspace = 0.4)

	#Compute the cross correlation and plot it.
		
	Matrix =zeros([len(s),len(s)])
	Correlation = zeros([len(s),len(s)])

	for i in range(len(s)):
			
		for j in range(i):
			#subplot('31%i' %i)
			a=xcorr(s[i][Trans:]-s[i][Trans:].mean(),s[j][Trans:]-s[j][Trans:].mean(),normed=True, usevlines=False, maxlags=None, ls='-', marker='None')
			
			#b=acorr(s[i][Trans:]-s[i][Trans:].mean(),normed=True,usevlines=False,maxlags=200,ls='-',marker='None')
			#xlim([0,200])
			#savefig(pjoin(path,'Autocorrelation_%i.pdf' %i))
			#close()
			
				
			##############################
			# Compute the maximum of     #
			# the delay and its position #
			#############################
				
	
			C = list(a[1])
			MAX1 = C.index(max(C))
			lagvalue=list(a[0])
				
			lagg = lagvalue[MAX1]
			
			
			############################
			# Filling the delay matrix #
			############################
			
			Matrix[i,j]= lagg
			Correlation[i,j]=max(C)
			
			
	for i in range(len(Correlation)):
		for j in range(i):
			print >> fout, i, j, Correlation[i,j], Matrix[i,j]
	savetxt(pjoin(path,'Delay_Matrix.dat'),Matrix)
	savetxt(pjoin(path,'XCorr_Matrix_2.dat'),Correlation)		
	#exit()
	#Plots adjustments
	#f=figure(figsize=(8,8))
	#f.text(0.5,0.975,'Cross-correlations for 100 connected voxels',horizontalalignment='center',verticalalignment='top')
'''	
	pcolor(Matrix,edgecolors='k')
	#pcolor(Matrix,cmap='bone', shading='faceted',edgecolors='k')
	#imshow(Matrix,cmap='bone', interpolation='nearest', aspect='equal',origin='upper')
	xlim([1,nNodes])
	ylim([1,nNodes])
	title('Delay matrix');xlabel('Voxel number');ylabel('Voxel number')
	cbar=plt.colorbar()
	cbar.ax.set_ylabel('Delay in ms')
	savefig(pjoin(path,'Delay_Matrix_K_%s.pdf' %(Kv)))
	close()
	
	pcolor(Correlation,cmap='spectral', edgecolors='k')
#	plt.imshow(corrcoef(s),cmap='bone',interpolation='None', aspect='equal',origin='upper')
	xlim([1,nNodes])
	ylim([1,nNodes])
	title('Correlation matrix');xlabel('Voxel number');ylabel('Voxel number')
	cbar=plt.colorbar()
	cbar.ax.set_ylabel('Correlation coefficient')
	savefig(pjoin(path,'Correlation_Matrix_K_%s.pdf' %(Kv)))
	close()
'''


