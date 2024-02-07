n = int(input('escolha um numero pra saber a tabuada: '))
for i in range(0,11):
    print('{} X {:2} = {}'.format(n, i, n*i))