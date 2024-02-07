n= int(input('Digite um Número que queira saber o fatorial: '))
print('Calculando {0}! = {0} '.format(n), end='')
i=n-1
while i > 0:
    n = n*i
    print('X {} '.format(i), end='')
    i-= 1
print('= ', n)