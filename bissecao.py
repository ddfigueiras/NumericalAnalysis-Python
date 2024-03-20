def f(x):
    return x**3 - 2*x - 5

def bissecao(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        #Não existe.
        return None

    for i in range(max_iter):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

a, b = 1, 3
tolerance = 1e-5
max_iterations = 20
result = bissecao(a, b, tolerance, max_iterations)
print(f"Raiz aproximada: {result:.5f}")
