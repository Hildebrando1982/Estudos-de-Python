"""
Fatiamento de strings
 012345678 #indice positivo começa com 0
 Olá Mundo 
-987654321 #indice negativo começa com o ultimo caractera com número -1

Fatiamento [i:f:p] [::] #i é início, f é fim , p é passo
 
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Olá Mundo'
print(variavel[-4])
print(variavel[-8])
print(variavel[4])
print(variavel[0])
print(variavel[3])
print(variavel[6])

print(variavel[4:]) #inicial com indice 4 e repete o restante até o final
print(variavel[4:7]) #inicial com indice 4 e vai até o indice aterioe, neste caso é 6
print(variavel[0:5]) #inicial com indice 0 e vai até o indice aterioe, neste caso é 4
print(variavel[-8:-2]) #inicial com indice 0 e vai até o indice anterior, neste caso é 4

print(len(variavel)) #mostra a quantidade de índices que tem a variável
print(variavel[0:len(variavel):1]) #esse 1 é o passo, ou seja, de quantos em quantos vai pular
print(variavel[0:9:2]) #esse 2 é o passo, ou seja, pula de 2 em 2
print(variavel[::-1]) #exibe a variável escrita ao contrário (espelhado)
print(variavel[-1:-7:-1]) #exibe a variável escrita ao contrário (espelhado)

