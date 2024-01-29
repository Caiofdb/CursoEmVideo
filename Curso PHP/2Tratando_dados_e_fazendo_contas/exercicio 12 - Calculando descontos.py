produto = float(input('Qual o preço do produto? R$'))
print('o produto que custava R${:.2f}, '
      'na promoção com desconto de 5% custará R${:.2f}'
      .format(produto, produto*0.95))
