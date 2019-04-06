"""
Calcula el polinomio en la forma de newton que interpola unos datos y evalua el polinomio en algun punto     
"""
import newton_interpolation
import numpy as np
import matplotlib.pyplot as plt

def vectorize_newton(coef_newton, x, x0):
    y0 = np.array([])
    n = x0.shape[0] # numero de elementos de x0
    for k in range(n):
        eval_newton=newton_interpolation.newton_evaluation(coef_newton, x, x0[k])
        y0 = np.append(y0, eval_newton)

    return y0

x = np.array([5, -7, -6, 0])
y = np.array([1, -23, -54, -954])

coef_newton = newton_interpolation.newton_interpolation(x, y)
print("Coeficientes del polinomio de interpolacion en la forma de newton:\n", coef_newton)

# grafica del polinomio de interpolacion en la forma de Newton y de los puntos interpolados

x0 = np.linspace(min(x), max(x), 1000)
plt.plot(x, y, "go", label='Puntos interpolados')
y0 = vectorize_newton(coef_newton, x, x0)
plt.plot(x0, y0, label='Polinomio de interpolacion')
plt.grid()
plt.title("Polinomio de interpolacion en la forma de Newton")
plt.legend()
plt.show()

