nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minusculas é {nome.lower()}')
cortado = len(nome) - nome.count(' ')
print(f'Seu nome tem ao todo {cortado} letras')
primeiro = nome.find(' ')
print(f'Seu primeiro nome tem {primeiro} letras')