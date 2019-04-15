import numpy as np
import scipy.linalg as sl


# retorna el primer indice del elemento mayor(si hubiera dos mayores)
def max_index(x):   
    element_max = max(x)
    index = [k for k in range(len(x)) if x[k] == element_max]
    return index[0]

# cambia la fila k por la fila j en A
def change_row(A, k, j):
    row_aux = A[k,]
    A[k,] = A[j,]
    A[j,] = row_aux
    
    return A


def lu(A):
    nrow = np.shape(A)[0]
    invL = np.identity(nrow)
    U = A
    ident = np.identity(nrow)
    P = np.identity(nrow)
    for k in range(nrow):
        index = max_index(U[k:,k])+k
        # crea P (matrix de permutacion), iteracion k
        Pk = change_row(ident, k, index)
        P = np.dot(Pk, P) # matriz de permutaciones P = P_{nrow}xP_{nrow-1}x...xP_{2}xP_{1}
        # crea L (elimina elementos en la fila k), iteracion k
        a = np.zeros(nrow).reshape(nrow, 1)
        a[k+1:,0] = U[k+1:,k]/U[k,k]
        e = np.zeros(nrow).reshape(1, nrow)
        e[0,k] = 1
        Lk = ident - np.dot(a, e)
        LPk = np.dot(Lk,Pk)
        U = np.dot(LPk, U)
        invL = np.dot(LPk, invL)

    L = sl.inv(invL) #calcula la inversa de una matriz triangular (invL)
    L = np.dot(P, L)

    return L, U, P

# resuelve el sistema Ax = b, con A matriz triangular inferior
def solve_trinf(A, b): 
    nrow = np.shape(A)[0]
    x = np.zeros(nrow).reshape(nrow, 1)
    # calcula la solucion de Ax = b
    for k in range(nrow):
        x[k] = (b[k]-sum(np.dot(A[k,:k-1], x[:k-1])))/A[k,k]
    
    return x

# resuelve el sistema Ax = b, con A matriz triangular superior
def solve_trisup(A, b): 
    nrow = np.shape(A)[0]
    x = np.zeros(nrow).reshape(nrow, 1)
    # calcula la solucion de Ax = b
    for k in range(nrow-1,-1,-1): # range(nrow-1,-1,-1) = nrow-1, nrow-2, ..., 2,1,0
        x[k] = (b[k]-sum(np.dot(A[k, k+1:], x[k+1:])))/A[k,k]

    return x

def fact_lu(A):
    nrow = np.shape(A)[0]
    return np.alltrue([sl.det(A[:k+1,:k+1]) > 0 for k in range(nrow-1)])



def solvelu(A, b):
    if fact_lu(A):
        nrow = np.shape(A)[0]
        L, U , P= lu(A)
        b = np.dot(P, b)
        z = solve_trinf(L, b) # resuelve el sistema Lz = b, donde z = Ux y L es triangular inferior
        x = solve_trisup(U, z)  # resuelve el sistema Ux = z,  donde U es triangular superior

        return x
    else:
        print("La matriz no tiene un descomposicion LU.")
        return np.zeros_like(x)
