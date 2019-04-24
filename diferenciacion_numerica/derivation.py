# Implementa el calculo de la primera derivada de una funcion de clase C2
# y cuya tercer derivada exista


def first_deriv(x0, f, h=1, MAX_ITERATIONS=100):
	phi = lambda h: (f(x0+h)-f(x0-h))/(2*h)
	r0 = phi(h)
	h /= 2
	r1 = phi(h)
	
	for k in range(1,MAX_ITERATIONS):
		h /= 2
		r = phi(h)	
		if abs(r1-r0) <  abs(r-r1):
			return r1
		r0 = r1
		r1 = r
	
	return r1


def second_deriv(x0, f, h=1, MAX_ITERATIONS=100):
	phi = lambda h: (f(x0+h)+f(x0-h)-2*f(x0))/h**2 
	r0 = phi(h)
	h /= 2
	r1 = phi(h)
	
	for k in range(1, MAX_ITERATIONS):
		h /= 2
		r = phi(h)
		if abs(r1-r0) < abs(r-r1):
			return r1
			
		r0 = r1
		r1 = r
		
	return r1



def third_deriv(x0, f, h=1, MAX_ITERATIONS=100):
	phi = lambda h: (3/h**3)*(f(x0+h)-f(x0-h)-2*first_deriv(x0, f)*h)
	r0 = phi(h)
	h /=2
	r1 = phi(h)
	
	
	for k in range(1, MAX_ITERATIONS):
		h /= 2
		r = phi(h)
		if abs(r1-r0) < abs(r-r1):
			return r1
		r0 = r1
		r1 = r
		
	return r1
