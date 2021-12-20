tot18 = total_homens = total_mulheres = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        total_homens +=1
    if sexo == 'F' and idade < 20:
        total_mulheres += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
         break
print(f'Total de pessoas com mais de 18 anos : {tot18}')
print(f'Ao todo temos {total_homens} homens cadastrados')
print(f'E temos {total_mulheres} mulheres com mais de 20 anos')