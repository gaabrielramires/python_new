# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

nome = 'Otávio'
# print(nome[2]) # Acessando índice da string
# print(nome[-4]) # Acessando pelo índice negativo

# print('vio' in nome) # Checando se as letras estão na string nome
# print('zero' in nome) # Checando se as letras estão na string nome
# print(10 * '-')
# print('vio' not in nome) # Checando se as letras não estão na string nome
# print('zero' not in nome)# Checando se as letras não estão na string nome

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')