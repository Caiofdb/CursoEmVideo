m= float(input('Digite uma medida em metro: '))
print('{}km \n{}hm \n{}dan \n'
      '{}dm \n{}cm \n{}mm'
      .format(m/1000, m/100, m/10, m*10, m*100, m*1000))
