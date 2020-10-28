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
fout1 = open('%s/Correlation_Regularity_connected.dat' %path,'w')
fout2 = open('%s/Correlation_Regularity_not_connected.dat' %path,'w')



Trans=5000

A=loadtxt('%s/List_Reg.dat' %path, unpack=True)

B=loadtxt('%s/Cross_correlation_connected_edges.dat' %path, unpack=True)

C=loadtxt('%s/Cross_correlation_not_connected_edges.dat' %path, unpack=True)

Data=loadtxt('%s/Data_0155.dat' %path,unpack=True)

fout1=open('%s/List_Correlation_Conn_Regularity.dat' %path,'w')
fout2=open('%s/List_Correlation_No_Conn_Regularity.dat' %path,'w')
fout3=open('%s/List_Correlation_Regularity_All.dat' %path,'w')


Rows_Conn=[]
Rows_No_Conn=[]
Rows_Total=[]
for i in range(len(B[0])):
	
	for j in range(len(A[0])):
			
		for k in range(len(A[0])):
			
			if(int(B[0][i]) == int(A[0][j])):
				if(int(B[1][i]) == int(A[0][k])):
			#Rows_Conn+=(B[0][i],B[1][i],B[2][i],Data[int(B[0][i])][Trans:].mean(),A[2][j],Data[int(B[1][i])][Trans:].mean(),)
					Rows_Conn.append((B[0][i],B[1][i],B[2][i],Data[int(B[0][i])][Trans:].mean(),A[2][j],Data[int(B[1][i])][Trans:].mean(),A[2][k],(A[2][j]+A[2][k])/2,B[2][i]))
					Rows_Total.append((B[0][i],B[1][i],B[2][i],Data[int(B[0][i])][Trans:].mean(),A[2][j],Data[int(B[1][i])][Trans:].mean(),A[2][k],(A[2][j]+A[2][k])/2,B[2][i]))		
		
for i in range(len(C[0])):
	for j in range(len(A[0])):
		for k in range(len(A[0])):
			if(int(C[0][i])==int(A[0][j])):
				if(int(C[1][i]) == int(A[0][k])):
					Rows_No_Conn.append((C[0][i],C[1][i],C[2][i],Data[int(C[0][i])][Trans:].mean(),A[2][j],Data[int(C[1][i])][Trans:].mean(),A[2][k],(A[2][j]+A[2][k])/2,-1))
					Rows_Total.append((C[0][i],C[1][i],C[2][i],Data[int(C[0][i])][Trans:].mean(),A[2][j],Data[int(C[1][i])][Trans:].mean(),A[2][k],(A[2][j]+A[2][k])/2,-1))




Rows_Total.sort(key=lambda tup: tup[2])

for row in range(len(Rows_Total)):
	print >> fout3,Rows_Total[row]	
for row in range(len(Rows_Conn)):
	print >> fout1,Rows_Conn[row]
for row in range(len(Rows_No_Conn)):
	print >> fout2,Rows_No_Conn[row]


'''		
for i in range(len(C)):
	for j in range(len(A)):
		if((int(C[j][0])-1,int(C[j][1])-1) == (int(B[i][0]),int(B[i][1]))):
			C_Conectats.append((C[j][0],C[j][1],C[j][2]))		
	
	
'''	
	
