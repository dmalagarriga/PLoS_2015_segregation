#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
from scipy import *
from pylab import *
from numpy import *
import glob
import os
from os.path import join as pjoin
import spectrum
#from matplotlib.backends.backend_pdf import PdfPages


def comparacio(a,b):
        
	(Sepa,numa) = a.split('_')
	(pa,exta) = numa.split('.')	

	(Sepb,numb) = b.split('_')
	(pb,extb) = numb.split('.')
        value=float(pa)-float (pb)
        return int(value/abs(value))



nTrans=1000
path=os.getenv('P_Dir')
nNodes=int(os.getenv('Nodes'))
#p=os.getenv('p')
infile = ( '%s/Data_0155.dat' %(path))
		
	
#(Sep,num) = infile.split('_')
         
#(p,ext) = num.split('.')

#Load data 
#########################################################################
y0 = loadtxt(infile, unpack=True)
for i in range(1,nNodes):
	#f=y0[i][nTrans:]
	
	A = average(y0[i])
	
	#M = y0[i][nTrans:] - A		
		

	
# Begin plots
##################################################################
	
	time = loadtxt(infile, unpack=True, usecols = [0])
	
	(pxx,freqs)=spectrum.PSD(time[nTrans:], y0[i][nTrans:]-y0[i][nTrans:].mean(),16384)
	plot(freqs, pxx)
	grid('on')
	#title('P= %s' %p)
	xlabel('Frequency')
	ylabel('PSD (1/Hz)')
	xlim([0, 40])	
	#ylim([-6, 5])
	MAXTAB1 = list(pxx)
	MAX1= MAXTAB1.index(max(MAXTAB1))
	xs,ys =freqs[MAX1],max(MAXTAB1)
	ax = gca()
	#ax.annotate('(Frequency = %.3f, PSD = %.3f)' %(freqs[MAX1],max(MAXTAB1)),xy=(freqs[MAX1],max(MAXTAB1)))
	ax.annotate('%.3f' %(freqs[MAX1]),xy=(freqs[MAX1],max(MAXTAB1)))
	plot(xs,ys,marker='o')
	#hold()
	#spectrum.savefig(pjoin(path, 'Spectrum_%s_%i.eps' % (p,i)))	
	#spectrum.savefig(pjoin(path, 'Spectrum_%s.eps' % (p)))	

	
	#close()	
	
#################################################################
	
	
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

	
	file1 = 'Spectrum.dat'	
	path_file12 = pjoin(path, file1)
	arx1 = open(path_file12,'w')
	
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	
	'''
	Filename1 = 'SpectrumFreq1.dat'
	path_file13 = pjoin(path, Filename1)
	Arx1 = open(path_file13, 'a')
	'''
	
	
	
	
	for j in range(len(freqs)):
		print >>arx1, freqs[j], str(pxx[j]).strip('[]')
	#print >>arx1, p, str(max(MAXTAB[1])).strip('[]')#convert to string to write without brackets	
	arx1.close()			 
	#print >>Arx1, p, freqs[MAX1]
	
close()



#Arx1.close()
	
		
