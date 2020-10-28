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
import spectrum

def comparacio(a,b):
        
	(Sepa,numa) = a.split('_')
	(pa,exta) = numa.split('.')	

	(Sepb,numb) = b.split('_')
	(pb,extb) = numb.split('.')
        value=float(pa)-float (pb)
        return int(value/abs(value))
       

path=os.getenv('P_Reg')
#Kv=float(os.getenv('K_Conn'))
alpha=float(os.getenv('alpha'))
beta=float(os.getenv('beta'))
#Freq=float(os.getenv('Frequencia'))

fout=open('./Output_Ring_Connectivity/Regularity/Regularity_alpha_%05.2f/Regularity_beta_%05.2f/Maxima_alpha_%05.2f_beta_%05.2f.dat' %(alpha,beta,alpha,beta),'w')
infiles=sorted(glob.glob('%s/A_mean_alpha_%05.2f_beta_%05.2f.dat' %(path,alpha,beta)))

indexmax=0
posmax=0
indexmax1=[]
posmax1=[]




for infile in infiles:
	
	s = loadtxt(infile, unpack=False)
	
	MaxTab,MinTab= spectrum.peakdet(s[:401],0.1)
	#plot(s)
	for i in range(len(MaxTab)):
		indexmax,posmax=MaxTab[i]
		indexmax1.append(indexmax)
		posmax1.append(posmax)
		
	#print >> fout, indexMax, posmax
		print >> fout,str(indexmax1[i]).strip('[]'),str(posmax1[i]).strip('[]')
	#	ax=gca()
	#	ax.annotate('%.3f' %(posmax1[i]),xy=(indexmax1[i],posmax1[i]))
	#savefig(pjoin(path, 'Maxima_Plot_%s.eps' %Kv))
	close()
		
	
	
	
	
	
	
