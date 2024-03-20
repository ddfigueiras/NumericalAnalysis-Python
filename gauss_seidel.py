def gauss_seidel(A, b, x0, max_iterations, tolerance):
    n = len(A)
    x = x0.copy()
    for k in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):
            return x_new
        x = x_new
    return x
def main():
    print("===================================================")
    print('=>\t\tInicio do programa\t\t<=')
    print("===================================================\n")
    while(True):

        n = int(input("\nDigita a dimensão da matriz (n).\n=> "))
        A = []
        b = []
        x0 = []
        for i in range(n):
            row = list(map(float, input(f"\nDigita os coeficientes da linha {i+1} da matriz A separados por espaços.\n=> ").split()))
            A.append(row)
            b_value = float(input(f"\nDigita o valor de b[{i}].\n=> "))
            b.append(b_value)
            x0_value = float(input(f"\nDigita o valor de x0[{i}].\n=> "))
            x0.append(x0_value)

        max_iterations = int(input("\nDigita o número máximo de iterações.\n=> "))
        tolerance = float(input("\nDigita a tolerância (ex: 1e-4).\n=> "))

        result = gauss_seidel(A, b, x0, max_iterations, tolerance)
        print("Solução aproximada (Gauss-Seidel):", result)
        continua = input("\nQueres fazer mais alguma vez? (s/n)")
        continua = input("\nQuer fazer mais alguma vez? (s/n): ")
        if continua[0] != "s":
            break
main()
