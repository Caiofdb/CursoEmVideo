saque = int(input( 'Qual valor deseja sacar: '))
n50 = n20 = n10 = n1 = 0
while True:
    if saque//50 >= 1:
        n50 = saque//50
        saque -= 50*n50
        print('Notas de 50R$: ', n50)
    elif saque//20 >= 1:
        n20 = saque//20
        saque -= 20*n20
        print('Notas de 20R$: ', n20)
    elif saque//10 >= 1:
        n10 = saque//10
        saque -= 10*n10
        print('Notas de 10R$: ', n10)
    elif saque//1>=1:
        n1 = saque//1
        saque -= n1
        print('Notas de 1R$: ', n1)
    if saque == 0:
        break