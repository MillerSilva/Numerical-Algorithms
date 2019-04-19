"""
Implementa la aceleracion de Aitken, utilizando iteradores

r: sucesion a aplicar la aceleracion de Aitken (r es un iterador)
s: sucesion obtenida de la aplicacion de la aceleracion de Aitken a r

NOTA:
    El algoritmo se detiene cuando s se estanca (es decir para un n los valores de s(k) son casi iguales a s(n), donde k > n)
"""
import itertools  
import numpy as np
import matplotlib.pyplot as plt


def aitken(r):
    r0 = next(r)
    r1 = next(r)
    r2 = next(r)
    
    s0 = (r0*r2-r1**2)/(r2-2*r1+r0)
    yield s0
    while True:
        r0 = r1
        r1 = r2
        r2 = next(r)
        yield (r0*r2-r1**2)/(r2-2*r1+r0)
        
# Implementar un funcion que genera un iterador solo si el proximo no esta muy proximo a el (estancamiento, VER NOTA)
def convergencia_aitken(r, MAX_ITERATIONS=1000):
    s = aitken(r)
    n = 1
    s1 = next(s)
    s2 = next(s)
    while n < MAX_ITERATIONS:
        s1 = s2
        s2 = next(s)
        n += 1

    return s2, n

# grafica los MAX_ITERATIONS primeras iteraciones de ambas sucesiones.
# SOLUCIONAR PROBLEMA CON ITERADOR r(SOLO UN USO)
def graf_aitken(r, MAX_ITERATIONS=1000):
    n = np.arange(MAX_ITERATIONS)

    s = aitken(r)   # primer uso de r
    rn = np.array(list(itertools.islice(r, MAX_ITERATIONS)))    # segundo uso de r
    sn = np.array(list(itertools.islice(s, MAX_ITERATIONS)))

    plt.plot(n, rn, 'o', label='sin aceleracion')
    plt.plot(n, sn, 'o', label='con aceleracion')
    plt.title("Comparacion de convergencia.")
    plt.xlabel('Iteraciones')
    plt.legend()
    plt.show()