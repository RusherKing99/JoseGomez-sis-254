import numpy as np

# Definir el sistema de ecuaciones
def gauss_seidel(A, b, x0, tol=1e-10, max_iterations=100):
    n = len(b)
    x = x0.copy()

    for k in range(max_iterations):
        x_new = x.copy()

        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]

        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f"Convergió en la iteración {k+1}")
            return x_new

        x = x_new

    print("No convergió")
    return x

# Matriz de coeficientes
A = np.array([
    [3, -0.1, -0.2],
    [0.1, 7, -0.3],
    [0
