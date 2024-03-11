def calculadora():
    print("Selecione a operação: ")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")

    escolha = int(input(" Digite sua escolha (1/2/3/4/5): "))

    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    match escolha:
        case 1:
            print(num1, "+", num2, "=", num1 + num2)
        case 2:
            print(num1, "-", num2, "=", num1 - num2)
        case 3:
            print(num1, "*", num2, "=", num1 * num2)
        case 4:
            if num2 != 0:
                print(num1, "/", num2, "=", num1 / num2)
            else:
                print("Erro Divisão por Zero não é permitida!")
        case 5:
            print(num1, "^", num2, "=", num1 ** num2)

        case _:
            print("Entrada invalida!")


calculadora()
