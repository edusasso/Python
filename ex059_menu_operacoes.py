n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')

    opcao = int(input('Qual é sua opção? '))
    
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}')
    elif opcao == 2:
        print(f'A multiplicação de {n1} com {n2} é: {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior valor é {n1}')
        else:
            print(f'Entre {n1} e {n2} o maior valor é: {n2}')
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')    
    print('=-=' *10)

print('Fim do programa! Volte sempre!')