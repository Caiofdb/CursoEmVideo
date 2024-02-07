n = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão \n[1] Converter para binario\n'
      '[2] Converter para octal \n[3] Converter para hexadecimal')
n2 = int(input())
if n2==1:
    print(bin(n)[2:])
elif n2==2:
    print(oct(n)[2:])
elif n2==3:
    print(hex(n)[2:])
else:
    print('Opção invalida')
