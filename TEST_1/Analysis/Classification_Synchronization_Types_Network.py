import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy
import scipy
import os
import pylab
import networkx as nx
pylab.ion()

########################
# Computes which pairs are highly cross 
# correlated and highly PLV (Phase Locking Value) 
# correlated
########################

path=os.getenv('P_Dir')
initial_nodes=1

C = numpy.genfromtxt('%s/Cross_correlation_connected_edges.dat' %(path),dtype=(int,int,float,float))
D = numpy.genfromtxt('%s/PLV_connected_edges.dat' %(path),dtype=(int,int,float))
#C = numpy.genfromtxt('%s/Correlation_Sorted_By_Pairs.dat' %(path),dtype=(tuple,tuple,float,float))
#C = numpy.loadtxt('%s/Correlation_Sorted_By_Pairs.dat' %(path), unpack=True)
B = numpy.genfromtxt('./Input/Edge_distribution_BARABASI_1.dat',dtype=(tuple,tuple),delimiter=',')
B=[(int(a[0].strip('(')),(int(a[1].strip(')')))) for i,a in enumerate(B)]

Complete_Sync_Pairs=[]
PLV_Sync_Pairs=[]
Lag_Sync_Pairs=[]
Not_Sync_Pairs=[]

for j in range(len(C)):
	if(C[j][3]==0.0):
		if(C[j][2] >=0.9):
			Complete_Sync_Pairs.append((C[j][0],C[j][1]))
		else:
			Not_Sync_Pairs.append((C[j][0],C[j][1]))
	elif(C[j][3]!=0.0):
		if(C[j][2] >=0.9):
			Lag_Sync_Pairs.append((C[j][0],C[j][1]))

		else:
			Not_Sync_Pairs.append((C[j][0],C[j][1]))
	
print Not_Sync_Pairs
				
for j in range(len(D)):
	if(D[j][2]>=0.9):
		if((D[j][0],D[j][1])!=(C[j][0],C[j][1])):
			PLV_Sync_Pairs.append((D[j][0],D[j][1]))



# Draw the graph with highlighted edges

G=nx.barabasi_albert_graph(50,initial_nodes,seed=1)
H=G.to_directed()
for u,v,d in sorted(H.edges(data=True)): #u,v -> pairs, d=weight
	d['weight']=1./H.in_degree(v)


#position = nx.spring_layout(H)
position = {0:  ([ 0.42171447,  0.36624474]), 1:  ([ 0.27835402,  0.57645869]), 2:  ([ 0.70713832,  0.43504537]), 3:  ([ 0.79295514,  0.63469889]), 4:  ([ 0.87275703,  0.31531177]), 5:  ([ 0.19338322,  0.25321228]), 6:  ([ 0.62960323,  0.60557565]), 7:  ([ 0.80488831,  0.79570882]), 8:  ([ 0.22708454,  0.12506547]), 9:  ([ 0.86004523,  0.6818332 ]), 10:  ([ 0.23780114,  0.83137355]), 11:  ([ 0.50635835,  0.31935575]), 12:  ([ 0.19578812,  0.50293847]), 13:  ([ 0.85244911,  0.45402593]), 14:  ([ 0.2100549 ,  0.95737484]), 15:  ([ 0.42108751,  0.16371832]), 16:  ([ 0.79616455,  0.92104627]), 17:  ([ 0.32502199,  0.40051425]), 18:  ([ 0.81118556,  0.23715869]), 19:  ([ 1.04908159,  0.20114414]), 20:  ([ 0.9603631 ,  0.34510215]), 21:  ([ 0.20749589,  0.61441376]), 22:  ([ 0.1067045 ,  0.66612503]), 23:  ([ 0.10661692,  0.40643112]), 24:  ([ 0.02109619,  0.71804176]), 25:  ([ 0.29630843,  0.75620989]), 26:  ([ 0.77264734,  0.32278909]), 27:  ([ 0.59637322,  0.30288791]), 28:  ([ 0.40646795,  0.68953242]), 29:  ([ 0.71585117,  0.70037731]), 30:  ([ 0.94090026,  0.46592304]), 31:  ([ 0.37341987,  0.03891329]), 32:  ([ 0.29356884,  0.12460151]), 33:  ([ 0.05802269,  0.32214673]), 34:  ([ 0.00977545,  0.22167312]), 35:  ([ 0.79315063,  1.05        ]), 36:  ([ 0.53349251,  0.20963861]), 37:  ([ 0.44142946,  0.50166274]), 38:  ([ 0.3032838,  -0.1        ]), 39:  ([ 0.36181199,  0.59372331]), 40:  ([ 0.70089743,  0.31080511]), 41:  ([ 0.07144408,  0.15225059]), 42:  ([ 0.        ,  0.09694259]), 43:  ([ 0.100334,  0.5529214 ]), 44:  ([ 0.80433902,  0.53163181]), 45:  ([ 0.44638934,  0.008488029]), 46:  ([ 0.2051538,  0.38861911]), 47:  ([ 0.0016441 ,  0.38750248]), 48:  ([ 0.5716443 ,  0.09833529]), 49:  ([ 0.20562024,  0.74734859])}
nx.set_node_attributes(H,'pos',position)

nx.draw_networkx_nodes(H,pos=position, node_color='b')
a=nx.draw_networkx_edges(H,position,edgelist=Complete_Sync_Pairs, width=2.5,edge_color='r', label="Complete synchronized")
b=nx.draw_networkx_edges(H,position,edgelist=Lag_Sync_Pairs,width=2.5,edge_color='g',label="Lag synchronized")
c=nx.draw_networkx_edges(H,position,edgelist=PLV_Sync_Pairs,width=2.5,edge_color='m',label="Phase locked")
nx.draw_networkx_edges(H,position,edgelist=Not_Sync_Pairs,width=1.0)
#nx.draw_networkx_labels(H,position)


ax1=plt.gca()
ax1.legend([a,b,c],['Complete synchronization','Lag synchronization','Phase locked'], frameon=False,loc='lower right')
ax1.set_frame_on(False)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_xticklabels([])
pylab.savefig('%s/Network.eps' %path)
pylab.close()

