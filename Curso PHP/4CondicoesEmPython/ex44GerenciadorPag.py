compra = float(input('Digite o valor da compra: '))
modo = input('digite a forma de pagamento\n[1]Dinheiro\n[2]cheque\n'
             '[3]cartão à vista\n[4]cartão parcelado\n')
if modo=='1' or modo=='2':
    print('sua compra de R${:.2f} sairá por R${:.2f} com desconto'
          .format(compra,compra*.90))
elif modo=='3':
    print('sua compra sairá no valor de R${:.2f}'.format(compra*.95))
elif modo=='4':
    par= int(input('quantas parcelas?'))
    if par>2:
        print('sua compra sairá no valor integral de R${:.2f} com parecelas'
              'de R${}'.format(compra*1.20, (compra*1.20)/par))
    else:
        print('sua compra sairá no valor integral de R${} com parecelas'
              'de R${}'.format(compra, compra/par))