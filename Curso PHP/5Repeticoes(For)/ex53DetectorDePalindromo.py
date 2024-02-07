pal = input('Digite frase a ser verificada: ').replace(' ', '').upper()
ver = str()
for i in range(pal.__len__()-1, -1, -1):
    ver += pal[i]
if pal == ver:
    print('A frase digitada é um palindromo  {}'.format(ver))
else:
    print('A frase não é um palindromo {}  {}'.format(pal, ver))
