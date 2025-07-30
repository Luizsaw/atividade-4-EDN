def classificar_numeros():
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            break
        if not entrada.isdigit():
            print("Entrada inválida, digite apenas números ou 'sair'.")
            continue

        numero = int(entrada)
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")

classificar_numeros()