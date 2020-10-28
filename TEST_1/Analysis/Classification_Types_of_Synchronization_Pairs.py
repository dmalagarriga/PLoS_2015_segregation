#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
from scipy import *
from pylab import *
from numpy import * 
from matplotlib.collections import LineCollection
import glob
import os

path_op=os.getenv('P_OP')
path_reg=os.getenv('P_Reg')
fout=open('./Output_2_coupled_nodes/Output_0001/Types_of_Synchronization_2.dat', 'a')
#fout2=open('./Output_2_coupled_nodes/Output_0001/Types_of_Synchronization_Sorted_by_Sync_2.dat', 'a')

Trans=5000
path = os.getenv('P_Dir')
Correlation=('%s/Correlation_SurfPlot.dat' %path_op)
Delay=('%s/Delay_SurfPlot.dat' %path_op)
PLV=('%s/PLV_SurfPlot_2.dat' %path_op)
Substraction_XCorr_Reg=('%s/Substraction_Reg_XCorr.dat' %path_reg)
Substraction_PLV_XCorr=('%s/Substraction_XCorr_PLV_2.dat' %path_op)

Regular_Complete_Sync=[] # 1
Regular_Lag_Sync=[] # 2
Chaos_Complete_Sync=[] # 3
Chaos_Lag_Sync=[] # 4
Phase_Sync=[] # 5
Generalized_Sync=[] # 6
Types_of_sync=[]


A=loadtxt(Correlation, unpack=True)
B=loadtxt(Delay, unpack=True)
C=loadtxt(PLV, unpack=True)
D=loadtxt(Substraction_XCorr_Reg,unpack=True) #For chaos sync
E=loadtxt(Substraction_PLV_XCorr,unpack=True) #For phase sync


for i in range(len(A[0])):
	
	if(float(A[2][i])>0.9):
		if(float(B[2][i])!=0.0):
			Types_of_sync.append((A[0][i],A[1][i],2)) #Lag sync (regular)
		if(float(B[2][i])==0.0):	
			Types_of_sync.append((A[0][i],A[1][i],1)) # Complete sync (regular)
	
	if(float(D[2][i])>=0.7):
		if((float(B[0][i]),float(B[1][i]))==(float(D[0][i]),float(D[1][i]))):
			if(float(B[2][i])==0.0):
				Types_of_sync.append((D[0][i],D[1][i],3)) # Complete sync (chaos)	
			if(float(B[2][i])!=0.0):
				Types_of_sync.append((D[0][i],D[1][i],4)) # Lag sync (chaos)
				
	if(float(E[2][i]>=0.4)):
		if((float(B[0][i]),float(B[1][i]))==(float(E[0][i]),float(E[1][i]))):
			Types_of_sync.append((E[0][i],E[1][i],5)) # Phase sync 
	
	if(float(A[2][i])<0.9):
		if(float(D[2][i])<=0.7):
			if(float(E[2][i]<=0.4)):
				Types_of_sync.append((E[0][i],E[1][i],0)) # Not sync
			
		
	

Types_of_sync.sort(key=lambda tup: tup[0])
#Types_of_sync.sort(key=lambda tup: tup[2])




for row in range(len(Types_of_sync)):
	print >> fout, str(Types_of_sync[row]).strip('()')	
	if(Types_of_sync[row+1][0]!=Types_of_sync[row][0]):
		print >> fout, " "

'''
for i in range(len(A[0])):
	if(float(A[2][i])>0.9):
		if(float(B[2][i])!=0.0):
			print A[0][i],A[1][i]
			if(A[0][i+1]!=A[0][i]):
				print " "
		
'''



