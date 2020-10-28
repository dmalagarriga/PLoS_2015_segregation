#include "../Headers/Heun.h"
#include "../Headers/rhsjansen.h"
#include "../Headers/voxel.h"
#include "../Headers/Parameters.h"
#include <math.h>
#include "gsl/gsl_rng.h"
#include "gsl/gsl_randist.h"

void Heun (Parameters *P){
		
	rhsjansen(P);	
	
	for (int iV=0; iV < P->nNodes; iV++){
		P->V[iV].X=sqrt(2*P->V[iV].epsilon*P->dt)*gsl_ran_gaussian(r,1.0);
		
 		for (int iEq=0; iEq < 6; iEq++){
                       
			P->V[iV].yold[iEq] = P->V[iV].y[iEq];
			
			P->V[iV].f_old[iEq] = P->V[iV].f[iEq];
			
			P->V[iV].y[iEq] += (P->V[iV].f[iEq])*(P->dt); // This is y_tild

			 
                       		       }				 
			   P->V[iV].y[4]+=P->V[iV].X;	


					     }
				


	rhsjansen(P);	// This is f_tild
	for (int iV=0; iV<P->nNodes; iV++){
		for (int iEq=0; iEq < 6; iEq++){
			P->V[iV].y[iEq]=P->V[iV].yold[iEq]+0.5*(P->V[iV].f[iEq]+P->V[iV].f_old[iEq])*(P->dt);	
     }

			   P->V[iV].y[4]+=P->V[iV].X;	
	 

		
} 

};
