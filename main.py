from CALCULADORA.operacoes_simples import soma

print("CALCULADORA")
if __name__ =="__main__":
    opcao = 1
    while opcao != 3:

        print(30*("="))
        print('1 - SOMA')
        print("2-SUBTRAÇÃO")
        print("3 - SAIR")
        print(30*("="))
        opcao = int(input("OPCAO: "))

        if opcao == 1: 
            argumento1 = int(input('OPERADOR 1: ')) 
            argumento2 = int(input('OPERADOR2: '))       
            resultado = soma(argumento1,argumento2)
            print(f'O resultado da soma:{resultado} ')
            print()
        elif opcao == 2:
            print("OPÇÃO SUBTRAÇÃO.")
        elif opcao == 3:
            print("OBRIGADO POR USAR A NOSSA  CALCULADORA: ")