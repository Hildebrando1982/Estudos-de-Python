frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido Van Rossum.'

i = 0
qtd_mais_apareceu = 0
qtd_letra_mais_apareceu = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += i
        continue
    
    qtd_atual = frase.count(letra_atual)
    
    if qtd_atual > qtd_mais_apareceu:
        qtd_mais_apareceu = qtd_atual
        qtd_letra_mais_apareceu = letra_atual
    i += 1

print(f'A letra que mais apareceu foi "{qtd_letra_mais_apareceu}", por {qtd_mais_apareceu} vezes.')
