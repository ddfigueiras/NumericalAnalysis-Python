def f(x):
    return x**3 - 2*x - 5

def f_prime(x):
    return 3*x**2 - 2

def newton(x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x = x - f(x) / f_prime(x)
        if abs(f(x)) < tol:
            return x
    return x

initial_guess = 2
tolerance = 1e-9
max_iterations = 10
result = newton(initial_guess, tolerance, max_iterations)
print("Raiz aproximada: {:.9f}".format(result))
