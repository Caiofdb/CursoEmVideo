casa = float(input('valor da casa: R$'))
sal = float(input('Informe o seu sálario: R$'))
fin = float(input('informe em quantos pretende financiar: '))
prestacao = casa/(fin*12)
print('A prestação para pagar sua casa no valor de R${:.2f} '
      'em {} anos será de {:.2f}'.format(casa, fin, prestacao))
if prestacao<sal*.30:
    print('Emprestimo concedido')
else:
    print('Emprestimo Negado!')