#ifndef _RHSJANSEN_H_
#define _RHSJANSEN_H_
#include <iostream>
#include "../Headers/Parameters.h"
//#include "gsl/gsl_rng.h"
#include "gsl/gsl_rng.h"
#include "gsl/gsl_randist.h"

extern gsl_rng * r;



void rhsjansen (Parameters *);

#endif
