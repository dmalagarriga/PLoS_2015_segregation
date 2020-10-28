#include <iostream>
#include <cstdlib>
#include "../Headers/Parameters.h"
#include "../Headers/Heun.h"
#include "gsl/gsl_rng.h"
#include "gsl/gsl_randist.h"


using namespace std;


Parameters * P;

const gsl_rng_type * T;
//unsigned long int seed=atof(getenv("SEED"));
gsl_rng * r;
float FREQ=strtod(getenv("Frequencia"),NULL);
float AMP=strtod(getenv("Amplitud"),NULL);

int main (int argc, char *argv[]){
	
	int seed=atoi(argv[1]);
	P=new Parameters(argv[4],argv[5],argv[6]);

    gsl_rng_env_setup();
    
   
    T = gsl_rng_default;
    r = gsl_rng_alloc (T);

    gsl_rng_set(r,seed);

//Initial conditions	
	for (int i=0; i<P->nNodes; i++){
		
		for (int j=0; j<6; j++){
		
			P->V[i].y[j] = 1*gsl_ran_gaussian(r,10.0);
			P->V[i].phase=0;
				
					}
			P->V[i].alpha=atof(argv[2]);
			P->V[i].beta=atof(argv[3]);
		}
	//cout << P->Dir_Output;
	P->WriteInitialConditions(seed);

	for (int i=0;i<P->nNodes;i++){
		
		P->V[i].amp=AMP;
		P->V[i].freq=FREQ;
		
		
				     }
	
	for (P->it=0; (P->it) < (P->nt); P->it++){	

	        Heun(P); 
          	P->RefreshDelay();	
		P->t+=P->dt;

        if (P->it % P->ntout ==0)
		{	
		 P->WriteData(); 	
		}
	    
						}	
	gsl_rng_free (r);
	delete P;

return EXIT_SUCCESS;
}
