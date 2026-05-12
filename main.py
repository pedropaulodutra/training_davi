saldo = 0 

while True:
    opcao = input(''' 
[S]acar
[D]epositar
[E]xtrato
[Q]uit
                  
''')
    if opcao.upper() == 'S':
        valor = float(input('digite o valor que quer sacar'))
        if saldo < valor:
            print('nao tem dinheiro para sacar')
            continue
        saldo = saldo -valor
    elif opcao.upper() == 'D':
        valor = float(input('digite o valor que deseja depositar')) 
        saldo = saldo +valor 
    elif opcao.upper() == 'E':
        print(f'seu saldo e de R${saldo}')
    elif opcao.upper() == 'Q':
        break
    else:
        print('escolha uma opcao valida ')
        continue