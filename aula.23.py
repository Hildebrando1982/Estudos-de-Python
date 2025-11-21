
# Operadores in e not in
# Strings são iteráveis, eles possuem índices
#  0 1 2 3 4 5  (indice positivo)
#  D a n i e l
# -6-5-4-3-2-1 (indice negativo)
# nome = 'Daniel'
# print(nome[2])
# print(nome[-4])
# print('el' in nome)
# print('teo' in nome)
# print(10 * '-')
# print('dan' not in nome)
# print('eco' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
