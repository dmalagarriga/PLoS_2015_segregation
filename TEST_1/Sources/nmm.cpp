#include <iostream>
#include <cstdlib>
#include "../Headers/Parameters.h"
#include "../Headers/Heun.h"
#include "gsl/gsl_rng.h"
#include "gsl/gsl_randist.h"


using namespace std;

Parameters * P;
const gsl_rng_type * T;
unsigned long int seed=atof(getenv("SEED"));
gsl_rng * r;
float FREQ=strtod(getenv("Frequencia"),NULL);
float AMP=strtod(getenv("Amplitud"),NULL);




int main (int argc, char **argv){

    
    P=new Parameters;

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
//Initial conditions for the forced nodes (for auxiliary method)

 	//P->V[i].phase=gsl_ran_gaussian(r,15.0);
	//P->V[i].p +=1*gsl_ran_gaussian(r,0.0); //Gaussian distribution with sigma=2.0
	//P->V[i].p +=1* gsl_ran_flat(r,-4.0,4.0);
	//cout << P->V[i].p << " " << endl;
		}
	
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
