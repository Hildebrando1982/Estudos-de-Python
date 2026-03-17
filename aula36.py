'''
Faça um programa que peça ao usuário para digitar um número inteiro,
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''

horas = input('Digite um número inteiro: ')

if '.' in horas:
    print('Você digitou números decimais. Tente novamente')
elif horas.isdigit():
    horas = int(horas)
    if (horas >= 0) and (horas <= 11):
        print('Bom dia!')
    elif (horas >= 12) and (horas <= 17):
        print('Boa tarde!')
    elif (horas >= 18) and (horas <= 23):
        print('Boa noite!')
else:
    print('Você digitou um caractere inválido')
    print('Tente novamente')
