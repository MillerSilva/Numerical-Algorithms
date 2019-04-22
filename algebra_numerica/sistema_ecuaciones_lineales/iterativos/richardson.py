# Calcula la solucion del sistema Ax= b, mediante la iteraciones de richardson

import numpy as np
import scipy.linalg as sl

def rspectral(A, v0, f):
	
	for k in range(MAX_ITERATIONS):
		v = np.dot(A, v0)
    	r = f(v)/f(v0)
		v0 = v/sl.norm(v)
    
    return r


def richardson(A, b, x0, f, MAX_ITERATIONS=1000):
    nrow = np.shape(A)[0]
    if rspectral(np.identity(nrow)-A, v0=np.array([1,0,0]).reshape(3,1), f) < 1:
    
        for k in range(MAX_ITERATIONS):
            r = b-np.dot(A, x0)
            x = x0 + r
            x0 = x
    
        return x
    else:
        print("El metodo de richardson no es adecuado.")
        return x0
