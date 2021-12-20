total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = input('Nome do Produto: ')
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto        
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break
print('=-=' * 10, end= '')
print('FIM DO PROGRAMA', end = '')
print('=-=' * 10)
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totmil} prodotos custando mais de R$ 1.000')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
    