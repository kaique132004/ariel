while True:
    opcao1 = "1. Converter número decimal para as bases binário e octadecimal"
    opcao2 = "2. Converter números de bases binárias e octadecimais para decimal."
    opcao3 = "3. Calculadora aritmética de binários, que contemple as operações de soma e subtração."
    opcao4 = "4. Sair\n"
    
    print(opcao1)
    print(opcao2)
    print(opcao3)
    print(opcao4)
    
    opcao = int(input("Digite apenas o número da opção desejada:"))
    print(opcao)
    
    if opcao == 1:
        numdec = int(input("Digite um número decimal:"))
        numbin = bin(numdec)[2:]
        mumoct = oct(numdec)[2:]
        print("O número decimal", numdec, "convertido para binário é:", numbin)
        print("O número decimal", numdec, "convertido para octal é:", mumoct)
    
    elif opcao == 2:
        while True:
            opt = input(
                "Digite uma opção para converter\n 1. de octal para decimal.\n 2. de binario para decimal. \n 3. para sair do programa. \n Digite a opção: "
            )
    
            if opt == '1':
                num = input("Digite um número em octal: ")
                try:
                    decimal = int(num, 8)
                    print(f"\nO número octal para decimal é:\n {decimal}\n")
                except:
                    print("\nDigite um valor válido\n")
            elif opt == '2':
                num = input("Digite um número binário: ")
                try:
                    decimal = int(num, 2)
                    print(f"\nO número binário para decimal é:\n {decimal}\n")
                except:
                    print("\nO número binário só pode conter 0 e 1\n")
            elif opt == '3':
                print("\nComando Incorreto, Encerrando Programa.")
                break
    
    elif opcao == 3:
        def binario_adic(a, b):
            return bin(int(a, 2) + int(b, 2))[2:]
        
        def binario_sub(a, b):
            return bin(int(a, 2) - int(b, 2))[2:]
        
        print("Olá, é calculadora de binários")
        print("Operações que podem ser feitas: (+) Soma e (-) Subtração")
        
        N1 = input("Digite um número binário: ")
        N2 = input("Digite um número binário: ")
        
        Opc = input(
            "Digite a operação aritmética desejada (+) ou (-), caso queira sair da operação digite (x): "
        )
        
        if Opc == '+':
            R = binario_adic(N1, N2)
            print("A soma dos números em binário é:", R)
        elif Opc == '-':
            R2 = binario_sub(N1, N2)
            print("Resultado da subtração:", R2)
        elif Opc == 'x':
            print("Fim da operação, volte sempre :) ")
            break
   elif opcao == 4:
        print("Saindo do sistema")
        break
