#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>

typedef struct VEC {
   double x, y, z;
} vec;

double diffnorm (vec * a, vec * b) {
   double dx=a->x-b->x;
   double dy=a->y-b->y;
   double dz=a->z-b->z;
   return sqrt(dx*dx+dy*dy+dz*dz);
}

void random_step ( vec * L, int i, double R ) {
   double phi=M_PI*(1-2*((double)rand())/RAND_MAX);
   double cphi=cos(phi);
   double sphi=sin(phi);
   double ctheta=1-2*((double)rand())/RAND_MAX;
   double theta=acos(ctheta);
   double stheta=sin(theta);
   L[i].x=L[i-1].x+R*stheta*cphi;
   L[i].y=L[i-1].y+R*stheta*sphi;
   L[i].z=L[i-1].z+R*ctheta;
}

int collides ( vec * L, int i, double S ) {
   int j;
   int coll=0;
   for (j=0;!coll&&j<i;j++) {
      coll=(diffnorm(&L[i],&L[j])<S);
   }
   return coll;
}

int self_avoiding_step ( vec * L, int i, double R, double S, int maxtrial ) {
   int ntrial = 0;
   random_step(L,i,R);
   while (collides(L,i,S)&&ntrial<maxtrial) {
      random_step(L,i,R);
      ntrial++;
   }
   if (ntrial==maxtrial) {
      fprintf(stderr,"ERROR: could not place next SA walker in %d attempts.\n",maxtrial);
      return 1;
   }
   return 0;
}

int main ( int argc, char * argv[] ) {
  int i, w;
  int bail=0;
  int nsteps=10000;
  int nwalkers=100;
  double R = 1.0;
  double S = 0.5;
  int maxtrial = 10000;
  vec * RW;
  vec * SAW;
  double * rdist;
  double * sadist;
  FILE * fp;
  unsigned long int Seed = 293487;

  for (i=1;i<argc;i++) {
    if (!strcmp(argv[i],"-seed")) Seed=(unsigned long int)atoi(argv[++i]);
    else if (!strcmp(argv[i],"-S")) S=atof(argv[++i]);
    else if (!strcmp(argv[i],"-N")) nsteps=atoi(argv[++i]);
    else if (!strcmp(argv[i],"-W")) nwalkers=atoi(argv[++i]);
  }

  srand(Seed);
  RW=(vec*)malloc(nsteps*sizeof(vec));
  SAW=(vec*)malloc(nsteps*sizeof(vec));
  rdist=(double*)malloc(nsteps*sizeof(double));
  sadist=(double*)malloc(nsteps*sizeof(double));

  RW[0].x=RW[0].y=RW[0].z=0.0;
  SAW[0].x=SAW[0].y=SAW[0].z=0.0;

  for (i=0;i<nsteps;i++) {
     rdist[i]=sadist[i]=0.0;
  }
  bail=0;
  for (w=0;!bail&&w<nwalkers;w++) {
     fprintf(stdout,"Walker %d...\n",w);
     for (i=1;!bail&&i<nsteps;i++) {
        random_step(RW,i,R);
	bail=self_avoiding_step(SAW,i,R,S,maxtrial);
        rdist[i]+=diffnorm(&RW[i],&RW[0]);	
        sadist[i]+=diffnorm(&SAW[i],&SAW[0]);	
     }
  }
  if (bail) nwalkers=w;
  for (i=0;i<nsteps;i++) {
     rdist[i]/=nwalkers;
     sadist[i]/=nwalkers;
  }
  fp = fopen("out.dat","w");
  for (i=0;i<nsteps;i++) {
     fprintf(fp,"%i %.5lf %.5lf\n",i,rdist[i],sadist[i]);
  }
  fclose(fp);
}
