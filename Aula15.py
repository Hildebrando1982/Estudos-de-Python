nome = input('Qual o seu nome? \n ') #\n faz a quebra da linha
print(f'Seu nome é {nome}.')

#Forma para descobrir o valor da variável {nome=}
nome = input('Qual o seu nome? \n ')
print(f'Seu nome é {nome=}.')

#No caso abaixo a variável n~eo é número e sim string (letras)
numero1 = input("Digite um número: ")
numero2 = input("Digite um número: ")
print(f'A soma dos dois números é {numero1 + numero2}') #Aqui não houve soma e sim concatenação

#no caso abaixo as variáveis são inteiros e ocorrerá a soma
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
print(f'A soma dos dois números é {numero1 + numero2}')
