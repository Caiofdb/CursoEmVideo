print('Loja Ideal')
total = cont = b = 0
while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    ver = ' '
    while ver not in 'sSNn':
        ver = input('Quer continuar [S/N] ').upper()[0]
    total += preco
    if preco >1000:
        cont += 1
    if preco < b or b == 0:
        b = preco
        barato = produto
    if ver == 'N':
        break
print('total gasto na compra foi R${:.2f} \n {} produtos custam mais que 1000 R$ \n'
      '{} é o produto mais barato'.format(total, cont, barato))