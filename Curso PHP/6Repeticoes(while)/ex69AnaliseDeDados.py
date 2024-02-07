maior = menor = h = m = idade = 0
while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F] ').upper()
    if idade >= 18:
        maior+=1
    if sexo =='F' and idade<=20:
        menor+= 1
    if sexo == 'F':
        m=+1
    elif sexo =='M':
        h+=1
    prosseguir = input('Quer continuar? [S/N] ').upper()
    if prosseguir == 'N':
        break
print('Total de pessoas com mais de 18 anos: {}\n'
      '{} homens cadastrados\n'
      'e {} mulheres menores de 20 anos'.format(maior, h, menor))