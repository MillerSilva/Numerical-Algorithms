import numpy as np  
import scipy.linalg as sl

def gauss_seidel(A, b, x0, MAX_ITERATIONS):
    Q = trinf(A)
    invQ = sl.inv(Q)
    nrow = np.shape(A)[0]
    G = np.identity(nrow)-np.dot(invQ, A)
    if rspectral(G) < 1:
        for k in range(MAX_ITERATIONS):
            x = np.dot(G, x0) + b
            x0 = x
        return x

    else:
        print("El metodo de Gauss-Seidel no es adecuado.")
        return np.zeros_like(x0)
    




def trinf(A):
    Q = np.zeros_like(A)
    nrow = np.shape(A)[0]
    for k in range(nrow):
        Q[k,:k] = A[k, :k]

    return Q

def rspectral(A):
    pass
