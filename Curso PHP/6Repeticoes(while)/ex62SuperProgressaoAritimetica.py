a1= float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
print('Os 10 primeiros termos da PA são \n{}'.format(a1),end=' ')
cont = 9
while cont>=0:
    a1 +=r
    print('-> {}'.format(a1),end=' ')
    cont -= 1
    if cont == 0:
        cont = int(input('\nQuantos termos mais você quer saber: '))