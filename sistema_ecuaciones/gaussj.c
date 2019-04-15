// Implementa el emtodo de gauss-jordan para el sistema Ax = b

#include<stdio.h>

double **gaussj(double **A, int nrow);
void entrada_matrix(double **mat, int nrow);
void entrada_vector(double **mat, int nrow);
void copia(double **A0, double **A);


// Calcula la inversa de la  matrix A
double **gaussj(double **A, int nrow)
{
    int k;
    double **A0, **L;
    copia(A0, A, nrow); // copia A en A0

    for(k=0; k<nrow; k++){
        
    }
}

void copia(double **A0, double **A, int nrow)
{
    int i,j;
    
    for(i=0; i<nrow; i++){
        for(j=0; j<nrow; j++){
            A0[i][j] = A[i][j];
        }
    }
}


void entrada_matrix(double **mat, int nrow)
{
    int i,j;
    for(i=0; i<nrow; i++){
        for(j=0; j<nrow; j++){
            printf("A[%d][%d]: ",i+1,j+1);
            scanf("%lf",&mat[i][j]);
        }
    }
}


void entrada_vector(double *b, int nrow)
{
    int i;
    for(i=0; i<nrow; i++){
        printf("b[%d]: ", i+1);
        scanf("%lf",*(b+i))
    }
}

void main()
{
    int nrow;
    double **A, *b;
    printf("Ingrese el orden de la matriz: ");
    scanf("%d", &nrow);

    entrada_matrix(A, nrow);
    entrada_vector(b, nrow);
}