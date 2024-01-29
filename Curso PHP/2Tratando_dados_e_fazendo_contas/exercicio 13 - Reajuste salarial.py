salario = float(input('Qual o salario do funcionário: R$'))
print('o funcionário que ganhava R${:.2f}, com o aumento de 15%, '
      'passará a receber R${:.2f}'.format(salario, salario*1.15))