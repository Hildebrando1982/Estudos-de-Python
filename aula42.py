"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

'''while contador < 10:
    contador += 1
    if contador == 4:
        print(contador)
        break
    print(contador)
print('FIM')'''

while contador < 100:
    contador += 1
    if contador == 2:
        continue #neste caso o 6 não será exibido
    if contador >= 10 and contador <= 27:
        print('não mostro a sequência')
        continue
    print(contador)
    if contador == 40:        
        break #termina o laço
print('FIM')
