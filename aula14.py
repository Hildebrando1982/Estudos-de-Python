a = 'Windows'
b = 2000
c = 252.1
d = True

#Formatação de string com o método format

format = 'a={} b={} c={} d={}'.format(a, b, c, d)
print(format)

string = 'a={} b={} c={} d={}'
format2 = string.format(a,b,c,d) #string é a variável na linha 9
print(format2)
#se aparecer no terminal out the range significa que você tá querendo fazer algo que já foi concluído.
#por exemplo na linha 10 tem a,b,c,d. se na linha 9 você colocar um par de {} a mais, aparecerá o erro mencionado.

#Por índices
string2 = 'a={3} b={1} c={0} d={2}'
format3 = string2.format(a,b,c,d) #string é a variável na linha 9
print(format3)

#Parâmetro nomeado
string3 = 'a={0} b={1} c={nome3:.2f} d={nome4} d={nome4}'
format4 = string3.format(a,b, nome3=c, nome4=d) #tudo que vier do nome3 precisa ser renomeado para evitar erros
print(format4)
