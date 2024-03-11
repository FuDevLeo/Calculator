def calculadora():
    print("Selecione a operação: ")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")

    escolha = input(" Digite sua escolha (1/2/3/4/5): ")

    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    if escolha == "1":
        print(num1, "+", num2, "=", num1 + num2)
    elif escolha == "2":
        print(num1, "-", num2, "=", num1 - num2)
    elif escolha == "3":
        print(num1, "*", num2, "=", num1 * num2)
    elif escolha == "4":
        if num2 != 0:
            print(num1, "/", num2, "=", num1 / num2)
        else:
            print("Erro Divisão por Zero não é permitida!")
    elif escolha == '5':
        print(num1, "^", num2, "=", num1 ** num2)
    else:
        print("Entrada invalida!")


calculadora()
