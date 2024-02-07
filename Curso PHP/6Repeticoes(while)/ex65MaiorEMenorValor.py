soma = cont= maior = menor =0
ver = 'S'
while ver=='S':
    n=float(input('Digite um número: '))
    soma+=n
    if n>maior:
        maior =n
    if n<menor or menor==0:
        menor=n
    ver = input('Quer continuar [S/N] ').upper().strip()
    cont+=1
print('você digitou {:.0f} números a média dos valores foi {:.2f}\n'
      ' o maior foi {} e o menor {}'.format(cont, soma/cont, maior, menor))