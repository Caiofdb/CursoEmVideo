n = soma =0
cont= -1
while n!=999:
    soma+=n
    cont+=1
    n = int(input('Digite um número [999 para parar]'))
print('Você digitou {} números e a soma deles é {}'.format(cont, soma))