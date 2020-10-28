#ifndef _PARAMETERS_H_
#define _PARAMETERS_H_
#include <string>
#include <fstream>
#include <iostream>
#include <cstdlib>
#include "../Headers/voxel.h"
#include <math.h>
#include <gsl/gsl_rng.h>

using namespace std;

class Parameters{
//Atributs
	public:
	int it; //Contador
	int nt;	// Nombre de passos total
   	int ntout; // Nombre de pasos per l'output
	int neq; //Number of equations
	float dt; // Pas de temps
	float t;
	
	string Dir_Output;
	//char *Dir_Output;
    string Dir_Input;
    string NumPar_Dat;
	
	
	
	
	string Data_Dat;
	//char *Data_Dat;
	string Init_Cond_Dat;
   	int nNodes;
   	int nNodes_inh;
    string Kex_Dat;
    string Kin_Dat;
	
	float ** Kex; //Coupling matrix for excitatory population
	float ** Kin; //Coupling matrix for inhibitory population
	voxel * V; //Voxel
	
	
	
	ofstream fout_data;
	ofstream fout_init_cond;
		

    public:
   // Parameters();
    Parameters(char*,char*,char*);
    ~Parameters();
	
	//Mètodes
	
	void Read_Kex_Dat(void);
	void Read_Kin_Dat(void);
	void RefreshDelay(void);
	void Read_NumPar_Dat(void);
		
	
	void WriteData();
	void WriteInitialConditions(int);
	void openfiles();
	void closefiles();
	
        //private:

	
        

};

#endif
