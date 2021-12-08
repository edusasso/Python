from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print (f'O atleta tem {idade} anos')
if idade <= 9:
    print('Classificação: Mirim')
elif 14 >= idade > 9:
    print('Classificação: Infantil')
elif 19 >= idade > 14:
    print ('Classificação: Júnior')
elif 25 >= idade > 14:
    print('Classificação: Senior')
else:
    print('Classificação: Master')