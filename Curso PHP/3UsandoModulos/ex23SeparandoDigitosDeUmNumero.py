n = int(input('informe um valor: '))
print('O numero {}  tem \n unidade: {}\n dezena: {}\n centena: {}\n milhar: {}'
      .format(n, n%10, n%100//10, n%1000//100, n//1000))