import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pylab
import os


initial_nodes=1

nodeListEXCA=[]
nodeListEXCB=[]
nodeListINHA=[]
nodeListINHB=[]
Colormap1=[]
Colormap2=[]
#path=os.getenv('P_Dir')
path1 = 'Output_Scale_free_1_init_node_3/Output_Network_Seed_0001/Output_0001/Output_alpha_175.00/Output_beta_15.00/'
#path2 = 'Output_Scale_free_1_init_node/Output_Network_Seed_0001/Output_0001/Output_alpha_100.00/Output_beta_45.00/'
#alpha=os.getenv('alpha')
#beta=os.getenv('beta')
A=np.genfromtxt('%s/Which_cluster_Exc_Inh.dat' %path1,dtype="f8,|S3")
#B=np.genfromtxt('%s/Which_cluster_Exc_Inh.dat' %path2,dtype="f8,|S3")
C1 = np.loadtxt('%s/List_Reg_not_sorted.dat' %path1,unpack=True)
#C2 = np.loadtxt('%s/List_Reg_not_sorted.dat' %path2,unpack=True)
C1.view('f8,f8,f8').sort(order=['f0'], axis=-1) #Sort for colormapping
#C2.view('f8,f8,f8').sort(order=['f0'], axis=-1)

for i in range(50):
	if(A[i][1]=='Exc'):
		nodeListEXCA.append(i)
	if(A[i][1]=='Inh'):
		nodeListINHA.append(i)
	'''
	if(B[i][1]=='Exc'):
		nodeListEXCB.append(i)
	if(B[i][1]=='Inh'):
		nodeListINHB.append(i)
	'''
	Colormap1.append(C1[2][i])
	#Colormap2.append(C2[2][i])
 
G=nx.barabasi_albert_graph(50,initial_nodes,seed=1)
H=G.to_directed()
for u,v,d in sorted(H.edges(data=True)): #u,v -> pairs, d=weight
	d['weight']=1./H.in_degree(v)


#position = nx.spring_layout(H)
position = {0:  ([ 0.42171447,  0.36624474]), 1:  ([ 0.27835402,  0.57645869]), 2:  ([ 0.70713832,  0.43504537]), 3:  ([ 0.79295514,  0.63469889]), 4:  ([ 0.87275703,  0.31531177]), 5:  ([ 0.19338322,  0.25321228]), 6:  ([ 0.62960323,  0.60557565]), 7:  ([ 0.80488831,  0.79570882]), 8:  ([ 0.22708454,  0.12506547]), 9:  ([ 0.86004523,  0.6818332 ]), 10:  ([ 0.23780114,  0.83137355]), 11:  ([ 0.50635835,  0.31935575]), 12:  ([ 0.19578812,  0.50293847]), 13:  ([ 0.85244911,  0.45402593]), 14:  ([ 0.2100549 ,  0.95737484]), 15:  ([ 0.42108751,  0.16371832]), 16:  ([ 0.79616455,  0.92104627]), 17:  ([ 0.32502199,  0.40051425]), 18:  ([ 0.81118556,  0.23715869]), 19:  ([ 1.04908159,  0.20114414]), 20:  ([ 0.9603631 ,  0.34510215]), 21:  ([ 0.20749589,  0.61441376]), 22:  ([ 0.1067045 ,  0.66612503]), 23:  ([ 0.10661692,  0.40643112]), 24:  ([ 0.02109619,  0.71804176]), 25:  ([ 0.29630843,  0.75620989]), 26:  ([ 0.77264734,  0.32278909]), 27:  ([ 0.56637322,  0.29288791]), 28:  ([ 0.40646795,  0.68953242]), 29:  ([ 0.71585117,  0.70037731]), 30:  ([ 0.94090026,  0.46592304]), 31:  ([ 0.37341987,  0.03891329]), 32:  ([ 0.29356884,  0.12460151]), 33:  ([ 0.05802269,  0.32214673]), 34:  ([ 0.00977545,  0.22167312]), 35:  ([ 0.79315063,  1.05        ]), 36:  ([ 0.53349251,  0.20963861]), 37:  ([ 0.44142946,  0.50166274]), 38:  ([ 0.3032838,  -0.1        ]), 39:  ([ 0.36181199,  0.59372331]), 40:  ([ 0.70089743,  0.31080511]), 41:  ([ 0.07144408,  0.15225059]), 42:  ([ 0.        ,  0.09694259]), 43:  ([ 0.100334,  0.5529214 ]), 44:  ([ 0.80433902,  0.53163181]), 45:  ([ 0.44638934,  0.008488029]), 46:  ([ 0.2051538,  0.38861911]), 47:  ([ 0.0016441 ,  0.38750248]), 48:  ([ 0.5716443 ,  0.09833529]), 49:  ([ 0.20562024,  0.74734859])}
nx.set_node_attributes(H,'pos',position)

