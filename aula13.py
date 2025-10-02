#Calculadora simples de IMC em Python
#Desenvolvido por Hildebrando Marques
#Uso da f-strings, formatação da strings
#coloca o f antes das aspas e a variável estará dentro das aspas e dentro de chaves, para formatar as casas decimais coloca :,f (quantidade de f)


nome = input('Digite o seu nome: ')
altura = float(input('Digite sua altura em m (Ex.: 1.75): '))
peso = float(input('Digite o seu peso em kg (Ex.: 62.5): '))


imc = peso / (altura ** 2)

print(' ')

if (imc < 18.5):
    print(f"Olá {nome}!") #f-strings (formatação do strings)
    print(f"Sua altura é {altura:,.2f} m")
    print(f"Seu peso é {peso:,.2f} kg")
    print(f"Seu IMC é {imc:,.2f}")
    print('IMC considerado muito baixo')
    print('Risco à sua saúde. Consulte um médico e um nutricionista')

elif (imc > 18.5) and (imc<=24.9):
    print(f"Olá {nome}!")
    print(f"Sua altura é {altura:,.2f} m")
    print(f"Seu peso é {peso:,.2f} kg")
    print(f"Seu IMC é {imc:,.2f}")
    print('Você está com o peso normal')
    print('Mantenha seu peso com prática de atividade física e boa alimentação')

elif (imc > 24.9) and (imc <= 29.9):
    print(f"Olá {nome}!")
    print(f"Sua altura é {altura:,.2f} m")
    print(f"Seu peso é {peso:,.2f} kg")
    print(f"Seu IMC é {imc:,.2f}")
    print('Você esta com sobrepeso')
    print('Risco à sua saúde. Consulte um médico e um nutricionista')

else:
    print(f"Olá {nome}!")
    print(f"Sua altura é {altura:,.2f} m")
    print(f"Seu peso é {peso:,.2f} kg")
    print(f"Seu IMC é {imc:,.2f}")
    print('Você esta com obesidade muito elevada')
    print('Risco à sua saúde. Consulte urgente um médico e um nutricionista')
    
print(' ')
