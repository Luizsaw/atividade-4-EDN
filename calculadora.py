def calculadora():
    print("Calculadora Simples (+, -, *, /)")
    num1 = float(input("Digite o primeiro número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero.")
            return
    else:
        print("Operador inválido.")
        return

    print(f"Resultado: {resultado}")

calculadora()