#Precedência entre os operadores aritméticos

# 1. (n + n) --> Primeiro são os parênteses
# 2. ** --> Segundo a potenciação
# 3. * / // % ---> Terceiro o que vier primeiro entre multiplicação, divisão, divisão exata e mod
# 4. + - -->Quarto o que vier primeiro entre adição e subtração

conta_1 = 1 + 2 ** 5 - 10
print(conta_1)

conta_2 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_2)

conta_3 = (1 + 5 - (2 * 2)) ** (4) %2
print(conta_3)
