casa = float(input('Valor da casa: R$ '))
salario = float (input('Salário do Comprador: R$ '))
anos = int (input('Quantos anos de financiamento? '))
meses = anos * 12
prestacao = casa / meses
minimo = salario * 30 / 100
print(f'Para pegar uma casa de R$ {casa:.2f} em {anos} anos a prestação será de R$ {prestacao:.2f}')
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!')