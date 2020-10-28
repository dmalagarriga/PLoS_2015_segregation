import matplotlib
matplotlib.use('Agg')
import numpy
import scipy
import os
import pylab
import networkx as nx
pylab.ion()


nNodes = int(os.getenv('Nodes')) # Column 0 also counts

path=os.getenv('P_Dir')
#alpha_old=float(os.getenv('alpha_old'))
fout1 = open('%s/Cross_correlation_connected_edges.dat' %path,'w')
fout2 = open('%s/Cross_correlation_not_connected_edges.dat' %path,'w')
fout3 = open('%s/PLV_connected_edges.dat' %path,'w')
A=[]

C = numpy.genfromtxt('%s/Correlation_Sorted_By_Pairs.dat' %(path),dtype=(int,int,float,float))
#C = numpy.genfromtxt('%s/Correlation_Sorted_By_Pairs.dat' %(path),dtype=(tuple,tuple,float,float))
#C = numpy.loadtxt('%s/Correlation_Sorted_By_Pairs.dat' %(path), unpack=True)
B = numpy.genfromtxt('./Input/Edge_distribution_BARABASI_1.dat',dtype=(tuple,tuple),delimiter=',')
B=[(int(a[0].strip('(')),(int(a[1].strip(')')))) for i,a in enumerate(B)]
D = numpy.genfromtxt('%s/PLV_sync.dat' %(path),dtype=(int,int,float))



C_Conectats=[]
D_Conectats=[]
#C_NoConectats=[]

for i in range(len(B)):
	
	C_NoConectats=[]
	for j in range(len(C)):
		if((int(C[j][0]),int(C[j][1])) == (int(B[i][0]),int(B[i][1])) or (int(C[j][1]),int(C[j][0])) == (int(B[i][0]),int(B[i][1]))):
			C_Conectats.append((C[j][0],C[j][1],C[j][2],C[j][3]))
						
		else:
			
			C_NoConectats.append((C[j][0],C[j][1],C[j][2],C[j][3]))
	for j in range(len(D)):
		if((int(D[j][0]),int(D[j][1])) == (int(B[i][0]),int(B[i][1])) or (int(D[j][1]),int(D[j][0])) == (int(B[i][0]),int(B[i][1]))):
			D_Conectats.append((D[j][0],D[j][1],D[j][2]))


C_Conectats = sorted(C_Conectats,key=lambda item: item[2],reverse=True)
for i in range(len(C_Conectats)):			
	print >>fout1,C_Conectats[i][0],C_Conectats[i][1],C_Conectats[i][2],C_Conectats[i][3]
C_NoConectats = sorted(C_NoConectats,key=lambda item: item[2],reverse=True)
for j in range(len(C_NoConectats)):			
	print >>fout2,C_NoConectats[j][0],C_NoConectats[j][1],C_NoConectats[j][2], C_NoConectats[j][3]
D_Conectats = sorted(D_Conectats,key=lambda item: item[2],reverse=True)
for j in range(len(D_Conectats)):
	print >> fout3,D_Conectats[j][0],D_Conectats[j][1],D_Conectats[j][2]


