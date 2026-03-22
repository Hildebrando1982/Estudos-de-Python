
'''texto = 'Phyton é bom demais'

i = 0

while i < len(texto):
    print(texto[i], i)
    
    i+=1'''

#while é um laço de repetição indefinido, pode ser infinito
#for é um laço de repetição finito e definido

'''senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')
    repeticoes += 1
print(repeticoes)
print('aquele laço de repetição pode ter repetições infinitas.')'''

texto = 'Phyton é bom demais'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')
