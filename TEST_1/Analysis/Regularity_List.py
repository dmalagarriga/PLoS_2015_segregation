##!/usr/bin/python
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
       

path=os.getenv('P_Dir')
#Kv=float(os.getenv('K_Conn'))
alpha=float(os.getenv('alpha'))
beta=float(os.getenv('beta'))
#Freq=float(os.getenv('Frequencia'))
nNodes=int(os.getenv('Nodes'))

fout=open('%s/List_Reg.dat' %path,'w')
fout2=open('%s/List_Reg_not_sorted.dat' %path,'w')
infiles=sorted(glob.glob('%s/A_*.dat' %path))

indexmax=0
posmax=0
#indexmax1=[]
#posmax1=[]

Trans=5000
Data=loadtxt('%s/Data_0155.dat' %path, unpack=True)

t=[]
for infile in infiles:
	#One,two,thre,four,five,six = infile.split('/')
	#seven,eight=six.split('_')
	#Column,ext=eight.split('.')

	One,two,three,four,five=infile.split('/')
	six,seven=five.split('_')
	Column,ext=seven.split('.')
	
	s = loadtxt(infile, unpack=True)
	indexmax1=[]
	posmax1=[]
	MaxTab,MinTab= spectrum.peakdet(s[:401],0.1)
	
	for i in range(len(MaxTab)):
		indexmax,posmax=MaxTab[i]
		indexmax1.append(indexmax)
		posmax1.append(posmax)
	t.append((Column, Data[int(Column)][Trans:].mean(), sorted(posmax1,reverse=True)[1]))
	print >> fout2, Column, Data[int(Column)][Trans:].mean(), sorted(posmax1,reverse=True)[1]
A = sorted(t,key=lambda item: item[1],reverse=True)
for i in range(len(t)):
	print >> fout,A[i][0],A[i][1],A[i][2]


	
	
	
	
	
	
