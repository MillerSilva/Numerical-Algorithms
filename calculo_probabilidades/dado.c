// Calcula la probabilidad de cada elemento de un dado, para 10000 iteraciones

#include<stdio.h>
#include<time.h>
#include<stdlib.h>


# define MAX_ITERATIONS 10000 

void dado(float *p);
void imprime(float *p);
void zeros(float *p, int n);

void main()
{
    float p[6];   //vector probabilidad, p[i]: probabilidad de que salga el numero i

    zeros(p, 6);

    dado(p);
    imprime(p);
}

void zeros(float *p, int n)
{
    int i;
    for(i=0; i<n; i++)
        *(p+i) = 0.0;
    
} 


void dado(float *p)
{
    int k, aux;

    srand(time(NULL));
    for(k=0; k<MAX_ITERATIONS; k++){
        aux = rand()%6;
        *(p+aux) += 1.0/MAX_ITERATIONS;
    }
}

void imprime(float *p)
{
    int i;
    for(i=0; i<6; i++)
        printf("p([X = %d]) = %f\n", i+1, *(p+i));
}