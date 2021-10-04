salario = float(input('Qual o salário do funcionário? R$ '))
if salario > 1250.00:
    print(f'Quem ganhava {salario} passa a ganhar R$ {salario + (salario * 10)/100:.2f}')
else:
    print(f'Quem ganhava {salario} passa a ganhar R$ {salario + (salario * 15)/100:.2f}')