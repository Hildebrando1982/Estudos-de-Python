'''
Iterável -> (pode entregar uma coisa por vez) str, tange, etc (___iter___)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
'''


'''texto = iter('Hildebrando')  #'Hildebrando'.__iter__()
print(next(texto)) #print(texto.__next__())'''


#for letra in texto:
texto = 'Hildebrando' #iterável
iterador = iter(texto) #iterador

while True:
    try:
        letra =next(iterador)
        print(letra)
    except StopIteration:
        break
