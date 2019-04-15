import numpy as np
import scipy.linalg as sl

def gaussj(A):
    if sl.det(A) != 0:
        nrow = np.shape(A)[0]
        invA = np.identity(nrow)
        for k in range(nrow):
            # crea a
            a = np.reshape(A[:,k]/A[k,k], (nrow,1))
            a[k] = 1-1/A[k,k]
            # crea e, vector cononico ek
            e = np.zeros(nrow).reshape(1,nrow)
            e[0,k] = 1

            L = np.identity(nrow)-np.dot(a,e)
            A = np.dot(L, A)
            invA = np.dot(L, invA)    
        
        return invA
    else:
        print("La matriz no es inversible.")
        return np.zeros_like(A)

def solve_gaussj(A, b):
    
    if sl.det(A) != 0:
        A0 = gaussj(A) # A0 = A^{-1}
        return np.dot(A0, b)
    else:
        print("no existe solucion.")
        return np.zeros_like(A)

    