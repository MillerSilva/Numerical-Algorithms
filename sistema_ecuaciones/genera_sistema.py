import  numpy as np
import random as rdm


# genera un vector aleatorio de n elemento entre a y b
def vector_random(n, a, b):
    return np.array(rdm.uniform(a, b) for k in range(n))


def genera_sistema(nrow):
    x = vector_random(nrow, 10000, 1000000)
    A = np.zeros((nrow, nrow))
    index = np.arange(nrow)
    for k in range(nrow):
        A[k, index[index != k]] = vector_random(nrow-1,0, 1)
        
        aux = 1 - np.inner(A[k,:], x)/x[k]
        if aux > 0:
            A[k,k] = rdm.uniform(0, aux)
        else:
            return np.zeros((nrow, nrow)), x
    
    return A, x


def busca_sistema(nrow, MAX_ITERATIONS=1000):

    for k in range(MAX_ITERATIONS):
        A, x = genera_sistema(nrow)
        if np.alltrue(np.dot(A, x) > 0):
            return A, x

    print("No se hallo el sistema adecuado.")