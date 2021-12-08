soma_idade = 0
media_idade = 0
maior_idade = 0
total_mulher = 0
for p in range (1,5):
    print(f'----- {p}ª PESSOA-----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome
    if sexo in 'Ff' and idade > 20:
        total_mulher +=1
media_idade = soma_idade/4
print(f'A media de idade do grupo é de {media_idade} anos')
print(f'O homem mais velho tem {maior_idade} anos e se chama {nome_velho}')
print(f'Ao todo são {total_mulher} mulheres com menos de 20 anos')
