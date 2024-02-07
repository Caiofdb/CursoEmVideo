import random
pc = random.randint(0, 10)
j = int()
cont = 1
print('Adivinhe o numero que pensei entre 0 e 10')
j=int(input('Faça seu palpite: '))
while j !=pc:
    if j<pc:
        j = int(input('MAIS, tente novamente: '))
    else:
        j = int(input('MENOS, tente novamente: '))
    cont+=1
print('PARABÉNS!!, você acertou em {} palpites'.format(cont))