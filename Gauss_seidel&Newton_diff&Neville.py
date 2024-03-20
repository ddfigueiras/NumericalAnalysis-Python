def neville(points, x):
    n = len(points)
    table = [[0] * n for _ in range(n)]

    for i in range(n):
        table[i][0] = points[i][1]

    for i in range(1, n):
        for j in range(1, i + 1):
            denominator = points[i][0] - points[i - j][0]
            if denominator == 0:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = ((x - points[i - j][0]) * table[i][j - 1] -
                               (x - points[i][0]) * table[i - 1][j - 1]) / denominator

    return table[n - 1][n - 1]


def newton_diff(points):
    n = len(points)
    diffs = [point[1] for point in points]
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            denominator = points[j][0] - points[j - i][0]
            if denominator == 0:
                diffs[j] = 0  # ou qualquer outro valor desejado quando a divisão por zero ocorre
            else:
                diffs[j] = (diffs[j] - diffs[j - 1]) / denominator

    def interpolation(x):
        result = 0
        term = 1
        for i in range(n):
            result += term * diffs[i]
            term *= (x - points[i][0])
        return result

    return interpolation



def get_points_from_user():
    points = []
    num_points = int(input("=>\tQuantos testes vamos fazer?"))
    for i in range(num_points):
        x = float(input(f"Escreve o valor de: x{i + 1}: "))
        y = float(input(f"Escreve o valor de: y{i + 1}: "))
        points.append((x, y))
    return points

def test():
    test_data = [
        ([(1, 3), (1, 9), (4, 1), (5, 7)], 3.5),
        ([(0, 1), (2, 3), (4, 5), (6, 7)], 2.5),
        ([(8, 4), (5, 8), (6, 12), (8, 16)], 5),
        ([(2, 1), (4, 4), (6, 12), (8, 16)], 1),
        ([(3, 4), (1, 3), (6, 12), (8, 16)], 2),
        ([(1, 5), (8, 2), (6, 12), (8, 16)], 6),
        ([(0, 2), (1, 4), (2, 8), (3, 16)], 1.5),
        ([(1, 2), (2, 4), (3, 8), (4, 16)], 2.5),
        ([(1, 1), (2, 8), (3, 27), (4, 64)], 2.8),
    ]

    for points, x_value in test_data:
        result_neville = neville(points, x_value)
        print(f"Interpolação pelo Método de Neville em x={x_value}: {result_neville}")

        interpolation_function = newton_diff(points)
        result_newton = interpolation_function(x_value)
        print(f"Interpolação pelo Método de Newton em x={x_value}: {result_newton}")


def main():
    print('=>\tInicio do programa\t<=\n\n')
    
    programa = int(input("=>\tQual função queres utilizar?\n=>\t(1) Neville\n=>\t(2) Newton\n=>\t (3) Sair\n"));
    while(programa != 3):
        data_points = get_points_from_user()

        x_value = float(input("=>\tEscreve o valor de x para a interpolação\n"))
        
        if(programa == 1):
            result_neville = neville(data_points, x_value)
            print(f"Interpolação pelo Método de Neville em x={x_value}: {result_neville}")
        elif(programa == 2):
            interpolation_function = newton_diff(data_points)
            result_newton = interpolation_function(x_value)
            print(f"Interpolação pelo Método de Newton em x={x_value}: {result_newton}")
test()
