# Implementa el calculo del polinomio de interpolacion de la forma de newton(PFN)
# Implementa el calculo de los cueficientes del polinomio (PFN)  
# Implementa la evaluacion del polinomio de interpolacion en algun punto

import numpy as np

# calculo de los coeficientes, por el metodo de interpolacion de newton

def newton(x, y):
	"""
	Calcula los coeficientes del polinomio de interpolacion
	mediante el metodo de interpolacion de newton
	"""
	n = len(x)
	c = np.array([y[0]])	# coeficientes del polinomio de interpolacion
	
	for k in range(1, n):
		d = x[k] - x[k-1]
		y = c[k-1]
		for i in range(k-2, -1, -1):
			u = u*(x[k] - x[i]) + c[i]
			d *= x[k] - x[i]
		c = np.append(c, (y[k]-u)/d)
	
	return c
	
def difdiv(x, y):
	""""
	Metodo de interpolacion de diferencias divididas
	"""
	
	nrow = len(y)
	c = np.zeros((nrow, nrow))
	c[:,0] = y
	
	for j in range(1, nrow):
		for i in range(nrow-j):
			c[i,j] = (c[i+1, j-1] - c[i,j-1])/(x[i+j]-x[i])
	
	return c[0,:] 	#coeficientes del polinomio de interpolacion
	
	
def eval(c, x, x0): # c: coeficientes, x0: punto a evaluar el polinomio
	n = len(c)
	u  = c[-1]	#u: evaluacion de p en x0
	for i in range(n-1,-1,-1):
		u = u*(x0-x[i]) + c[i]
		
	return u
