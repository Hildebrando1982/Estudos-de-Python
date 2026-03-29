"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Argentina', 'Brasil', 1822, True, 5.2] # lista com os elementos da lista_a
lista_b = lista_a.copy() # cria uma lista com a cópia da lista_a 
print(lista_a[0]) # exibe o valor do índice 0 da lista_a
lista_a[0] = 'Qualquer coisa' # substitui no índice 0  'Qualquer coisa' por 'Argentina' 
print(lista_a)
print(lista_b)
