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

    
# Generate random features and distance matrix.
#x = scipy.rand(40)

D = scipy.zeros([50,50])
x = numpy.loadtxt('%s/XCorr_Matrix_3.dat' %path,unpack=True)


for i in range(50):
	for j in range(50):
		D[i,j] = 1./x[i+1][j+1]

numpy.savetxt('%s/Distance_matrix_Xcorr.dat' %path,D)




#fig = pylab.figure(figsize=(8,8))
Y = hcluster.linkage(D, method='single')

# Compute and plot first dendrogram.
#sch.dendrogram(Z, p=30, truncate_mode=None, 
#color_threshold=None, get_leaves=True, orientation='top', labels=None, count_sort=False,
# distance_sort=False, show_leaf_counts=True, no_plot=False, no_labels=False, color_list=None, 
#leaf_font_size=None, leaf_rotation=None, leaf_label_func=None, no_leaves=False, show_contracted=False, link_color_func=None)

#Z1 = augmented_dendrogram(Y,20, leaf_label_func=llf,leaf_rotation=90,truncate_mode='lastp')
#pylab.draw()
#pylab.show()
#raw_input()
#fig.savefig('dendrogram_Xcorr.png')
#A=[]
#B=[]
fout=open('./Clustering/Cluster_XCorr.dat','a')
for i in range(6,7):
    thresh = i
    clusters = hcluster.fclusterdata(numpy.transpose(D),thresh,criterion='distance',method='single')    
    #title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
    title = "%d" %len(set(clusters))
if(alpha_old!=alpha):
		print >> fout, " "
print >> fout, alpha, beta, title
#for i in range(10):
#	A=numpy.concatenate([D[i,:]])
#for j in range(11,20):
#	B=numpy.concatenate([D[j,:]])	

#pylab.title(title)
#pylab.scatter(A,B,c=clusters)
#pylab.axis("equal")
#time.sleep(0.5)
#pylab.draw()
#pylab.show()
#pylab.clf()