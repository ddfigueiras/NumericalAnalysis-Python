import numpy as np
import sympy as sp

def f(x, f_expr):
    f_lambda = sp.lambdify('x', f_expr, 'numpy')
    return f_lambda(x)

def newton_cotes_fechada(a, b, n, f_expr):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x, f_expr)
    integral = h * (y[0] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2]) + y[-1]) / 3
    return integral

def newton_cotes_aberta(a, b, n, f_expr):
    h = (b - a) / (n + 2)
    x = np.linspace(a + h, b - h, n)
    integral = h * (3 * (f(a, f_expr) + f(b, f_expr)) + 2 * sum(f(xi, f_expr) for xi in x)) / 2
    return integral

def main():
    print('=>\tInicio do programa\t<=\n\n')
    while True:
        programa = int(input("=>\tQual função queres utilizar?\n=>\t(1) newton cotes aberta\n=>\t(2) newton cotes fechada\n=>\t (3) Sair\n"))
        if programa == 3:
            break
        a_value = float(input("=>\tEscreve o primeiro extremo da função\n"))
        b_value = float(input("=>\tEscreve o segundo extremo da função\n"))
        y_expr = input("=>\tEscreve a função\n")
        f_expr = sp.sympify(y_expr)
        if programa == 2:
            integral_fechada = newton_cotes_fechada(a_value, b_value, 4, f_expr)
            print(f"Integral usando Newton-Cotes Fechada: {integral_fechada}")
        if programa == 1:
            integral_aberta = newton_cotes_aberta(a_value, b_value, 3, f_expr)
            print(f"Integral usando Newton-Cotes Aberta: {integral_aberta}")
main()
