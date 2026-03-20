"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

qte_linhas = 5
qte_colunas = 5

linha = 1
while linha <= qte_linhas:
    coluna = 1
    while coluna <= qte_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('FIM')
