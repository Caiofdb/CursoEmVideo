while True:
    n = int(input('Qual valor que ver a tabuada: '))
    if n <0:
        break
    for i in range(1, 11):
        print('{} x {:2} = {} '.format(n, i, n * i))
print('Fim')