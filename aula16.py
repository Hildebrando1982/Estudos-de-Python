"""Docstring
Nas condicionais, para o if ser executado, a condição tem que ser verdadeira.
Sendo o if falso, o programa lê o elif, se for verdadeiro executa.
Se o elif for falso, executa o else"""

# if / elif      / else
# se / senão se / senão

idade = int(input('Qual a sua idade? '))

if idade < 12: #Nesse caso só será executado se essa condição for verdadeira (idade menor que 12)
    print('Você é criança.')

elif idade < 18: #Nesse caso só será executado se essa condição for verdadeira (idade menor que 18)
    print('Você é adolescente')
else: #Nesse caso só será executado se essa condição for verdadeira (idade maior que 18)
    print('Você é adulto.')
