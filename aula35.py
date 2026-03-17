'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é número inteiro.
'''


numero = input('Digite um número inteiro: ')

if '.' in numero:
    print('O número digitado não é inteiro')
    print('O número digitado é decimal')
elif numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print('Par')
    else:
        print('Impar')
else:
    print('Você digitou um caractere inválido')
    print('Tente novamente') 
    

#A segunda forma de resolver a questão

numero = input('Digite um número: ')

try:
    if int(numero) % 2 == 0:
        print(f'O número {numero} é par!')
    else:
        print(f'O número {numero} é impar!')
except:
    print('Você digitou um número decimal.')
