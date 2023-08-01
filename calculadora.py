def calculadora(numero1, numero2, operacao):

    if operacao == 1:
        return numero1 + numero2
    
    elif operacao == 2:
        return numero1 - numero2
    
    elif operacao == 3:
        return numero1 * numero2
    
    elif operacao == 4:
        return numero1 / numero2
    
    return 0


while True:
    print("1:Soma")
    print("2:Subtração")
    print("3:Multiplicação")
    print("4:Divisao")
    print("0:Sair")

    operacao = int(input(""))
    if operacao > 4 or operacao < 0:
        print("Essa opção não existe, tente novamente")

    elif operacao == 0:
        print("Encerrando...")
        break
    
    else:
        numero1 = float(input("Primeiro número:"))
        numero2 = float(input("Segundo número:"))
        print("Resultado:", calculadora(numero1, numero2, operacao))
        
