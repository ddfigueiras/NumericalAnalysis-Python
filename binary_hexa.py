hexEmBinario = {
    '0000':'0', 
    '0001':'1', 
    '0010':'2', 
    '0011':'3', 
    '0100':'4', 
    '0101':'5', 
    '0110':'6', 
    '0111':'7', 
    '1000':'8', 
    '1001':'9', 
    '1010':'A', 
    '1011':'B', 
    '1100':'C', 
    '1101':'D', 
    '1110':'E', 
    '1111':'F' 
}

binarioEmHex = {
    '0':'0000', 
    '1':'0001', 
    '2':'0010', 
    '3':'0011', 
    '4':'0100', 
    '5':'0101', 
    '6':'0110', 
    '7':'0111', 
    '8':'1000', 
    '9':'1001', 
    'A':'1010', 
    'B':'1011', 
    'C':'1100', 
    'D':'1101', 
    'E':'1110', 
    'F':'1111' 
}

def main():
    opcao = input('=>\tInicio do programa Binario | Hexadecimal\t<=\nQueres converter de binario para hexadecimal?\nDigita \'1\'\nQueres converter de hexadecimal para binario?\nDigita \'2\'\nPara terminares o programa digita qualquer outra coisa (cuidado com os espaços).\n=> ')
    if(opcao[0] == '1'):     
        binarioParaHex()
    elif(opcao[0] == '2'):
        hexParaBinario()
    else:
        print('\nO programa foi terminado.')

def binarioParaHex():
    bNum=''
    hNum=''
    check = False
    while not(check):
        bNum = input('Escreve o numero que queres converter para Hexadecimal:\n=> ').replace(" ", "")
        bNumSize = len(bNum)
        check = True

        if bNum == '': 
            bNum='0000'
            hNum='0'
            print("Não escreveste nenhum numero, vamos assumir que é 0 então.")

        if bNumSize > 32:
            print('Infelizmente o máximo são 32 digitos...\n\t.:: A recomeçar ::.')
            check = False
            continue

        if not(validarNumBinario(bNum)):
            print("O numero tem que ser binario, isto é, zeros e uns.\n\t.:: A recomeçar ::.")
            check=False
            continue

    menos = int(0) 

    if (bNumSize % 4) != 0:     
        addZeros = 4 - bNumSize % 4    
        bNum = '0' * addZeros + bNum    
        bNumSize = bNumSize + addZeros
        menos = int(1)

    #marcações
    numD = bNumSize - 1    #é o ultimo numero
    numE = numD - (3)    #4 primeiros
    loops = int(bNumSize / 4)    #para fazer todos os grupos de 4

    for i in range(loops - menos):
        grupo = bNum[numE:(numD+1)]    #1 até outro mais pq pq no python nao o fim nao é contado para o grupo
        hNum = hexEmBinario[grupo] + hNum
        numD -= 4   #continuar mais 4
        numE -= 4

    print(bNum +' Em binario é ' + hNum + ' em hexadecimal.')
    main()

def hexParaBinario():
    hNum = input('Escreve o número que queres converter para Binário:\n=> ').strip(' ').upper()
    if hNum == '' or hNum == ' ':
        hNum = '0'
        print("Não escreveste nenhum número, vamos assumir que é 0 então.")

    bNum = ''

    for i in reversed(hNum):
        if i in binarioEmHex:
            bNum = binarioEmHex[i] + bNum
        else:
            print('O valor tem que ser hexadecimal...\n\t.:: A recomeçar ::.')
            hexParaBinario()  # pode dar erro dai voltamos ao inicio

    print(hNum + ' Em hexadecimal é ' + bNum + ' em binario.')
    main()

def validarNumBinario(bNum):
    for i in bNum:
        if(i != '0' and i != '1'):
            return False
    return True

main()