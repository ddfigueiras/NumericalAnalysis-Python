def convert_to_decimal(number, base):
    integer_part, fractional_part = number.split(".")
    decimal_integer = 0
    for i, digit in enumerate(reversed(integer_part)):
        if 'A' <= digit <= 'Z':
            decimal_integer += (ord(digit) - 55) * (base ** i)
        elif 'a' <= digit <= 'z':
            decimal_integer += (ord(digit) - 61) * (base ** i)
        else:
            decimal_integer += int(digit) * (base ** i)

    decimal_fractional = 0
    for i, digit in enumerate(fractional_part):
        if 'A' <= digit <= 'Z':
            decimal_fractional += (ord(digit) - 55) * (base ** (-i - 1))
        elif 'a' <= digit <= 'z':
            decimal_fractional += (ord(digit) - 61) * (base ** (-i - 1))
        else:
            decimal_fractional += int(digit) * (base ** (-i - 1))

    return decimal_integer + decimal_fractional

def convert_from_decimal(decimal_number, base):
    if base < 2 or base > 62:
        return "Base fora do intervalo (2-62)"
    
    integer_part = int(decimal_number)
    fractional_part = decimal_number - integer_part
    integer_part_base = ""
    fractional_part_base = ""

    while integer_part > 0:
        remainder = integer_part % base
        if 10 <= remainder <= 35:
            integer_part_base = chr(remainder + 55) + integer_part_base
        elif 36 <= remainder <= 61:
            integer_part_base = chr(remainder + 61) + integer_part_base
        else:
            integer_part_base = str(remainder) + integer_part_base
        integer_part //= base

    precision = 8
    while fractional_part > 0 and precision > 0:
        fractional_part *= base
        integer_part = int(fractional_part)
        if 10 <= integer_part <= 35:
            fractional_part_base += chr(integer_part + 55)
        elif 36 <= integer_part <= 61:
            fractional_part_base += chr(integer_part + 61)
        else:
            fractional_part_base += str(integer_part)
        fractional_part -= integer_part
        precision -= 1

    result = integer_part_base
    if fractional_part_base:
        result += "." + fractional_part_base

    return result

def main():
    print("===================================================")
    print('=>\t\tInicio do programa\t\t<=')
    print("===================================================\n")
    while True:
        base_origem = input("Digita a base de origem.\n=> ")
        
        base_origem = int(base_origem)
        while (base_origem < 2 or base_origem > 62):
            print("!!!=============================================!!!")
            print("\tA base de origem deve estar no intervalo de 2 a 62.")
            print("!!!=============================================!!!")
            base_origem = input("Digita a base de origem (entre 2 e 62) ou 'q' para sair.\n=> ")


        numero_origem = input("\nDigita o número na base de origem.\n=> ")
        valid_characters = ".0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"[:base_origem + 2]
        while any(char not in valid_characters for char in numero_origem):
            print("!!!=============================================!!!")
            print("\tNúmero inválido para a base.")
            print("!!!=============================================!!!")
            numero_origem = input("Digita o número na base de origem.\n=> ")
        if(numero_origem.find(".") == -1):
            numero_origem = numero_origem + ".0"


        base_destino = int(input("\nDigita a base de destino.\n=> "))
        while (base_destino < 2 or base_destino > 62):
            print("!!!=============================================!!!")
            print("\tA base de destino deve estar no intervalo de 2 a 62.")
            print("!!!=============================================!!!")
            base_destino = int(input("Digita a base de destino.\n=> "))


        decimal_number = convert_to_decimal(numero_origem, base_origem)
        resultado = convert_from_decimal(decimal_number, base_destino)
        print("===================================================")
        print(f"\tO número na base {base_destino} é: {resultado}")
        if(input("\n=> Queres continuar? (Escreve \"q\" para sair)\n") == "q"):
            break
        print("===================================================")

main()
