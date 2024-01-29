largura = float(input('Informe a largura da parede: '))
altura = float(input('informe a altura da parede: '))
print('Sua parede tem as dimensões de {} x {} e area de {:.2f}m²\n'
      'para pintala será necessario {:.2f}L de tinta'
      .format(largura, altura, largura*altura, (largura*altura)/2))
