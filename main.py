# DUNDER (_pycache_) É UM TIPO DE ARQUIVO BINÁRIO CRIADO PELO PYTHON PARA FACILITAR A LEITURA DOS 
# MÓDULOS CRIADOS
# O DUDER NÃO É INTERESSTE NOS adds, POR ISSO UTILIZAMOS CRIAMOS UM 
# ARQUIVO (.gitiginore) - NESTE CASO NÃO FOI NECESSÁRIO DEVIDO HÁ CONFIGURAÇÃO NA CRIAÇÃO DO REPOSITÓRIO.
from  CALCULADORA.operacoes_simples import soma, subtracao
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
            argumento3 = int(input('OPERADOR 1: ')) 
            argumento4 = int(input('OPERADOR2: '))      
            resultado1 = subtracao(argumento3, argumento4)
            print(f'o resultado da subtracoa:{resultado1}')
            print()
        elif opcao == 3:
            print("OBRIGADO POR USAR A NOSSA  CALCULADORA: ")         