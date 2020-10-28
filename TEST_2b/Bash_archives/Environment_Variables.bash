#!/bin/bash

export Dir_Output="Output"
export Dir_Input="Input"
export NumPar_Dat="Input/NumPar.dat"
export VoxPar_Dat="Input/VoxPar.dat"
export Kex_Dat="Input/Kex.dat"
export Kin_Dat="Input/Kin.dat"
export Data_Dat="Output/Data.dat"
export Init_Cond_Dat="Output/Init_Cond.dat"
export p=155
export K_Conn=800
export GSL_RNG_SEE=20
export Nodes=50
export SEED
export Frequencia=08.50
export Amplitud=65
export alpha
export beta
# Perque les comes siguin punts
LANG=C
export LANG
LC_ALL=C
export LC_ALL
export alpha_old=0

printf -v Num_p "%04i" $p
printf -v Num_freq "%04s" $Frequencia
printf -v Num_amp "%04i" $Amplitud