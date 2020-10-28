#!/usr/bin/python
# -*- coding: utf-8 -*-
from scipy import *
from sys import argv
import os

File_Dat1="./Input/Kex.dat"
File_Dat2="./Input/Kin.dat"
File_Dat3="./Input/Kex_2.dat"
File_Dat4="./Input/Kin_2.dat"
File_Dat5="./Input/Kex_3.dat"
File_Dat6="./Input/Kin_3.dat"
nNodes=int(os.getenv('Nodes'))
mu, sigma = 1.0, 0.0
mu2, sigma2 = 1.0, 0.0
mu3, sigma3 = 1.0, 0.0
mu4, sigma = 1.0, 0.0
mu5, sigma2 = 1.0, 0.0
mu6, sigma3 = 1.0, 0.0


if len(argv)>1:
   nNodes=int(argv[1])

if len(argv)>2:
   sigma=float(argv[2])

######################
# Filling the matrix #
######################
Matrix1=zeros([nNodes,nNodes])
for i in range(nNodes):
    for j in range(i,nNodes):
        x=mu + sigma*random.randn(1)
        Matrix1[i,j] = abs(x)/nNodes
        Matrix1[j,i] = Matrix1[i,j]
        if i==j:
           Matrix1[i,j]=0.0
#Matrix1=Matrix1/Matrix1.max()

fout1=open(File_Dat1,'w')
print >> fout1, nNodes
for i in range(nNodes):
    for j in range(nNodes):
        print >>fout1,Matrix1[i,j],
        if j!= nNodes-1:
           print >>fout1," ",
        else:
           print >>fout1
fout1.close()
#########################################
Matrix2=zeros([nNodes,nNodes])
for i in range(nNodes):
    for j in range(i,nNodes):
        x2=mu2 + sigma2*random.randn(1)
        Matrix2[i,j] = abs(x2)/nNodes
        Matrix2[j,i] = Matrix2[i,j]
        if i==j:
           Matrix2[i,j]=0.0
#Matrix2=Matrix2/Matrix2.max()

fout2=open(File_Dat2,'w')
print >> fout2, nNodes
for i in range(nNodes):
    for j in range(nNodes):
        print >>fout2,Matrix2[i,j],
        if j!= nNodes-1:
           print >>fout2," ",
        else:
           print >>fout2

fout2.close()
#########################################
Matrix3=zeros([nNodes,nNodes])
for i in range(nNodes):
    for j in range(i,nNodes):
        x3=mu3 + sigma3*random.randn(1)
        Matrix3[i,j] = abs(x3)
        Matrix3[j,i] = Matrix3[i,j]
        if i==j:
           Matrix3[i,j]=0.0
#Matrix3=Matrix3/Matrix3.max()

fout3=open(File_Dat3,'w')
print >> fout3, nNodes
for i in range(nNodes):
    for j in range(nNodes):
        print >>fout3,Matrix3[i,j],
        if j!= nNodes-1:
           print >>fout3," ",
        else:
           print >>fout3
fout3.close()
#########################################
# the histogram of the data
#n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

## add a 'best fit' line
#y = mlab.normpdf( bins, mu, sigma)
#l = plt.plot(bins, y, 'r--', linewidth=1)

#plt.xlabel('Smarts')
#plt.ylabel('Probability')
#plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
#plt.grid(True)

#plt.show()
