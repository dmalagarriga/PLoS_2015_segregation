#include "../Headers/voxel.h"
#include "../Headers/Parameters.h"

using namespace std;

/*Constructor*/
voxel::voxel(){
    
	
	VoxPar_Dat=string ( getenv("VoxPar_Dat") );
	Read_VoxPar_Dat();
	
	
	nDelays = 1000;
	
	c2 = 0.8*c1;
	c3 = 0.25*c1;
	c4 = 0.25*c1;
	c5 = 0.0;
 	c6 = 0.0;
 	Dim();
	set_Initial_Conditions();
	
};

/*Constructors*/
void voxel::Dim(void){
	y = new float[6];	
	yold = new float[6];
	f = new float[6];
	f_old =new float[6];
	
	y1y2 = new float[nDelays];
	for (int i=0; i < nDelays; i++){
	y1y2[i]=0;
	}
	
	
};

void voxel::Read_VoxPar_Dat(void){
	string str;
 	ifstream fin (VoxPar_Dat.c_str(),ifstream::in);

	fin >> A; getline(fin,str);
 	cout << "A: " <<A<<endl;
 	fin >> a; getline(fin,str);
 	cout << "a: " <<a<<endl;
 	fin >> B; getline(fin,str);
 	cout << "B: " <<B<<endl;
 	fin >> b; getline(fin,str);
 	cout << "b: " <<b<<endl;
 	fin >> c1; getline(fin,str); 	
	cout << "c1: " <<c1<<endl;
	fin >> e0; getline(fin,str);
 	cout << "e0: " <<e0<<endl;
 	fin >> r; getline(fin,str);
 	cout << "r: " <<r<<endl;
 	fin >> nu0; getline(fin,str);
 	cout << "nu0: " <<nu0<<endl;
 	fin >> Dv; getline(fin,str);
 	cout << "Delay: " <<Dv<<endl;
 	fin >> epsilon; getline(fin,str);
  	cout << "epsilon: " << epsilon << endl;
    fin >> amp; getline(fin,str);
    cout << "Amplitude: " << amp << endl;
    fin >> freq; getline(fin,str);
    cout << "Frequency: " << freq << endl;
 	cout << "abans: " << p << endl;
	p=atof(getenv ("p")) ;
	cout << "despres: "<< p << endl;
	//Kconn=strtod(getenv("K_Conn"),NULL);
	//alpha=strtod(getenv("alpha"),NULL);
	//beta=strtod(getenv("beta"),NULL);	
	fin.close();
	
 return;
};

/* Destructor */

voxel::~voxel(){

	delete [] y;
	delete [] yold;
	delete [] f;
	delete [] f_old;
	delete [] y1y2;
	
};

void voxel::set_Initial_Conditions(void){
/*y[0]=0.1;
y[1]=0.5;
*/};	
