#!/bin/bash

#source Environment_Variables.bash

#function Crea_Arxiu {
#cat >> ${File_Out} << EOF
#200 
#EOF
#return
#}

#printf "Creating input files ... "
#for i in $(seq 1)
#    do
#    Num=$(echo "${i}" | awk '{printf "%06.3f",$1*0.01}')
#    File_Out="Input/P.dat"
#    Crea_Arxiu
#done
#printf "done\n"

Create_Data=1
Analysis=1

export Dir_Output="Output"
export Dir_Input="Input"
export NumPar_Dat="Input/NumPar.dat"
export VoxPar_Dat="Input/VoxPar.dat"
export Kex_Dat="Input/Kex.dat"
export Kin_Dat="Input/Kin.dat"
export Data_Dat="Output/Data.dat"
export Init_Cond_Dat="Output/Init_Cond.dat"
export p=800
export K_Conn=800
export GSL_RNG_SEE=20
export Nodes=51
export SEED=10
export Frequencia=10.8
export Amplitud=10
export alpha
export beta
# Perque les comes siguin punts
LANG=C
export LANG
LC_ALL=C
export LC_ALL
export alpha_old=0

printf "Running ...\n "
for p in 155
	do
	for alpha in $(seq 00.00 05.00 180.00)
	#for alpha in 18.0
		do
		for beta in $(seq 00.00 05.00 50.00)
		#for beta in 8.0
			do
			#python Create_Matrix
			for ((SEED=1;SEED<=1;SEED++))
				do
				printf -v Num_p "%04i" $p
				printf -v Num_alpha "%05.2f" $alpha
				printf -v Num_beta "%05.2f" $beta
				printf -v Num_seed "%04i" $SEED
				mkdir -p Output
				mkdir -p Output/Output_${Num_seed}
        		mkdir -p Output/Output_${Num_seed}/Output_alpha_${Num_alpha}
				mkdir -p Output/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}
        			Dir_Output="Output/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}"
       				Data_Dat="Output/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Data_${Num_p}.dat" 
					Init_Cond_Dat="Output/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Init_Cond_${Num_seed}.dat"
				export P_Dir="Output/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}"
				mkdir -p Clustering
				#python Corr_Coefficient.py
				#python Clustering_XCorr.py 
				python Sum_Clusters.py
				done
					
		alpha_old=${alpha}
		done

	done

done
printf "done\n"
#rm -f nmm.exe


