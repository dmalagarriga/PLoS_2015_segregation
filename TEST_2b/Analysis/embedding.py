from scipy import *
from matplotlib import *
from pylab import *

Delay=10
path=os.getenv('P_Dir')
path_data=os.getenv('P_Data')
Kv=os.getenv('K')
fout=open('%s/Emb_plot_K_%s.dat' %(path,Kv),'w')
Lines=open('%s/Data_0155.dat' %path_data,'r').readlines()
for i,Line in enumerate(Lines):
    if i>Delay:
       Words=Line.split()
       Words2=Lines[i-Delay].split()
       print >> fout, Words2[1],Words[1], Words2[2],Words[2]