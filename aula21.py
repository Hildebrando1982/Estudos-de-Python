# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('Digite [E]ntrar ou [S]air: ')
    
if entrada == "E":
    senha_digitada = input('Digite a senha: ')
    senha_entrada = '123456'
    if senha_digitada == senha_entrada:
        print('Acesso Permitido!!!')
    else:
        print('Acesso negado!')
elif entrada == "S":
    print("Você optou em sair do sistema.")
else:
    print("Você digitou um caractere incorreto.")
    print("Tente novamente.")

# Avaliação de curto circuito
#senha = input('Senha: ') or 'Sem senha'
#print(senha)
