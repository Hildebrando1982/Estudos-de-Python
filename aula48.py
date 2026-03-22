frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido Van Rossum.'

i = 0
qte_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += i
        continue
    
    qtd_atual = frase.count(letra_atual)
    
    if qte_apareceu_mais_vezes <= qtd_atual:
        qte_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual
        
    i += 1
print(f'A letra que apareceu mais vezes foi'
      f' "{letra_apareceu_mais_vezes}" que apareceu'
      f' {qte_apareceu_mais_vezes}x')
