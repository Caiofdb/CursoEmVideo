nome = input('Qual seu nome completo: ')
silva = nome[str.find(nome, 'silva'):str.find(nome, 'silva')+5]
#m = 'silva' in str.lower(nome)
#print('Seu nome tem silva? ', m)
print('Seu nome tem silva? ', str.upper(silva) =='SILVA')
