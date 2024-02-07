n=int(input('Digite o número que quer verificar: '))
cont = int()
for i in range(1,n+1):
    if n%i==0:
        cont+= 1
        print('\033[34m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(i, end='\033[38m ')
if cont==2:
    print('O número {} foi dividido {} vezes então ele é primo'
          .format(n, cont))
else:
    print('O número {} foi dividido {} vezes então ele não é primo'
          .format(n, cont))
