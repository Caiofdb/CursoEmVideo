menor = 0
maior = 0
for i in range(1, 6, 1):
    peso = int(input('Digite o peso da {} ª pessoa: '.format(i)))
    if peso>maior:
        maior = peso
    elif peso<menor or menor ==0:
        menor=peso
print('O maior peso digitado foi {} \n'
      'O menor peso digitado foi {}'.format(maior, menor))