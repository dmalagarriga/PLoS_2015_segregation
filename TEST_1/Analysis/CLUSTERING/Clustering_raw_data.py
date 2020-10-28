import time
import scipy.cluster.hierarchy as hcluster
import numpy.random as random
import numpy
import scipy
import os

import pylab
pylab.ion()

alpha=float(os.getenv('alpha'))
beta=float(os.getenv('beta'))
nNodes = int(os.getenv('Nodes')) # Column 0 also counts
path = os.getenv('P_Dir')
alpha_old=float(os.getenv('alpha_old'))
#----- -------- ------- -------- ----- -------- ------- --------
def augmented_dendrogram(*args, **kwargs):

    ddata = hcluster.dendrogram(*args, **kwargs)

    if not kwargs.get('no_plot', False):
        for i, d in zip(ddata['icoord'], ddata['dcoord']):
            x = 0.5 * sum(i[1:3])
            y = d[1]
            pylab.plot(x, y, 'ro')
            pylab.annotate("%.3g" % y, (x, y), xytext=(0, -8),
                          textcoords='offset points',
                          va='top', ha='center')

    return ddata
#----- -------- ------- -------- ----- -------- ------- -------- 

def llf(id):
    return str(id)

#----- -------- ------- -------- ----- -------- ------- -------- 

x = numpy.loadtxt('%s/Data_0155.dat' %path,unpack=True)
#data[:100,:100] += 10
D = scipy.zeros([nNodes,nNodes])
Trans=9990
Sum=0
for i in range(0,50):
    for j in range(0,50):
    	#D[i,j] = abs(numpy.mean(abs(x[i+1][Trans:]-x[i+1][Trans:].mean()) - abs(x[j+1][Trans:]-x[j+1][Trans:].mean())))
    	 D[i,j] = numpy.sqrt((numpy.sum((x[i+1][Trans:]-x[j+1][Trans:])**2)))
numpy.savetxt('%s/Distance_matrix_alpha_%s_beta_%s.dat' %(path,alpha,beta),D)    	
Y = hcluster.linkage(D, method='single',metric='euclidean')
numpy.savetxt('%s/Linkage_matrix.dat' %path,Y)
fout = open('./Clustering/Cluster_raw_data.dat','a')
for i in range(60,61):
    thresh = i
    clusters = hcluster.fclusterdata(D,thresh,criterion='distance',method='single',metric='euclidean')
    #clusters = hcluster.fcluster(Y,thresh,criterion='distance')
    #title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
    title = "%d" %len(set(clusters))
if(alpha_old!=alpha):
		print >> fout, " "
print >> fout, alpha, beta, title
#Y = hcluster.linkage(D method='single',metric='euclidean')
#fig = pylab.figure(figsize=(8,8))



#Z1 = augmented_dendrogram(Y,50, color_threshold=2,leaf_label_func=llf,leaf_rotation=90,truncate_mode='lastp',show_leaf_counts=False)
#pylab.draw()
#pylab.show()
#fig.savefig('dendrogram.png') 
#raw_input()

#A=[]
#B=[]
#for i in range(25):
#	A=numpy.concatenate([D[i,:]],axis=0)
	#A.extend(D[i,:])
	#A.append(D[i,:])
#for j in range(25,50):
#	B=numpy.concatenate([D[j,:]],axis=0)
	#B.append(D[j,:])		
	#B.extend(D[j,:])

#Mat	= numpy.matrix([B,A])	
#numpy.savetxt('Matrix.dat',Mat)
#fig = pylab.figure(figsize=(8,8))	
#pylab.title(title)
#pylab.scatter(A,B,c=clusters,s=50)
#pylab.scatter(*Mat[:,:],c=clusters,s=50)
#pylab.scatter(D[:,10],D[:,13],c=clusters,s=50)
#pylab.scatter(D[:,1],D[:,2],D[:,3],c=clusters)
#pylab.axis("equal")
#time.sleep(0.5)

#pylab.draw()
#pylab.show()







