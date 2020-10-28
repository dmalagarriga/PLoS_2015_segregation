#ifndef _VOXEL_H_
#define _VOXEL_H_

//Class Voxel

//#include <cstdio>
#include <string>
#include <iostream>
#include <cstdlib>
#include "gsl/gsl_rng.h"
#include "gsl/gsl_randist.h"


extern gsl_rng * r;



using namespace std;
class voxel
{
	public:
	
	float * y;
	float * f;

	float * yold;
	float * f_old;
	float * y1y2;

	string VoxPar_Dat;
	
	
	int nDelays;
	int Dv;
	float X;
	float phase;
	float Kconn;
	float alpha;
	float beta;
	
	float A;
	float a;
	float B;
	float b;
	float c1; 
	float c2;
	float c3;
	float c4;
	float c5;
	float c6;
	float e0;
	float r;
	float nu0;
	float p;
	float epsilon;
	float amp;
	float freq;
	 
	public:	
	
	
	void set_Initial_Conditions(void);
	void Dim(void);
	void Read_VoxPar_Dat(void);

	voxel();
	~voxel();
};
#endif
