"""
Python é uma linguagem de programação de alto nível, com tipagem dinâmica e forte.
Isso significa que:

Dinâmica: você não precisa declarar o tipo das variáveis — o tipo é definido em tempo de execução.
Exemplo: x = 10 e depois x = "texto" é válido.

Forte: não há conversões implícitas entre tipos incompatíveis.
Exemplo: 1 + "2" gera erro, pois não mistura int com str automaticamente.

Uma linguagem de programação de alto nível é mais próxima da linguagem humana e abstrai detalhes complexos do hardware.
Ela facilita a escrita, leitura e manutenção do código, permitindo que o programador foque na lógica do problema, e não em detalhes como gerenciamento de memória ou registradores.
Exemplos: Python, Java, C#

str -> string -> texto
Strings são textos que estão dentro de aspas
"""

# Aspas simples
print('Hildebrando Marques') #aqui reconhece como texto
print(2025, 'Hildebrando "Marques"') #número e texto

# Aspas duplas
print("Hildebrando Marques")
print(2026, "Hildebrando 'Marques'")

# Escape
print("Hildebrando \"Marques\"") #aqui exibe as aspas duplas

# r
print(r"Hildebrando \"Marques\"") #aqui exibe as aspas duplas e o r

print("Hildebrando 'Marques'") #outra forma mais limpa de colocar aspas simples para exibir
