"""
procedure1: Calculo de los coeficientes del polinomio de interpolacion en la forma de newton.
procedure2: Evaluacion del polinomio de interpolacion(en la forma de Newton) en algun punto.
"""

def newton_interpolation(x, y):
    coef = [y[0]]

    for k in range(1, len(x)):
        d = x[k] - x[k-1]
        u = coef[k-1]
        for i in range(k-2,-1,-1):  # range(k-2, -1, -1) = k-2, k-1,..., 0
            u = u*(x[k]-x[i])+ coef[i]
            d *= (x[k]-x[i])
        coef.append((y[k]-u)/d)

    return coef


def newton_evaluation(coef, x, x0):
    u = coef[-1]    # u = p(x0)
    for i in range(len(coef)-1, -1,-1):
        u = u*(x0-x[i]) +coef[i]

    return u