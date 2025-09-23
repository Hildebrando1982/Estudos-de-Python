#A função print serve para exibir na tela

print(2025, "Brasil") #Aqui tem 2 argumentos, um argumento em número e o outro em texto.

'''Este comentário pode ser utilizado em mais de uma linha'''
#Já este comentário é somente para uma linha

print("Hello World!") #este comendo exibe na tela. É dado de saída

# \r \n --> CRLF
# \n --> LF (Unix, Linux, Mac)
print(10,11, sep='-', end = '\r\n') #Os windows mais recentes como o 10 e 11 já reconecem o CRLF e esse comando end='\r\n' é opcional
print(12,13, sep='-') #o comando sep é uma especie de separador entre os argumentos

'''
sem o comando sep será exibido assim:

10 11
12 13

com o comando sep será exibido assim:

10-11
12-13

'''

print("Resultado da MegaSena da Virada 2024")
print(1,17,19,29,50,57, sep='-')
