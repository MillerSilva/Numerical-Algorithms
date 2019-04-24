# Calcula la solucion de la siguiente ecuacion diferencial por el metodo de la serie de taylor.
#
# x' = cos(t) - sin(x) + t**2
# x(-1) = 3
#
# NOTA(notacion):
#	xk : derivada k-esima de x



from math import cos, sin
import numpy as np
import matplotlib.pyplot as plt

f = lambda x, t: cos(t) - sin(x) + t**2

def solve_taylor(x0, t0, h = 0.01, MAX_ITERATIONS=200):
	x = np.array([x0])	# vector con componenetes de x(t)
	t = np.array([t0])	# vector tiempo
	for k in range(MAX_ITERATIONS):
		x1 = lambda x, t: cos(t) - sin(x) + t**2 
		x2 = lambda x, t: -sin(t) -x1(x, t)*cos(x) + 2*t
		x3 = lambda x, t: -cos(t) - x2(x, t)*cos(x) + x1(x, t)**2*sin(x) + 2
		x4 = lambda x, t: sin(t) + (x1(x, t)**3-x2(x, t))*cos(x) + 3*x1(x, t)*x2(x, t)*sin(x)
		
		x0 = x0 + h*(x1(x0, t0) + (h/2)*(x2(x0, t0) + (h/3)*(x3(x0, t0) + (h/4)*x4(x0, t0))))
		t0 += h
		
		x = np.append(x, x0)
		t = np.append(t, t0)
		
	plt.plot(t, x, label="Solucion de la edo")
	plt.xlabel('t')
	plt.ylabel('x(t)')	
	plt.grid()
	plt.legend()
	plt.show()

