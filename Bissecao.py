toleranciaB = 1e-5
toleranciaN = 1e-9
iteradasB = 20
iteradasN = 10

def f(x):
    return x**3 - 2*x - 5 #1-cos

def f_prime(x):
    return 3*x**2 - 2

def bissecao(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        #nao há 
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

def newton(x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x = x - f(x) / f_prime(x)
        if abs(f(x)) < tol:
            return x
    return x

def secante(x0, x1, tol, max_iter):
    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    return x1

def main():
    print('=>\tInicio do programa\t<=\n\n')
    while(opcao[0] == '1'):
        opcao = input('Digita \'1\' para escolheres o método.\n\nDigita qualquer outra coisa para terminares o programa.\n=> ')
        opcao_metodo = input('=>\tFunções disponiveis:\t<=\n\nDigita \'1\' para o Método da Bissecção.\n\nDigita \'2\' para o Método de Newton.\n\nDigita \'3\' para o Método da Secante.\n=> ')
        
        if(opcao_metodo[0] == '1'):
            a = input('Digita o primeiro extremo...')
            b = input('Digita o segundo extremo...')
            result = bissecao(a, b, toleranciaB, iteradasB)
            print("Raiz aproximada: {:.5f}".format(result))
        elif(opcao_metodo[0] == '2'):
            suposicao = input('Digita a suposição inicial')
            result = newton(suposicao, toleranciaN, iteradasN)
            print("Raiz aproximada: {:.9f}".format(result))
        else:
            a = input('Digita a 1ª suposição inicial para a raiz')
            b = input('Digita a 2ª suposição inicial para a raiz')
            result = secante(a, b, toleranciaN, iteradasN)
            print("Raiz aproximada: {:.9f}".format(result))
    print('\nO programa foi terminado.')
main()

# Método da Bissecção:
#
#O Método da Bissecção é um método de busca de raízes que encontra a raiz de uma função em um intervalo especificado.
#O objetivo é reduzir o intervalo inicial pela metade repetidamente até que a raiz seja encontrada dentro de uma tolerância especificada.
#Este método é robusto e funciona bem para funções contínuas em intervalos onde a função muda de sinal.

#Método de Newton:
#
#O Método de Newton, também conhecido como Método de Newton-Raphson, é um método iterativo que busca a raiz de uma função.
#O objetivo é encontrar uma suposição inicial próxima o suficiente da raiz, de modo que as iterações subsequentes se aproximem da raiz com alta precisão.
#Este método utiliza a derivada da função para calcular as iterações e é particularmente eficaz quando a derivada é fácil de obter.

#Método da Secante:
#
#O Método da Secante é outro método iterativo para encontrar raízes de funções.
#O objetivo é encontrar uma suposição inicial próxima da raiz, mas não requer o cálculo direto da derivada da função.
#Em vez disso, ele usa uma reta secante entre dois pontos iniciais e estima a raiz onde a secante cruza o eixo x.
#É uma alternativa ao Método de Newton quando o cálculo da derivada é difícil.

#Esses métodos são usados para encontrar raízes de funções matemáticas, o que pode ser útil em uma variedade de aplicações, 
#desde engenharia e ciência até finanças e análise de dados. Cada método tem suas próprias características e é escolhido com base 
#na natureza da função e na disponibilidade de informações (como a derivada). Eles são úteis para encontrar soluções para equações 
#não lineares e são amplamente utilizados em cálculos numéricos.