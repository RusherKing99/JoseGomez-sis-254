import numpy as np

# Coeficientes de las ecuaciones
A = np.array([
    [0.52, 0.20, 0.25],
    [0.30, 0.50, 0.20],
    [0.18, 0.30, 0.55]
])

# Resultados de las ecuaciones
b = np.array([4800, 5810, 5690])

# Tolerancia y valores iniciales
tolerance = 0.001
x = np.zeros_like(b)
max_iterations = 100

# Método de Jacobi
for iteration in range(max_iterations):
    x_new = np.zeros_like(x)
    
    x_new[0] = (b[0] - A[0, 1] * x[1] - A[0, 2] * x[2]) / A[0, 0]
    x_new[1] = (b[1] - A[1, 0] * x[0] - A[1, 2] * x[2]) / A[1, 1]
    x_new[2] = (b[2] - A[2, 0] * x[0] - A[2, 1] * x[1]) / A[2, 2]

    # Condición de convergencia
    if np.allclose(x, x_new, atol=tolerance):
        break
    
    x = x_new

print(f"Solución después de {iteration + 1} iteraciones:")
print(f"x1 = {x[0]:.4f}, x2 = {x[1]:.4f}, x3 = {x[2]:.4f}")
