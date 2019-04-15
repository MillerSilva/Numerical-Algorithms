# Calcula la solucion del sistema Ax= b, mediante la iteraciones de richardson

import numpy as np
import scipy.linalg as sl


def richardson(A, b, x0, MAX_ITERATIONS=1000):
    for k in range(MAX_ITERATIONS):
        r = b-np.dot(A, x0)
        x = x0 + r
        x0 = x
    
    return x

