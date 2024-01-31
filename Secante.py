def f(x):
    return x**3 - 2*x - 5

def secante(x0, x1, tol, max_iter):
    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    return x1

x0, x1 = 2, 3
tolerance = 1e-9
max_iterations = 10
result = secante(x0, x1, tolerance, max_iterations)
print("Raiz aproximada: {:.9f}".format(result))














