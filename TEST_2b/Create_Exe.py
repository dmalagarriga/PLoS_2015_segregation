#!/bin/python

from scipy import *
from numpy import *

seed_min = 1
seed_max = 1

alpha_min = 0
alpha_max = 0

beta_min = 0
beta_max = 0

fout1=open('Run.bash','w')
fout2=open('Parameters01.txt','w')
fout3=open('Create_Folders.bash','w')

print >> fout1, '#!/bin/bash'
print >> fout1, 'source Bash_archives/Environment_Variables.bash'
print >> fout3, '#!/bin/bash'
print >> fout3, 'source Bash_archives/Environment_Variables.bash'

#print >> fout, 'Create_Data=1'
#print >> fout, 'Analysis=0'
#print >> fout, ' '

print >> fout1, 'printf "Compiling ..."'
print >> fout1, 'make'
print >> fout1, 'printf "Compiled!"'
#print >> fout, ' '
print >> fout1, 'printf "Running ..."'

#print >> fout, 'printf -v Num_p "%04i" $p'
#print >> fout, 'printf -v Num_freq "%04s" $Frequencia'
#print >> fout, 'printf -v Num_amp "%04i" $Amplitud'
#print >> fout1, './nmm.exe'
print >> fout3, 'for alpha in $(seq %02.02f 01.00 %02.02f)' %(alpha_min,alpha_max)
print >> fout3, '		do'
print >> fout3, '		for beta in $(seq %02.02f 01.00 %02.02f)' %(alpha_min,alpha_max) 
print >> fout3, '			do'
print >> fout3, '			for ((SEED=%01i;SEED<=%01i;SEED++))' %(seed_min,seed_max)
print >> fout3, '				do'
print >> fout3, '				printf -v Num_seed "%04i" $SEED'
print >> fout3, '				printf -v Num_alpha "%05.2f" $alpha'
print >> fout3, '				printf -v Num_beta "%05.2f" $beta'
print >> fout3, '				mkdir -p Output/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}' 
print >> fout3, '				done'
print >> fout3, '			done'
print >> fout3, '		done'

for seed in range(1,2):
	for alpha in range(0,1):
		for beta in range(0,1):
			print >> fout2, '%04i %05.2f %05.2f Output/Output_%04i/Output_alpha_%05.2f/Output_beta_%05.2f/ Output/Output_%04i/Output_alpha_%05.2f/Output_beta_%05.2f/Data_0155.dat Output/Output_%04i/Output_alpha_%05.2f/Output_beta_%05.2f/Init_Cond_%04i.dat > Output/Output_%04i/Output_alpha_%05.2f/Output_beta_%05.2f/P_Hist_alpha_%05.2f_beta_%05.2f.dat' %(seed,alpha,beta,seed,alpha,beta,seed,alpha,beta,seed,alpha,beta,seed,seed,alpha,beta,alpha,beta) 
			print >> fout1, './nmm.exe %04i %05.2f %05.2f Output/Output_%04i/Output_alpha_%05.2f/Output_beta_%05.2f/ Output/Output_%04i/Output_alpha_%05.2f/Output_beta_%05.2f/Data_0155.dat Output/Output_%04i/Output_alpha_%05.2f/Output_beta_%05.2f/Init_Cond_%04i.dat > Output/Output_%04i/Output_alpha_%05.2f/Output_beta_%05.2f/P_Hist_alpha_%05.2f_beta_%05.2f.dat' %(seed,alpha,beta,seed,alpha,beta,seed,alpha,beta,seed,alpha,beta,seed,seed,alpha,beta,alpha,beta) 

print >> fout1, 'printf "done!\n"'
print >> fout1, 'rm -f nmm.exe'
