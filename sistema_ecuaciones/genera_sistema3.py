import numpy as np
import random as rdm

def vector_random(n, a, b):
    return np.array([rdm.uniform(a, b) for k in range(n)])

def genera_sistema(nrow, L, U):
    x = vector_random(nrow, L, U)
    A =  np.zeros((nrow, nrow))
    index = np.arange(nrow)
    for k in range(nrow):
        sk = sum(x[index != k])
        A[k, index[index != k]] = vector_random(nrow-1, 0, 1)/sk
        a = 1-1/x[k]
        if a > 0:
            A[k,k] = rdm.uniform(0, a)
        else:
            return np.zeros_like(A), np.zeros_like(x)
    
    return A, x

def busca_sistema(nrow, L, U, MAX_ITERATIONS=1000):
    for k in range(MAX_ITERATIONS):
        A, x = genera_sistema(nrow, L , U)
        A0 = np.identity(nrow)-A
        if np.alltrue(np.dot(A0,x) > 0):
            return A, x

    return np.zeros_like(A), np.zeros_like(x)