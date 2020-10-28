#!/usr/bin/python
import numpy
from pylab import *
from numpy import *
from scipy import *
from scipy.stats import mode
from scipy.misc.common import factorial
from scipy.spatial.distance import correlation,euclidean
from math import log
import os

path=os.getenv('P_Dir')

#Mutual information
'''
Definition:

                                        p(x,y)
    I(X;Y) = sum     sum    p(x,y) log --------
            x in X  y in Y             p(x)p(y)

'''


def log2(n):  return log(n)*1.0/log(2)
def log10(n):  return log(n)*1.0/log(10)

def mutual_info(x,y):
    N=double(x.size)
    I=0.0
    eps = numpy.finfo(float).eps
    for l1 in unique(x):
        for l2 in unique(y):
            #Find the intersections
            l1_ids=nonzero(x==l1)[0]
            l2_ids=nonzero(y==l2)[0]
            pxy=(double(intersect1d(l1_ids,l2_ids).size)/N)+eps
            I+=pxy*log2(pxy/((l1_ids.size/N)*(l2_ids.size/N)))
    return I

    
#Normalized mutual information
def nmi(x,y):
    N=x.size
    I=mutual_info(x,y)
    Hx=0
    for l1 in unique(x):
        l1_count=nonzero(x==l1)[0].size
        Hx+=-(double(l1_count)/N)*log2(double(l1_count)/N)
    Hy=0
    for l2 in unique(y):
        l2_count=nonzero(y==l2)[0].size
        Hy+=-(double(l2_count)/N)*log2(double(l2_count)/N)
    return I/((Hx+Hy)/2)
    
PLV=loadtxt('%s/PLV_sync.dat' %path,unpack=True)
Corr=loadtxt('%s/Correlation_Sorted_By_Pairs.dat' %path,unpack=True)
XCorr=correlation(PLV[2],Corr[2])

print (XCorr)