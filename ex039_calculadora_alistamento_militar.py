from datetime import date
nascimento = int(input('Ano de nascimento: '))
anos = date.today().year - nascimento
print(f'Quem nasceu em {nascimento} tem {anos} anos em {date.today().year}')
alistamento = 18 - anos
if alistamento > 0:
    print(f'Ainda faltam {alistamento} anos para o alistamento')
    print(f'Seu alistamento será em {date.today().year + alistamento}')
elif alistamento < 0:
    print(f'Você já deveria ter se alistado há {alistamento * -1} anos.')
    print(f'Seu alistamento foi em {date.today().year + alistamento}')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')