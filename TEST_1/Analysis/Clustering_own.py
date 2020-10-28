import matplotlib
matplotlib.use('Agg')
import numpy
import scipy
import os
import pylab
import networkx as nx
pylab.ion()

#alpha=float(os.getenv('alpha'))
#beta=float(os.getenv('beta'))
nNodes = int(os.getenv('Nodes')) # Column 0 also counts
#path_Xcorr = os.getenv('P_XCorr')
#path_Delay = os.getenv('P_Delay')
path=os.getenv('P_Dir')
#alpha_old=float(os.getenv('alpha_old'))


x = numpy.loadtxt('%s/XCorr_Matrix_2.dat' %path,unpack=True)
d = numpy.loadtxt('%s/Delay_Matrix.dat' %path,unpack=True)
g = numpy.loadtxt('%s/Cross_correlation_connected_edges.dat' %path,unpack=True)
#fout=open('%s/Cross_Correlation_linearized.dat' %(path),'w')
fout2=open('%s/Pair_Distribution.dat' %(path),'w')
#fout3=open('Clusters_alpha_%s_beta_%s' %(alpha,beta),'w')
fout4=open('%s/Connected_Clusters.dat' %(path),'w')
Clust=0
j_old=0
Y=[]


'''
for j in range(nNodes+1):
	for i in range(j):
	 	if (i!=0):
		    print >> fout, i,j, x[i][j], abs(d[i][j]*0.005) #Cross-correlation with its delay 
fout.close()
'''
B=numpy.loadtxt('%s/Cross_Correlation_linearized.dat' %(path),unpack=True)

fout5=open('%s/Cross_Correlation_linearized_All.dat' %(path),'w')

for i in range(len(B[0])):
	for j in range(len(g[0])):	
		if((B[0][i],B[1][i])==(g[0][j], g[1][j])):
			print >> fout5, B[0][i],B[1][i], B[2][i], g[2][j]
	if((B[0][i],B[1][i])!=(g[0][j], g[1][j])):
		print >> fout5, B[0][i],B[1][i], B[2][i], -1
	
fout5.close()

C = numpy.genfromtxt('%s/Cross_Correlation_linearized_All.dat' %(path),dtype=(tuple,tuple,float,float))
CC = numpy.sort(C,order=['f2'],axis=0)

for i in range(len(CC)):
	print >> fout2, CC[i]
	 
fout2.close()

#for j in range(nNodes):
#	if(j_old!=j):
#		print >> fout, " "
#	for i in range(j):
#		if(x[i][j]>=0.8):
#			Clust=1
#		else:
#			Clust=0	
#		print >> fout3, i, j, Clust
A=[]
for j in range(nNodes):
	for i in range(j):
		if(x[i][j]>=0.9):
			#Clust.append(i)
			#Clust.append(j)
			z = (i,j)
			A.append(z)
			G = nx.Graph(A)
			print >> fout4, nx.connected_components(G)
		
	
	
			
