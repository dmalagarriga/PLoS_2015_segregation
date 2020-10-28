import matplotlib
matplotlib.use('Agg')
import numpy
import scipy
import os
import pylab
import networkx as nx
pylab.ion()

path_reg=os.getenv('P_Reg')
path_op=os.getenv('P_OP')
#fout1 = open('%s/Multiplication_Reg_XCorr.dat' %path_reg,'w')
#fout2 = open('%s/Substraction_Reg_XCorr.dat' %path_reg,'w')
fout3 = open('%s/Substraction_XCorr_PLV_2.dat' %path_op,'w')

#Reg=numpy.loadtxt('%s/Regularity.dat' %path_reg,unpack=True)
XCorr=numpy.loadtxt('%s/Correlation_SurfPlot.dat' %path_op,unpack=True)
PLV=numpy.loadtxt('%s/PLV_SurfPlot_2.dat' %path_op,unpack=True)


for i in range(len(XCorr[0])):	
	'''
	for j in range(len(Reg[0])):
		if((float(Reg[0][j]),float(Reg[1][j]))==(float(XCorr[0][i]),float(XCorr[1][i]))):
			print >> fout2, XCorr[0][i],XCorr[1][i], abs(XCorr[2][i]-Reg[2][j]),Reg[2][j], XCorr[2][i]
			if(float(Reg[0][i+1])!=Reg[0][i]):
				print >> fout2," "
			print >> fout1, XCorr[0][i],XCorr[1][i], Reg[2][j]*XCorr[2][i],Reg[2][j], XCorr[2][i]
			if(float(Reg[0][i+1])!=Reg[0][i]):
				print >> fout1," "
	'''
	for j in range(len(PLV[0])):
		if((float(XCorr[0][j]),float(XCorr[1][j]))==(float(PLV[0][i]),float(PLV[1][i]))):
			print >> fout3, XCorr[0][i],XCorr[1][i], PLV[2][j]-XCorr[2][i], PLV[2][j], XCorr[2][i]
			if(float(XCorr[0][i+1])!=XCorr[0][i]):
				print >> fout3," "
		