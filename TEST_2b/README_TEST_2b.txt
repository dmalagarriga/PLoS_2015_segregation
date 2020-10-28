#####################################################################################
# Guide for the simulation. Follow the following steps to perform the simulations:	#	
# 	1 - First run 'python Create_Exe.py' to create 'Run.bash' file. 				#
#   2 - chmod +x to 'Create_Folders.bash' and run './Create_Folders.bash'			#	
#	*( - There is a loop for writing the parameters in the Run.bash, 			 	# 	
#		as well as the random number generator seed (explained below). It's not	 	#
#		necessary to modify parameters.	)											#
#	3 - chmod +x to Run.bash													 	#
#	4 - Execute ./Run.bash															#
#	5 - Results are in folder 'Output/Output_{SEED}/Output_alpha_{alpha}/			#	
#		Output_beta{}/Data_{p}.dat' 												#
#   6 - Plot column 1 (time) against other columns (up to 51) in 'Data_{p}.dat'     #
#   	to get timetraces. 															#
#####################################################################################

* Beware of the parameters alpha and beta range set in 'Create_Exe.py'. If you want to simulate for only 1 condition, 
please modify the loop inside accordingly (see example below).

e.g.

CHANGE
"""
for seed in range(1,21):
	for alpha in range(0,181):
		for beta in range(0,51):
"""

TO 
"""
for seed in range(1,2):
	for alpha in range(0,1):
		for beta in range(0,1):
"""