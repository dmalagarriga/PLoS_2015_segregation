#!/bin/bash

# Perque les comes siguin punts
LANG=C
export LANG
LC_ALL=C
export LC_ALL
export alpha
export beta
export alpha_old=0
export Nodes=50
export Initial_Nodes=1
export Network=BARABASI
export Seed

for alpha in $(seq 00.00 05.00 00.00)
	do
	for beta in $(seq 00.00 05.00 00.00)
		do
		for ((Seed=1;Seed<=1;Seed++))
			do
			printf -v Num_alpha "%05.2f" $alpha
			printf -v Num_beta "%05.2f" $beta
			printf -v Num_seed "%04i" $Seed
			#python Create_Network.py
			./Run.bash
			mkdir -p Output_Scale_free_1_init_node/Output_Network_Seed_${Num_seed}/Output_0001
			mv Output_0001/* Output_Scale_free_1_init_node/Output_Network_Seed_${Num_seed}/Output_0001/
			rm -r Output_0001
			#export P_Dir="Output_Scale_free_1_init_node/Output_Network_Seed_${Num_seed}/Output_0001/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}"
			#export P_Dir="Output_Ring_Connectivity/Output_0001/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}"
			#python ./CLUSTERING/Sum_Clusters.py
			#python Create_Exc_Inh_figure.py
			#python Clustering_own.py
			#python Cross_correlation_connected_edges.py 
			#python Regularity_List.py
			#python Scatter_degree_Exc_Inh.py
			#python Scatter_Regularity.py
			#python EIS.py
			#gnuplot Plot_Correlation_Connected_Edges.gnu
			#python Regularity_New.py
			#python Correlation_Regularity.py
			#gnuplot Plot_Corr_vs_Pair.gnu
			#python PLV.py
			#python correlationbo.py
			#python coherence.py
			#python Classification_Synchronization_Types.py
			done
		alpha_old=${alpha}		
		done
	#alpha_old=${alpha}
	done
printf "done\n"
