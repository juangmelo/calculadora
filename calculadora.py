def calculadora(numero1, numero2, operacao):

    if operacao == "+":
        return numero1 + numero2
    
    elif operacao == "-":
        return numero1 - numero2
    
    elif operacao == "x":
        return numero1 * numero2
    
    elif operacao == ":":
        return numero1 / numero2
    
    return 0

numero1 = float(input())
operacao = input("")
numero2 = float(input(""))

print(calculadora(numero1, numero2, operacao))