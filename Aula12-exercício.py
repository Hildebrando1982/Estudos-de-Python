'''
Crie o IMC com os dados nome, idade, altura e peso
Sabe-se que para calcular o IMC é o peso (kg) dividido pelo quadrado da altura (m)
'''

nome = input('Digite o seu nome: ')
peso = int(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
idade =  int(input('Digite sua idade: '))

imc = peso / (altura ** 2)

print('Seu nome é', nome)
print('Sua idade é', idade)
print('Seu peso é', peso)
print('Sua altura é', altura)
print('Seu IMC é', imc)
