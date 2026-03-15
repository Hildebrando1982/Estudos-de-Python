"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}$')
print(f'{variavel: >10}$')
print(f'{variavel: <10}$')
print(f'{variavel: ^10}$')
print(f'{variavel:-^10}')
print(f'{-1000.452112014:,.2f}')
print(f'{-1000.452112014:.2f}')
print(f'{-1000.452112014:0>+10.2f}')
print(f'{-1000.452112014:0=10.2f}')
print(f'O hexadecimal de 1500 é {2026:04X}') #hexadecimal
print(f' {variavel!r}') 
print(f' {variavel!s}') 
print(f' {variavel!a}') 
