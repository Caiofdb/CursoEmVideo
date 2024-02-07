n1 = float(input('primeiro número: '))
n2 = float(input('segundo número: '))
ver = 0
while ver!= 5:
    print('Qual operação realizar digite:\n [1]Somar'
          '\n[2]Multiplicar\n[3]Maior\n[4]Novos Numeros\n[5]Sair do programa ')
    ver = int(input())
    if ver==1:
        print('A soma entre {} + {} = {}'.format(n1, n2, n1 + n2))
    elif ver==2:
        print('A Multiplicação entre {} x {} = {}'.format(n1, n2, n1*n2))
    elif ver==3:
        if n1>n2:
            print('O Maior entre {} e {} é {}'.format(n1, n2, n1))
        else:
            print('O Maior entre {} e {} é {}'.format(n1, n2, n2))
    elif ver==4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif ver == 5:
        print('Finalizando...')
    else:
        print('opção invalida')


