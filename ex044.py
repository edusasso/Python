valor = float (input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int (input('Qual é a opção '))
if opcao == 1:
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
    parcela = valor / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela} SEM JUROS')
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print(f'Sua compra será parcelada em {totalparc}x de R$ {parcela:.2f} COM JUROS')
else:
    total = valor
    print('Opção inválida de pagamento. Tente novamente!')
print(f'Sua compra de R$ {valor:.2f} vai custar R$ {total:.2f} no final')