node_color_EXCA = []
node_color_EXCB = []
node_color_INHA = []
node_color_INHB = []



for i in range(len(nodeListEXCA)):
	node_color_EXCA.append(Colormap1[nodeListEXCA[i]])
for i in range(len(nodeListEXCB)):
	node_color_EXCB.append(Colormap1[nodeListEXCB[i]])
for i in range(len(nodeListINHA)):
	node_color_INHA.append(Colormap1[nodeListINHA[i]])
for i in range(len(nodeListINHB)):
	node_color_INHB.append(Colormap1[nodeListINHB[i]])


nx.draw_networkx_nodes(H,pos=position, nodelist=nodeListEXCA, node_color="b",label=None)
nx.draw_networkx_nodes(H,pos=position, nodelist=nodeListINHA, node_color="b",label=None)

nx.draw_networkx_edges(H,position)
#nx.draw_networkx_labels(H,position)

# specifiy edge labels explicitly
#nx.draw_networkx_edge_labels(H,position,edge_labels={(0,2):r'$\alpha,\beta $'},fontsize=30)
#nx.draw_networkx_edge_labels(H,position,edge_labels={(2,3):r'$\alpha,\beta $'},fontsize=30)

pylab.savefig('./Output_Scale_free_1_init_node_3/Network.eps')
pylab.close()
'''
nx.draw_networkx_nodes(H,pos=position, nodelist=nodeListEXCA, node_color="g",label=None)
nx.draw_networkx_nodes(H,pos=position, nodelist=nodeListINHA, node_color="r",label=None)
'''
nx.draw_networkx_nodes(H,pos=position, nodelist=nodeListEXCA, node_color=np.array(node_color_EXCA),node_shape="^",cmap=matplotlib.cm.gnuplot,labels=None)
nx.draw_networkx_nodes(H,pos=position, nodelist=nodeListINHA, node_color=np.array(node_color_INHA),node_shape="s",cmap=matplotlib.cm.gnuplot,labels=None)

nx.draw_networkx_edges(H,position)
#nx.draw_networkx_labels(H,position)


cb=plt.colorbar(shrink=0.7)
cb.set_alpha(1)
cb.set_ticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
cb.set_ticklabels([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
for a in cb.ax.get_yticklabels():
	a.set_fontsize(20)
plt.clim([0.0,1.0])
cb.set_label('Reg',fontsize=20,labelpad=15)

ax1=plt.gca()
ax1.set_frame_on(False)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_xticklabels([])
#ax1.set_ytickslabels([])

#pylab.savefig('%s/Exc_Inh_alpha_%s_beta_%s.eps' %(path1,alpha,beta))
pylab.savefig('%s/Exc_Inh_alpha_175_beta_15_4.eps' %(path1))
pylab.close()
'''
#nx.draw_networkx_nodes(H,pos=position, nodelist=nodeListEXCB, node_color="g",node_shape="^")
#nx.draw_networkx_nodes(H,pos=position, nodelist=nodeListINHB, node_color="r",node_shape="s")

nx.draw_networkx_nodes(H,pos=position, nodelist=nodeListEXCB, node_color=np.array(node_color_EXCB),node_shape="^",cmap=matplotlib.cm.gnuplot)
nx.draw_networkx_nodes(H,pos=position, nodelist=nodeListINHB, node_color=np.array(node_color_INHB),node_shape="s",cmap=matplotlib.cm.gnuplot)

nx.draw_networkx_edges(H,position)
nx.draw_networkx_labels(H,position)

cb=plt.colorbar(shrink=0.7)
cb.set_alpha(1)
cb.set_ticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
cb.set_ticklabels([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
for a in cb.ax.get_yticklabels():
	a.set_fontsize(20)
plt.clim([0.0,1.0])

cb.set_label('Reg',fontsize=20,labelpad=15)
ax1=plt.gca()
ax1.set_frame_on(False)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_xticklabels([])
#ax1.set_ytickslabels([])
#pylab.savefig('%s/Exc_Inh_alpha_%s_beta_%s.eps' %(path2,alpha,beta))
pylab.savefig('%s/Exc_Inh_alpha_100_beta_45_3.eps' %(path2))
pylab.close()
'''
