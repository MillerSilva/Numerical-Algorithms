import numpy as np  
import scipy.linalg as sl

def gauss_seidel(A, b, x0, MAX_ITERATIONS):
    if isdiag_domin(A):
        Q = trinf(A)
        invQ = sl.inv(Q)
        nrow = np.shape(A)[0]
        G = np.identity(nrow)-np.dot(invQ, A)
        c = np.dot(invQ, b)
        for k in range(MAX_ITERATIONS):
            x = np.dot(G, x0) + c
            x0 = x
        return x

    else:
        print("El metodo de Gauss-Seidel no es adecuado.")
        return np.zeros_like(x0)
    
def isdiag_domin(A):
    nrow = np.shape(A)[0]
    index = np.arange(nrow)
    for k in range(nrow):
        if abs(A[k,k]) < sum(np.abs(A[k, index[index != k]])):
            return False
    return True



def trinf(A):
    Q = np.zeros_like(A)
    nrow = np.shape(A)[0]
    for k in range(nrow):
        Q[k,:k] = A[k, :k]

    return Q

