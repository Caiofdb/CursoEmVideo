import random
num = [0, 1, 2, 3, 4, 5]
pc = random.choice(num)
chute = int(input('Vou pensar em um numero entre 0 e 5, em que numero pensei?'))
if pc == chute:
    print('Parabéns!, você acertou')
else:
    print('Não foi dessa vez!, pensei no número ', pc)
