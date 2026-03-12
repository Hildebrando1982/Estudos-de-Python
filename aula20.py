# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('Digite [E]ntrar ou [S]air: ')
    
if entrada == "E".lower():
    senha_digitada = input('Digite a senha: ')
    senha_entrada = '123456'
    if senha_digitada == senha_entrada:
        print('Acesso Permitido!!!')
    elif not senha_digitada:
        print('Você não digitou nada.')
        print('Tente novamente.')
    else:
        print('Acesso negado!')
elif entrada == "S".lower():
    print("Você optou em sair do sistema.")
else:
    print("Você digitou um caractere incorreto.")
    print("Tente novamente.")  

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)
