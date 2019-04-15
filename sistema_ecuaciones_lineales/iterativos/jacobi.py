import numpy as np

def isdiag_domin(A):
    nrow = np.shape(A)[0]
    index = np.arange(nrow)
    for k in range(nrow):
        if abs(A[k,k]) < sum(np.abs(A[k, index[index != k]])):
            return False

    return True

def jacobi(A, b, x0, MAX_ITERATIONS=1000):
    if isdiag_domin(A):
        Q = np.diag(np.diag(A)**(-1))
        for k in range(MAX_ITERATIONS):
            b0 = np.dot(Q-A, x0)+b
            x = sl.solve(Q, b0)
            x0 = x
        return x

    else:
        print("La matrix no es diagonalmnete dominante.")
        return x0
