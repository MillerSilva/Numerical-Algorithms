# Continuar impementacion

import numpy as np

# retorna el primer indice del elemento mayor(si hubiera dos mayores)
def max_index(x):   
    element_max = max(x)
    index = [k for k in range(len(x)) if x[k] == element_max]
    return index[0]

# cambia la fila k por la fila j en A
def change_row(A, k, j):
    row_aux = A[k,]
    A[k,] = A[j,]
    A[j,] = row_aux
    
    return A


def gaussiana_pivote(A, b):
    nrow = np.shape(A)[0]
    Ab = np.concatenate((A, b), axis=1) # matriz extendida [A|b]

    for k in range(nrow):
        index = max_index(Ab[k:, k])+k
        
    