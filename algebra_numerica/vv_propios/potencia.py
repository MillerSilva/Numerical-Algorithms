"""
Implemenetacion del metodo de potencia y del metodo de potencia inversa
"""

import numpy as np
import scipy.linalg as sl

def potencia(A, x0, f, MAX_ITERATIONS=100):
    
    for k in range(MAX_ITERATIONS):
        x = np.dot(A, x0)
        r = f(x)/f(x0)
        x0 = x/sl.norm(x)
    
    return r, x/sl.norm(x)


def potencia_inv(A, x0, f, MAX_ITERATIONS=100):
    if sl.det(A) != 0:
        for k in range(MAX_ITERATIONS):
            x = sl.solve(A, x0)
            r = f(x)/f(x0)
            x0 = x/sl.norm(x)
        return r, x/sl.norm(x)
    else:
        print("El metodo de potencia inversa no es adecuado.")
        return 0, np.zeros_like(x0), 