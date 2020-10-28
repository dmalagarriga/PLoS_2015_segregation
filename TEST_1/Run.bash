#!/bin/bash

source Bash_archives/Environment_Variables.bash

Create_Data=1
Analysis=0

printf "Compiling ... \n "
make
printf "Compiled!\n"
printf "Running ...\n "
for p in 155
	do
	for alpha in $(seq 00.00 01.00 00.00)
		do
		for beta in $(seq 00.00 01.00 00.00)
			do
			for ((SEED=1;SEED<=1;SEED++))
				do
				for Frequencia in 08.50
					do
					for Amplitud in 65
						do
						
						printf -v Num_p "%04i" $p
						printf -v Num_alpha "%05.2f" $alpha
						printf -v Num_beta "%05.2f" $beta
						printf -v Num_seed "%04i" $SEED
						printf -v Num_freq "%04s" $Frequencia
						printf -v Num_amp "%04i" $Amplitud

						mkdir -p Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}
        				Dir_Output="Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}"
       					Data_Dat="Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Data_${Num_p}.dat" 
						Init_Cond_Dat="Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Init_Cond_${Num_seed}.dat"
						
						if [ $Create_Data -eq 1 ];then
						
						./nmm.exe > Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/P_Hist_alpha_${Num_alpha}_beta_${Num_beta}.dat  
						fi
						#tar rf Output.tar Output/*  
						#tar czf Output.tar.gz Output.tar
						#rm -r Output
						#export P_Dir="Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}"
						#export P_OP="Output_${Num_seed}/OrderParameter"
						#mkdir -p Output_${Num_seed}/Regularity/
						#export P_Reg="Output_${Num_seed}/Regularity"
						#mkdir -p Output_${Num_seed}/OrderParameter
						
						if [ $Analysis -eq 1 ];then
						./Bash_archives/Analysis.bash
						fi
						
						done
					done
				
				done
		alpha_old=${alpha}
		done
	#rm Output.tar
	
	done
	
	#rm Output.tar
done

#gnuplot Plot_SurfPlot_OP.gnu
#gnuplot Plot_SurfPlot_Reg.gnu
 
printf "done\n"
rm -f nmm.exe


