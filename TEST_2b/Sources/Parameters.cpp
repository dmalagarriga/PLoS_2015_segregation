#include "../Headers/Parameters.h"
//#include "../Headers/voxel.h"


/* Constructor */
Parameters::Parameters(char *arg1, char *arg2, char *arg3){
  cout << "\nCreating parameters object." << endl;
  //Dir_Output=string( getenv("Dir_Output") );
   Dir_Output=arg1;
  Dir_Input=string( getenv("Dir_Input") ); 
  NumPar_Dat=string( getenv("NumPar_Dat") );
  //Data_Dat=string( getenv("Data_Dat") );
  Data_Dat=arg2;
  //Init_Cond_Dat=string(getenv("Init_Cond_Dat"));
  Init_Cond_Dat=arg3;
  Kex_Dat=string( getenv("Kex_Dat") );
  Kin_Dat=string( getenv("Kin_Dat") ); 
  t=0;
  
  Read_NumPar_Dat();
  Read_Kex_Dat();
  Read_Kin_Dat();
  
  V=new voxel[nNodes];
  
  //Create (give dimensions to) voxels
 
  openfiles();
};



/* Destructor */ 
Parameters::~Parameters(){

for (int i=0;i<nNodes;i++) {delete[] Kex[i]; delete[] Kin[i];}
delete [] Kex;
delete [] Kin;
cout << "Destroying parameters object." << endl;
delete [] V;
closefiles();
};


/* Read Data to build the Parameter object */
void Parameters::Read_Kex_Dat(void){
 
 string str;
 ifstream fin (Kex_Dat.c_str(),ifstream::in);
 fin >> nNodes;  getline(fin,str);
 cout << "nNodes:" << nNodes << endl;

 Kex=new float*[nNodes];
	for (int i=0;i<nNodes;i++) {Kex[i]=new float[nNodes];}

	for (int i=0;i<nNodes;i++){
		for (int j=0;j<nNodes;j++){fin >> Kex[i][j];}		  
				  }
 fin.close();
	
 return;
};

void Parameters::Read_Kin_Dat(void){
 
 string str;
 ifstream fin (Kin_Dat.c_str(),ifstream::in);
 fin >> nNodes_inh;  getline(fin,str);
 cout << "nNodes_inh:" << nNodes_inh << endl;

 Kin=new float*[nNodes_inh];
	for (int i=0;i<nNodes_inh;i++) {Kin[i]=new float[nNodes_inh];}

	for (int i=0;i<nNodes_inh;i++){
		for (int j=0;j<nNodes_inh;j++){fin >> Kin[i][j];}		  
				  }
 fin.close();
	
 return;
};

/* Read Data to build the Parameter object */
void Parameters::Read_NumPar_Dat(void){
 
 string str;
 ifstream fin (NumPar_Dat.c_str(),ifstream::in);
 fin >> nt;  getline(fin,str);
 cout << "nt: " << nt << endl;
 fin >> ntout; getline(fin,str);
 cout << "ntout: " <<ntout<<endl;
 fin >> dt; getline(fin,str);
 cout << "dt: " <<dt<<endl;
 
 fin.close();

 return;
};

//Delay
void Parameters::RefreshDelay(void){
	
	for (int j=0; j<nNodes; j++){
	
	for (int i=V->nDelays; i>0; i--){	
		
	V[j].y1y2[i]=V[j].y1y2[i-1];
	
		
		         		}				    
	V[j].y1y2[0]=V[j].y[1]-V[j].y[2];

					}			
return;				     				    
				};

//Write data to file
void Parameters::openfiles(void){
fout_data.open(Data_Dat.c_str(),ofstream::out);
fout_init_cond.open(Init_Cond_Dat.c_str(),ofstream::out);
 return;
};

void Parameters::closefiles(void){
 fout_data.close();
 fout_init_cond.close();
  return;
};


void Parameters::WriteData(void){

float Vmean;
for (int j=0;j<nNodes;j++){
			
		Vmean+=(V[j].y[1]-V[j].y[2])/nNodes;
	} 
fout_data << t ;
//fout_data<< " " << Vmean << endl;
for (int i=0;i<nNodes;i++){fout_data << " " << V[i].y[1] - V[i].y[2] ;}
fout_data << " " << endl;

};

void Parameters::WriteInitialConditions(int O){

for (int j=0;j<6;j++){
for (int i=0;i<nNodes;i++){
	
	fout_init_cond << " " << V[i].y[j];
	
	  }
	fout_init_cond << " " << endl;
	}

fout_init_cond << " " << "Seed: " << O << " " << endl;
 return;

};


