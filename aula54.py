'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
'''

#        +01234
#        -54321
string = 'ABCDE' #5 caracteres (len)

#lista = list() menos comum
#lista = [] # ''
#print(bool([])) #false
#print (lista, type(lista))

#indice   0      1       2   3
#indices  -4    -3      -2  -1
lista = [123, 'Brasil', 1.2, []]
print(lista)
lista[-3] = 'Maria'
print(lista[1].upper(), type(lista[1])) # aqui ele vai dizer o indice da lista e que tipo ela se refere
print(lista[-3], type(lista[-3])) # aqui ele vai dizer o indice da lista e que tipo ela se refere
print(len(lista)) # aqui ele vai contar que tem 4
