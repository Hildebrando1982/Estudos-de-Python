"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

'''condicao = True
while condicao: #loop infinito
    print(1)
    print(2)
    print(3)'''
    
'''condicao = True
while condicao: #loop infinito
    nome = input('Qual o seu nome?: ')
    print(f'Seu nome é {nome}')'''
    
condicao = True
while condicao: #loop infinito
    nome = input('Qual o seu nome?: ')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair':
        break
print('acabouu!')
