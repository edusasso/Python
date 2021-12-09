resposta = 'S'
soma = 0
qtd = 0
media = 0
maior = 0
menor = 0
while resposta == 'S':
    num = int(input('Digite um número: '))
    soma += num
    qtd += 1
    if qtd == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    resposta = input('Quer continuar? [S/N] ').upper().strip()[0]
media = soma / qtd
print(f'Você digitou {qtd} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
