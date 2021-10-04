n1 = float (input('Primeira Nota: '))
n2 = float (input('Segunda Nota: '))
media = (n1 + n2)/2
print (f'Tirando {n1} e {n2}, a média do aluno é: {media:.1f}')
if media < 5.0:
    print ('O aluno está REPROVADO')
elif 6.9 >=  media >= 5.0 :
    print('O aluno está em RECUPERAÇÃO')
else:
    print('O aluno está APROVADO')