def jacobi(A, b, x0, max_iterations, tolerance):
    n = len(A)
    x = x0.copy()
    for k in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):
            return x_new
        x = x_new
    return x

def main():
    print("===================================================")
    print('=>\t\tInicio do programa\t\t<=')
    print("===================================================\n")
    while True:
        n = int(input("\nDigite a dimensão da matriz (n):\n=> "))
        A = []
        b = []
        x0 = []
        for i in range(n):
            row = list(map(float, input(f"\nDigite os coeficientes da linha {i+1} da matriz A separados por espaços:\n=> ").split()))
            A.append(row)
            b_value = float(input(f"\nDigite o valor de b[{i}]:\n=> "))
            b.append(b_value)
            x0_value = float(input(f"\nDigite o valor de x0[{i}]:\n=> "))
            x0.append(x0_value)

        max_iterations = int(input("\nDigite o número máximo de iterações:\n=> "))
        tolerance = float(input("\nDigite a tolerância (ex: 1e-4):\n=> "))

        result = jacobi(A, b, x0, max_iterations, tolerance)
        print("\n\nSolução aproximada:", result)
        continua = input("\nQuer fazer mais alguma vez? (s/n): ")
        if continua[0] != "s":
            break

main()
